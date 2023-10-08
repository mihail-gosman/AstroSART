import matr_rgb
import os

PATH = os.getcwd()
PATH_DATA_IN = os.path.join(PATH, 'data_in')
NAME_FILE = os.listdir(PATH_DATA_IN)[0]

# matrix from image conversion
image_pix_data = matr_rgb.img_convert(os.path.join(PATH_DATA_IN, NAME_FILE))

# matrix processing
image_matrix = []
for i in range(0, len(image_pix_data)):
    row = []
    for j in range(0, len(image_pix_data[i])):
        row.append(image_pix_data[i][j][0])
    image_matrix.append(row)


# image from matrix conversion
matr_rgb.matr_convert(image_matrix)