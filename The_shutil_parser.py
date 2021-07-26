import shutil

import os 

def main():

    list_of_files = os.listdir()

    desired_location = '/home/wolf/Desktop/Run_folder/Desired_ortho_sequences'

    location = '/home/wolf/Desktop/Rijan/ortho_results/OrthoOutput/Rijan_Orthofinder_directory/protein_data/OrthoFinder/Results_Apr14/Orthogroup_Sequences'

    with open('Ortho_groups_of_interest_.txt', 'rt') as desired_list:
        list_of_names = desired_list.readlines()
        list_of_names = list_of_names.rstrip('\n')

    for i in list_of_names:
        for root_path, dir_names, file_names in os.walk(location,topdown=True):
            for file_name in file_names:
                file_path = os.path.join(root_path,file_name)
                file_path_upper = file_path.upper()
                if i in file_path_upper:
                    shutil.copy(file_path,desired_location)



main()