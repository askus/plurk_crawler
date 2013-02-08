import sys 
from plurk_oauth.PlurkAPI import PlurkAPI
import json
import socket


def xstr( inpt ):
	#if isinstance( inpt, str):
	#	return inpt
	#print inpt
	#return str( inpt)

	print inpt 

	if inpt == None:
		return ""
	if isinstance( inpt, float) or isinstance( inpt , bool) or isinstance( inpt, int )  :
		return str( inpt )
	if isinstance( inpt, list) :
		return "|".join( inpt)  
	return inpt.encode("utf8").replace( "\r","").replace("\n", "").strip()

def plurk_authorize(  ): 
	plurk = PlurkAPI("GZpz46uhKUJv", "EWoX6KK9laSEOhtWCJt8n6xZUmvxrliq")
	plurk.authorize("UNtfaxzZFPI2", "BXP7E9V8GVrHFWJaIDCiZ2ArXKF0xrB8")
	return plurk	

# need authorization first 

def get_api_result( plurk, api, param ) : 
	try:
		temp = plurk.callAPI( api , param )
	except:
		temp = None 
	return temp 

def get_userdata( plurk , user_id ) :
	temp = get_api_result( plurk, "/Users/getUserData" , {"page_uid": user_id } ) 
	if temp == None:
		return None
	temp['user_id'] = user_id 
	return temp 
def get_userdata_keys( plurk):
	return get_userdata( plurk, 3 ).keys() 


def get_profile( plurk, user_id ):
	temp = get_api_result( plurk,  "/APP/Profile/getPublicProfile", {"user_id": user_id} )
	if temp == None:
		return None
	return temp.get("user_info") 
def get_profile_keys( plurk   ) :
	return get_profile( plurk, 3 ).keys() # alvin's id  


def main( argv= sys.argv ):
	dataset="plurk_iii"

	script, filename= argv
	infile = open(filename, "r")

	filename_prefix= filename.split("/")[-1]

	total_length = len( infile.read().split("\n") )
	infile.close()
	infile = open(filename, "r")

	outf = open("result/%s.user_table.txt" %(   filename_prefix ), "w") 

	plurk = plurk_authorize( ) 
	keys = get_userdata_keys( plurk ) 
	print >>outf , "\t".join( keys) 

	i= 0
	for l in infile:
		# time counting  
		print "[%s][%.2f] %d/%d" %( filename_prefix  , ( float(i)/ float(total_length) ) , i, total_length ) 
		i +=1 
		# get profile  
		tmp = l.strip().split("\t")
		user_id = tmp[0]
		userdata = get_userdata( plurk, user_id )  
		if userdata ==None:
			continue 
		print >>outf , "\t".join( [ xstr(v)  for v in  userdata.values() ] ) 
	
	infile.close()
	outf.close()
