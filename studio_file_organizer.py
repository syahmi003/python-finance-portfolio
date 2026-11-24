import os
import shutil

# Define folder categories and their corresponding file extensions
FILE_CATEGORIES = {
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Audio_Podcasts": [".mp3", ".wav", ".aac", ".m4a"],
    "Images_Thumbnails": [".jpg", ".jpeg", ".png", ".webp", ".svg"],
    "Documents_Reports": [".pdf", ".docx", ".txt", ".xlsx", ".csv"],
}


def organize_directory(target_folder):
    """
    Scans a target directory and automatically moves files into categorized subfolders
    based on their file extensions.
    """
    if not os.path.exists(target_folder):
        print(f"Error: The folder path '{target_folder}' does not exist.")
        return

    moved_count = 0
    print(f"\nScanning directory: {target_folder}...")

    for filename in os.listdir(target_folder):
        file_path = os.path.join(target_folder, filename)

        # Skip subfolders and hidden system files
        if os.path.isdir(file_path) or filename.startswith("."):
            continue

        # Extract the file extension in lowercase
        _, extension = os.path.splitext(filename)
        extension = extension.lower()

        destination_category = "Others"
        for category, extensions in FILE_CATEGORIES.items():
            if extension in extensions:
                destination_category = category
                break

        # Create category subfolder if it doesn't exist yet
        category_folder = os.path.join(target_folder, destination_category)
        os.makedirs(category_folder, exist_ok=True)

        # Move the file safely (avoid overwriting if file with same name exists)
        destination_path = os.path.join(category_folder, filename)
        if os.path.exists(destination_path):
            base_name, ext = os.path.splitext(filename)
            destination_path = os.path.join(category_folder, f"{base_name}_copy{ext}")

        shutil.move(file_path, destination_path)
        print(f"Moved: {filename}  --->  {destination_category}/")
        moved_count += 1

    print("-" * 50)
    if moved_count == 0:
        print("Directory is already clean! No loose files found to organize.")
    else:
        print(f"Success! Organized {moved_count} file(s) into categorized folders.")


def main():
    print("=== AUTOMATED STUDIO MEDIA & DOCUMENT ORGANIZER ===")
    print("Tip: Do NOT run this directly on your Python code folder!")
    folder_path = input("Enter the full path of the messy folder to organize: ").strip().strip('"')

    if not folder_path:
        print("Error: Folder path cannot be empty.")
        return

    confirm = input(f"Are you sure you want to organize all files in '{folder_path}'? (y/n): ").strip().lower()
    if confirm == "y":
        organize_directory(folder_path)
    else:
        print("Operation cancelled.")


if __name__ == "__main__":
    main()
