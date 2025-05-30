
import os
import zipfile 
from zipfile import ZipFile

path2_file='/content/sample_data/HRcommasep1603576336980.zip'

print(os.getcwd())
#extract_path='/content/sample_data/HRcommasep1603576336980.zip'

extract_path='/content/ExtFile'

with zipfile.ZipFile('/content/sample_data/HRcommasep1603576336980.zip', 'r') as zip_ref:
       zip_ref.extractall('extract_path')
       print('File Extraction Successfull:')
