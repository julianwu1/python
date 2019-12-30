import os
import socket
import time
import sqlite3
from ippy import myip 
def idcfun(id=[]):
	otid=[]
	outstr=''
	allstr=''
	if len(id)==3:
		cok=True
		i=0
		while i<len(id):
			otid.insert(i,hex(id[i]))
			i=i+1
		while i>0:
			i=i-1
			outstr=''+otid[i]
			allstr=allstr+outstr[2:]
		outstr=int(allstr,16)
	else:
		cok=False
	return cok,outstr
def opend():
#	print(time.time())
	print("opendoor")
	time.sleep(5)
#	print(time.time())

def rtdb():
	rtdate=time.strftime("%Y-%m-%d",time.localtime())
	nttime=int(time.strftime("%H%M%S"))
	ottime=0
	if 80000<nttime<95500:
		ottime=1
	elif 95600<nttime<120000:
		ottime=2
	elif 141200<nttime<162200:
		ottime=3
	elif 162300<nttime<180000:
		ottime=4
	elif 190000<nttime<210000:
		ottime=5
	else:
		pass
	return rtdate,ottime

#print(myip)
outudp=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
getudp=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
getudp.bind(("",8018))
a=1
#os.system('sudo date -s "2019-12-21 11:11:11"')
svradd=("192.168.1.11",8016)
outstr="wt"
outudp.sendto(outstr.encode(),svradd)
#opend()
#print(rtdb()) 
try:

	while True:
		ndate,ntime=rtdb()
		pass
		getdb,gadds=getudp.recvfrom(1024)
#		print("R:%s , %s \n" %(gadds,getdb))
#		print(gadds[0])
#		print(gadds[1])
		if getdb[0:2]=='st':
			os.system("sudo date -s \""+ getdb[2:] +"\"")
		elif getdb[0:2]=='op':
			opend()
			
		else:
			pass
#		print(a)
#		time.sleep(2)
#		a=a+1
#		outudp.sendto(str(a).encode(),("192.168.1.29",8068))
except KeyboardInterrupt:
	outudp.close
		


