import friend_crawler.friend_crawler as crawler 
import sys
script, filename = sys.argv 
output_dir = "result/friends/"
crawler.main( filename , output_dir ) 
