import os

savepath = 'C:\\Mp6'
file_name = input("Enter File Name")
complete_path = os.path.join(savepath, file_name+".txt")
file1 = open(complete_path, "r")

file1.read()