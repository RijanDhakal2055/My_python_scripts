import pickle

def main():
	with open('species_dict2.pkl','rb') as handle:
		the_dict = pickle.load(handle)

	with open('chromatin.tsv','rt') as the_base_file:
		the_base_file_line = the_base_file.readlines()

	for the_line in the_base_file_line:
		for the_key in the_dict:
			the_line = the_line.replace(the_key,the_dict[the_key])
		print(the_line)
	
		


main()
