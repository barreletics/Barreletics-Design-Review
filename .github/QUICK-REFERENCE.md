# PR Automation — Quick Reference

## One-Command Workflow

### Default (Recommended)
```bash
make pr
```

### With Custom Message
```bash
make pr MSG="Your commit message here"
```

### Direct Script
```bash
python3 scripts/create_pr.py "Your commit message"
bash scripts/pr.sh "Your commit message"
```

---

## Workflow

| Step | Automatic? | Action |
|------|-----------|--------|
| 1 | ✓ | Check for uncommitted changes |
| 2 | ✓ | Create `ai-review-*` branch |
| 3 | ✓ | Commit changes |
| 4 | ✓ | Push to GitHub |
| 5 | ✓ | Create/update Pull Request |
| 6 | ✓ | Post ChatGPT review request |
| 7 | ✗ | **You review & approve** |
| 8 | ✗ | **You click Merge** |

---

## Before Running

```bash
# 1. Make your changes
nano docs/04-COMPONENT-LIBRARY.md

# 2. Stage them
git add .

# 3. Then run one command
make pr MSG="Your message"
```

---

## After Running

1. **Script outputs PR link** → Click it
2. **Review changes** → Check "Files changed" tab
3. **Read ChatGPT feedback** → In "Conversation" tab
4. **Approve** → Comment ✅ or ✓ Approve button
5. **Merge** → Click "Merge pull request"

---

## Common Tasks

### List Open PRs
```bash
make pr-list
gh pr list
```

### Check PR Status
```bash
make pr-status
```

### View Specific PR
```bash
gh pr view 42 --web
```

### Close a PR (Cancel)
```bash
gh pr close <NUMBER>
```

### Add More Commits to PR
```bash
git add .
git commit -m "More changes"
git push origin ai-review-12345
```

### Install GitHub CLI
```bash
make install-tools
gh auth login
```

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| "No changes detected" | Run `git add .` first |
| "GitHub CLI not found" | Optional but recommended: `make install-tools` |
| "PR already exists" | That's okay, workflow updates it |
| Script doesn't work | Try Python version: `python3 scripts/create_pr.py "msg"` |
| Can't merge PR | Check branch protection rules on GitHub |

---

## Never Have to Do Manually Again

❌ `git checkout -b ai-review-...`  
❌ `git add .`  
❌ `git commit -m "..."`  
❌ `git push origin ...`  
❌ Manual PR creation on GitHub  
❌ Posting review requests  

✅ **Just:** `make pr MSG="..."`

---

## Key Guarantees

- ✓ Main branch **never touched**
- ✓ All changes **visible in PR**
- ✓ **You control** when to merge
- ✓ **ChatGPT reviews** automatically
- ✓ **One command** to start

---

**Need more details?** Read [PR-AUTOMATION.md](PR-AUTOMATION.md)  
**Questions?** Check the Troubleshooting section
