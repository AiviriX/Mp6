from os import mkdir, path
import os.path
from os.path import exists
import json

dirPath = "C:/Mp6/Projects"
projectPath = "C:/Mp6/Projects/Current Projects.txt"
allProjects = "C:/Mp6/Projects/All Projects.txt"
completedProjects = "C:/Mp6/Projects/Completed Projects.txt"


projects = []

def sep_line():
    '''Printing Dashes'''
    return "-----------------"

def input_project():
    '''Entering Project Details'''
    print(sep_line())
    print("Input Project Details")
    id_num = int(input("ID Number: "))
    title = input("Title: ")
    size = int(input("Number of pages: "))
    prio = int(input("Priority: ")) 
    projects.append({'ID NUMBER':id_num,
                     'TITLE': title,
                     'SIZE': size,
                     'PRIORITY': prio})
    #Dump List Contents into a file
    try:
        file = open(projectPath, "x")
        file.close()
    except FileExistsError:
        file = open(projectPath, 'w')
        for data in projects:
            file.write(str(data['ID NUMBER'])+"\n")
            file.write(str(data['TITLE'])+"\n")
            file.write(str(data['SIZE'])+"\n")
            file.write(str(data['PRIORITY'])+"\n")
            file.write(str("\n"))




    print("Project", title, "successfully added.")
    print(projects)

def view_project():
    '''View Projects'''
    print(sep_line())
    print('a. One Project\nb. Completed Projects\n c. All Projects')
    viewchoice = input("Enter Choice: ")
    if viewchoice == 'a':
        v_get_id = int(input("Enter Project ID: "))
        for i in projects:
            if i['ID NUMBER'] == v_get_id:
                print('\nID NUMBER', i['ID NUMBER'])
                print('\nNAME', i['TITLE'])
                print('\nSIZE', i['SIZE'])
                print('\nPRIORITY', i['PRIORITY'])
    elif viewchoice == 'b':
        print("choice B")
    elif viewchoice == 'c':
        print("choice c")

#------------ RUN EVERYTIME THE PROGRAM LAUNCHES ---------------
#Check if the directory Exists
folderCheck = os.path.isdir(dirPath)
try:
    if folderCheck != True:
        mkdir("C:/Mp6/Projects")
        print("Created the Project Folder.")
    else:  
        #If file exists, check for contents
        print("Folder Exists")
        file = open(projectPath, "r")
        file.read
except FileNotFoundError:
    mkdir("C:/Mp6/")
    print("File MP6 and CreateProject Created")



#----------------------------------------------------------------

while True:
    print("1. Input Project Details")
    print("2. View Projects")
    print("3. Schedule Projects")
    print("4. Get a Project")
    print("5. Exit")

    menu1 = int(input("Enter Choice: "))

    if menu1 == 1:
        print("Select one")
        input_project()
    elif menu1 == 2:
        #insert 2
        print(sep_line())
        print("Viewing Projects:")
        view_project()
    elif menu1 == 3:
                print("1. Create Schedule\n"
                    "2. View Updated Schedule\n")
                choice = int(input("Enter Choice: "))

                if choice == 1:
                    queue_projects = create_schedule()
                elif choice == 2:
                    show_all(queue_projects)
                else:
                    print("Wrong input, try again.")
    elif menu1 == 4:
        #insert 4
        print("Select four")
    elif menu1 == 5:
        print("Select 5")
        break