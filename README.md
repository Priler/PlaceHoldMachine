# PlaceHoldMachine

Advanced &amp; easy2use Python class for making image placeholders.  
Supports massive convertion with the speed of light.

# Benefits
  - Requires only Python (both 2.x and 3.x supported) and PIL to be installed on your system
  - Works on most popular Operating Systems, i.e. with Linux, Windows and Mac OS, even Android and iOS can be supported if you want to
  - Really fast speed, PlaceHoldMachine can convert up to 1.000 heavy weight images to placeholders within 30 seconds (~3 seconds for 100 files)
  - Supports primary color detection and usage of it as background color (you can disable this if you want to)
  - Highly customizable, use your own fonts, your own colors, your own styles e.t.c.
  - Robust startup. You can startup convertion just for 12 lines of code!

# How it works?
  1) Install Python, as well as PIL on your system
  2) Download this repo (you can use "Download Zip" button for the sake of speed)
  3) Open "use.py" for edit (or create your own if you want)
  4) Setup settings as you want
  5) List directories that need to be processed (in "dirs" array)
  6) Run "use.py" (or your own file, if you have one) within Terminal and wait few seconds
  7) Done! Watch the result :)

# How to work with this?
First of all, see "examples" directory.  
> Also, here is the very simple example of mass convertivg images to placeholders.
```
# -*- coding: utf-8 -*- 
from PlaceHoldMachine import PlaceHoldMachine #import class

i = PlaceHoldMachine() #create instance
i.log_level = 2#set log level to 2, so we can see errors

# set directories, where all images must be converted into placeholders
dirs = [
	'C:/MyTemplate/images/demo/',
	'C:/MyTemplate/images/ads/',
	'C:/MyTemplate/images/team/'
]

i.walk_recursive(dirs) #find all images in listed directories
i.start() #start conversion process
```

# Available class instance methods:

  - **load_image( path_to_image )** used for loading image
  - **create_placeholder()** used to build placeholder
  - **disable_color_detection()** used to disable detection of primary color
  - **enable_color_detection** used to enable detection of primary color
  - **set_primary_color( (r, g, b) )** used to set your own primary color
  - **set_contrast_color( (r, g, b) )** used to set your own contrast color (aka font color)
  - **emulate_default()** used to restore default styling settings
  - **emulate_ubuntu()** used to emulate Ubuntu style behavior
  - **emulate_ubuntu_orange()** used to emulate Ubuntu Orange style behavior
  - **emulate_envato()** used to emulate Envato style behavior
  - **emulate_facebook()** used to emulate Facebook style behavior
  - **emulate_twitter()** used to emulate Twitter style behavior
  - **emulate_placehold_it()** used to emulate style behavior of http://placehold.it
  - **emulate_csshopper_placeholder()** used to emulate style behavior of http://lab.csschopper.com/placeholder/
  - **show()** used to display current placeholder in system's image viewer
  - **walk_recursive( dirs )** used to recursively find all images in provided directories list
  - **walk( dirs )** used to find all images only in provided directories list
  - **start()** used to start convertion process of finded images

# Available class instance properties:
  - **text_prefix** used to prefix text that will be drawed on every placeholder (default is "")
  - **font_name** path to required font (default is "UbuntuCondensed-Regular")
  - **font_size** used to set font size in pixels or in percents (i.e. value may be "15%") (default is "7%")
  - **quality** used to set resulting quality of each placeholder image, value from 0 to 100 can be used (default is 90)
  - **log_level** used to set logs printing level (default is 1)
     - 0 - No logs will be printed
     - 1 - Only INFO level logs will be printed
     - 2 - INFO and ERRORS level logs will be printed
     - 3 - INFO, ERRORS and WARNINGS level logs will be printed

# How to install Python?
> Visit http://python.org/ and download Python for your system (Python 2.x is preffered)

# How to install PIL?

> Installation instructions for your OS you can find here https://python-pillow.github.io/ and here http://pillow.readthedocs.org/en/3.0.x/installation.html

> If you using **Linux**:
```
sudo pip install PIL --allow-external PIL --allow-unverified PIL
```

> If you using **Windows**: Visit this page and download installation package for your Python version http://www.pythonware.com/products/pil/

> If you using ***MAC***:
```
pip install PIL --allow-external PIL --allow-unverified PIL
```

### Version
1.0.0

### Author

Abraham Tugalov (a.k.a. Priler)

### Development

Want to contribute? Great!

Just fork this, make required changes and do pull request.

### Todos

 - GUI for Linux, Windows and MAC
 - Thumbnailing
 - File names suffixing
 - Watermarks support
 - Gradients support
 - Background images support
 - Event system

License
----

MIT


**Free Software, Hell Yeah!**