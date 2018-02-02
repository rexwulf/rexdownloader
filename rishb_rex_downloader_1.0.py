#!/usr/bin/python
import os,re,subprocess
from bs4 import BeautifulSoup, NavigableString
import urllib.request as urllib2
import os.path
import pathlib
import shutil

musicdir=""

def download(downname,downurl,wd):
	#print(downurl)
	if wd == 1:
		r=os.system("axel -a -n 16 -o ./320kbps/"+downname+" "+downurl),
	elif wd == 2: 
		r=os.system("aria2c -x 16 -d ./320kbps/ -o "+downname+" "+downurl),
	elif wd == 3: 
		r=os.system("wget --show-progress -O "+musicdir.replace(' ','\ ')+"/320kbps/"+downname.replace(' ','\ ')+" "+downurl)
	return r


if __name__ == '__main__' :
	row, col = os.popen('stty size', 'r').read().split()
	print("\n\n")
	print("-"*int(col))
	print("ＲＩＳＨＢ ＲＥＸ ＤＯＷＮＬＯＡＤＥＲ １．０".center(shutil.get_terminal_size().columns-20))
	print("Author: Rishabh Bharti".center(shutil.get_terminal_size().columns))
	print("License: No fuck license".center(shutil.get_terminal_size().columns))

	print("-"*int(col))
	print("\nSelect downloader: \n1. Axel \n2. Aria2c \n3. Wget\n")
	wd = int(input())
	musicdir = "/Users/rex/Downloads/New Folder With Items/untitled folder"
	os.chdir(musicdir)
	os.system("mkdir ./320kbps")
	print("Directory created: files will be stored in 320kbps")
	files = [f for f in os.listdir('.') if os.path.isfile(f)]
	i = 1
	downname=""
	ln=str(len(files))
	print("\nFollowing "+ln+" files will be processed:")
	for f in files:
		print(str(f))
	for f in files:
		print("\nProcessing ("+str(i)+"/"+ln+") : \n")
		if f[0] == '.' :
			print("Not a valid file")
			os.system("clear")
			i=i+1
			continue
		n = f.split('.')[0]
		name = re.sub(r'[\W_]+', '-', n)
		url1 = "http://www.theinstamp3.com/download/"+name+".html"
		req = urllib2.Request(url1, headers={'User-Agent': 'Mozilla/5.0'})
		page1 = urllib2.urlopen(req)
		soup = BeautifulSoup(page1, "html.parser")

		yo = soup.find_all("a", {"class" : "downnow"})
		pre = "http://www.theinstamp3.com/mp3"
		l=[]
		for link in yo:
				if isinstance(link, NavigableString):
					continue
				if link["href"].startswith(pre):
					l.append(link["href"])
					break
		#print(yo)
		#print("\nAvailable locations:\n")
		#print(l)
		for url2 in l:
			req = urllib2.Request(url2, headers={'User-Agent': 'Mozilla/5.0'})
			page2 = urllib2.urlopen(req)
			soup = BeautifulSoup(page2, "html.parser")
			yo = soup.find_all(href=True)
			pre = "http://yt2converter.com"
			downurl = ""
			print("Starting Download: "+n+"\n")
			for link in yo:
				if isinstance(link, NavigableString):
					continue
				if link["href"].startswith(pre):
					downurl=(link["href"])
					break
					
			downname = name+".mp3"
			downurl = "\""+downurl+"\""
			r = download(downname,downurl,wd)
			if type(r) != int:
				r = int(r[0])
			print(str(r)+" so ")
			if r != 256:
				break
			print("trying a different source...")
			
		try:
			os.rename(downname,n+".mp3")
		except:
			print(downname+" but "+n+".mp3")
		i=i+1
		os.system("clear")
		
	print("-"*int(col))
	print("ＣＯＭＰＬＥＴＥＤ".center(shutil.get_terminal_size().columns-10))
	print("-"*int(col))
	exit()
	
