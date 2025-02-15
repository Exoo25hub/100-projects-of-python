import os
import shutil

# Define folder categories
CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".tar"],
    "Code": [".py", ".html", ".css", ".js"]
}

def organize_folder(folder_path):
    """Organizes files into categorized folders."""
    if not os.path.exists(folder_path):
        print("Folder does not exist!")
        return

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            file_ext = os.path.splitext(filename)[1].lower()
            
            for category, extensions in CATEGORIES.items():
                if file_ext in extensions:
                    category_path = os.path.join(folder_path, category)
                    os.makedirs(category_path, exist_ok=True)
                    shutil.move(file_path, os.path.join(category_path, filename))
                    print(f"Moved: {filename} → {category}/")
                    break  # Stop checking after finding a match

    print("Files organized successfully!")

# Change this path to the folder you want to organize
folder_to_organize = "C:/Users/YourName/Downloads"
organize_folder(folder_to_organize)
