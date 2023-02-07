"""image to drawing"""

import cv2 
import matplotlib.pyplot as plt
def cartoon_to_image(Path):
    original_image = cv2.imread(Path)
    original_image = cv2.cvtColor(original_image,cv2.COLOR_BGR2RGB)
    if original_image is None:
        print("load again")
    Res1 = cv2.resize(original_image,(224,224))
    gray_scale = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    Res2 = cv2.resize(gray_scale,(224,224))
    smoothGrayScale = cv2.medianBlur(gray_scale,5)
    res3 = cv2.resize(smoothGrayScale,(224,224))
    edge = cv2.adaptiveThreshold(smoothGrayScale,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,9)
    res4 = cv2.resize(edge,(224,224))
    images = [Res1,res4]
    fig,axes = plt.subplots(1,2,figsize=(9,9),subplot_kw={'xticks':[], 'yticks':[]}, gridspec_kw=dict(hspace=0.1, wspace=0.1))
    for i, ax in enumerate(axes.flat):
        ax.imshow(images[i])
    plt.show()
    
    
x=cartoon_to_image("C:/Users/Avilab/Desktop/naruto.png")