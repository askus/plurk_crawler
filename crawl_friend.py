import friend_crawler.userdata_crawler as userdata_crawler 
import sys 
import os.path , os 
script , filename, output_dir = sys.argv
if not os.path.exists( output_dir ) :
	os.makedirs( output_dir ) 
userdata_crawler.main( filename, output_dir ) 
