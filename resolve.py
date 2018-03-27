from PIL import Image
from pytesseract import image_to_string
import pyscreenshot as ImageGrab
from google import google

#coords to screen capture 0 168 541 764
im = ImageGrab.grab(bbox=(0, 305, 541, 764))
im.save('questions/img.png')
#OCR
data = image_to_string(Image.open('questions/img.png'))
#print(data)
queries=data.split("\n\n")#data.splitlines()
print(queries)
#search
results = google.search(queries[0],3)
#print results
#collect results
desc=list(res.description for res in results)
count=[0,0,0]
for des in desc:
    #for search in queries[1:len(queries)]:
    for i in range (1,len(queries)):
        #print "searching for", queries[i]
        if queries[i].replace('\n','').strip() in des:
            count[i-1]+=1
for i in range (1,len(queries)):
    print queries[i], count[i-1]

