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

class Pillars():
	p1Score = 0
	p2Score = 0
	p3Score = 0
	p4Score = 0 
	p5Score = 0 
	p6Score = 0
	p7Score = 0
	p8Score = 0
	
	@app.route('/p1')
	def p1(self):
		# Grab data and do calculations
		return "P1 processed"

	@app.route('/p2')
	def p2(self):
		return "P2 processed"

	@app.route('/p3')
	def p3(self):
		return "P3 processed"

	@app.route('/p4')
	def p4(self):
		return "P4 processed"	

	@app.route('/p5')
	def p5(self):
		return "P5 processed"	

	@app.route('/p6')
	def p6(self):
		return "P6 processed"	

	@app.route('/p7')
	def p7(self):
		return "P7 processed"	

	@app.route('/p8')
	def p8(self):
		return "P8 processed"	

# / is the root directory/home page
# Ties URL to python function 
@app.route('/')
def home():
	return 'Hello World'

@app.route('/cookie')
def cookieProgram():
	# Change this to site user enters <blah>
	siteURL = 'benefits.gov'
	cookieCount = 0
	TLDomain = ['.com', '.gov', 'org', 'net', 'int', '.edu', '.mil']
	websiteList = []
	# if len(sys.argv) != 2:
	# 	siteURL = input('Please enter your website URL: ')
	# else: 
	# 	siteURL = sys.argv[1]

	if (siteURL[:11] == 'http://www.' or siteURL[:12] == 'https://www.') and siteURL[-4:] in TLDomain:
		pass
	elif (siteURL[:7] != 'http://' or siteURL[:8] != 'https://') and siteURL[:4] == 'www.' and siteURL[-4:] in TLDomain:
		print(siteURL[:6])
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

@app.route('/pillar1')
def pillar1():
	return "Hello"



if __name__ == '__main__':
	app.run()