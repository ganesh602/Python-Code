from zipfile import *

zipPath = "D:\Python\Git Tutorials\Websites\Python_Code\All_Python_Code\File Handling\ZipAndUnzip\images.zip"

with ZipFile(zipPath,'r',ZIP_DEFLATED) as file:
    file.extractall("D:\Python\Git Tutorials\Websites\Python_Code\All_Python_Code\File Handling\ZipAndUnzip\DecompressFiles")

