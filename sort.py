
#Program to sort contents of a fle into corresponding directories
# to run this use : python2 sort.py

import os
import shutil



path=raw_input("Give path >")
if not os.path.exists(path):
    print "%s does not exist \n Exiting...."%path
    exit(0)
print "%s exists\n...........\n" %path



####<<<<<<<<<<<<<<<< sortables >>>>>>>>>>>>>>>>>####
dirs={ "txt":"//Text","vid":"//Video","img":"//Images","msc":"//Music","exec":"//Executables","othr":"//Others"}
texts=["txt"]
images=["jpg","png","gif","tif"]
video=["avi","mp4","mov","wmv","flv","mkv"]
music=["mp3","wav"]
execu=["exe","bat","sh","py","php","rpm","deb"]
othr=["doc","pdf","rar","gz","tar"]
####<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>####

path = path.replace("/","//")
print path
for key,val in dirs.items():
    if not os.path.exists(path+val):
        os.mkdir(path+val)
        print "creating directory %s"%val
    else:
        print "%s exits"%val
        continue
fil=[]
    
for folder,subf,filenm in os.walk(path):
    fil.extend(filenm)
       
for fname in fil:
    ext=fname.split(".")
   
    if ext[1] in images:
        shutil.move((path+'//'+fname),(path+dirs["img"]+'//'+fname))
        
    elif ext[1] in texts:
        shutil.move((path+'//'+fname),(path+dirs["txt"]+'//'+fname))

    elif ext[1] in video:
        shutil.move((path+'//'+fname),(path+dirs["vid"]+'//'+fname))

    elif ext[1] in execu:
        shutil.move((path+'//'+fname),(path+dirs["exec"]+'//'+fname))

    elif ext[1] in music:
        shutil.move((path+'//'+fname),(path+dirs["msc"]+'//'+fname))

    elif ext[1] in othr:
        shutil.move((path+'//'+fname),(path+dirs["othr"]+'//'+fname))
        

        
