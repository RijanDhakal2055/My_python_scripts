import pickle

def main():

	species_identifiers = {}

	with open("proper_names.txt",'rt') as species_id_pairs:
		specie_id_line = species_id_pairs.readlines()

	for current_line in specie_id_line:
		current_line = current_line.rstrip('\n')
		current_line = current_line.rsplit('\t')
		for i in current_line:
			a = current_line[0]
			b = current_line[1]
			species_identifiers[a] = b

	#the print statement is just me trying to make sure that the cose is working properly

	dict_file = open("species_dict2.pkl","wb")
	pickle.dump(species_identifiers,dict_file)
	dict_file.close()

main()
