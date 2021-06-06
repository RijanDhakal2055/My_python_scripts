from io import SEEK_CUR


def main():

    with open('Filtered_list.txt','rt') as Filtered_list:
        Filtered_list_lines = Filtered_list.readlines()
    
    with open('Gene_list.txt','rt') as Gene_list:
        Gene_list_lines = Gene_list.readlines()

    with open('Species_identifier_list.txt','rt') as Species_list:
        Species_list_lines = Species_list.readlines()

    for i in Filtered_list_lines:
        x = 'Vocar'
        if x in i:
            S_count = i.count(x)
            print(S_count)


main()