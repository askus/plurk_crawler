from crawler import plurk_authorize, get_api_result 
CACHE_LENGTH =10

def get_fan( plurk, user_id , size  ):
	ret = list()

	if size == 0 :
		return None 

	for i in xrange(   (size/CACHE_LENGTH) +1 ):
		offset = i* CACHE_LENGTH  
		# cal expect number 
		if offset + CACHE_LENGTH  <= size  :
			expect = CACHE_LENGTH 
		else:
			expect = size - offset
		temp = get_api_result( plurk, "/APP/FriendsFans/getFansByOffset", {"user_id":user_id , "limit": expect,  "offset": offset} )
		if temp == None:
			break
		ret.extend( temp ) 
	if len( ret ) == 0:
		return None
	else: 
		return ret 
def main( filename, output_dir  ):

	infile = open(filename, "r")
	filename_prefix= filename.split("/")[-1]

	total_length = len( infile.read().split("\n") )
	infile.close()
	infile = open(filename, "r")

	outf = open("%s/%s.fan.txt" %(  output_dir , filename_prefix ), "w") 

	plurk = plurk_authorize( ) 

	i= 0
	for l in infile:
		# time counting  
		print "[%s][%.2f] %d/%d" %( filename_prefix  , ( float(i)/ float(total_length) ) , i, total_length ) 
		i +=1 
		# get fans  
		tmp = l.strip().split("\t")
		user_id = long(tmp[1] ) # need repair
		size = int( tmp[0] ) # need repair
		fans = get_fans( plurk, user_id,size  ) 

		if fans ==None:
			continue 
		for fan_dict in fans:
			fan_id = fan_dict['id'] 
			print >> outf, "%d\t%d" %( user_id , fan_id )
		print "%d: %d/ %d" %( user_id, len( fans ), size)
	infile.close()
	outf.close()

