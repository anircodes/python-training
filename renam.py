import os

# Directory containing the files
directory = '/path/to/your/directory'

# Loop through all files in the directory
for filename in os.listdir(directory):
    old_file = os.path.join(directory, filename)
    
    # Example: Rename files by adding a prefix "new_"
    new_filename = 'new_' + filename
    new_file = os.path.join(directory, new_filename)
    
    # Rename the file
    os.rename(old_file, new_file)

    print(f"Renamed: {old_file} to {new_file}")
