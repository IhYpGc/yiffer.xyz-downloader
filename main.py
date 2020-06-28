## JSMNN'S YIFFER.XYZ DOWNLOADER
## IF YOU THINK IT'S UGLY; YOU'RE ABSOLUTELY RIGHT, IT'S MY FIRST PYTHON CODE.

import requests
import ctypes
import sys
import os
import zipfile
import shutil
ctypes.windll.kernel32.SetConsoleTitleW("JSMNN's Yiffer.XYZ Downloader")

print("If you want to download more comics than one, please put a ', ' between them.")
websiteURL = str(input("Please enter yiffer.xyz URL(s): "))
splittedinput, comicnameholder = [], []

## VARIABLES
INDEX_URL    = "https://yiffer.xyz/"
COMICS_URL   = INDEX_URL + "comics/"

CBZ = 1

## MAIN CODE
if INDEX_URL in websiteURL:
    splittedinput = websiteURL.split(', ')

    for i in splittedinput:
        comicnameholder.append(i.replace(INDEX_URL, ""))

    for i in comicnameholder:
        A_02          = 1                      						## USED FOR LOOPING FILES (01.jpg, 02.jpg, numbers are A_02)
        A_02B         = True                   						## USED FOR WHILE LOOP :DDDD, IF THERE'S AN ERROR (DATA.status_code != requests.codes.ok)
        
        if CBZ == 1:
            DirectoryPath = "Download"
        else:
            DirectoryPath = sys.path[0] + "\\" + i.replace("%20", " ")  ## EXPLAINS ITSELF.            
        
        DirectoryPath2 = sys.path[0] + "\\" + i.replace("%20", " ")  ## EXPLAINS ITSELF.            

        if not os.path.exists(DirectoryPath):
            os.mkdir(DirectoryPath)
            print("[Created Directory for Comic]: " + i.replace("%20", " "))
            while A_02B == True:
                DATA = requests.get("https://yiffer.xyz/comics/" + i.replace(
                    ' ', "%20") + "/" + "{0:02d}".format(A_02) + ".jpg", stream=True)
                if DATA.status_code == requests.codes.ok:
                	with open(DirectoryPath + "\\" + "{0:02d}".format(A_02) + ".jpg",'wb') as f:
                		for block in DATA.iter_content(1024):
                			if not block:
                				break
                			f.write(block)
                	print("[Downloaded]: " + str(A_02))
                	A_02 = A_02 + 1
                else:
                    print("[Done Downloading]: " + i)
                    A_02B = False

        if CBZ == 1:
            comic_zip = zipfile.ZipFile(DirectoryPath2+'.cbz', 'w')
            for folder, subfolders, files in os.walk(DirectoryPath):
                for file in files:
                    comic_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), DirectoryPath), compress_type = zipfile.ZIP_DEFLATED)
            comic_zip.close()
            shutil.rmtree(DirectoryPath, ignore_errors=False, onerror=None)

        else:
            print("[Directory exists]: " + DirectoryPath)