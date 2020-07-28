from PIL import Image


img = Image.open("waldo.jpg")
img_size = img.size
aspect = img_size[0] / img_size[1]

new_size = (480, int(480/aspect))

out = img.transpose(Image.FLIP_LEFT_RIGHT)
out.thumbnail(new_size)

out.save("waldo.jpg")
