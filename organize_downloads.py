import os
import shutil

def organize_files_by_extension(folder_path, extension_destinations):
    # List all files in the folder
    files = os.listdir(folder_path)
    
    # Iterate over each file in the folder
    for file_name in files:
        # Construct the full file path
        file_path = os.path.join(folder_path, file_name)
        
        # Check if it is a file (not a directory)
        if os.path.isfile(file_path):
            # Get the file extension
            _, file_extension = os.path.splitext(file_name)
            
            # Check if the file extension is in the extension_destinations dictionary
            if file_extension in extension_destinations:
                # Get the destination folder for this file extension
                destination_folder = extension_destinations[file_extension]
                
                # Create the destination folder if it doesn't exist
                if not os.path.exists(destination_folder):
                    os.makedirs(destination_folder)
                
                # Construct the destination file path
                destination_file_path = os.path.join(destination_folder, file_name)
                
                # Move the file to the destination folder
                shutil.move(file_path, destination_file_path)
                print(f"Moved: {file_path} -> {destination_file_path}")

# Example usage
folder_path = "path/to/your/downloads/folder"
extension_destinations = {
    ".json": "path/to/json/folder",
    ".step": "path/to/step/folder",
    ".stl": "path/to/stl/folder",
    ".pdf": "path/to/pdf/folder",
    ".3mf": "path/to/3mf/folder"
}

organize_files_by_extension(folder_path, extension_destinations)
