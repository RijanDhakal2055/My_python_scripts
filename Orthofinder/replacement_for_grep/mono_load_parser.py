def main():
    with open('8_orthos.txt','rt') as small_list:
        small_list_lines = small_list.readlines()

    for i in small_list_lines:
        i = i.rstrip('\n')
        parser(i)

def parser(current):
    
    with open('Orthogroups.tsv','rt') as big_list:
        big_list_lines = big_list.readlines()
    
    for line in big_list_lines:
        split_by_tabs = line.rsplit('\t')
        for the_comma_group in split_by_tabs:
            split_by_commas = the_comma_group.rsplit(',')
            for the_gene in split_by_commas: #this opens the individual words/genes in the line as a list and tries to see for partial strings in indiviudual words/genes
                if current in the_gene:
                    print(current,line)

main()

