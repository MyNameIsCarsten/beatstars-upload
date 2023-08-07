import cv2
import numpy as np

def create_crop():
    # Import Image
    img = cv2.imread(r"D:\Dropbox\Youtube Uploads\next.png")

    crop_img = img[270:810, 690:1230]

    # Display cropped image
    # cv2.imshow("cropped", crop_img)

    # Save cropped image
    cv2.imwrite(r"D:\Dropbox\Youtube Uploads\Cropped_Image.jpg", crop_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return