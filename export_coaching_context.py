from pathlib import Path
import shutil
import subprocess

root = Path(__file__).parent
profile = root / "ai_life_coach_profile.md"
journals = sorted((root / "journal").glob("*.md"))

parts = [profile.read_text().rstrip()]
for journal in journals:
    entry = journal.read_text().strip()
    if entry.startswith("# "):
        entry = entry.split("\n", 1)[-1].strip()
    parts.extend([f"\n\n---\n\n# Journal: {journal.stem}\n\n{entry}"])

content = "\n".join(parts) + "\n"
(root / "coaching_context.md").write_text(content)

clipboard = next((shutil.which(cmd) for cmd in ("wl-copy", "xclip", "xsel", "pbcopy", "clip.exe") if shutil.which(cmd)), None)
if clipboard:
    if clipboard.endswith("wl-copy"):
        args = [clipboard, "--paste-once"]
    elif clipboard.endswith(("xclip", "xsel")):
        args = [clipboard, "-selection", "clipboard"]
    else:
        args = [clipboard]
    try:
        subprocess.run(args, input=content, text=True, check=True, capture_output=True, timeout=3)
        print(f"Copied profile and {len(journals)} journal entries to clipboard.")
    except (OSError, subprocess.CalledProcessError, subprocess.TimeoutExpired):
        print("Clipboard unavailable; saved to coaching_context.md only.")
else:
    print("Clipboard tool not found; saved to coaching_context.md only.")
