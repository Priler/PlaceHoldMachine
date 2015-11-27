# -*- coding: utf-8 -*- 
from PlaceHoldMachine import PlaceHoldMachine #import class

i = PlaceHoldMachine() #create class instance
i.log_level = 2 #set log level to 2, so we can see errors

# set directories list, where all images will be replaced with placeholders
dirs = [
	'C:/MyTemplate/images/demo',
	'C:/MyTemplate/images/ads',
	'C:/MyTemplate/images/team'
]

i.font_name = 'C:/Windows/fonts/Arial.ttf' #Path to custom TrueType font
i.font_size = '15%' #Custom font size, in percents
#i.font_size = 75 #Custom font size, in pixels

i.walk_recursive(dirs) #recursively find all images in given directories
i.start() #begin conversion process