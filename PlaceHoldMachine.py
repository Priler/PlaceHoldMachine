# -*- coding: utf-8 -*- 
from PIL import Image, ImageDraw, ImageFont
import os, time, sys
from math import ceil

class PlaceHoldMachine:
	'''Author: Abraham Tugalov (aka Priler)'''
	text = ""
	prefix = ""
	font_name = 'fonts/Ubuntu_Condensed/UbuntuCondensed-Regular.ttf'
	font_size = '7%'
	font = None
	active_image = None
	active_image_size = (0, 0)
	active_image_size_str = '0x0'
	primary_color = (0, 0, 0)
	contrast_color = (255, 255, 255)
	placeholder_image = None
	images_list = []
	log_level = 1
	color_detection = True
	quality = 90
	allowed_image_formats = '*'

	def __init__(self):
		'''Self initialization'''
		self.load_font(self.font_name, 1)

	# @image open
	def load_image(self, path):
		'''Load image into current class instance or return False if trying to load not image.'''
		try:
			img = Image.open(path)
			self.active_image = img
			self.active_image_size = self.active_image.size
			self.text = self.active_image_size_str = str(self.active_image_size[0]) + 'x' + str(self.active_image_size[1])
			return True
		except IOError:
			self.log(path + ' is not image', 2)
			return False

	# @image primary color
	def compute_primary_color(self):
		'''Get primary color of image'''
		if not self.active_image:
			self.log('image is not loaded', 2)
			return False

		if not self.color_detection:
			return False

		optimized_img = self.active_image.resize((50, 50)).convert("RGB")
		width, height = optimized_img.size

		r_ave = 0
		g_ave = 0
		b_ave = 0

		for x in range(0, width):
		    for y in range(0, height):
		        r, g, b = optimized_img.getpixel((x,y))
		        r_ave = (r + r_ave) / 2
		        g_ave = (g + g_ave) / 2
		        b_ave = (b + b_ave) / 2

		self.primary_color = (int(r_ave), int(g_ave), int(b_ave))
		self.compute_contrast_color()
		self.font_color = self.contrast_color
		return True

	# @compute contrast color
	def compute_contrast_color(self):
		'''Translate primary color to Luma and identify contrast color'''
		if (self.primary_color[0]*0.299 + self.primary_color[1]*0.587 + self.primary_color[2]*0.114) > 186:
			self.contrast_color = (0, 0, 0)
		else:
			self.contrast_color = (255, 255, 255)

		return True

	# @smart font size detection
	def detect_font_size(self):
		'''Translates percentaged font size into pixel representation'''
		percents = int(self.font_size[:-1])
		h = max(self.active_image_size)
		return int(ceil((h * percents) / 100))

	# @load font
	def load_font(self, file, size = 16):
		'''Load truetype font'''
		self.font_name = file
		self.font = ImageFont.truetype(file, size)
		return True

	# @create placeholder
	def create_placeholder(self):
		'''Convert image into placeholder'''
		if not self.active_image:
			self.log('image is not loaded', 2)
			return False

		if not self.primary_color:
			self.log('primary_color is not loaded', 2)
			return False

		if not self.font:
			self.log('font is not loaded', 2)
			return False

		if str(self.font_size).endswith('%'):
			font_size = self.detect_font_size()
			self.load_font(self.font_name, font_size)
		else:
			font_size = self.font_size
			self.load_font(self.font_name, font_size)

		text = str(self.text)
		if len(self.prefix) > 0:
			text = str(self.prefix) + str(self.text)

		self.placeholder_image = Image.new("RGB", self.active_image_size, self.primary_color)
		draw = ImageDraw.Draw(self.placeholder_image)
		tsize = draw.textsize(text, font = self.font)
		pos = [(self.active_image_size[0] / 2) - (tsize[0] / 2), (self.active_image_size[1] / 2) - (tsize[1] / 2)]
		pos[1] = (self.active_image_size[1] / 2) - (font_size / 2)
		draw.text(pos, text, self.contrast_color, font = self.font)
		del draw

	# @enable color detection
	def enable_color_detection(self):
		'''Turn on primary color detection'''
		self.color_detection = True

	# @disable color detection
	def disable_color_detection(self):
		'''Turn off primary color detection'''
		self.color_detection = False

	# @set primary color
	def set_primary_color(self, new_value = (0, 0, 0)):
		'''Change active primary color'''
		if len(new_value) >= 3:
			self.primary_color = (new_value[0], new_value[1], new_value[2])

	# @set contrast color
	def set_contrast_color(self, new_value = (0, 0, 0)):
		'''Change active primary color'''
		if len(new_value) >= 3:
			self.contrast_color = (new_value[0], new_value[1], new_value[2])

	# @emulate default
	def emulate_default(self):
		'''Restore default settings'''
		self.enable_color_detection()
		self.load_font('./fonts/Ubuntu_Condensed/UbuntuCondensed-Regular.ttf', 1)
		self.font_size = '7%'

	# @emulate ubuntu
	def emulate_ubuntu(self):
		'''Emulate Ubuntu'''
		self.disable_color_detection()
		self.set_primary_color([99, 16, 92])
		self.set_contrast_color([255, 255, 255])
		self.load_font('./fonts/Ubuntu_Condensed/UbuntuCondensed-Regular.ttf', 1)
		self.font_size = '7%'

	# @emulate ubuntu orange
	def emulate_ubuntu_orange(self):
		'''Emulate Orange Ubuntu'''
		self.disable_color_detection()
		self.set_primary_color([221, 72, 20])
		self.set_contrast_color([255, 255, 255])
		self.load_font('./fonts/Ubuntu_Condensed/UbuntuCondensed-Regular.ttf', 1)
		self.font_size = '7%'

	# @emulate envato
	def emulate_envato(self):
		'''Emulate Envato'''
		self.disable_color_detection()
		self.set_primary_color([130, 181, 64])
		self.set_contrast_color([255, 255, 255])
		self.load_font('./fonts/Dosis/Dosis-Medium.ttf', 1)
		self.font_size = '7%'

	# @emulate facebook
	def emulate_facebook(self):
		'''Emulate Facebook'''
		self.disable_color_detection()
		self.set_primary_color([69, 97, 157])
		self.set_contrast_color([255, 255, 255])
		self.load_font('./fonts/Roboto_Condensed/RobotoCondensed-Regular.ttf', 1)
		self.font_size = '7%'

	# @emulate twitter
	def emulate_twitter(self):
		'''Emulate Twitter'''
		self.disable_color_detection()
		self.set_primary_color([85, 172, 238])
		self.set_contrast_color([255, 255, 255])
		self.load_font('./fonts/Roboto_Condensed/RobotoCondensed-Regular.ttf', 1)
		self.font_size = '7%'

	# @emulate placehold_it
	def emulate_placehold_it(self):
		'''Emulation of placehold.it website behavior'''
		self.disable_color_detection()
		self.set_primary_color([204, 204, 204])
		self.set_contrast_color([150, 150, 150])
		self.load_font('./fonts/Roboto_Condensed/RobotoCondensed-Regular.ttf', 1)
		self.font_size = '7%'

	# @emulate csshopper placeholder
	def emulate_csshopper_placeholder(self):
		'''Emulation of ab.csschopper.com/placeholder website behavior'''
		self.disable_color_detection()
		self.set_primary_color([188, 188, 188])
		self.set_contrast_color([57, 57, 57])
		self.load_font('./fonts/Roboto_Condensed/RobotoCondensed-Bold.ttf', 1)
		self.font_size = '7%'

	# @set allowed formats
	def set_allowed_image_formats(self, formats = []):
		if type(formats) is list or type(formats) is tuple:
			self.allowed_image_formats = formats

	# @show placeholder
	def show(self):
		'''Display placeholder image'''
		self.placeholder_image.show()

	# @log
	def log(self, message, loglevel = 0):
		'''Log something.'''
		# levels available:
		# 0 = No messages
		# 1 = Info messages
		# 2 = Error messages
		# 3 = Warning messages
		if self.log_level >= loglevel:
			if loglevel == 1:
				print('[Info] ' + message)
			elif loglevel == 2:
				print('[Error] ' + message)
			elif loglevel == 3:
				print('[Warning] ' + message)
			else:
				print('[Unknown message level] ' + message)

	# @walk_recursive
	def walk_recursive(self, dirs = []):
		'''Walk though directories, recursively'''
		if len(dirs):
			for cdir in dirs:
				if os.path.isdir(cdir):
					for root, dirs, files in os.walk(cdir):
						for cfile in files:
							fpath = os.path.join(root, cfile)
							if os.path.isfile(fpath):
								self.images_list.append(fpath)
		return True

	# @walk
	def walk(self, dirs = []):
		'''Walk though directories, not recursively'''
		if len(dirs):
			for cdir in dirs:
				if os.path.isdir(cdir):
					files = os.listdir(cdir)
					for cfile in files:
						fpath = os.path.join(cdir, cfile)
						if os.path.isfile(fpath):
							self.images_list.append(fpath)
		return True

	# @start
	def start(self):
		'''Replace images with placeholders'''
		proceed = 0
		time_start = time.time()
		if len(self.images_list):
			for image in self.images_list:
				if self.load_image(image):
					if self.allowed_image_formats != '*':
						if not self.active_image.format in self.allowed_image_formats:
							continue
					self.compute_primary_color()
					self.create_placeholder()
					try:
						self.placeholder_image.save(image, quality = self.quality)
						proceed += 1
					except:
						self.log('access denied to write into' + image, 2)
				else:
					self.log(image + ' is not image, skipping', 3)
			self.log('Done! ' + str(proceed) + ' images processed and replaced with placeholders! ' + ':)', 1)
			self.log(str(time.time() - time_start) + ' seconds spent. Woop Woop Woop!', 1)
		else:
			self.log('images_list not loaded', 2)
