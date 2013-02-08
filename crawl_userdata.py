import friend_crawler.userdata_crawler as userdata_crawler 
import sys 
import os.path , os 
script , filename = sys.argv

output_dir = "/tmp2/r99944049/"

if not os.path.exists( output_dir ) :
	os.makedirs( output_dir ) 

userdata_crawler.main( filename, output_dir ) 
