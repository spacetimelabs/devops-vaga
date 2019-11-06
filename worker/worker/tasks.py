import time
import random
from io import BytesIO
import numpy
import skimage.io


def randomize_image(data, block_size=(60, 60)):

    time.sleep(15)
    im = skimage.io.imread(BytesIO(data))

    block_width, block_height = block_size
    blocks = []

    for w in range(0, im.shape[0], block_width):
        for h in range(0, im.shape[1], block_height):
            if w + block_width <= im.shape[0] and h + block_height <= im.shape[1]:
                blocks.append((w, h))

    random_blocks = blocks.copy()
    random.shuffle(random_blocks)

    randomized_im = numpy.empty(im.shape)
    for i, (w, h) in enumerate(random_blocks):
        a, b = blocks[i]
        part = im[w : w + block_width, h : h + block_height]
        randomized_im[a : a + part.shape[0], b : b + part.shape[1]] = part

    out = BytesIO()
    skimage.io.imsave(out, randomized_im, format="PNG")
    out.seek(0)

    return out.read()
