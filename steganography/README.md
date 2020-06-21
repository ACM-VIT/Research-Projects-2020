
# Steganography
Implimenting Steganography (Hidding text and images inside an image)

## About Steganography

Steganography is the art of hiding a message inside another message. In this case we will hide a text message inside an image. An image will most propably go unnotified, not a bunch of people will suspect a message hidden inside an image. Steganography is no means of encryption, just a way of hiding data inside an image.

The diffrence in this project is that I have added an encryption messure which is encryting the text with a used defined key 

If you want to learn about Steganography in detail head over to [the Wikipedia article](https://en.wikipedia.org/wiki/Steganography)

## Structure

Main Page will have 2 options 
- Encode 
- Decode
##
Encode will take in the following :

	- Image in which the text is to be hidden
	- Key , which would encrypt the text 
	- Text to be hidden

And it would output image with the encrypted and hidden message  

##
Deocde  will take in the following :

	- Image in which the text is hidden
	- Key , which would decrypt the text 
	

And it would output the hidden text.

## How to use:
	run encrypt.py and visit http://127.0.0.1:5000/
