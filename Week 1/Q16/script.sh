#!/bin/bash

# Define variables
ZIP_FILE="q-move-rename-files.zip"
EXTRACT_DIR="extracted"
FINAL_DIR="final_files"

# Step 1: Extract the ZIP file
unzip "$ZIP_FILE" -d "$EXTRACT_DIR"

# Step 2: Create a final directory to store all files
mkdir -p "$FINAL_DIR"

# Step 3: Move all files from subdirectories to FINAL_DIR
find "$EXTRACT_DIR" -type f -exec mv {} "$FINAL_DIR" \;

# Step 4: Rename files, replacing each digit with the next (9→0)
cd "$FINAL_DIR"

for file in *; do
    new_name=$(echo "$file" | sed 's/0/1/g; s/1/2/g; s/2/3/g; s/3/4/g; s/4/5/g; s/5/6/g; s/6/7/g; s/7/8/g; s/8/9/g; s/9/0/g')
    mv "$file" "$new_name"
done

echo "Processing complete. Files are in '$FINAL_DIR'."
