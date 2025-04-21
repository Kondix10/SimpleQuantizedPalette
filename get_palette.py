from PIL import Image
import time
import cv2
import math
import os.path


#function to get a quantized color palette using PIL quantize function
def get_palette(cv2_image, colors_number: int):  #cv2_image in BGR format!
    cv2_image = cv2.cvtColor(cv2_image, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(cv2_image)
    pil_image = pil_image.quantize(colors_number, None, 0, None, 0)
    
    #getting RGB values of each pixel
    color_palette = list(set((pil_image.convert("RGB")).getdata()))  #set - removing duplicates, getting the quantized color palette

    if len(color_palette)<colors_number:          #Filling in remaining colors if image doesn't have enough colors for "colors_number"
        for i in range(len(color_palette),colors_number):
            color_palette.append((255,255,255))
            
    return color_palette


#constants
i=0
width=80
height=60

#inputs
file_exists = False
while(not file_exists):
    name_in = input('Input file name[+extension]: ')
    file_exists = os.path.isfile(name_in)
    if(not file_exists):
        print("File does not exist!")

name_out = input('Output file name: ')

#opening video with opencv, printing information
cap = cv2.VideoCapture(name_in)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
fps = int(cap.get(cv2.CAP_PROP_FPS))
name_out = ("palette_"+name_out+".rgbp")
print("\n\n====== INFO ======"+'\n'+"Input file: "+name_in+'\n'+"Output file: "+name_out+'\n'+"Frames: "+str(total_frames)+'\n'+"Framerate: "+str(fps)+'\n')
input('Press any key to continue')


#creating output file
f=open(name_out, "wb")


#main loop
t1 = time.time()
colors = 16


while i<int(total_frames):
    cap.set(1, i)
    ret, frame = cap.read()
    frame = cv2.resize(frame, (width,height))
    palette = get_palette(frame, colors)
    for j in range(colors):
        f.write(bytes([palette[j][0]])) #R
        f.write(bytes([palette[j][1]])) #G
        f.write(bytes([palette[j][2]])) #B

    print("===",name_in,"-",int((i/int(total_frames))*100),"%","-","frame", i, 'of',str(int(total_frames)),'===', end='\r')
    i=i+1
f.close()
print("\nElapsed time: "+str(round((time.time()-t1),2))+"s")
print('\n'+'File ready -',name_out,)
input("Press any key")
