import os
import shutil

def move_files(source_dir, json_dest_dir, pdf_dest_dir, verbose=True):
    """
    Move all .json files to json_dest_dir and all .pdf files to pdf_dest_dir from source_dir.

    Args:
        source_dir (str): Path to the directory containing files.
        json_dest_dir (str): Path to the directory where .json files will be moved.
        pdf_dest_dir (str): Path to the directory where .pdf files will be moved.
        verbose (bool): If True, prints progress messages. Defaults to True.

    Returns:
        None
    """
    try:
        # Ensure source directory exists
        if not os.path.exists(source_dir):
            raise FileNotFoundError(f"Source directory does not exist: {source_dir}")

        # Create destination directories if they don't exist
        for dir_path in [json_dest_dir, pdf_dest_dir]:
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
                if verbose:
                    print(f"Created directory: {dir_path}")

        # Loop through files once and segregate
        for file_name in os.listdir(source_dir):
            src_path = os.path.join(source_dir, file_name)
            if not os.path.isfile(src_path):  # Skip directories or invalid files
                continue

            if file_name.endswith('.json'):
                dest_path = os.path.join(json_dest_dir, file_name)
            elif file_name.endswith('.pdf'):
                dest_path = os.path.join(pdf_dest_dir, file_name)
            else:
                continue  # Skip non-matching files

            try:
                shutil.move(src_path, dest_path)
                if verbose:
                    print(f"Moved: {file_name} -> {dest_path}")
            except shutil.Error as move_err:
                print(f"Error moving {file_name}: {move_err}")

    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except PermissionError as perm_error:
        print(f"Permission error: {perm_error}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Example usage:
source_directory = r"C:/Users/chris/Documents/pdfs"
json_destination_directory = r"C:/Users/chris/OneDrive/Documents/GPT Reference Files/gpt_jsons"
pdf_destination_directory = r"C:/Users/chris/OneDrive/Documents/GPT Reference Files/working PDFs"

# Uncomment the line below to run the function:
move_files(source_directory, json_destination_directory, pdf_destination_directory)

