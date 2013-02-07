from sys import argv
from plurk_oauth.PlurkAPI import PlurkAPI
import json
import socket


dataset="plurk_iii"

#plurk = PlurkAPI("TmJ2fUfRcy3X", "kuBsGZH8qBw34h9uytZgNWFC37PkYv66")
#plurk.authorize("fqG3DURTDfvA", "EcpTJdGsxHEaCx4TxIMlKR1tksPEuf09")


plurk = PlurkAPI("GZpz46uhKUJv", "EWoX6KK9laSEOhtWCJt8n6xZUmvxrliq")
plurk.authorize("UNtfaxzZFPI2", "BXP7E9V8GVrHFWJaIDCiZ2ArXKF0xrB8")



script, filename= argv
infile = open(filename, "r")

filename_prefix= filename.split("/")[-1]

total_length = len( infile.read().split("\n") )
infile.close()
infile = open(filename, "r")

errorfile = open("error/%s/%s.error.txt" %( dataset, filename_prefix ) , "w")
outf = open("result/%s/%s.user_table.txt" %(  dataset, filename_prefix ), "w") 

#print >> outfile, (string[0] + "\tgender")


i= 0
for l in infile:
	tmp = l.strip().split("\t")
	userid = tmp[0]
	try:
		temp = plurk.callAPI("/APP/Profile/getPublicProfile", {"user_id": userid})
	except:
		continue

	print "[%s][%.2f] %d/%d" %( filename_prefix  , ( float(i)/ float(total_length) ) , i, total_length )  
	i +=1 
	if not temp == None:
		userinfo = temp.get("user_info")
		print >>outf, userinfo
	else:
		print >> errorfile, (userid + " could not find!")
	

infile.close()
outf.close()
errorfile.close()

