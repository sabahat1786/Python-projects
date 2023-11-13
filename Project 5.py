import os
import re
import shutil

# Function to rename files in a directory based on a specified pattern
def rename_files_in_directory(directory_path, pattern):
    try:
        # Iterate through files in the directory
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)

            # Check if the file matches the specified pattern
            if re.match(pattern, filename):
                # Construct the new name based on the pattern
                new_name = re.sub(pattern, r'\1_new_name\2', filename)

                # Create the full path for the new file name
                new_file_path = os.path.join(directory_path, new_name)

                # Rename the file
                shutil.move(file_path, new_file_path)
                print(f'Renamed: {filename} to {new_name}')
    
    except Exception as e:
        print(f'An error occurred: {str(e)}')

# Input: Directory path and the pattern to match
directory_path = input("Enter the directory path: ")
pattern = input("Enter the pattern to match (use regular expressions): ")

# Call the function to rename files based on the pattern
rename_files_in_directory(directory_path, pattern)

print("File renaming completed.")
