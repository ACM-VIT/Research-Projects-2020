from PIL import Image
from cryptography.fernet import Fernet
def genData(data): 
		newd = [] 		
		for i in data: 
			newd.append(format(ord(i), '08b')) 
		return newd 

def encrypt(key, msg):
    encryped = []
    for i, c in enumerate(msg):
        key_c = ord(key[i % len(key)])
        msg_c = ord(c)
        encryped.append(chr((msg_c + key_c) % 456))
    return ''.join(encryped)

def decrypt(key, encryped):
    msg = []
    for i, c in enumerate(encryped):
        key_c = ord(key[i % len(key)])
        enc_c = ord(c)
        msg.append(chr((enc_c - key_c) % 456))
    return ''.join(msg)



def modPix(pix, data): 
	
	datalist = genData(data) 
	lendata = len(datalist) 
	imdata = iter(pix) 

	for i in range(lendata): 
		pix = [value for value in (imdata.__next__()[:3] + imdata.__next__()[:3] + imdata.__next__()[:3])]
		for j in range(0, 8): 
			if (datalist[i][j]=='0') and (pix[j]% 2 != 0): 
				
				if (pix[j]% 2 != 0): 
					pix[j] -= 1
					
			elif (datalist[i][j] == '1') and (pix[j] % 2 == 0): 
				pix[j] -= 1
		if (i == lendata - 1): 
			if (pix[-1] % 2 == 0): 
				pix[-1] -= 1
		else: 
			if (pix[-1] % 2 != 0): 
				pix[-1] -= 1

		pix = tuple(pix) 
		yield pix[0:3] 
		yield pix[3:6] 
		yield pix[6:9] 

def encode_enc(newimg, data): 
	w = newimg.size[0] 
	(x, y) = (0, 0) 
	
	for pixel in modPix(newimg.getdata(), data):  
		newimg.putpixel((x, y), pixel) 
		if (x == w - 1): 
			x = 0
			y += 1
		else: 
			x += 1

def encode(imagename,text, passkey,newimgname): 
	img = imagename
	image = Image.open(img, 'r') 
	
	data = text
	key=passkey

	data = encrypt(key, data)	
	#print(data)
	if (len(data) == 0): 
		raise ValueError('Data is empty') 
		
	newimg = image.copy() 
	encode_enc(newimg, data) 
	
	new_img_name = newimgname 
	new_img_name=str(new_img_name.split(".")[0])+".png"
	newimg.save(new_img_name, "png")
	image.close() 

def decode(imagename,passkey): 
	img = imagename 
	image = Image.open(img, 'r') 
	
	data = '' 
	imgdata = iter(image.getdata()) 
	
	while (True): 
		pixels = [value for value in imgdata.__next__()[:3] + imgdata.__next__()[:3] + imgdata.__next__()[:3]]  
		binstr = '' 
		
		for i in pixels[:8]: 
			if (i % 2 == 0): 
				binstr += '0'
			else: 
				binstr += '1'
				
		data += chr(int(binstr, 2)) 
		if (pixels[-1] % 2 != 0):
			print(data)
			# key=input("Input")
			return decrypt(passkey, data) 
		 
