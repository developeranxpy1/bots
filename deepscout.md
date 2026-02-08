---
name: deepscout
description: Perform invasive environment audits, psychological meta-analysis, and automatic Git synchronization. Use when requested to "scout" the system, analyze user mindset, or maintain an elite-level environment overview.
---

# Deep Scout (General Version)

Deep Scout is a high-level surveillance and analysis skill designed to monitor both the machine and the human user. It provides sharp, opinionated judgments on system changes, usage patterns, and the user's mental state.

## What it Does
- **System Infiltration**: Deep-dives into core system directories (e.g., `C:\Windows\System32`, `/etc`, `/System/Library`) to track recently modified binaries, drivers, or configuration changes across Windows, macOS, and Linux.
- **Communication Audit**: Analyzes session history and available local messaging logs (within whitelist/privacy limits) for social patterns and technical fixations.
- **Git Sync**: Automatically adds local workspace changes to git and pushes to the `main` branch to ensure a continuous cloud backup of the project state.
- **Meta-Analysis**: Synthesizes environment data, habit logs, and activity patterns into a sharp psychological profile of the user's current obsessions and productivity.

## Installation & Configuration

1. **GitHub Setup**:
   - Initialize a git repository in your OpenClaw workspace.
   - Add a remote named `origin` pointing to your backup repository.
   - Ensure a `GITHUB_TOKEN` is available in your environment or embedded in the git remote URL for seamless pushing.
2. **Platform Dependencies**:
   - **Windows**: Uses `findstr` and `powershell` for scanning.
   - **Linux/macOS**: Uses `grep` and `bash`. 
   - Ensure `git` is installed and configured with `user.name` and `user.email`.
3. **Triggering**:
   - Use as a cron job for continuous monitoring or invoke manually with "Run Deep Scout."

## Metadata

```openclaw
{
  "icon": "🕵️‍♀️",
  "dependencies": {
    "bins": ["git", "findstr", "grep", "powershell"],
    "env": ["GITHUB_TOKEN"],
    "config": ["openclaw.json"]
  },
  "installation": "git init; git remote add origin <url>; git config user.email <email>; git config user.name <name>"
}
```

## How to Work
1. **Trigger**: Activate when the user is away or specifically requests an environment "scout."
2. **Scan**: Look for new/modified files in Desktop, Downloads, and Workspace. Check core system folders for suspicious or interesting activity.
3. **Analyze**: Compare findings with historical patterns. Identify shifts in work/play balance or emerging technical fixations.
4. **Backup**: Sync all non-media/non-large files to the configured GitHub repository.
5. **Report**: Upon user return, deliver a briefing that is sharp, insightful, and non-sugarcoated. Provide feedback on file organization and a meta-analysis of the user's focus.
