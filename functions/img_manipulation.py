import numpy as np
import cv2
import PIL
from PIL import Image, ImageEnhance
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab


def transformations(img_array, f_br, f_co, f_sh, f_sa, cs_r, cs_g, cs_b):
    img = Image.fromarray(img_array, 'RGB')
    img = (PIL.ImageEnhance.Brightness(img)).enhance(f_br)
    img = (PIL.ImageEnhance.Contrast(img)).enhance(f_co)
    img = (PIL.ImageEnhance.Sharpness(img)).enhance(f_sh)
    img = (PIL.ImageEnhance.Color(img)).enhance(f_sa)
    matrix = ( int(cs_r), 0, 0, 0, 0, int(cs_g), 0, 0, 0, 0, int(cs_b), 0)
    img = img.convert("RGB", matrix)

    r, g, b = img.split()
    r, g, b = r.histogram(), g.histogram(), b.histogram()

    if not cs_r:
        r[0] = 0
    if not cs_g:
        g[0] = 0
    if not cs_b:
        b[0] = 0

    fig, ax = plt.subplots()
    ax.set_facecolor("#202020")
    plt.xlim(xmax = 256, xmin = -1)
    plt.ylim(ymax = max([max(r), max(g), max(b)]), ymin = 0)
    #fig.set_size_inches(2.4, 1.1, forward=True)

    if cs_b:
        plt.plot( b, color ='b', label='Blue',linewidth=5.)
        plt.fill_between(np.arange(0, 256), b, color='b', alpha=0.4)
    if cs_g:
        plt.plot( g, color ='g', label='Green',linewidth=5.)
        plt.fill_between(np.arange(0, 256), g, color='g', alpha=0.4)
    if cs_r:
        plt.plot( r, color='r', label='Red',linewidth=5.)
        plt.fill_between(np.arange(0, 256), r, color='r', alpha=0.4)
    
    ax.axes.get_xaxis().set_visible(False)
    ax.axes.get_yaxis().set_visible(False)
    #plt.show()

    fig.canvas.draw()
    data = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8, sep='')
    data = data.reshape(fig.canvas.get_width_height()[::-1] + (3,))

    plt.close(fig)
    return np.array(img), data


def difference(img1, img2):
    # compute difference
    diff = cv2.subtract(img1, img2)
    return diff