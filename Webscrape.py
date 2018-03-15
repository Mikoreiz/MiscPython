from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

def yesstyle():
	
	while True:
		
		x = input('Do you want to see the sales for Mens Tops? 1=Yes, 2=No: ')
		if x == '1':	
			##SCRAPES THE WEB PAGE FOR CLOTHEING INFO
			##The url of the webpage
			mentop_url = 'http://www.yesstyle.com/en/men-tops/list.html/bcc.14160_bpt.46'
			##Ureq opens the URL
			uClient = uReq(mentop_url)
			##Variable where the link is read
			page_html = uClient.read()
			##Closed
			uClient.close()
			##Variable for webpage. Soup parses it.
			mentopsoup_page = soup(page_html, 'html.parser')
			##Variable where the div class with the class that contains all the clothing
			mens_tops = mentopsoup_page.find_all('div', {'class':'itemContainer'})
		
			
			##PRINTS OUT THE NAME, PRICE AND DISCOUNT 
			##For loop to see all the tops
			for tops in mens_tops:
				##div class in mens_tops that contains the name of top
				top_title = tops.find_all('div', {'class':'itemTitle'})
				## .text to only get the next (so html code is disregarded)
				product_name = top_title[0].text
				
				##div class in mens_tops that contains the price of top
				top_price = tops.find_all('div', {'class':'itemPrice'})
				## .text to only get the next (so html code is disregarded)
				product_price = top_price[0].text
		
				##div class in mens_tops that contains the discount of top
				top_discount = tops.find_all('div', {'class':'itemStatus'})
				## .text to only get the next (so html code is disregarded)
				product_discount = top_discount[0].text
		
				print('--------------------------------------')
				print('')
				print(product_name)
				print(product_price)
				print(product_discount)
		else:
			break
yesstyle()
	
	
