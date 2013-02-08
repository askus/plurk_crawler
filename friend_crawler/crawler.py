
from plurk_oauth.PlurkAPI import PlurkAPI
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


