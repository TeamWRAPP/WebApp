#!/usr/bin/python

# Using Moz API to use Pyscrape 

# see what type of cookies website use
# analyze the SEO of website
# track where the user is using geopy

from flask import Flask
import requests
from flask import render_template 
import wrappCookieChecker

app = Flask(__name__)

# / is the root directory/home page
# Ties URL to python function 
@app.route('/')
def home():
	return 'Hello World'

@app.route('/cookie')
def cookieProgram():
	siteURL = 'benefits.gov'
	cookieCount = 0
	TLDomain = ['.com', '.gov', 'org', 'net', 'int', '.edu', '.mil']
	websiteList = []
	# if len(sys.argv) != 2:
	# 	siteURL = input('Please enter your website URL: ')
	# else: 
	# 	siteURL = sys.argv[1]

	if siteURL[:6] != 'http://' and siteURL[:4] == 'www.' and siteURL[-4:] in TLDomain:
		siteURL = 'http://' + siteURL
	elif siteURL[:4] != 'www.' and siteURL[-4:] in TLDomain:
		siteURL = 'http://www.' + siteURL
	else:
		print('Invalid URL')
		exit(-1)

	printThis = wrappCookieChecker.crawler(siteURL)
	return printThis
	#return wrappCookieChecker.testing()
	#return siteURL

if __name__ == '__main__':
	app.run()