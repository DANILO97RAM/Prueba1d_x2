#!/usr/bin/env python3

# load, split and scale the maps dataset ready for training


from os import listdir
from numpy import asarray
from numpy import vstack
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import load_img
from numpy import savez_compressed


# load all images in a directory into memory
def load_images(path, size=(256,512)):

	i = 0
	src_list, tar_list = list(), list()

	# enumerate filenames in directory, assume all are images
	for filename in listdir(path):

		# load and resize the image
		pixels = load_img(path + filename, target_size=size)

		# convert to numpy array
		pixels = img_to_array(pixels)

		# split into satellite and map
		tar_img, src_img = pixels[:, :256], pixels[:, 256:]
		src_list.append(src_img)
		tar_list.append(tar_img)
		i = i+1

	print('Total loaded images: ', i)
	return [asarray(src_list), asarray(tar_list)]
	


# dataset path
path = 'dip/val/'

# load dataset
[src_images, tar_images] = load_images(path)
print('Loaded: ', src_images.shape, tar_images.shape)

# save as compressed numpy array
arrays_file = 'geo_dip_val_256.npz'
savez_compressed(arrays_file, src_images, tar_images)
print('Saved dataset: ', arrays_file)
