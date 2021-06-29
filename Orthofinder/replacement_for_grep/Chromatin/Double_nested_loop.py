def main():

    with open('chromatin_orthos.txt','rt') as Filtered_list:
        Filtered_list_lines = Filtered_list.readlines()

    with open('species_id.txt','rt') as Species_list:
        Species_list_lines = Species_list.readlines()

    for ortho_line in Filtered_list_lines:
        for species_identifier in Species_list_lines:
            species_identifier = species_identifier.rstrip('\n')       
            current_line_count = ortho_line.count(species_identifier)
            print(ortho_line[:9],species_identifier,current_line_count, sep="\t")
        
main()
