#_*_coding=UTF-8_*_
# copyright 2019 BILLAL FAUZAN
# Karya Anak Bangsa
# MD5 DENCRYPT Offline 90%

"""
NOTE:
	Please Abang Eneng Jangan Ubah Source Code Ny
	Saya Susah Payah Membuat Program Ini
	Saya Sengaja Open Source Supaya Anak Indonesia Bisa Membuat Program Sendiri

	Jadi
	Jangan Di Recode Bangsat!!
"""
__banner__ = """
    __  __           __    ____
   / / / /___ ______/ /_  / __ \___  _____
  / /_/ / __ `/ ___/ __ \/ / / / _ \/ ___/
 / __  / /_/ (__  ) / / / /_/ /  __/ /__
/_/ /_/\__,_/____/_/ /_/_____/\___/\___/
     copyright 2019 Billal Fauzan

INFO:
    Author : Billal Fauzan
    Version: 1.0
    Name   : Hash Dencrypter Offline 50%

"""
try:
	import os,sys,time,hashlib
except Exceptions as E:
	print ("[Err]: "+str(E))
	sys.exit()

def dencrypt(hash,password):
	sys.stdout.write("\r\n[!] Trying: "+str(password))
	sys.stdout.flush()
	time.sleep(0.1)
	md5 = hashlib.md5()
	md5.update(str(password))
	md = md5.hexdigest()
	if hash == md:
		print ("\n[+] Found: "+str(password))
		sys.exit()

def main():
	print (__banner__)
	hash = raw_input("[?] Hash: ")
	wordlist =""
	while True:
		p = raw_input("[?] Wordlist Default? (Y/n): ")
		if p in ["Y","y"]:
			wordlist = "password.txt"
			break
		elif p in ["N","n"]:
			wordlist = raw_input("[?] Wordlist: ")
			break
	try:
		pw = open(wordlist,"r").read()
		for password in pw.splitlines():
			dencrypt(hash,password)
	except IOError:
		print ("[Err]: File %s not found"%(wordlist))
		sys.exit()
main()
