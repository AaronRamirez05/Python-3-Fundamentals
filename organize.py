import os
import shutil

# Define the path to the desktop
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# Define file type categories and their associated extensions
file_categories = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx'],
    'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv'],
    'Audio': ['.mp3', '.wav', '.aac', '.flac'],
    'Code': ['.py', '.java', '.cpp', '.html', '.css', '.js']
}

# Function to create subfolder if it doesn't exist
def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Organize the files
def organize_files():
    for item in os.listdir(desktop_path):
        item_path = os.path.join(desktop_path, item)
        
        # Skip if the item is a directory
        if os.path.isdir(item_path):
            continue
        
        # Get the file extension
        _, file_extension = os.path.splitext(item)
        
        # Move files based on their extension
        for category, extensions in file_categories.items():
            if file_extension.lower() in extensions:
                category_folder = os.path.join(desktop_path, category)
                create_folder(category_folder)
                shutil.move(item_path, category_folder)
                print(f'Moved: {item} -> {category_folder}')
                break

# Run the organization function
if __name__ == "__main__":
    organize_files()