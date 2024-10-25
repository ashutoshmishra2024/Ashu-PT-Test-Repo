import os
import json
import csv
import zipfile

replace_files = {
    "transaction" : "Label",
    "sampleCount" : "# Samples",
    "errorCount" : "errorCount",
    "errorPct" : "Error %",
    "meanResTime" : "Average", 
    "minResTime" : "Min",
    "maxResTime" : "Max",
    "pct1ResTime" : "90% Line",
    "pct2ResTime" : "95% Line",
    "pct3ResTime" : "99% Line",
    "throughput" : "throughput",
    "receivedKBytesPerSec" : "receivedKBytesPerSec",
    "sentKBytesPerSec" : "sentKBytesPerSec"
}

# Output of ls command
import subprocess
subprocess.run(['ls', '-al'])

# Path to the directory you want to navigate to
directory_path = 'home/docker/actions-runner/_work/Ashu-PT-Test-Repo/Ashu-PT-Test-Repo/HTMLReport'

# Change the current working directory
os.chdir(directory_path)

# Verify the current working directory
print("Current working directory:", os.getcwd())

zip_file_path = 'home/docker/actions-runner/_work/Ashu-PT-Test-Repo/Ashu-PT-Test-Repo/HTMLReport'
extraction_dir = 'home/docker/actions-runner/_work/Ashu-PT-Test-Repo/Ashu-PT-Test-Repo/'



# Create the destination directory if it doesn't exist
os.makedirs(extraction_dir, exist_ok=True)

# Unzip the file
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extraction_dir)
print(f'Unzipped {zip_file_path} to {extraction_dir}')


# Function to unzip the folder
#def unzip_folder(zip_file_path, extraction_dir):
 #   with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
  #      zip_ref.extractall(extraction_dir)

# Use the function
#unzip_folder(zip_file_path, extraction_dir)
