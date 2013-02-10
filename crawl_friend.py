import friend_crawler.friend_crawler as crawler 
import sys
import os , os.path
script, filename = sys.argv 

output_dir = "/tmp2/r99944049/"

if not os.path.exists( output_dir ) :
	os.makedirs( output_dir ) 


crawler.main( filename , output_dir ) 
