# AI Life Coach

A folder that turns an AI coding agent (Claude Code, Codex, or anything that reads `AGENTS.md`) into a personal life coach. It keeps a profile of your life and a daily journal, and uses both to give candid, specific advice instead of generic advice.

Everything stays as plain Markdown files on your computer.

## Setup

1. Open this folder in Claude Code (or another agent that reads `AGENTS.md`).
2. Say **"set up my coach"** (or run `/coach-setup` in Claude Code).
3. The coach interviews you about your goals, work, money, family, relationships, health, habits, history and how you want to be coached, and writes `ai_life_coach_profile.md` as you go. It asks in quick numbered batches and follows up on vague answers. Choose quick start (~15–20 min) or the full interview (1–2 hours, can be split). You can stop anytime and resume later.

## Daily use

- Just talk to it: daily updates, decisions, hard situations, check-ins.
- It journals to `journal/YYYY-MM-DD.md` and updates your profile when something important changes.
- Say "off the record" for anything you don't want saved.
- `python export_coaching_context.py` combines your profile and all journals into `coaching_context.md` and copies it to your clipboard, so you can paste your context into a chat app.

## Files

| File | What it is |
|---|---|
| `AGENTS.md` | Coaching instructions (also read via `CLAUDE.md`) |
| `.claude/skills/coach-setup/` | The setup interview and the blank profile template |
| `ai_life_coach_profile.md` | Your profile (created by setup, git-ignored) |
| `journal/` | Your daily entries (git-ignored) |

## Privacy

Your profile, journals and the exported context are listed in `.gitignore`, so pushing this repo won't upload them. If you want to back them up with git, use a **private** repo and remove those lines from `.gitignore`.
