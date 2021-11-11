projects = [{'ID NUMBER' : '', 'TITLE':'', 'SIZE':'', 'PRIORITY':''}]

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
            menu1 = int(input("Enter Choice: "))
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
        
        
def __sortProjects(self):
    def mergeSort(projects,l,h):
        # l is low, h is high
        if (l < h):
            m = (l+h)//2  # middle of l to h
            mergeSort(projects,l,m)
            mergeSort(projects,m+1,h)
            merge(projects,l,m,h)
    def merge(projects,l,m,h):
            n1 = m-l+1  
            n2 = h-m    
            left = []   
            right = []  
            for i in range(n1):
                left.append(projects[l+i-1])
            for i in range(n2):
                right.append(projects[m+i])
            lCtr = 0
            rCtr = 0
            k = l-1
            while (lCtr < len(left) and rCtr < len(right)):
                if (left[lCtr].getPriority() < right[rCtr].getPriority()):
                    projects[k] = left[lCtr]
                    lCtr += 1
                elif (left[lCtr].getPriority() > right[rCtr].getPriority()):
                    projects[k] = right[rCtr]
                    rCtr+=1
                else:
                    if (left[lCtr].getSize() < right[rCtr].getSize()):
                        projects[k] = left[lCtr]
                        lCtr+=1
                    else:
                        projects[k] = right[rCtr]
                        rCtr+=1
                k+=1
            if (lCtr != len(left)):
                for i in range(k,h):
                    projects[i] = left[lCtr]
                    lCtr+=1
            elif (rCtr != len(right)):
                for i in range(k,h):
                    projects[i] = right[rCtr]
                    rCtr+=1
        mergeSort(self.__currentProjects,1,len(self.__currentProjects))
        
        def create_schedule():
    sort = sorted(projects.items(), key=lambda item: item[1][2], reverse=True)
    sorted_priority = {k: v for k, v in sort}
    first_run = True
    last_run = 0
    temp_dict = {}
    sorted_size = {}
    temp = ''
    for count in sorted_priority.keys():
        if first_run:
            temp_dict[count] = [sorted_priority[count][0], sorted_priority[count][1], sorted_priority[count][2]]
            last_run = last_run + 1
            first_run = False
        elif temp != sorted_priority[count][2]:
            sort = sorted(temp_dict.items(), key=lambda item: item[1][1], reverse=True)
            temp_dict = {k: v for k, v in sort}
            sorted_size.update(temp_dict)
            temp_dict = {}
            temp_dict[count] = [sorted_priority[count][0], sorted_priority[count][1], sorted_priority[count][2]]
            last_run = last_run + 1
        elif temp == sorted_priority[count][2]:
            temp_dict[count] = [sorted_priority[count][0], sorted_priority[count][1], sorted_priority[count][2]]
            last_run = last_run + 1

        if last_run == len(sorted_priority):
            sort = sorted(temp_dict.items(), key=lambda item: item[1][1], reverse=True)
            temp_dict = {k: v for k, v in sort}
            sorted_size.update(temp_dict)
            temp_dict = {}

        temp = sorted_priority[count][2]

    return sorted_size