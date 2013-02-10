from crawler import plurk_authorize, get_api_result 
CACHE_LENGTH =10

def get_friend( plurk, user_id , size  ):
	ret = list()
	
	for i in xrange(   (size/CACHE_LENGTH) +1 ):
		offset = i* CACHE_LENGTH  
		# cal expect number 
		if offset + CACHE_LENGTH  <= size  :
			expect = CACHE_LENGTH 
		else:
			expect = size - offset
		temp = get_api_result( plurk, "/APP/FriendsFans/getFriendsByOffset", {"user_id":user_id , "limit": expect,  "offset": offset} )
		if temp == None:
			break

		#print "offset =%d, expect = %d, size=%d, len( temp) = %d" % ( offset, expect, size, len( temp) )
		#while True:	
		#	temp = get_api_result( plurk, "/APP/FriendsFans/getFriendsByOffset", {"user_id":user_id , "limit": expect,  "offset": offset} )
		#	if temp == None:
		#		break
		#	if len( temp) < expect :
		#		print "offset =%d, expect = %d, size=%d, len( temp) = %d" % ( offset, expect, size, len( temp) )
		#		continue 

		ret.extend( temp ) 

	#if temp == None:
	#	return None
	#print temp
	#return temp 
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

	outf = open("%s/%s.friend.txt" %(  output_dir , filename_prefix ), "w") 

	plurk = plurk_authorize( ) 

	i= 0
	for l in infile:
		# time counting  
		print "[%s][%.2f] %d/%d" %( filename_prefix  , ( float(i)/ float(total_length) ) , i, total_length ) 
		i +=1 
		# get friends  
		tmp = l.strip().split("\t")
		user_id = long(tmp[1] ) # need repair
		size = int( tmp[3] ) # need repair
		friends = get_friend( plurk, user_id,size  ) 
		print "%d: %d/ %d" %( user_id, len( friends ), size)

		if friends ==None:
			continue 
		for friend_dict in friends:
			friend_id = friend_dict['id'] 
			print >> outf, "%d\t%d" %( user_id , friend_id )
			print >> outf, "%d\t%d" %( friend_id, user_id ) 
	infile.close()
	outf.close()

