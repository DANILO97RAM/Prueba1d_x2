#!/usr/bin/env python3

from PIL import Image

#im1 = Image.open('dip/train/Dip_a1.png')
#im2 = Image.open('dip/train/Dip_a2s40.png')


def get_concat_h(im1, im2):
    dst = Image.new('L', (im1.width + im2.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst


for i in range(1,55):
	im1 = Image.open('dip/train_separate/Dip_q{}.png'.format(i))
	im2 = Image.open('dip/train_separate/Dip_q{}s40.png'.format(i))
	get_concat_h(im1, im2).save('dip/train/dip_q{}.png'.format(i))
