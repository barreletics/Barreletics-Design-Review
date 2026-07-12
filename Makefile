.PHONY: help pr pr-python pr-bash pr-status pr-list pr-clean install-tools

# Default to Python version (more robust)
DEFAULT_SHELL := /bin/bash

help:
	@echo "Barreletics PR Automation Commands"
	@echo ""
	@echo "Usage:"
	@echo "  make pr [MSG='Your commit message']"
	@echo "  make pr MSG='Update components'"
	@echo ""
	@echo "Advanced:"
	@echo "  make pr-python MSG='...'     Use Python version (recommended)"
	@echo "  make pr-bash MSG='...'       Use Bash version"
	@echo "  make pr-status               Check PR status via GitHub CLI"
	@echo "  make pr-list                 List all open PRs"
	@echo "  make install-tools           Install GitHub CLI"
	@echo ""
	@echo "Examples:"
	@echo "  make pr                                    # Uses default message"
	@echo "  make pr MSG='Add new components'          # Custom message"
	@echo "  make pr-python MSG='Update design system' # Force Python"
	@echo ""

# Default pr target - uses Python if available, falls back to bash
pr: MSG = Update via AI assistant
pr: check-changes
	@if command -v python3 >/dev/null 2>&1; then \
		$(MAKE) pr-python MSG="$(MSG)"; \
	else \
		echo "⚠ Python3 not found, using Bash version"; \
		$(MAKE) pr-bash MSG="$(MSG)"; \
	fi

# Python version (recommended)
pr-python: MSG = Update via AI assistant
pr-python: check-changes
	@echo "Using Python PR automation..."
	@python3 scripts/create_pr.py "$(MSG)"

# Bash version (lightweight fallback)
pr-bash: MSG = Update via AI assistant
pr-bash: check-changes
	@echo "Using Bash PR automation..."
	@bash scripts/pr.sh "$(MSG)"

# Check if there are uncommitted changes
check-changes:
	@if ! git diff-index --quiet HEAD --; then \
		echo "✓ Changes detected, proceeding..."; \
	else \
		echo "⚠ No uncommitted changes detected"; \
		echo "Stage your changes first: git add <files>"; \
		exit 1; \
	fi

# PR status via GitHub CLI
pr-status:
	@if command -v gh >/dev/null 2>&1; then \
		echo "=== Open PRs ==="; \
		gh pr list --state open; \
	else \
		echo "GitHub CLI not installed. Install with: make install-tools"; \
		exit 1; \
	fi

# List all open PRs
pr-list:
	@if command -v gh >/dev/null 2>&1; then \
		gh pr list --state open --limit 20; \
	else \
		echo "GitHub CLI not installed"; \
		echo "Install with: brew install gh  (macOS)"; \
		echo "Or visit: https://cli.github.com"; \
		exit 1; \
	fi

# Clean up old ai-review branches (local only)
pr-clean:
	@echo "Cleaning up old ai-review branches..."
	@git fetch --prune origin
	@for branch in $$(git branch --list 'ai-review-*'); do \
		echo "Delete local branch: $$branch? (y/n)"; \
		read response; \
		if [ "$$response" = "y" ]; then \
			git branch -D $$branch; \
			echo "Deleted $$branch"; \
		fi; \
	done

# Install GitHub CLI
install-tools:
	@echo "Installing GitHub CLI..."
	@if [[ "$$OSTYPE" == "darwin"* ]]; then \
		echo "macOS detected, using Homebrew..."; \
		brew install gh; \
	elif [[ "$$OSTYPE" == "linux-gnu"* ]]; then \
		echo "Linux detected..."; \
		echo "Follow instructions at: https://cli.github.com"; \
	else \
		echo "Manual installation: https://cli.github.com"; \
	fi
	@echo ""
	@echo "After installation, authenticate with:"
	@echo "  gh auth login"

# Quick reference
.DEFAULT_GOAL := help
