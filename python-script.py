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

zip_file_path = 'home/docker/actions-runner/_work/Ashu-PT-Test-Repo/Ashu-PT-Test-Repo/HTMLReport'
extraction_dir = 'home/docker/actions-runner/_work/Ashu-PT-Test-Repo/Ashu-PT-Test-Repo/HTMLReport'

zip_path = '/home/docker/actions-runner/_work/Ashu-PT-Test-Repo/Ashu-PT-Test-Repo/HTMLReport'
extract_to = '/home/docker/actions-runner/_work/Ashu-PT-Test-Repo/Ashu-PT-Test-Repo/HTMLReport'


# Function to unzip the folder
def unzip_folder(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

# Use the function
unzip_folder(zip_file_path, extraction_dir)
