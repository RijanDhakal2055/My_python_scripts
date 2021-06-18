import pickle

def main():
	with open('species_dict.pkl','rb') as handle:
		the_dict = pickle.load(handle)

	with open('Base_asr.tre','rt') as the_base_file:
		the_base_file_line = the_base_file.readlines()

	for lines in the_base_file_line:
		x = 'AagrBONN'
		if x in lines:
			print(lines)


main()