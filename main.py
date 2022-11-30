import streamlit as kp
from PIL import Image

kp.title('IMAGE TO GRAYSCALE')

with kp.expander('Start the camera'):
 st=kp.camera_input('camera')
if st:
#print(st)
    greys=Image.open(st)
    new_grey=greys.convert('L')
    kp.image(new_grey)
jp=kp.file_uploader('Upload pic')
if jp:
    greys = Image.open(jp)
    new_grey = greys.convert('L')
    kp.image(new_grey)