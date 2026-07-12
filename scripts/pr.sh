#!/bin/bash

# Barreletics AI Review PR Automation
# One-command workflow: stages, commits, pushes, and creates PR automatically

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Default values
COMMIT_MESSAGE="${1:-Update via AI assistant}"
BRANCH_NAME="${2:-}"
REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || echo '.')"

# Helper functions
print_header() {
  echo -e "\n${BLUE}=== $1 ===${NC}\n"
}

print_success() {
  echo -e "${GREEN}✓ $1${NC}"
}

print_error() {
  echo -e "${RED}✗ $1${NC}"
}

print_warning() {
  echo -e "${YELLOW}⚠ $1${NC}"
}

# Check if we're in a git repository
if ! git rev-parse --git-dir > /dev/null 2>&1; then
  print_error "Not in a git repository"
  exit 1
fi

# Check if we're on main (shouldn't be modifying main directly)
CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)
if [ "$CURRENT_BRANCH" = "main" ]; then
  print_warning "You're on the 'main' branch"
  echo "This script is designed to work on feature/ai-review branches."
  echo "You can still use it, but be careful."
fi

print_header "Barreletics AI Review PR Workflow"

# Step 1: Check for uncommitted changes
echo "Step 1: Checking for changes..."
if git diff-index --quiet HEAD --; then
  print_warning "No uncommitted changes detected"
  echo "Did you forget to save your changes or stage files?"
  echo ""
  echo "To see unstaged changes:"
  echo "  git status"
  echo ""
  exit 0
else
  print_success "Changes detected"
  echo ""
  echo "Files with changes:"
  git diff --stat
  echo ""
fi

# Step 2: Display changes summary
echo "Step 2: Commit message"
echo "Message: \"${COMMIT_MESSAGE}\""
echo ""

# Confirm before proceeding
read -p "Proceed with this commit message? (y/n) " -n 1 -r
echo ""
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
  print_warning "Cancelled by user"
  exit 0
fi

# Step 3: Generate branch name if not provided
if [ -z "$BRANCH_NAME" ]; then
  BRANCH_NAME="ai-review-$(date +%s)"
  print_success "Generated branch name: $BRANCH_NAME"
else
  print_success "Using branch: $BRANCH_NAME"
fi
echo ""

# Step 4: Create/switch to branch
print_header "Creating/Switching to Branch"
if git rev-parse --verify "$BRANCH_NAME" > /dev/null 2>&1; then
  print_warning "Branch already exists, checking it out"
  git checkout "$BRANCH_NAME"
else
  print_success "Creating new branch: $BRANCH_NAME"
  git checkout -b "$BRANCH_NAME"
fi
echo ""

# Step 5: Stage changes
print_header "Staging Changes"
git add -A
print_success "All changes staged"
echo ""
echo "Files to commit:"
git diff --cached --stat
echo ""

# Step 6: Commit
print_header "Creating Commit"
git commit -m "$COMMIT_MESSAGE"
print_success "Commit created"
echo ""
git log -1 --oneline
echo ""

# Step 7: Push to remote
print_header "Pushing to Remote"
echo "Pushing branch '$BRANCH_NAME' to origin..."
git push -u origin "$BRANCH_NAME"
print_success "Branch pushed to origin"
echo ""

# Step 8: Trigger GitHub Actions workflow
print_header "Triggering GitHub Actions"
echo "Triggering AI Review PR workflow..."
echo ""

# Use GitHub CLI if available, otherwise provide manual instructions
if command -v gh &> /dev/null; then
  print_success "GitHub CLI found, triggering workflow..."
  gh workflow run ai-review-pr.yml \
    -f commit_message="$COMMIT_MESSAGE" \
    -f branch_name="$BRANCH_NAME"
  print_success "Workflow triggered"
  echo ""
  echo "Workflow will:"
  echo "  1. Create/update Pull Request"
  echo "  2. Post review request comment"
  echo "  3. Wait for your approval"
  echo ""
else
  print_warning "GitHub CLI not found"
  echo ""
  echo "To complete PR creation manually:"
  echo "  1. Go to: https://github.com/barreletics/Barreletics-Design-Review"
  echo "  2. Click 'New Pull Request'"
  echo "  3. Select 'compare: $BRANCH_NAME'"
  echo "  4. Click 'Create Pull Request'"
  echo ""
  echo "Or install GitHub CLI (gh) for full automation:"
  echo "  https://cli.github.com"
  echo ""
fi

# Final summary
print_header "Summary"
echo "Branch: $BRANCH_NAME"
echo "Commit: $COMMIT_MESSAGE"
echo "Status: ✅ Ready for PR review"
echo ""
echo "Next steps:"
echo "  1. Wait for PR creation (GitHub Actions will handle it)"
echo "  2. Review the PR at: https://github.com/barreletics/Barreletics-Design-Review/pulls"
echo "  3. Get ChatGPT review in PR comments"
echo "  4. Approve and merge manually"
echo ""
print_success "Workflow complete!"
