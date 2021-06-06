def main():

    with open('Filtered_list.txt','rt') as Filtered_list:
        Filtered_list_lines = Filtered_list.readlines()
    
    with open('Gene_list.txt','rt') as Gene_list:
        Gene_list_lines = Gene_list.readlines()

    with open('Species_identifier_list.txt','rt') as Species_list:
        Species_list_lines = Species_list.readlines()

    for ortho_line in Filtered_list_lines:
        for gene_name in Species_list_lines:
            for species_identifier in Species_list_lines:
                if species_identifier in ortho_line:
                    current_line_count = ortho_line.count(species_identifier)
                    print(gene_name,species_identifier,current_line_count)
        
main()