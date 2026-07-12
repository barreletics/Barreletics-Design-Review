# Barreletics AI Review PR Automation

**One-command workflow for creating Pull Requests with ChatGPT review integration.**

This system automates the entire PR workflow: staging, committing, pushing, and PR creation—all from a single command.

---

## Quick Start

### Prerequisites

- Git installed and configured
- GitHub CLI (optional but recommended for full automation)
- Python 3.7+ (for Python version of the script)

### Installation

The workflow files are already in the repository. No additional installation needed.

To enable GitHub CLI (recommended):

```bash
# macOS (Homebrew)
brew install gh

# Linux (apt)
sudo apt-get install gh

# Then authenticate
gh auth login
```

### One-Command Workflow

**Make sure you have uncommitted changes staged!**

```bash
# Using Makefile (recommended)
make pr

# With custom commit message
make pr MSG="Update component library"

# Using scripts directly
python3 scripts/create_pr.py "Your commit message"
bash scripts/pr.sh "Your commit message"
```

That's it. The workflow will:

1. ✓ Check for uncommitted changes
2. ✓ Create an `ai-review-*` branch
3. ✓ Commit your changes
4. ✓ Push to GitHub
5. ✓ Create/update Pull Request
6. ✓ Post ChatGPT review request comment
7. ✓ Wait for your manual approval & merge

---

## How It Works

### Architecture

```
┌─────────────────────────────────────┐
│  Local Changes (git add ...)        │
└──────────────┬──────────────────────┘
               │
               v
┌─────────────────────────────────────┐
│  make pr                            │
│  (or python3 scripts/create_pr.py)  │
└──────────────┬──────────────────────┘
               │
               ├─ Check changes exist
               ├─ Create ai-review-* branch
               ├─ Commit changes
               ├─ Push to origin
               │
               v
        GitHub Actions Triggered
               │
               ├─ Create/Update PR (ai-review-* → main)
               ├─ Post review request comment
               ├─ Add PR metadata
               │
               v
        ChatGPT Reviews in PR Comments
               │
               ├─ Approve or request changes
               │
               v
        You Manually Merge (click button)
               │
               v
        Done ✓ (main branch updated)
```

### Files Involved

- **`.github/workflows/ai-review-pr.yml`** — GitHub Actions workflow
  - Triggers when you run the local script
  - Manages branch creation, commit, push, PR creation
  - Posts review request comment

- **`scripts/create_pr.py`** — Python script (recommended)
  - More robust, better error handling
  - Pretty terminal output
  - Auto-detects GitHub CLI

- **`scripts/pr.sh`** — Bash script (lightweight)
  - Pure shell, no dependencies
  - Simple and portable
  - Fallback if Python unavailable

- **`Makefile`** — Convenience commands
  - `make pr MSG="..."` for quick access
  - `make install-tools` for setup

---

## Usage Guide

### Scenario 1: Simple Update

```bash
# Make changes to files
# Edit Component Library, update design specs, etc.

# Stage your changes
git add .

# Create PR
make pr

# Follow prompts, confirm commit message
# Workflow handles the rest!
```

### Scenario 2: Custom Commit Message

```bash
make pr MSG="Expand Component Library with all section specs"

# Or directly
python3 scripts/create_pr.py "Your custom message here"
```

### Scenario 3: Custom Branch Name

```bash
python3 scripts/create_pr.py "Message" "my-custom-branch-name"

# Or with bash
bash scripts/pr.sh "Message" "my-custom-branch-name"
```

### Scenario 4: Checking PR Status

```bash
# List all open PRs
make pr-list

# View PR status
make pr-status

# View PRs in browser
gh pr list

# Open a specific PR
gh pr view 123 --web
```

---

## GitHub Actions Workflow

The workflow (`.github/workflows/ai-review-pr.yml`) runs automatically when triggered and:

1. **Checks for changes** — Verifies there are uncommitted changes
2. **Creates/switches branch** — Creates `ai-review-*` if needed
3. **Stages & commits** — Stages all changes and creates commit
4. **Pushes to GitHub** — Pushes branch to origin
5. **Creates/updates PR** — Creates new PR or updates existing one
6. **Posts comment** — Requests ChatGPT review

### Workflow Inputs

When running via GitHub UI (optional manual trigger):

- `commit_message` — Your commit message (default: "Update via AI assistant")
- `branch_name` — Optional custom branch name (auto-generated if empty)

### PR Metadata

Each PR created by this workflow includes:

- Title: `AI Review: [Your commit message]`
- Body: Explains changes, links to files, instructions for approval
- Label: Can be added manually
- Comment: Review request for ChatGPT

---

## ChatGPT Integration

### How ChatGPT Reviews PRs

1. **Automatic comment posted** — Workflow posts review request
2. **ChatGPT responds** — You (or ChatGPT API) provides feedback
3. **Comment in PR** — Review appears in "Conversation" tab
4. **You decide** — Approve or request changes

### ChatGPT Review Checklist

The automatic comment includes a checklist:

- [ ] Code quality and style consistency
- [ ] No syntax errors
- [ ] Documentation is updated if needed
- [ ] Changes align with project goals
- [ ] No breaking changes to existing functionality

You can reply to the comment with:

```markdown
✅ All items reviewed and approved
```

Or request changes:

```markdown
Please update the spacing in Section 3 before merging
```

---

## Troubleshooting

### No Uncommitted Changes Detected

**Problem:** Script exits saying "no changes detected"

**Solution:**
1. Check what files have changed:
   ```bash
   git status
   ```
2. Stage the files:
   ```bash
   git add .
   ```
3. Re-run the script

### GitHub CLI Not Found

**Problem:** Script says "GitHub CLI not found"

**Reason:** `gh` is optional but recommended

**Solution:**
1. Install GitHub CLI:
   ```bash
   make install-tools
   ```
2. Authenticate:
   ```bash
   gh auth login
   ```
3. Re-run the script (will now show full automation output)

### PR Already Exists for This Branch

**Problem:** Running the script again for the same branch

**Result:** Workflow will update the existing PR instead of creating a new one

**This is expected!** Use this to:
- Add more commits to the same PR
- Update the PR description
- Keep feedback in one place

To start a fresh PR, use a different branch name:
```bash
python3 scripts/create_pr.py "Message" "new-branch-name"
```

### Workflow Didn't Trigger

**Problem:** Nothing happened after running script

**Reason:** GitHub Actions workflow might have failed

**Solution:**
1. Check GitHub Actions logs:
   ```bash
   gh run list --workflow ai-review-pr.yml
   ```
2. View run details:
   ```bash
   gh run view <RUN_ID> --log
   ```
3. Check your git config:
   ```bash
   git config --list | grep user
   ```

### Can't Merge PR (Permission Denied)

**Problem:** GitHub says you can't merge this PR

**Reason:** May need admin approval or repo settings require reviews

**Solution:**
1. Ensure your GitHub account has write access
2. Check branch protection rules (might require approval first)
3. Ask repository admin for access if needed

---

## Configuration

### PR Title & Body Template

Edit `.github/workflows/ai-review-pr.yml` lines 147-164 to customize:

```yaml
const title = 'AI Review: ${{ github.event.inputs.commit_message }}';
const body = `## AI-Assisted Changes
...`;
```

### ChatGPT Review Comment

Edit lines 200-220 to customize the review request:

```yaml
const reviewRequestBody = `## 🤖 AI Review Required
...`;
```

### Branch Naming

Change the branch naming pattern in `scripts/create_pr.py` or `scripts/pr.sh`:

**Python version** (line 140):
```python
BRANCH_NAME = f"ai-review-{int(datetime.now().timestamp())}"
```

**Bash version** (line 46):
```bash
BRANCH="ai-review-$(date +%s)"
```

Custom example:
```bash
BRANCH="feature/$(date +%Y%m%d)-custom-name"
```

---

## Best Practices

### 1. Always Stage Changes First

```bash
git add .          # Stage all
# Or
git add src/       # Stage specific files
```

### 2. Use Clear Commit Messages

```bash
make pr MSG="Expand Component Library with founder, problem, manifesto sections"
# Better than
make pr MSG="update"
```

### 3. Review PR Before Merging

1. Click the PR link in the output
2. Read the "Files changed" tab
3. Check ChatGPT's comments
4. Approve if satisfied
5. Click "Merge pull request"

### 4. Keep Branches Clean

Periodically clean up old branches:
```bash
make pr-clean       # Interactive cleanup
# Or manually
git branch -D old-branch-name
```

### 5. Never Force Push to Main

The workflow prevents this automatically by:
- Always creating feature branches
- Never touching `main` directly
- Requiring manual merge approval

---

## Workflow Guarantees

✓ **Main branch is never touched** — Only feature branches are created/pushed  
✓ **No force pushes** — History is preserved  
✓ **No hidden commits** — All commits are visible in PR  
✓ **ChatGPT can review** — Workflow posts review request automatically  
✓ **You merge manually** — Full control over when changes hit main  
✓ **One command to start** — `make pr` handles everything  

---

## Examples

### Example 1: Update Component Library

```bash
# Edit docs/04-COMPONENT-LIBRARY.md
nano docs/04-COMPONENT-LIBRARY.md

# Stage and create PR
git add docs/
make pr MSG="Add Founder Letter and Manifesto component specs"

# Workflow:
# ✓ Created branch: ai-review-1689123456
# ✓ Committed changes
# ✓ Pushed to GitHub
# ✓ Created PR #42
# ✓ Posted review request

# Now review at: https://github.com/.../pull/42
# Get ChatGPT feedback
# Manually click "Merge pull request"
```

### Example 2: Multiple Changes

```bash
# Make several changes across files
git add .

# Create PR with detailed message
make pr MSG="Refactor design system: update colors, spacing, typography"

# All changes in one atomic PR
# Easy to review
# Easy to revert if needed
```

### Example 3: Emergency Hotfix

```bash
# Quick fix
git add src/bug-fix.js

make pr MSG="Fix critical bug in PDP gallery"

# Fast-track review and merge
```

---

## Limitations & Workarounds

### Can't Merge Without Approval?

Branch protection might require approval. Add the approver:
```bash
gh pr review <PR_NUMBER> --approve
```

### Need to Cancel a PR?

Close the PR manually on GitHub, or:
```bash
gh pr close <PR_NUMBER>
```

### Want to Add More Commits to a PR?

Just push to the same branch:
```bash
git add .
git commit -m "Additional changes"
git push origin ai-review-12345
```

The PR will automatically update!

---

## Security

### Authentication

- Workflow uses GitHub's built-in `GITHUB_TOKEN` (safe)
- No personal tokens stored
- No passwords transmitted
- All operations are read-from-remote or push-to-remote (no deletions)

### Access Control

- Only PR creator can merge
- Main branch never modified by workflow
- All changes visible in PR
- Requires manual approval before merge

---

## Support & Debugging

### Enable Debug Output

```bash
export DEBUG=1
python3 scripts/create_pr.py "Message"
```

### Check GitHub Actions Logs

```bash
# List recent runs
gh run list --workflow ai-review-pr.yml --limit 5

# View specific run
gh run view <RUN_ID> --log
```

### Manual PR Creation (Fallback)

If automation fails, create PR manually:

```bash
# Ensure branch is pushed
git push -u origin your-branch

# Create PR via CLI
gh pr create --base main --head your-branch --title "Your PR Title"

# Or via GitHub UI: https://github.com/.../pulls/new
```

---

## Future Enhancements

- [ ] Auto-add labels based on files changed
- [ ] Auto-request reviewers from team
- [ ] Generate changelog from commits
- [ ] Run automated tests before PR
- [ ] Post summary stats (files changed, lines added)

---

## Questions?

For issues or improvements:

1. Check this document first (troubleshooting section)
2. Review GitHub Actions logs
3. Test the script manually
4. Check git status and recent commits

---

**Last Updated:** 2026-07-12  
**Status:** Production-ready  
**Maintainer:** AI Assistant  
