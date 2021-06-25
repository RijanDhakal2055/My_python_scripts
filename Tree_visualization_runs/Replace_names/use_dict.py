from os import replace
import pickle
import re

def main():

	real_lines = []
	with open('species_dict.pkl','rb') as handle:
		the_dict = pickle.load(handle)

	with open('Base_asr.tre','rt') as the_base_file:
		the_base_file_line = the_base_file.readlines()
<<<<<<< HEAD
=======

	for the_line in the_base_file_line:
		for the_key in the_dict:
			the_line = the_line.replace(the_key,the_dict[the_key])
		print(the_line)
	
		
>>>>>>> 7aaa3b55edba84e1c5e485b34d943595ab9d360b

	for the_line in the_base_file_line:
		for the_key in the_dict:
			x = the_line.replace(the_key,the_dict[the_key])
			print(x)	

main()