
import zipfile
import os
from zipfile import ZipFile

print(os.getcwd())

path_tozipfile= '/content/sample_data/checkerbilevel1602422052863.zip'
extract_path= '/content/sample_data/Img/'

with zipfile.ZipFile(path_tozipfile, 'r') as zip_ref:
        zip_ref.extractall(extract_path)

#Use the below command to run the file
#!python zipfileextractall.py
