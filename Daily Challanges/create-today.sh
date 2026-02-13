#!/bin/bash

# Get today's date in YYYY-MM-DD format
today=$(date +%Y-%m-%d)
year=$(date +%Y)
month=$(date +%m)
month_name=$(date +%B)

# Create folder name in format YYYY-MM-MonthName
folder_name="${year}-${month}-${month_name}"
folder_path="Daily Challanges/${folder_name}"

# Create folder if it doesn't exist
mkdir -p "$folder_path"

# Create both .py and .js files
touch "$folder_path/${today}.py"
touch "$folder_path/${today}.js"

echo "✅ Created files for $today:"
echo "   - $folder_path/${today}.py"
echo "   - $folder_path/${today}.js"
