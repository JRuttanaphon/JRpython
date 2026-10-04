import os
import shutil
import sys
import argparse
import logging
from pathlib import Path
from datetime import datetime

FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".pptx", ".csv"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".wmv"],
    "Audio": [".mp3", ".wav", ".flac", ".aac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".cpp", ".c", ".json"],
    "Others": []
}

def setup_logging(log_path):
    logging.basicConfig(
        filename=log_path,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(logging.Formatter("%(message)s"))
    logging.getLogger().addHandler(console)

def get_category(extension):
    for category, extensions in FILE_CATEGORIES.items():
        if extension.lower() in extensions:
            return category
    return "Others"

def organize_folder(target_dir, dry_run=False):
    target_path = Path(target_dir)
    if not target_path.exists():
        logging.error(f"Path does not exist: {target_dir}")
        return

    moved_count = 0
    skipped_count = 0

    for item in target_path.iterdir():
        if item.is_dir():
            continue

        extension = item.suffix
        category = get_category(extension)
        category_folder = target_path / category

        if not category_folder.exists() and not dry_run:
            category_folder.mkdir(parents=True, exist_ok=True)

        destination = category_folder / item.name

        if destination.exists():
            skipped_count += 1
            logging.warning(f"Skipped (already exists): {item.name}")
            continue

        if dry_run:
            logging.info(f"[DRY RUN] Would move: {item.name} -> {category}/")
        else:
            shutil.move(str(item), str(destination))
            logging.info(f"Moved: {item.name} -> {category}/")

        moved_count += 1

    logging.info(f"Done. {moved_count} files processed, {skipped_count} skipped.")

def main():
    parser = argparse.ArgumentParser(description="Organize files in a folder by type")
    parser.add_argument("directory", help="Path to the folder to organize")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without moving files")
    args = parser.parse_args()

    log_filename = f"organizer_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    log_path = Path(args.directory) / log_filename
    setup_logging(str(log_path))

    organize_folder(args.directory, dry_run=args.dry_run)

if __name__ == "__main__":
    main()