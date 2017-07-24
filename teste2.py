import socket

def retBanner(ip, port):
	try:
		socket.setdefaulttimeout(2)
		s = socket.socket()
		s.connect((ip, port))
		banner = s.recv(1024)
		return banner
	except:
		return

def checkVulns(banner):
	f = open("vuln_banners.txt",'r')
	for line in f.readlines():
		if line.strip('\n') in banner:
			print "[+] Server is vulnerable: "+banner.strip('\n')



	"""if 'FreeFloat Ftp Server (Version 1.00)' in banner:
		print '[+] FreeFloat FTP Server is vulnerable.'
	elif '3Com 3CDaemon FTP Server Version 2.0' in banner:
		print '[+] 3CDaemon FTP Server is vulnerable.'
	elif 'Ability Server 2.34' in banner:
		print '[+] Ability FTP Server is vulnerable.'
	elif 'Sami FTP Server 2.0.2' in banner:
		print '[+] Sami FTP Server is vulnerable.'
	else:
		print '[-] FTP Server is not vulnerable.'
	return"""

def main():
	portList = [21,22,25,80,110,443,6666]
	for x in range(134, 190):
		ip = "10.50.20." + str(x)
		for port in portList:
			banner = retBanner(ip,port)
			if banner:
				print '[+] ' + ip + ': ' + banner
				checkVulns(banner)
	"""ip1 = '192.168.95.150'
	ip2 = '10.50.20.167'
	ip3 = '10.50.20.189'
	port = 6666

	banner1 = retBanner(ip1,port)
	if banner1:
		print '[+] ' + ': ' + banner1.strip('\n')
		checkVulns(banner1)
	banner2 = retBanner(ip2,port)
	if banner2:
		print '[+] ' + ': ' + banner2.strip('\n')
		checkVulns(banner2)
	banner3 = retBanner(ip3,port)
	if banner3:
		print '[+] ' + ': ' + banner3.strip('\n')
		checkVulns(banner3)"""
if __name__ == '__main__':
	main()