def main():

    with open('Filtered_list.txt','rt') as Filtered_list:
        Filtered_list_lines = Filtered_list.readlines()
    
    with open('Gene_list.txt','rt') as Gene_list:
        Gene_list_lines = Gene_list.readlines()

    with open('Species_identifier_list.txt','rt') as Species_list:
        Species_list_lines = Species_list.readlines()

    
main()