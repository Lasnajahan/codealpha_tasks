
import os
import shutil

# Source folder containing JPG files
source_folder = input("Enter the folder path containing JPG files: ")

# Destination folder
destination_folder = os.path.join(source_folder, "JPG_Images")

# Create destination folder if it doesn't exist
os.makedirs(destination_folder, exist_ok=True)

# Move JPG files
count = 0

for filename in os.listdir(source_folder):
    if filename.lower().endswith(".jpg"):
        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(destination_folder, filename)

        if os.path.isfile(source_path):
            shutil.move(source_path, destination_path)
            count += 1

print(f"\nSuccessfully moved {count} JPG file(s).")
print(f"Destination folder: {destination_folder}")

