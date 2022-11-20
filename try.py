import numpy as np
import random
import cv2
import matplotlib.pyplot as plt

from tkinter import *
from PIL import ImageTk, Image

# Create an instance of tkinter window
win = Tk()

# Define the geometry of the window
win.geometry("700x500")

frame = Frame(win, width=600, height=400)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

def sp_noise(image,prob):
    '''
    Add salt and pepper noise to image
    prob: Probability of the noise
    '''
    output = np.zeros(image.shape,np.uint8)
    thres = 1 - prob 
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output

img = cv2.imread('/home/scyeroux/python/image_processing-basics/images/Lenna.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
noise_img = sp_noise(img,0.3)

# Create an object of tkinter ImageTk
noise_img = ImageTk.PhotoImage(noise_img)

# Create a Label Widget to display the text or Image
label = Label(frame, image = noise_img)
label.pack()

win.mainloop()