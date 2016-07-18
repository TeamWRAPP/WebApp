#! /usr/bin/env/ python3

# Author: James Bui for Team WRAPP
# File: wrappCookieChecker.py
# Last Modified: July 12, 2016
# Description: This script scraps the website the user enters in to parse out 
#		       the <a> tags that contains links related to the website domain.
#			   It stores the websites in a list and determines if the website 
#			   collects response cookies. Response cookies are cookies that the
#			   website server sends to the client (browser) as opposed to request
#			   cookies, in which the client (browser) requests to the server. 
#		   	   Currently works with federal websites because most comply with 
#			   regulations and standards. Does not work with all private websites. 
from urllib.request import Request, build_opener, HTTPCookieProcessor, HTTPHandler, urlopen
#from urllib.request import build_opener, HTTPCookieProcessor, HTTPHandler, urlopen
from urllib.error import HTTPError
import http.cookiejar
from html.parser import HTMLParser  
from urllib import parse
import argparse 
import sys
import requests
import time 
from bs4 import BeautifulSoup


def crawler(siteURL):
	cookieCount = 0
	finalCookieCount = 0
	siteName = siteURL[11:]
	siteList = []
	r = requests.get(siteURL)
	data = r.text
	soup = BeautifulSoup(data, "html.parser")
	for link in soup.find_all('a'):
		#print(link.get('href'))
		fromDomainURL = link.get('href')
		if isinstance(fromDomainURL, str) and siteName in fromDomainURL:
			#print("FOUND %s"%fromDomainURL)
			siteList.append(fromDomainURL)
		else:
			continue
	for site in siteList:
		#print(site)
		finalCookieCount = getCookie(site, cookieCount)
		#print(cookieCount)
		cookieCount = finalCookieCount
		return 'Your website uses cookies!'
	if finalCookieCount == 0:
		print('Your website does not use any cookies!')
		return 'Your website does not use any cookies!'

def getCookie(url, cookieCount):
	r = requests.get(url)
	c =  r.cookies
	for c in r.cookies:
		cookieCount = cookieCount + 1
		print(c.name, c.value)
	return cookieCount 

def testing():
	return 'Hi my name is James'

def main():
	cookieCount = 0
	TLDomain = ['.com', '.gov', 'org', 'net', 'int', '.edu', '.mil']
	websiteList = []
	if len(sys.argv) != 2:
		siteURL = input('Please enter your website URL: ')
	else: 
		siteURL = sys.argv[1]

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

	printThis = crawler(siteURL)
	print(printThis)



# if __name__ == '__main__':
# 	main()