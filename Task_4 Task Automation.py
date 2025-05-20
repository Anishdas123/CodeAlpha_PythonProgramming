import os
import shutil

source_folder = 'C:/Users/Anish Das/Downloads'

file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx'],
    'Videos': ['.mp4', '.mkv', '.avi'],
    'Music': ['.mp3', '.wav'],
    'Archives': ['.zip', '.rar', '.tar'],
    'Scripts': ['.py', '.js', '.sh'],
    'Others': []
}

def organize_files(folder):
    if not os.path.exists(folder):
        print(f"❌ The folder '{folder}' does not exist.")
        return

    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)

        if os.path.isfile(file_path):
            file_ext = os.path.splitext(filename)[1].lower()
            moved = False

            for folder_name, extensions in file_types.items():
                if file_ext in extensions:
                    target_folder = os.path.join(folder, folder_name)
                    os.makedirs(target_folder, exist_ok=True)

                    try:
                        shutil.move(file_path, os.path.join(target_folder, filename))
                        moved = True
                    except PermissionError:
                        print(f"⛔ Skipping '{filename}' (file in use).")
                    break

            if not moved:
                other_folder = os.path.join(folder, 'Others')
                os.makedirs(other_folder, exist_ok=True)
                try:
                    shutil.move(file_path, os.path.join(other_folder, filename))
                except PermissionError:
                    print(f"⛔ Skipping '{filename}' (file in use).")

    print("✅ File organization completed.")

organize_files(source_folder)
