# -*- coding: utf-8 -*- 
from PlaceHoldMachine import PlaceHoldMachine

i = PlaceHoldMachine()
i.log_level = 2

dirs = [
	'C:/MyTemplate/images'
]

i.walk_recursive(dirs)
i.start()