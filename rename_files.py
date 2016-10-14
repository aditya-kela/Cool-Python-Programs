#from os import listdir
#from os import chdir
#from os import rename
def rename_files():
    file_list = listdir(r"/Users/adityakela/Desktop/prank")
    print(file_list)
    chdir(r"/Users/adityakela/Desktop/prank")

    for file_name in file_list:
    	rename(file_name, file_name.translate(None, '0123456789'))
    print(file_list)	

rename_files()

