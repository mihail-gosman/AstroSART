import os
import cv2
import numpy as np

PATH = os.getcwd()
PATH_DATA_IN = os.path.join(PATH, 'data_in')
NAME_FILE = os.listdir(PATH_DATA_IN)[2]


image = cv2.imread(os.path.join(PATH_DATA_IN, NAME_FILE))
cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 21)

for i in range(0, 22):
    buffer = cv2.applyColorMap(image, i)
    #buffer = cv2.GaussianBlur(buffer, (2, 2), cv2.BORDER_DEFAULT)
    cv2.imwrite('images_out\\img'+str(i)+'.png', buffer)
