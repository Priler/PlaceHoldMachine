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

i.disable_color_detection() #disable primary color detection
i.set_primary_color( (255, 0, 0) ) #set background color to Red
i.set_contrast_color( (0, 0, 0) ) #set font color to Black

i.walk_recursive(dirs) #recursively find all images in given directories
i.start() #begin conversion process