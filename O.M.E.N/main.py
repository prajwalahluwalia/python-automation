# ==============================================
#   OMEN — Organising My Entities Nicely
#   Professional File Organizer (Simplified)
#   Author: Prajwal Ahluwalia
#   Description: Automatically organizes messy
#                folders by file type.
# ==============================================

import shutil
import argparse
import logging
import csv 
from datetime import datetime
from pathlib import Path

DEFAULT_MAP = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Music": [".mp3", ".wav", ".flac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Others": []
}

def setup_logging(log_file):
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )


def organise(folder: Path, mapping: dict, dry_run: bool, manifest_path: Path):
    if not folder.is_dir():
        logging.error(f"The provided path '{folder}' is not a directory.")
        return

    files = [f for f in folder.iterdir() if f.is_file()]

    for file in files:
        moved = False
        for category, extensions in mapping.items():
            if any(file.name.lower().endswith(ext) for ext in extensions):
                moved = True
                destination_folder = folder/category
                print("Destination Folder:", destination_folder)
                destination_folder.mkdir(exist_ok=True)
                move_files(destination_folder, file, dry_run, manifest_path)
                

        if not moved:
            destination_folder = folder/"Miscellaneous"
            destination_folder.mkdir(exist_ok=True)
            move_files(destination_folder, file, dry_run, manifest_path)

def move_files(destination_folder: Path, file: Path, dry_run: bool, manifest_path: Path):
    target = destination_folder/file.name
    if dry_run:
        print(f"[Dry Run] Would move '{file}' to '{target}'")

    else:
        shutil.move(str(file), str(target))
        logging.info(f"Moved '{file}' to '{target}'")

        with open(manifest_path, 'a', newline='') as manifest_file:
            writer = csv.writer(manifest_file)
            writer.writerow([file.name, str(file), str(target), datetime.now().isoformat()])

if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Organise files in a folder based on their types.")
    parser.add_argument("--path", "-p", required = True, help="Folder to organise")
    parser.add_argument("--dry-run", action="store_true", help="Simulate the organisation without moving files.")
    parser.add_argument("--log-file", type=Path, default="omen.log", help="Path to the log file.")
    parser.add_argument("--manifest", type=Path, default="manifest.csv", help="Path to the manifest CSV file.")

    args = parser.parse_args()

    setup_logging(args.log_file)

    target_folder = Path(args.path).expanduser().resolve()
    mapping = DEFAULT_MAP
    
    print("Starting organising of folder:", target_folder)
    organise(target_folder, mapping, args.dry_run, args.manifest)
    print("Organising completed.")