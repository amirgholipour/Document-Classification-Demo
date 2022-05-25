from PIL import Image
import os, sys

path = "/Users/skasmani/Downloads/Redhat/Redhat_git/ai-project/Document-Classification-demo/data/raw/data/Scientific/"
dirs = os.listdir( path )
final_size = 512;

def resize_aspect_fit():
    for item in dirs:
        if item == '.DS_Store':
             continue
        if item == 'Thumbs.db':
             continue
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            size = im.size
            # print(im.size)
            ratio = float(final_size) / max(size)
            new_image_size = tuple([int(x*ratio) for x in size])
            im = im.resize((final_size,final_size), Image.ANTIALIAS)
            # new_im = Image.new("RGB", (final_size, final_size))
            # new_im.paste(im, ((final_size-new_image_size[0])//2, (final_size-new_image_size[1])//2))
            im.save(f + '_resized.jpg', 'JPEG', quality=90)
            os.remove(path+item)
resize_aspect_fit()