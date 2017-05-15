import os
def rename_files():
    file_list = os.listdir("/Users/ma/Downloads/prank")
    os.chdir("/Users/ma/Downloads/prank")
    saved_path = os.getcwd()
    print(file_list)
    for file_name in file_list:
        os.rename(file_name, file_name.translate(str.maketrans('','','0123456789')))
        os.chdir(saved_path)
    
rename_files()
