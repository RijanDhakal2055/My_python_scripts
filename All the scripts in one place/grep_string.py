def main():

    list_of_orthos =[]

    with open('spindle_orthos.txt','rt') as read_file:
        list_of_lines = read_file.readlines()
        #list_of_lines = list_of_lines.rstrip()
    
    for i in list_of_lines:
        x = 'OG'
        list_of_tabbs = i.rsplit('\t')
        for g in list_of_tabbs:
            if x in g:
                if g not in list_of_orthos:
                    list_of_orthos.append(g)

    for r in list_of_orthos:
        r = r.rstrip('\n')
        print(r)
main()
