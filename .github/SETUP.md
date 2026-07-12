# PR Automation Setup Guide

This guide walks through enabling the PR automation system in this repository.

## Status

✅ **All files are already in place.**

The workflow is ready to use immediately. No setup required!

---

## What Was Installed

```
.github/
├── workflows/
│   └── ai-review-pr.yml          # GitHub Actions workflow
├── PR-AUTOMATION.md              # Full documentation
├── QUICK-REFERENCE.md            # Quick reference guide
└── SETUP.md                       # This file

scripts/
├── create_pr.py                  # Python automation script
└── pr.sh                          # Bash automation script (fallback)

Makefile                           # Convenience commands
```

---

## Quick Enable

### 1. Verify Files Exist

```bash
ls -la .github/workflows/ai-review-pr.yml
ls -la scripts/create_pr.py
ls -la scripts/pr.sh
cat Makefile
```

All should exist. ✓

### 2. Make Scripts Executable

```bash
chmod +x scripts/create_pr.py
chmod +x scripts/pr.sh
```

### 3. Test It Works

```bash
# See help
make help

# Should show:
# Barreletics PR Automation Commands
# Usage:
#   make pr [MSG='Your commit message']
```

### 4. Optional: Install GitHub CLI

```bash
# macOS
brew install gh

# Linux
sudo apt-get install gh

# Then authenticate
gh auth login
```

---

## Usage

### First Time

```bash
# Stage your changes
git add .

# Create a PR
make pr MSG="Your commit message"

# Follow the prompts, then visit the PR link
```

### Every Time After

```bash
git add .
make pr MSG="Your message"
```

That's it.

---

## What Each File Does

### `.github/workflows/ai-review-pr.yml`

- Runs on GitHub Actions servers
- Triggered by local script
- Automatically creates/updates PR
- Posts review request comment
- **You don't modify this** — it just works

### `scripts/create_pr.py`

- Python version (recommended)
- Better error handling
- Pretty terminal output
- Calls GitHub Actions workflow
- Fallback: Works offline if gh CLI missing

### `scripts/pr.sh`

- Bash version (lightweight)
- No dependencies beyond git
- Fallback if Python unavailable
- Simpler, portable

### `Makefile`

- Convenience shortcuts
- `make pr` — Main command
- `make pr-list` — View PRs
- `make install-tools` — Setup helpers

### `.github/PR-AUTOMATION.md`

- Complete documentation
- Troubleshooting guide
- Configuration options
- Examples and best practices

### `.github/QUICK-REFERENCE.md`

- One-page cheat sheet
- Common commands
- Quick troubleshooting

---

## Verification Checklist

- [ ] Files exist in `.github/workflows/`
- [ ] Scripts exist in `scripts/`
- [ ] Makefile exists in repo root
- [ ] Scripts are executable: `chmod +x scripts/*.py scripts/*.sh`
- [ ] You can run `make help` without errors
- [ ] You have git configured: `git config --list | grep user`
- [ ] Optional: GitHub CLI installed: `gh --version`
- [ ] Optional: Python 3: `python3 --version`

---

## Activation Steps

### Step 1: Make Scripts Executable

```bash
chmod +x scripts/create_pr.py scripts/pr.sh
git add scripts/
git commit -m "Make PR automation scripts executable"
git push origin main
```

### Step 2: Test the System

```bash
# Create a small test change
echo "# Test PR Automation" >> TEST.md

# Stage it
git add TEST.md

# Run the workflow
make pr MSG="Test PR automation setup"

# Verify:
# - Script ran successfully
# - Branch was created and pushed
# - PR was created on GitHub
```

### Step 3: Review and Clean Up

1. Go to: https://github.com/barreletics/Barreletics-Design-Review/pulls
2. See your test PR
3. Delete the test file:
   ```bash
   rm TEST.md
   git add TEST.md
   make pr MSG="Remove test file"
   ```
4. Merge or close the test PR

### Step 4: Document It

You're done! Add this to your team wiki/docs:

```markdown
## PR Workflow

We use automated PR creation:

1. Make changes: `nano file.md`
2. Stage them: `git add .`
3. Create PR: `make pr MSG="Your message"`

That's it. Workflow handles the rest.

See `.github/QUICK-REFERENCE.md` for details.
```

---

## First Real Use

### You:
```bash
# Edit components library
nano docs/04-COMPONENT-LIBRARY.md

# Stage changes
git add docs/

# Create PR
make pr MSG="Expand Component Library with founder sections"
```

### System (Automatic):
✓ Checks for changes  
✓ Creates `ai-review-*` branch  
✓ Commits and pushes  
✓ Creates PR  
✓ Posts review request  

### You (Again):
1. Click PR link
2. Review changes
3. Read ChatGPT feedback
4. Approve (comment ✅)
5. Click "Merge pull request"

**Done.** Changes are in main, and you never touched git commands.

---

## Disable (If Needed)

To temporarily disable the workflow:

1. Go to: `.github/workflows/ai-review-pr.yml`
2. Change `on:` to `on: workflow_dispatch_disabled:` (or delete the file)
3. Commit and push

To re-enable: Revert the change.

---

## Troubleshooting Setup

### "Command not found: make"

Install Make:
```bash
# macOS
brew install make

# Linux
sudo apt-get install make

# Windows (WSL2)
sudo apt-get install make
```

### "No module named 'subprocess'"

Python is missing a standard library. This is rare.

```bash
# Reinstall Python
brew reinstall python3  # macOS
sudo apt-get reinstall python3  # Linux
```

### "Permission denied: scripts/create_pr.py"

Scripts aren't executable:
```bash
chmod +x scripts/create_pr.py scripts/pr.sh
```

### GitHub CLI Auth Error

```bash
gh auth login

# Select "HTTPS"
# Paste your GitHub token or authenticate via browser
```

### "fatal: not a git repository"

You're not in the repo directory:
```bash
cd /path/to/Barreletics-Design-Review
make pr MSG="Your message"
```

---

## Next Steps

1. ✅ Verify files are in place
2. ✅ Make scripts executable: `chmod +x scripts/*.sh scripts/*.py`
3. ✅ Test: `make help`
4. ✅ Optional: Install GitHub CLI: `make install-tools`
5. ✅ Ready to use: `make pr MSG="Your message"`

## Daily Workflow

```bash
# Every time you want to create a PR:
git add .
make pr MSG="Your message"

# Visit the PR link
# Get ChatGPT review
# Manually merge when ready
```

---

## Configuration (Optional)

### Change Branch Naming

Edit `scripts/create_pr.py` line 140 or `scripts/pr.sh` line 46.

### Customize PR Template

Edit `.github/workflows/ai-review-pr.yml` lines 147–220.

### Add Auto-Labels

Edit workflow to add labels to PRs (see GitHub Actions docs).

---

## Support

- **Quick help:** See `.github/QUICK-REFERENCE.md`
- **Full docs:** See `.github/PR-AUTOMATION.md`
- **Troubleshooting:** See both files' troubleshooting sections
- **Debug:** Add `DEBUG=1` before running script

---

## Summary

**Before:** Manual git commands, manual PR creation, wasted time on process.

**After:** `make pr MSG="..."` and you're done.

The system is **ready now**. Start using it today.

```bash
git add .
make pr MSG="Your message"
```

**That's all you need to know.**

---

**Setup complete!** 🎉

Status: ✅ Production-ready  
Last Updated: 2026-07-12  
