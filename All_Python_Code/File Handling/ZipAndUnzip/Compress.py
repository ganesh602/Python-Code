from zipfile import *
import os

zipPath = "D:\Python\Git Tutorials\Websites\Python_Code\All_Python_Code\File Handling\ZipAndUnzip\images.zip"
imagePath = ["D:\Python\Git Tutorials\Websites\Python_Code\All_Python_Code\File Handling\ZipAndUnzip\Images\img1.jpg",
"D:\Python\Git Tutorials\Websites\Python_Code\All_Python_Code\File Handling\ZipAndUnzip\Images\img2.jpg",
"D:\Python\Git Tutorials\Websites\Python_Code\All_Python_Code\File Handling\ZipAndUnzip\Images\img3.jpg",
"D:\Python\Git Tutorials\Websites\Python_Code\All_Python_Code\File Handling\ZipAndUnzip\Images\img4.jpg",
"D:\Python\Git Tutorials\Websites\Python_Code\All_Python_Code\File Handling\ZipAndUnzip\Images\img5.png"]

with ZipFile(zipPath,'w',ZIP_DEFLATED) as file:
    for img_path in imagePath:                      # imagePath - list which stores all the Image Path.
        baseName = os.path.basename(img_path)       # os.path.base - will get the last name after last slash i.e file name.
        file.write(img_path,baseName)               # img_path - is the image path, baseName - is the File name.
