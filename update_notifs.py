#!/usr/bin/env python3.6

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests, time, csv
import templated_smtp as mail
import database as db


PATH = "/usr/local/lib/node_modules/chromedriver/lib/chromedriver/chromedriver"
url = 'https://www.bseindia.com/corporates/ann.html'
base = 'https://www.bseindia.com'
options = Options()
options.add_argument('--headless')
browser = webdriver.Chrome(PATH, chrome_options=options)


c=0
save_buffer_names,save_buffer_category,save_buffer_info,save_buffer_links = [],[],[],[]
while(1):
	browser.get(url)
	time.sleep(0.5)
	
	table = browser.find_elements_by_class_name('tdcolumngrey')[:19]
	names, category = [],[]
	for i,mod_four in enumerate(table):
		if i%4==0:
			names.append(mod_four.text)
		elif i%4==1:
			category.append(str(mod_four.text))

	info = []
	for i in range(1,len(names)+1):
		xpath = '//*[@id="lblann"]/table/tbody/tr[4]/td/table['+str(i)+']/tbody/tr[2]/td'
		time.sleep(1)
		td = browser.find_element_by_xpath(xpath)
		info.append(td.text)


	link_elements = browser.find_elements_by_class_name('tablebluelink')[1:20]
	pdf_links = []
	for each in link_elements:
		pdf_links.append(each.get_attribute("href"))

	# for i in range(len(names)):
	# 	print(names[i],'\t',category[i],'\t',pdf_links[i],'\t')

	# compare page with previous load
	if c!=0:
		# get all updates
		for i,each in enumerate(save_buffer_names):
			if each == names[i]:
				break
			elif each != names[i]:
				try:
					while each!=names[i]:
						print('--->',names[i],each)
						# check if updates match my keyword
						if 'Disclosure' in names[i]:
							# maintain recipients list
							RECIPIENTS = []
							# db.

							mail.template_mail(RECIPIENTS,
								'Update on '+names[i].split('-')[0],
								names[i],
								info[i],
								pdf_links[i])
						i+=1
				except:
					pass
				break
		print(i)


		# if matched send emails

	# update old buffers
	save_buffer_names = names
	save_buffer_category = category
	save_buffer_info = info
	save_buffer_links = pdf_links

	time.sleep(3)

	c+=1
	if c==40:
		break






