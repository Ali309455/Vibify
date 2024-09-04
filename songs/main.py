import os
import json

# Define the folder you want to search
root_folder = "songs"

# Initialize a list to store subfolder names
subfolders = []

# Walk through the directory to find all subfolders
for root, dirs, files in os.walk(root_folder):
    for dir_name in dirs:
        # Get the relative path of the subfolder
        subfolder_path = os.path.join(root, dir_name)
        # Append subfolder info to the list
        subfolders.append(subfolder_path)

# Define the output JSON file path
output_file = "subfolders.json"

# Write the list of subfolders to a JSON file
with open(output_file, "w") as json_file:
    json.dump(subfolders, json_file, indent=4)

print(f"Subfolder names have been written to '{output_file}'.")


# Define the root folder containing songs
root_folder = "songs\\AnuvJain"

# Initialize an empty list to store song information
songs_list = []

# Walk through the directory to find all .mp3 files
for root, dirs, files in os.walk(root_folder):
    for file in files:
        if file.endswith(".mp3"):
            # Get the relative path of the .mp3 file
            relative_path = os.path.join(root, file)
            # Remove the root folder prefix for a cleaner JSON output
            clean_path = relative_path.replace(f"{root_folder}/", "")
            # Append song info to the list
            songs_list.append({"title": file.replace(".mp3", ""), "url": relative_path})

# Define the output file name
output_file = "songs.json"

# Write the list of songs to a JSON file
with open(output_file, "w") as json_file:
    json.dump(songs_list, json_file, indent=4)

print(f"{output_file} has been created with {len(songs_list)} songs.")
