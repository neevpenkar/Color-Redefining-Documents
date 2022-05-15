from typing import Iterable
from PIL import Image

R, G, B = 0, 1, 2
page_count = 2 # Actually page count + 1

# Please change destination and source according to your needs

def change_color(image_data):
    new_image = []

    for pixel in d:
        ratio1 = pixel[R] / (pixel[G] + 1)
        ratio2 = pixel[R] / (pixel[B] + 1)

        if ratio1 > 1.6 or ratio2 > 1.6:
            new_image.append((int(pixel[R] / 4), int(pixel[G] * 1.5), int(pixel[B] * 1.5)))
        else:
            new_image.append((pixel[R], pixel[G], pixel[B]))
    return new_image



#for i in range(1, page_count):
#    if i < 10:
#        basefilename = "Images\Binary Trees-0" + str(i) + ".jpg"
#    else:
#        basefilename = "Images\Binary Trees-" + str(i) + ".jpg"

#    img = Image.open(basefilename)
#    img = img.convert("RGB")

#    d = img.getdata()

#    img.putdata(change_color(d))
#    destination = "New Images\Altered" + str(i) + ".jpg"
#    img.save(destination)


def makePDFfromImages(source_path, filename, page_count, destination_folder, extension):
    img_list = []

    im1 = Image.open(source_path + filename + "1" + extension)
    im1 = im1.convert("RGB")

    for i in range(2, page_count):
        destination = source_path + filename + str(i) + extension

        img = Image.open(destination)
        img = img.convert("RGB")

        img_list.append(img)

    im1.save(destination_folder + "Altered PDF Document.pdf", save_all=True, append_images=img_list)

makePDFfromImages("Images\\", "Altered", page_count, "New Images\\", ".jpg")
print("Done!")

