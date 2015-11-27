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

i.emulate_placehold_it() #emulate placehold.it service
#i.emulate_csshopper_placeholder() #emulate csshopper placeholder service
#i.emulate_ubuntu() #emulate Ubuntu style
#i.emulate_ubuntu_orange() #emulate Ubuntu Orange style
#i.emulate_envato() #emulate Envato style
#i.emulate_facebook() #emulate Facebook style
#i.emulate_twitter() #emulate Twitter style
#i.emulate_default() #drop to default styling settings

i.walk_recursive(dirs) #recursively find all images in given directories
i.start() #begin conversion process