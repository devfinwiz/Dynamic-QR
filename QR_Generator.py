from distutils.version import Version
from turtle import width
import qrcode
from PIL import Image
import requests

flag=0

def url_checker(url):
	try:
		#Get Url
		get = requests.get(url)
		# if the request succeeds 
		if get.status_code == 200:
			return True
		else:
			return False

	#Exception
	except requests.exceptions.RequestException as e:
        # print URL with Errs
		raise SystemExit(f"{url}: is Not reachable \nErr: {e}")

def generate_qr(url,qr_color):
    if(url==""):
            return "Failed"
        
    if(url_checker(url)):
    
        #Logo_link = logoo
    
        #logo = Image.open(Logo_link)
    
        # taking base width
        #basewidth = 190
    
        # adjust image size
        #wpercent = (basewidth/float(logo.size[0]))
        #hsize = int((float(logo.size[1])*float(wpercent)))
        #logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)

        QRcode = qrcode.QRCode(version=1,box_size=12,
        error_correction=qrcode.constants.ERROR_CORRECT_H
        )
        
        # adding URL or text to QRcode
        QRcode.add_data(url)
        # generating QR code
        QRcode.make()
        
        # taking color name from user
        QRcolor = qr_color
        
        # adding color to QR code
        QRimg = QRcode.make_image(
            fill_color=QRcolor, back_color="black").convert('RGB')
        
        #pos = ((QRimg.size[0] - logo.size[0]) // 2,
        #   (QRimg.size[1] - logo.size[1]) // 2)
        #QRimg.paste(logo, pos)

        # save the QR code generated
        QRimg.save('Generated_QRCode.png')
        
        return "Success",QRimg 
