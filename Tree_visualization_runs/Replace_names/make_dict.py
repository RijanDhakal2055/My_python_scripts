def main():

	species_identifiers = {}

	with open("species_id.txt",'rt') as species_id_pairs:
		specie_id_line = species_id_pairs.readlines()

	for current_line in specie_id_line:
		current_line = current_line.rstrip('\n')
		current_line = current_line.rsplit('\t')
		for i in current_line:
			a = current_line[0]
			b = current_line[1]
			species_identifiers[a] = b

	print(species_identifiers)

main()
