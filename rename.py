import shutil
import os

files = os.listdir("./") 

for key in range(0, len(files)):
#    print(files[key])
   startInx = files[key].find('(')
   endInx =files[key].rfind(')')
   if(startInx != -1 and endInx != -1):
    newName = "".join((files[key][:startInx-1],'',files[key][endInx+1:]))
    print(files[key]+":"+newName)
    shutil.move("./" + files[key],"./" + newName)
    print(files[key])

# s="cdabcjkewabcef"
# snew="".join((s[:9],"###",s[12:]))