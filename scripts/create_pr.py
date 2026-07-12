#!/usr/bin/env python3
"""
Barreletics AI Review PR Automation
One-command workflow for creating PR with ChatGPT review integration
"""

import os
import sys
import subprocess
import json
import re
from datetime import datetime
from pathlib import Path
from typing import Tuple, Optional

# Color codes for terminal output
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_header(text: str):
    """Print a section header"""
    print(f"\n{Colors.BLUE}{Colors.BOLD}=== {text} ==={Colors.END}\n")

def print_success(text: str):
    """Print success message"""
    print(f"{Colors.GREEN}✓ {text}{Colors.END}")

def print_error(text: str):
    """Print error message"""
    print(f"{Colors.RED}✗ {text}{Colors.END}")

def print_warning(text: str):
    """Print warning message"""
    print(f"{Colors.YELLOW}⚠ {text}{Colors.END}")

def print_info(text: str):
    """Print info message"""
    print(f"{Colors.CYAN}ℹ {text}{Colors.END}")

def run_command(cmd: str, capture_output: bool = False, check: bool = True) -> Tuple[int, str, str]:
    """Run a shell command and return exit code, stdout, stderr"""
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=capture_output,
            text=True,
            check=False
        )
        return result.returncode, result.stdout.strip(), result.stderr.strip()
    except Exception as e:
        print_error(f"Failed to run command: {cmd}")
        print_error(str(e))
        sys.exit(1)

def get_git_root() -> str:
    """Get the root directory of the git repository"""
    code, output, _ = run_command("git rev-parse --show-toplevel", capture_output=True)
    if code != 0:
        print_error("Not in a git repository")
        sys.exit(1)
    return output

def check_uncommitted_changes() -> bool:
    """Check if there are uncommitted changes"""
    code, _, _ = run_command("git diff-index --quiet HEAD --", capture_output=True)
    return code != 0  # Returns True if changes exist

def get_current_branch() -> str:
    """Get the current git branch"""
    code, output, _ = run_command("git rev-parse --abbrev-ref HEAD", capture_output=True)
    if code == 0:
        return output
    return "unknown"

def get_changed_files() -> str:
    """Get a summary of changed files"""
    code, output, _ = run_command("git diff --stat", capture_output=True)
    if code == 0:
        return output
    return "Unable to determine changes"

def check_gh_cli_available() -> bool:
    """Check if GitHub CLI is installed"""
    code, _, _ = run_command("which gh", capture_output=True)
    return code == 0

def get_github_token() -> Optional[str]:
    """Get GitHub token from environment or gh CLI"""
    # Try environment variable first
    token = os.environ.get('GITHUB_TOKEN') or os.environ.get('GH_TOKEN')
    if token:
        return token

    # Try gh CLI
    if check_gh_cli_available():
        code, output, _ = run_command("gh auth token", capture_output=True)
        if code == 0 and output:
            return output

    return None

def get_repo_info() -> Tuple[str, str, str]:
    """Get repository owner, name, and remote URL"""
    code, output, _ = run_command("git config --get remote.origin.url", capture_output=True)
    if code != 0:
        print_error("Could not determine repository")
        sys.exit(1)

    # Parse GitHub URL (both https and ssh formats)
    url = output
    match = re.search(r'(?:https://github\.com/|git@github\.com:)([^/]+)/(.+?)(?:\.git)?$', url)
    if match:
        owner, repo = match.groups()
        return owner, repo, url

    print_error(f"Could not parse repository URL: {url}")
    sys.exit(1)

def create_branch_if_needed(branch_name: str) -> bool:
    """Create branch if it doesn't exist, return True if created"""
    code, _, _ = run_command(f"git rev-parse --verify {branch_name}", capture_output=True)

    if code == 0:
        # Branch exists
        print_warning(f"Branch '{branch_name}' already exists, checking out...")
        run_command(f"git checkout {branch_name}")
        return False
    else:
        # Branch doesn't exist, create it
        print_success(f"Creating new branch: {branch_name}")
        run_command(f"git checkout -b {branch_name}")
        return True

def stage_and_commit(message: str) -> bool:
    """Stage all changes and create a commit"""
    print_info("Staging all changes...")
    run_command("git add -A")

    print_header("Files to Commit")
    code, output, _ = run_command("git diff --cached --stat", capture_output=True)
    if output:
        print(output)

    print_info(f"Creating commit: \"{message}\"")
    code, output, error = run_command(f'git commit -m "{message}"', capture_output=True)

    if code != 0:
        print_error(f"Commit failed: {error}")
        return False

    print_success("Commit created")
    run_command("git log -1 --oneline")
    return True

def push_branch(branch_name: str) -> bool:
    """Push branch to remote"""
    print_header("Pushing to Remote")
    code, output, error = run_command(f"git push -u origin {branch_name}", capture_output=True)

    if code != 0:
        print_error(f"Push failed: {error}")
        return False

    print_success(f"Branch '{branch_name}' pushed to origin")
    return True

def trigger_github_workflow(commit_message: str, branch_name: str) -> bool:
    """Trigger GitHub Actions workflow"""
    print_header("Triggering GitHub Actions")

    if not check_gh_cli_available():
        print_warning("GitHub CLI not found")
        print_info("Install 'gh' CLI for full automation: https://cli.github.com")
        return False

    cmd = f'''gh workflow run ai-review-pr.yml \\
        -f commit_message="{commit_message}" \\
        -f branch_name="{branch_name}"'''

    code, output, error = run_command(cmd, capture_output=True)

    if code != 0:
        print_warning(f"Workflow trigger failed: {error}")
        return False

    print_success("Workflow triggered successfully")
    print_info("The workflow will create/update the PR automatically")
    return True

def get_pr_url(owner: str, repo: str) -> str:
    """Get the PR creation URL"""
    return f"https://github.com/{owner}/{repo}/pulls"

def main():
    """Main workflow"""

    # Parse arguments
    commit_message = sys.argv[1] if len(sys.argv) > 1 else "Update via AI assistant"
    branch_name = sys.argv[2] if len(sys.argv) > 2 else None

    # Verify we're in a git repo
    git_root = get_git_root()

    print_header("Barreletics AI Review PR Workflow")

    # Check for changes
    print("Step 1: Checking for uncommitted changes...")
    if not check_uncommitted_changes():
        print_warning("No uncommitted changes detected")
        print_info("Changes must be staged before running this script")
        sys.exit(0)

    print_success("Changes detected")
    print("\nFiles with changes:")
    print(get_changed_files())

    # Show commit message
    print_header("Commit Details")
    print(f"Message: \"{commit_message}\"")

    # Confirm
    response = input(f"\n{Colors.CYAN}Proceed with commit and PR creation? (y/n) {Colors.END}")
    if response.lower() != 'y':
        print_warning("Cancelled by user")
        sys.exit(0)

    # Generate branch name if needed
    if not branch_name:
        branch_name = f"ai-review-{int(datetime.now().timestamp())}"
        print_success(f"Generated branch name: {branch_name}")
    else:
        print_success(f"Using branch: {branch_name}")

    # Create/checkout branch
    print_header("Git Operations")
    create_branch_if_needed(branch_name)
    print_success(f"On branch: {branch_name}")

    # Stage and commit
    if not stage_and_commit(commit_message):
        sys.exit(1)

    # Push
    if not push_branch(branch_name):
        sys.exit(1)

    # Trigger workflow
    trigger_github_workflow(commit_message, branch_name)

    # Get repo info
    owner, repo, _ = get_repo_info()

    # Final summary
    print_header("Workflow Summary")
    print(f"Branch: {Colors.BOLD}{branch_name}{Colors.END}")
    print(f"Commit: {Colors.BOLD}{commit_message}{Colors.END}")
    print(f"Status: {Colors.GREEN}{Colors.BOLD}✓ Ready for Review{Colors.END}")

    print_header("Next Steps")
    print(f"1. View PR: {Colors.CYAN}{get_pr_url(owner, repo)}{Colors.END}")
    print("2. Wait for GitHub Actions to create/update PR")
    print("3. Review changes with ChatGPT in PR comments")
    print(f"4. Approve and manually merge when ready")

    print(f"\n{Colors.GREEN}{Colors.BOLD}✓ All done!{Colors.END}\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print_warning("\nInterrupted by user")
        sys.exit(0)
    except Exception as e:
        print_error(f"Unexpected error: {str(e)}")
        sys.exit(1)
