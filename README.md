# Glitcheer

Simple, it glitches images.

For now only supports JPEG compressed images (technically, it works on BMP too, but doesn't do much on them). The PNG format is a bitch to work on.

It takes random bytes from the image, and places them in some other random positions. I tried not to touch the headers, but it fails sometimes.

The second parameter is the amount of pixels that will be moved. Notice that if it's too high, the image just breaks (Huffman tables just blow up).

"Too high" depends on the image size. For an image of 640x640px, 60 pixels seems the limit (the image breaks most of the time, but it sometimes renders correctly)

## Requirements

- Python 3

## How to run

`./glitchy.py {target\_file} {bytes\_to\_move} --output {output\_file\_(optional)}
