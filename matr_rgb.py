from PIL import Image

def img_convert(path):
    file=path

    img=Image.open(file)

    width,height=img.size
    #print(f'width={width}, height={height}')

    pixel_matr=[]


    for x in range(width):
        row = []
        for y in range(height):
            pixel=img.getpixel((x,y))
            row.append(pixel)
        pixel_matr.append(row)
    return pixel_matr
"""
with open('rgb_data.txt','w') as data:
    for item in pixel_matr:
        data.write(str(item)+'\n')
"""
#o sa printeze toate seturile de rgb din imagine
#print(pixel_matr)


def matr_convert(matrix):
    img = Image.new('RGB', (len(matrix), len(matrix[0])), (0, 0, 0, 0))
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            pixel = matrix[i][j]
            img.putpixel((i, j), (pixel, pixel, pixel))
    img.show()

