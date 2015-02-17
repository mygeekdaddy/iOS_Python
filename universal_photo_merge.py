# script based on Federico Vittici WF in Pythonista post
# http://www.macstories.net/stories/automating-ios-how-pythonista-changed-my-workflow/

import clipboard
import Image
import console
import photos

# Select/copy two images from Photos app first

#im1 = clipboard.get_image(idx=0)
#im2 = clipboard.get_image(idx=1)

console.clear()

console.alert("Pick first image", "", "Select")
im1 = photos.pick_image(show_albums=True)

console.alert("Pick second image", "", "Select")
im2 = photos.pick_image(show_albums=True)

console.clear()

console.show_activity()

w,h = im1.size

print im1.size
print 'Ratio is ' + str((w*1.0)/h)

def image_merge(img):
	if (w*1.0)/h > 1:
		print 'Landscape screenshot...'
		#(2048, 1536)
		#Landscape screenshot
		print 'Landscape screenshot...'
		#background = Image.new('RGB', (2068, 3102), (255,255,255))
		background = Image.new('RGB', ((w+20), ((h*2)+30)), (255,255,255))
		print "Generating image..."
		background.paste(im1,(10,10))
		background.paste(im2,(10,(h+20)))
		background.show()
		#console.hide_activity()
		photos.save_image(background)	
	else:
		#(1536, 2048)
		#Portrait screenshot
		print 'Portrait screenshot...'	
		#background = Image.new('RGB', (3102,2068), (255, 255, 255))
		background = Image.new('RGB', (((w*2)+30),(h+20)), (255, 255, 255))
		print "Generating image..."
		#	_1 = im1.resize((924,1232),Image.ANTIALIAS)
		#	_2 = im2.resize((924,1232),Image.ANTIALIAS)
		background.paste(im1,(10,10))
		background.paste(im2,((w+20),10))
		background.show()
		photos.save_image(background)	


image = image_merge(im1)
			
#print "\n\n Image set to clipboard"
print "\n\nDone."