import os
import sys

commandLineArgs = sys.argv

if len(commandLineArgs) > 1:
    pattern = commandLineArgs[1] + "_{}"
else:
    print('Please enter the pattern for the new filenames as a command line argument')
    sys.exit()
    
# Define the directory where the files are located
dir_path = "files" # Or long path eg dir_path = "C:\\Users\\Sharl\\Desktop\\files"

# Initialize a counter variable for naming the files
counter = 1

# Iterate over the files in the directory
for filename in os.listdir(dir_path):
    print("Renaming: " + filename + "...")
    
    # Get the file extension
    file_ext = os.path.splitext(filename)[1]
    
    # Create the new file name based on the pattern and counter
    new_filename = pattern.format(counter) + file_ext
    
    # Rename the file with the new file name
    oldFileName = os.path.join(dir_path, filename)
    newFileName = os.path.join(dir_path, new_filename)
    os.rename(oldFileName, newFileName)
    
    # Increment the counter
    counter += 1
    
print("All files renamed.")
