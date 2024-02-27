from PIL import Image
import os


def painter(filename, dir_in, dir_out):
    img = Image.open(os.path.join(dir_in, filename)).resize((80, 80))
    for k in range(8):
        cim = img.copy()
        for i in range(80):
            for j in range(80):
                data = cim.getpixel((i, j))
                if k == 0:
                    pass
                elif k == 1:
                    cim.putpixel((i, j), (data[0] // 4, data[1] // 4, data[2] // 4))
                elif k == 2:
                    cim.putpixel((i, j), (data[0], 0, 0))
                elif k == 3:
                    cim.putpixel((i, j), (0, data[1], 0))
                elif k == 4:
                    cim.putpixel((i, j), (0, 0, data[2]))
                elif k == 5:
                    cim.putpixel((i, j), (data[0], data[1], 0))
                elif k == 6:
                    cim.putpixel((i, j), (0, data[1], data[2]))
                elif k == 7:
                    cim.putpixel((i, j), (data[0], 0, data[2]))
        cim.save(os.path.join(dir_out, f'{k}_pimage.png'))


painter('car2.png', 'Data', 'colored')