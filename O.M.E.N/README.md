# 🔮 OMEN  
### Organising Manual Entities Nicely

OMEN is a **professional yet simple Python automation tool** that automatically organizes files in a folder based on their type.

Instead of manually dragging PDFs, images, ZIPs, and spreadsheets every day, OMEN does it for you — safely, predictably, and transparently.

---

## Why OMEN?

Most people have a Downloads folder that looks like chaos.

OMEN helps you:
- clean messy folders in seconds
- save time every week
- avoid manual file sorting
- keep your workspace organised
- use automation in real, practical workflows

This is **not a demo project**.  
This is something you can actually use at work.

---

## How OMEN Works

OMEN:
1. Scans all files in a given folder
2. Detects file types using extensions
3. Creates category folders if needed
4. Moves files into the right folders
5. Logs every action
6. Saves a manifest for reference or undo
7. Supports a **dry-run mode** for safety

---

## File Categories (Default)

OMEN organizes files into these folders by default:

| Category        | Extensions |
|-----------------|------------|
| Images          | `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp` |
| Documents       | `.pdf`, `.docx`, `.doc`, `.txt`, `.pptx` |
| Spreadsheets    | `.xls`, `.xlsx`, `.csv` |
| Archives        | `.zip`, `.tar`, `.gz`, `.rar` |
| Videos          | `.mp4`, `.mkv`, `.mov`, `.avi` |
| Misc            | Anything not listed above |

Files with unknown or no extensions are safely moved to **`Misc/`**.

---

## Dry Run Mode (Very Important)

OMEN supports a **dry-run** mode.

Dry-run:
- shows what would happen
- does NOT move any files
- does NOT change your system
- helps you preview actions safely

Think of it as **practice mode**.

---

## How to Run OMEN
### MAC
python3 main.py --path ~/folder_name
python3 main.py --path ~/folder_name --dry-run

### Windows
python main.py --path "C:/Users/YourName/folder_name" --dry-run
python main.py --path "C:/Users/YourName/folder_name"

### Save the script
Save the Python file as:

