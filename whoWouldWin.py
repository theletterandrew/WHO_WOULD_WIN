# Who would win generator

# TODO
# Take user input for side1, side2 text
# Take user input for side1, side2 image (drag and drop?)

# generate an image that meets the format of the meme.

# Imports
from PIL import Image, ImageDraw, ImageFont

# Open template image to paste to
template = Image.open('Template.png')
tWidth, tHeight = template.size

# Open images to paste to template
image1 = Image.open('Examples/heart.jpg')
oneWidth, oneHeight = image1.size
image2 = Image.open('Examples/saltybois.png')
twoWidth, twoHeight = image2.size

# check if images need to be resized.
SQUARE_FIT_SIZE = 200

if oneWidth > SQUARE_FIT_SIZE and oneHeight > SQUARE_FIT_SIZE:
	# Calculate the new width and height to resize to.
	if oneWidth > oneHeight:
		oneHeight = int((SQUARE_FIT_SIZE / oneWidth) * oneHeight)
		oneWidth = SQUARE_FIT_SIZE
	else:
		oneWidth = int((SQUARE_FIT_SIZE / oneHeight) * oneWidth)
		oneHeight = SQUARE_FIT_SIZE

	image1 = image1.resize((oneWidth, oneHeight))

if twoWidth > SQUARE_FIT_SIZE and twoHeight > SQUARE_FIT_SIZE:
	# Calculate the new width and height to resize to.
	if twoWidth > twoHeight:
		twoHeight = int((SQUARE_FIT_SIZE / twoWidth) * twoHeight)
		twoWidth = SQUARE_FIT_SIZE
	else:
		twoWidth = int((SQUARE_FIT_SIZE / twoHeight) * twoWidth)
		twoHeight = SQUARE_FIT_SIZE

	image2 = image2.resize((twoWidth, twoHeight))


# paste images to template image
template.paste(image1, (122, 100))
template.paste(image2, (444, 100))

# Save changes
template.save("Examples/WhoWouldWin.png")