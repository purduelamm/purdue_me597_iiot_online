import os
import shutil

def replace_in_files(directory, old_string, new_string):
    """
    Recursively search all files in the directory and subdirectories,
    and replace the specified old_string with new_string.
    """
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)

            # Check file extension to process only text-based files
            if file_name.endswith(('.ipynb', '.html', '.txt', '.md', '.py', '.json')):
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        content = file.read()
                    
                    # If the old_string exists in the file, replace it
                    if old_string in content:
                        # Replace content and save changes
                        updated_content = content.replace(old_string, new_string)
                        with open(file_path, 'w', encoding='utf-8') as file:
                            file.write(updated_content)
                        print(f"Updated: {file_path}")
                except Exception as e:
                    print(f"Error processing file {file_path}: {e}")

# Specify the directory, old string, and new string
target_directory = f"D:\Github\purdue_me597_iiot_online_online"  # Change to your target directory
old_string = "purdue_me597_iiot_online"
new_string = "purdue_me597_iiot_online_online"

# Call the function
replace_in_files(target_directory, old_string, new_string)
