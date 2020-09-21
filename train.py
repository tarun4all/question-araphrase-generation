import zipfile
import requests, zipfile, io
import os

zip_file_url = "https://datascience-models-ramsri.s3.amazonaws.com/t5_paraphraser.zip"
folder_path = zip_file_url.split("/")[-1].replace(".zip","")

if not os.path.exists(folder_path):
    r = requests.get(zip_file_url)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall('./t5_paraphraser')
else:
    print ("Folder available: ",folder_path)