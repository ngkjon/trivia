from PIL import Image
from pytesseract import image_to_string
import pyscreenshot as ImageGrab
#0 168 541 764
im = ImageGrab.grab(bbox=(0, 125, 541, 764))
im.save('questions/img.png')


