def main():

    with open('Filtered_list.txt','rt') as Filtered_list:
        Filtered_list_lines = Filtered_list.readlines()
    
    with open('Gene_list.txt','rt') as Gene_list:
        Gene_list_lines = Gene_list.readlines()

    for i in Filtered_list_lines:
        X ="AT3G48750"
        if X in i:
            print(i)

main()