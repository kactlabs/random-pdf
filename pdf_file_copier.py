import os
import shutil
from pathlib import Path
from dotenv import load_dotenv


def copy_pdf_files(source_folder, dest_folder):
    """
    Copy all PDF files from source folder to destination folder.
    
    Args:
        source_folder: Path to source directory
        dest_folder: Path to destination directory
    """
    source_path = Path(source_folder)
    dest_path = Path(dest_folder)
    
    # Check if source folder exists
    if not source_path.exists():
        print(f"Error: Source folder '{source_folder}' does not exist.")
        return
    
    # Create destination folder if it doesn't exist
    dest_path.mkdir(parents=True, exist_ok=True)
    
    # Find all PDF files in source folder
    pdf_files = list(source_path.glob('*.pdf'))
    
    if not pdf_files:
        print(f"No PDF files found in '{source_folder}'")
        return
    
    # Copy each PDF file
    copied_count = 0
    for pdf_file in pdf_files:
        try:
            dest_file = dest_path / pdf_file.name
            shutil.copy2(pdf_file, dest_file)
            print(f"Copied: {pdf_file.name}")
            copied_count += 1
        except Exception as e:
            print(f"Error copying {pdf_file.name}: {e}")
    
    print(f"\nTotal files copied: {copied_count}/{len(pdf_files)}")


if __name__ == "__main__":
    # Load environment variables from .env file
    load_dotenv()
    
    SOURCE_FOLDER = os.getenv("SOURCE_FOLDER")
    DEST_FOLDER = os.getenv("DEST_FOLDER")
    
    if not SOURCE_FOLDER or not DEST_FOLDER:
        print("Error: SOURCE_FOLDER and DEST_FOLDER must be set in .env file")
        exit(1)
    
    copy_pdf_files(SOURCE_FOLDER, DEST_FOLDER)
