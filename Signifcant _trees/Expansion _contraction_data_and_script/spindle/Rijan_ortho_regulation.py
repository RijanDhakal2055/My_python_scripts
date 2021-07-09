import re
import pandas as pd

"""
Make sure you change:
r_path: the pathway to your files (line 12)
sp_df: your file name for the .tab file (line 13)
with open..... line with the correct corresponding .tre file (line 20)
my_df.to_csv.... line to save your file - give it an appropriate name (line 59)
"""

r_path = '/home/wolf/Desktop/My_python_scripts/Signifcant _trees/Expansion _contraction_data_and_script/spindle/'
sp_df = pd.read_csv(r_path + 'Spindle_Base_change.tab', delim_whitespace=True)
sp_df.set_index('FamilyID', inplace=True)
print(sp_df.shape)
print(sp_df.iloc[:5,:5])

my_df = pd.DataFrame(columns=['ortho_group', 'node_name', 'type'])

with open(r_path + "Significant_spindle_asr.tre") as fp:
    Lines = fp.readlines()
    for line in Lines:
        # getting name of ortho group: i.e. OG0123456
        # this makes it to a list
        ort = re.findall(r'TREE (.*) =', line)
        # should only be a list of one item
        if len(ort) > 1:
            ortho = 'failed'
        else:
            ortho = ort[0]
        print('ortho is {}'.format(ortho))
        # put all significant (*) nodes to list: i.e. <19>*
        sigs = re.findall(r'<[0-9][0-9]*>\*', line)
        # for each significant node
        for i in range(0,len(sigs)):
            my_list=[]
            # get name of node wihtout the *
            name = sigs[i].split('*')[0]
            # column names from the .tab file that contain the significant node name
            one = [col for col in sp_df.columns if name in col]
            # going to the .tab file and find number as per index and column name
            regulation = sp_df.loc[ortho,one[0]]
            # give the number an exquivalent of Expansion or Contraction if + or - value
            if int(regulation) > 0:
                reg = 'Expansion'
            elif int(regulation) < 0:
                reg = 'Contraction'
            else:
                reg = "NILL"
            #Put 3 values to a list and then add to dataframe
            my_list.append(ortho)
            my_list.append(one[0])
            my_list.append(reg)
            len_df = my_df.shape[0]
            my_df.loc[len_df] = my_list
            
            
print(my_df.shape)
my_df.to_csv(r_path + 'Rijan_spindle.csv', index=False)
