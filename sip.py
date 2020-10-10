from selenium import webdriver
import time
import re  
import pytesseract

class nuu(object):
	#SIP_URL ='' #school sip url
	def __init__(self):
		self.browser = webdriver.Chrome()
		pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

	def login(self,account: str, password: str):
		self.browser.get(self.SIP_URL)
		time.sleep(2)
		element = browser.find_element_by_xpath('//*[@id="captchaBox"]/img')
		element.screenshot('pic.png')
		time.sleep(2)
		img = convert_Image(getImage(),127.5)
		browser.find_element_by_name('ctl00$baseContent_cph$act_id_txt').send_keys(account)
		browser.find_element_by_id('act_pwd_txt').send_keys(password)
		browser.find_element_by_name('ctl00$baseContent_cph$confirm_txt').send_keys(change_Image_to_text(img))
		time.sleep(5)
		browser.find_element_by_xpath('//*[@id="baseContent_cph_signIn_btn"]').click()

	def getImage():
		img = Image.open('pic.png')
		return img

	def convert_Image(img, standard=127.5):
		image = img.convert('L')
		pixels = image.load()
		for x in range(image.width):
			for y in range(image.height):
				if pixels[x, y] > standard:
					pixels[x, y] = 255
				else:
					pixels[x, y] = 0
		return image

	def change_Image_to_text(img):
		textCode = pytesseract.image_to_string(img, lang='eng')
		textCode = re.sub("\W", "", textCode)
		return textCode
	

if __name__ == '__main__':
    main()


