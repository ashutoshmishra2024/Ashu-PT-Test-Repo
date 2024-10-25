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

zip_file_path = /home/docker/actions-runner/_work/Ashu-PT-Test-Repo/Ashu-PT-Test-Repo/HTMLReport
extraction_dir = /home/docker/actions-runner/_work/Ashu-PT-Test-Repo/Ashu-PT-Test-Repo/HTMLReport
