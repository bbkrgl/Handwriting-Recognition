from PIL import ImageTk, Image, ImageDraw
import PIL
from Tkinter import *
import trainer
import numpy as np

width = 200
height = 200
center = height//2
white = (255, 255, 255)
green = (0, 128, 0)


def paint(event):
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    cv.create_oval(x1, y1, x2, y2, fill="black", width=5)
    draw.line([x1, y1, x2, y2], fill="black", width=5)


root = Tk()

cv = Canvas(root, width=width, height=height, bg='white')
cv.pack()

result_text = Label(text="Prediction")
result_text.pack()

image1 = PIL.Image.new("RGB", (width, height), white)

draw = ImageDraw.Draw(image1)
cv.pack(expand=YES, fill=BOTH)
cv.bind("<B1-Motion>", paint)


def img2bitmap_array(img):
    arr = np.array(img)

    r, g, b = np.split(arr, 3, axis=2)
    r=r.reshape(-1)
    g=g.reshape(-1)
    b=b.reshape(-1)

    bitmap = list(map(lambda x: 0.299*x[0]+0.587*x[1]+0.114*x[2], zip(r, g, b)))
    bitmap = np.array(bitmap).reshape([arr.shape[0], arr.shape[1]])
    bitmap = np.dot((bitmap > 128).astype(float), 255)
    return np.array(bitmap)


def save():
    size = 8, 8
    image1.thumbnail(size, PIL.Image.ANTIALIAS)
    print img2bitmap_array(image1)
    """print trainer.predict(data)"""


button = Button(text="Predict", command=save)
button.pack()

root.mainloop()
