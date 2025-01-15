import os

def rename_files_in_folder(folder_path, reference_name):
    # List all files in the folder
    files = os.listdir(folder_path)
    
    # Iterate over each file in the folder
    for file_name in files:
        # Construct the old file path
        old_file_path = os.path.join(folder_path, file_name)
        
        # Check if it is a file (not a directory)
        if os.path.isfile(old_file_path):
            # Construct the new file name by adding the reference name at the beginning
            new_file_name = reference_name + "_" + file_name
            
            # Construct the new file path
            new_file_path = os.path.join(folder_path, new_file_name)
            
            # Rename the file
            os.rename(old_file_path, new_file_path)
            print(f"Renamed: {old_file_path} -> {new_file_path}")

# Example usage
folder_path = "path/to/your/folder"
reference_name = "reference"
rename_files_in_folder(folder_path, reference_name)

#______


#To use this script:
#1. Replace `"path/to/your/folder"` with the path to the folder containing the files you want to rename.
#2. Replace `"reference"` with the reference name you want to add to the beginning of each file name.
#3. Run the script.
