########### IMPORT LIBRARIES ##############
from datetime import datetime
import re

################### LOGIN SECTION #################

# getting username
username = str(input("Enter Your Username: ")).lower()
# reading and looping through 'user.txt' for username
with open("user.txt", "r+") as username_file:
    # reading file lines
    read_file1 = username_file.readlines()
    while read_file1:
        # looping through the file lines and indexing the usernames
        for word in read_file1:
            new_file = word.replace(",","")
            the_usernames = new_file.split()
            # username confirmation 
            if username == the_usernames[0]:
                break
        # username error message and repeated input
        if username != the_usernames[0]:
            print("You have entered the wrong username, please try again.")
            username = str(input("Enter Your Username: ")).lower()
        else:
            pass
        # username confirmation loop break
        if username == the_usernames[0]:
            break

# getting password
password = input("Enter Your Password: ").lower()
#storing the entered details
details = f"{username}, {password}"
 # For Python 3: use input() instead
with open('user.txt') as f:
    # read the file lines and listing them
    read_f = f.readlines()
    # running a while loop
    while read_f:
        # looping through the lines
        for line in read_f:
            new_file2 = line.replace("\n","")
        # username and password confirmation
            if details == new_file2:
                  break 
        if details == new_file2:
            break
        elif details != new_file2:
            print("You have entered the wrong password, please try again.")
            password = input("Enter Your Password: ").lower()
            details = f"{username}, {password}"
            if details == new_file2:
                break
            else:
                continue
        else:
            pass

while True:
    # Present the menu to the user and 
    # make sure that the user input is converted to lower case.
    if username == "admin":
        menu = input('''Select one of the following options:
        r - register a user
        a - add task
        va - view all tasks
        vm - view my tasks
        gr - generate reports
        s - statistics
        e - exit
        : ''').lower()
    else: 
        menu = input('''Select one of the following options:
        r - register a user
        a - add task
        va - view all tasks
        vm - view my tasks
        e - exit
        : ''').lower()

    if menu == 'r':
        def reg_user(username):
            if username == "admin":
            # creating a new 'user.text' file for registered user
                with open("user.txt", "r+") as register:
                    # new username input
                    new_username = str(input("Enter Username: ")).lower()
                    # reading the lines of the file
                    read_register = register.readlines()
                    # looping thorugh each line on the file
                    for line in read_register:
                        # splitting the lists
                        split_register = line.split(",")
                        # indexing the usernames
                        the_username = split_register[0:1:2]
                        # looping the usernames
                        for word in the_username:
                            # validating if 'new username' exists
                            existing_username = word
                            if new_username == existing_username:
                                print("Username Already Exists")
                            else:
                                pass
        
                        if new_username != existing_username:
                            pass
                        # prompting if the new username exists
                        while new_username == existing_username:
                            print("Try Entering Another Username.")
                            new_username = str(input("Enter Username: ")).lower()
                            if new_username != existing_username:
                                break
                            else:
                                continue
                        else:
                            pass
                    # new password input
                    new_password = input("Enter Password: ").lower()
                    # password confirmation
                    confirm_password = input("Confirm Password: ").lower()
                    while new_password != confirm_password:
                        confirm_password = input("Confirm Password: ").lower()
                    else:
                        # writing the details into 'user.txt' file
                        register.write(f"\n{new_username}, {confirm_password}") 
            else:
                # confirming 'admin' permission
                print("Only Admin can register users\n")
        reg_user(username)

    elif menu == 'a':
        def add_task():
            # username input
            task_username = str(input("Enter Username: ")).lower()
            # title input
            title = str(input("Enter Title: "))
            # description input
            description = str(input("Enter Description: "))
            # due date input
            print("Please enter the due date in the the format stated (eg. 23 Oct 2023):")
            day = int(input("Day (eg. 23): "))
            month = (input("Month (eg. Oct): "))
            year = int(input("Year (eg. 2023): "))
            # current date registration
            now = datetime.now()
            current_date = now.strftime("%d %b %Y")
            # task completion checker
            task_completion = "No"
            # appending the added task into the 'tasks.txt' file
            with open("tasks.txt", "a+") as tasks:
                # writing the details into 'tasks.txt' file
                tasks.write(f"\n{task_username}, {title}, {description}, {day} {month} {year}, {current_date}, {task_completion}")
        add_task()


    elif menu == 'va':
        def view_all():
            # reading the tasks from 'tasks.txt' file
            with open("tasks.txt", "r") as view_tasks:
                read_tasks = view_tasks.readlines()
                # looping through the tasks registered
                for screening_all_tasks in read_tasks:
                    all_tasks = screening_all_tasks.split(",")
                    # printing in 'output 2' format
                    print("___________________________________________\n")
                    print(f"Task:\t\t\t{all_tasks[1]}")
                    print(f"Assigned to: \t\t {all_tasks[0]}")
                    print(f"Date Assigned:\t\t{all_tasks[3]}")
                    print(f"Due Date:\t\t{all_tasks[4]}")
                    print(f"Task Complete?\t\t{all_tasks[5]}")
                    print(f"Task Description:\n {all_tasks[2]}\n")
                    print("___________________________________________\n")
        view_all()
      

    elif menu == 'vm':
        
        # reading file for use
        with open("tasks.txt", "r+") as my_tasks:

            # reading lines and coverting them into a list
            read_file3 = my_tasks.readlines()
            # looping though the list for each item
            for screening_task in read_file3:
                    # splitting the item on its commas
                    screening = screening_task.split(",")
                    # indexing the username
                    registered_username = screening[0]
                    # 'username' confirmation
                    if username == registered_username:
                            # searching though the sentences to find 'username'
                            word_search = [ x for x in read_file3 if username in x]
                            # looping through the sentences that the 'username' is in
                            for count, real_task in enumerate(word_search, start=1):
                                    # splitting the sentences that have 'username'
                                    screening_search = real_task.split(",")
                                    # printing using 'output 2' format
                                    print("___________________________________________\n")
                                    print(f"Task No.: {count}")
                                    print(f"Task:\t\t\t{screening_search[1]}")
                                    print(f"Assigned to: \t\t {screening_search[0]}")
                                    print(f"Date Assigned:\t\t{screening_search[3]}")
                                    print(f"Due Date:\t\t{screening_search[4]}")
                                    print(f"Task Complete?\t\t{screening_search[5]}")
                                    print(f"Task Description:\n {screening_search[2]}\n")
                                    print("___________________________________________\n")
                            # asking for task no input
                            task_selection = int(input("Select A Task: Type the number of your task, Type '-1' to return to main menu.\n"))
                            # validating task number 
                            for entry in range (1,len(read_file3)+1):
                                # validating if task number is equal to range
                                if task_selection == entry:
                                    # get task choice
                                    task_choice = int(input("Edit Task(1) or Mark Task(2): "))
                                    if task_choice == 1:
                                        # looping through the tasks 
                                        for count, task_editor in enumerate(read_file3, start=1):
                                            # validating task selection
                                            if task_selection == count:
                                                # reading 'tasks' file 
                                                with open("tasks.txt", "r") as task_editors:
                                                    # reading 'tasks' lines
                                                    read_file4 = task_editors.readlines()
                                                    # indexing string of task selected
                                                    for target_string in read_file4[task_selection-1:task_selection]:
                                                        # checking if task is not complete
                                                        task_complete_marker = r"No"
                                                        # validating if task is uncompleted 
                                                        match = re.search(task_complete_marker, target_string)
                                                        # conditionals for uncompleted task
                                                        if match != None: 
                                                            # getting input for task editing options
                                                            changer = int(input("Change Person Responsible For Task(1) or Change Due Date(2):\n"))
                                                            if changer == 1:
                                                                # getting new name for tasks
                                                                new_person = input("Enter A New Name: ")
                                                                # opening the file for writing
                                                                with open("tasks.txt", "w") as the_tasks:
                                                                        # replacing the 'No' with 'Yes'
                                                                        responsible_person = target_string.replace(screening_search[0],new_person)
                                                                        # looping through the line
                                                                        for sentence in read_file4:
                                                                            # writing and replace existing line
                                                                            if line != task_selection:
                                                                                the_tasks.write(sentence)
                                                                                the_tasks.write(responsible_person)
                                                                                break
                                                            elif changer == 2:
                                                                # getting new due date input
                                                                print("Enter New Due Date:")
                                                                day = int(input("Day (eg. 23): "))
                                                                month = (input("Month (eg. Oct): "))
                                                                year = int(input("Year (eg. 2023): "))
                                                                # opening the file for writing
                                                                with open("tasks.txt", "w") as the_tasks:
                                                                        # replacing the 'No' with 'Yes'
                                                                        new_due_date = target_string.replace(screening_search[4],f" {day} {month} {year}")
                                                                        # looping through the line
                                                                        for sentence in read_file4:
                                                                            # writing and replace existing line
                                                                            if line != task_selection:
                                                                                the_tasks.write(sentence)
                                                                                the_tasks.write(new_due_date)
                                                                                break

                                                        else:
                                                            print("Match Not found")
                                                            

                                    elif task_choice == 2:
                                        # getting task marker input
                                        task_marker = input("Mark Task as complete(Yes/No): ").lower()
                                        # conditionals for 'yes' option
                                        if task_marker == "yes":
                                            # looping through the tasks 
                                            for count, checking_task in enumerate(read_file3, start=1):
                                                # matching task selection with task number 
                                                if task_selection == count:
                                                    # opening the file for writing
                                                    with open("tasks.txt", "w") as the_tasks:
                                                        # indexing the task selected
                                                        for exact_task in read_file3[task_selection-1:task_selection]:
                                                            # replacing the 'No' with 'Yes'
                                                            marking_task = exact_task.replace("No","Yes")
                                                            # looping through the line
                                                            for line in read_file3:
                                                                # writing and replace existing line
                                                                if line != task_selection:
                                                                    the_tasks.write(line)
                                                                    the_tasks.write(marking_task)
                                                                    break
                                        # conditionals for 'yes' option
                                        elif task_marker == "no":
                                            # looping through the tasks 
                                            for count, checking_task in enumerate(read_file3, start=1):
                                                # splitting the sentences that have 'username'
                                                if task_selection == count:
                                                    # opening the file for writing
                                                    with open("tasks.txt", "w") as the_tasks:
                                                        # indexing the task selected
                                                        for exact_task in read_file3[task_selection-1:task_selection]:
                                                            # replacing the 'No' with 'Yes'
                                                            marking_task = exact_task.replace("Yes","No")
                                                            # looping through the line
                                                            for line in read_file3:
                                                                # writing and replace existing line
                                                                if line != task_selection:
                                                                    the_tasks.write(line)
                                                                    the_tasks.write(marking_task)
                                                                    break
                                            
                                elif task_selection == -1:
                                    break
                            

                    # exception message if there's no tasks
                    else:
                        ("No tasks available.")
                    break
    elif menu == "gr":


                # creating to 'task_overview.txt'
                with open("task_overview.txt", "w") as task_overview:
                # reading file
                    with open("tasks.txt", "r") as tasks_file:
                        # splitting text file lines into a list
                        read_file5 = tasks_file.readlines()

                        # total number of tasks
                        total_no_tasks = len((read_file5))
                    
                        # total number of completed tasks
                        completed_tasks = sum("Yes" in lines for lines in read_file5)

                        # total number of incompleted tasks
                        incomplete_tasks = sum("No" in lines for lines in read_file5)

                        # total number of tasks that are not complete and are overdue, percentage of tasks that are incomplete, percentage of overdue tasks
                        # total number of tasks that are incomplete and are overdue
                        the_current_date = datetime.now()
                        incomplete_and_overdue_tasks = 0
                        for line in read_file5:
                            line_search = line.split(",")
                            if ("No" in lines for lines in read_file5):
                                line_date = datetime.strptime(line_search[4], " %d %b %Y") 
                                if the_current_date > line_date:
                                    incomplete_and_overdue_tasks += 1

                        # percentage of tasks that are incomplete
                        incomplete_tasks2 = sum("No" in lines for lines in read_file5)
                        percentage_incomplete_tasks = int((incomplete_tasks2/len(read_file5))*100)
                        # percentage of overdue tasks
                        overdue_tasks = 0
                        for line in read_file5:
                            if the_current_date > line_date:
                                overdue_tasks += 1
                                percentage_overdue_tasks = int((overdue_tasks/len(read_file5))*100)
                        
                        # writing to 'task_overview.txt'
                        task_overview.write(f"TASK OVERVIEW REPORT\n\n")
                        task_overview.write(f"Total number of tasks: {total_no_tasks}\n")
                        task_overview.write(f"Total number of completed tasks: {completed_tasks}\n")
                        task_overview.write(f"Total number of incompleted tasks: {incomplete_tasks}\n")
                        task_overview.write(f"Total number of tasks that are incomplete and are overdue: {incomplete_and_overdue_tasks}\n")
                        task_overview.write(f"Percentage of tasks that are incomplete: {percentage_incomplete_tasks}%\n")
                        task_overview.write(f"Percentage of overdue tasks: {percentage_overdue_tasks}%")


                # creating to 'user_overview.txt'
                with open("user_overview.txt", "w") as user_overview:
                    
                    with open("tasks.txt", "r") as users_file:
                        read_file6 = users_file.readlines()

                        user_overview.write(f"\nUSER OVERVIEW REPORT\n\n")
                        # total number of users registered
                        registered_users = []
                        for liner in read_file6:
                            liner_search = liner.split(",")
                            if (liner_search[0::6] in word for word in liner):
                                registered_users += liner_search[0::6]
                        seen_users = []
                        for username in registered_users:
                            if username not in seen_users:
                                seen_users.append(username)
                        number_registered_users = len(seen_users)
                        user_overview.write(f"Total number of users registered: {number_registered_users}\n")

                        # total number of tasks registered
                        registered_tasks = []
                        for assigned_task in read_file6:
                            task_search = assigned_task.split(",")
                            if (task_search[1::6] in task for task in assigned_task):
                                registered_tasks += task_search[1::6]
                        seen_tasks = []
                        for the_tasks in registered_tasks:
                            if the_tasks not in seen_tasks:
                                seen_tasks.append(the_tasks)
                        number_registered_tasks = len(seen_tasks)
                        user_overview.write(f"total number of tasks registered: {number_registered_tasks}\n")



                        # user statistics
                        # number of tasks per user
                        user_overview.write(f"\nNumber of tasks per user:\n\n")
                        for user in seen_users:
                                user_tasks = [task for task in read_file6 if user in task]
                                user_tasks_total = len(user_tasks)
                                user_overview.write(f"{user}'s Tasks - {user_tasks_total}\n")
                    
                        # percentage of total number of tasks per user
                        user_overview.write(f"\nPercentage of total number of tasks per user:\n\n")
                        for user in seen_users:
                                user_tasks2 = [task for task in read_file6 if user in task]
                                user_tasks2_total = len(user_tasks2)
                                percentage_number_tasks = round((user_tasks2_total/len(read_file6))*100, 2)
                                user_overview.write(f"{user}'s Tasks: {percentage_number_tasks}%\n")

                        # percentage of total number of completed tasks per user
                        user_overview.write(f"\nPercentage of total number of completed tasks per user:\n\n")
                        for user in seen_users:
                                user_tasks2 = [task for task in read_file6 if user in task]
                                user_tasks_total2 = len(user_tasks2)
                                user_completed_tasks = [task for task in user_tasks2 if "Yes" in task]
                                total_user_completed_tasks = len(user_completed_tasks)
                                user_complete_percentage = (total_user_completed_tasks/user_tasks_total2)*100
                                user_overview.write(f"{user}: {user_complete_percentage}%\n")
                    
                        # percentage of total number of incompleted tasks per user
                        user_overview.write(f"\nPercentage of total number of incompleted tasks per user:\n\n")
                        for user in seen_users:
                                user_tasks3 = [task for task in read_file6 if user in task]
                                user_tasks_total3 = len(user_tasks3)
                                user_incompleted_tasks = [task for task in user_tasks3 if "No" in task]
                                total_user_incompleted_tasks = len(user_incompleted_tasks)
                                user_incomplete_percentage = (total_user_incompleted_tasks/user_tasks_total3)*100
                                user_overview.write(f"{user}: {user_incomplete_percentage}%\n")


                        # percentage of user's tasks that are incomplete and are overdue
                        user_overview.write(f"\nPercentage of user's tasks that are incomplete and are overdue:\n\n")
                        the_current_date = datetime.now()
                        for user in seen_users:
                                user_tasks4 = [task for task in read_file6 if user in task]
                                incompleted_user_tasks4 = [words for words in user_tasks4 if "No" in words]
                                for line in incompleted_user_tasks4:
                                    line_search = line.split(",")
                                    if ("No" in lines for lines in incompleted_user_tasks4):
                                        line_date = datetime.strptime(line_search[4], " %d %b %Y")
                                        if the_current_date > line_date:
                                            incomplete_overdue_tasks = []
                                            total_user_tasks4 = len(user_tasks4)
                                            incomplete_overdue_tasks.append(incompleted_user_tasks4)  
                                            total_incomplete_overdue_tasks = len(incomplete_overdue_tasks)
                                            percentage_incomplete_overdue_tasks = (total_incomplete_overdue_tasks/total_user_tasks4)*100

                                            user_overview.write(f"{user}: {percentage_incomplete_overdue_tasks}%\n")
                                            break
                                        # all the other users that have not appeared have 0 incomplete and overdue tasks

                    
                    
    elif menu == "s":
                    try:
                        with open("task_overview.txt", "r") as task_statitics:
                             the_task_statistics = task_statitics.read()
                             print(the_task_statistics)

                        with open("user_overview.txt", "r") as user_statitics:
                             the_user_statistics = user_statitics.read()
                             print(the_user_statistics)
                    
                    except:
                        # creating to 'task_overview.txt'
                        with open("task_overview.txt", "w") as task_overview:
                        # reading file
                            with open("tasks.txt", "r") as tasks_file:
                                # splitting text file lines into a list
                                read_file5 = tasks_file.readlines()

                                # total number of tasks
                                total_no_tasks = len((read_file5))
                    
                                # total number of completed tasks
                                completed_tasks = sum("Yes" in lines for lines in read_file5)

                                # total number of incompleted tasks
                                incomplete_tasks = sum("No" in lines for lines in read_file5)

                                # total number of tasks that are not complete and are overdue, percentage of tasks that are incomplete, percentage of overdue tasks
                                # total number of tasks that are incomplete and are overdue
                                the_current_date = datetime.now()
                                incomplete_and_overdue_tasks = 0
                                for line in read_file5:
                                    line_search = line.split(",")
                                    if ("No" in lines for lines in read_file5):
                                        line_date = datetime.strptime(line_search[4], " %d %b %Y")
                                        if the_current_date > line_date:
                                            incomplete_and_overdue_tasks += 1

                                # percentage of tasks that are incomplete
                                incomplete_tasks2 = sum("No" in lines for lines in read_file5)
                                percentage_incomplete_tasks = int((incomplete_tasks2/len(read_file5))*100)
                                # percentage of overdue tasks
                                overdue_tasks = 0
                                for line in read_file5:
                                    if the_current_date > line_date:
                                        overdue_tasks += 1
                                        percentage_overdue_tasks = int((overdue_tasks/len(read_file5))*100)
                        
                                # writing to 'task_overview.txt'
                                task_overview.write(f"TASK OVERVIEW REPORT\n\n")
                                task_overview.write(f"Total number of tasks: {total_no_tasks}\n")
                                task_overview.write(f"Total number of completed tasks: {completed_tasks}\n")
                                task_overview.write(f"Total number of incompleted tasks: {incomplete_tasks}\n")
                                task_overview.write(f"Total number of tasks that are incomplete and are overdue: {incomplete_and_overdue_tasks}\n")
                                task_overview.write(f"Percentage of tasks that are incomplete: {percentage_incomplete_tasks}%\n")
                                task_overview.write(f"Percentage of overdue tasks: {percentage_overdue_tasks}%")

                        # printing the 'tasks statistics'
                        with open("task_overview.txt", "r") as task_statitics:
                             the_task_statistics = task_statitics.read()
                             print(the_task_statistics)


                        # creating to 'user_overview.txt'
                        with open("user_overview.txt", "w") as user_overview:
                    
                            with open("tasks.txt", "r") as users_file:
                                read_file6 = users_file.readlines()

                                user_overview.write(f"\nUSER OVERVIEW REPORT\n\n")
                                # total number of users registered
                                registered_users = []
                                for liner in read_file6:
                                    liner_search = liner.split(",")
                                    if (liner_search[0::6] in word for word in liner):
                                        registered_users += liner_search[0::6]
                                seen_users = []
                                for username in registered_users:
                                    if username not in seen_users:
                                        seen_users.append(username)
                                number_registered_users = len(seen_users)
                                user_overview.write(f"Total number of users registered: {number_registered_users}\n")

                                # total number of tasks registered
                                registered_tasks = []
                                for assigned_task in read_file6:
                                    task_search = assigned_task.split(",")
                                    if (task_search[1::6] in task for task in assigned_task):
                                        registered_tasks += task_search[1::6]
                                seen_tasks = []
                                for the_tasks in registered_tasks:
                                    if the_tasks not in seen_tasks:
                                        seen_tasks.append(the_tasks)
                                number_registered_tasks = len(seen_tasks)
                                user_overview.write(f"total number of tasks registered: {number_registered_tasks}\n")



                                # user statistics
                                # number of tasks per user
                                user_overview.write(f"\nNumber of tasks per user:\n\n")
                                for user in seen_users:
                                        user_tasks = [task for task in read_file6 if user in task]
                                        user_tasks_total = len(user_tasks)
                                        user_overview.write(f"{user}'s Tasks - {user_tasks_total}\n")
                    
                                # percentage of total number of tasks per user
                                user_overview.write(f"\nPercentage of total number of tasks per user:\n\n")
                                for user in seen_users:
                                        user_tasks2 = [task for task in read_file6 if user in task]
                                        user_tasks2_total = len(user_tasks2)
                                        percentage_number_tasks = round((user_tasks2_total/len(read_file6))*100, 2)
                                        user_overview.write(f"{user}'s Tasks: {percentage_number_tasks}%\n")

                                # percentage of total number of completed tasks per user
                                user_overview.write(f"\nPercentage of total number of completed tasks per user:\n\n")
                                for user in seen_users:
                                        user_tasks2 = [task for task in read_file6 if user in task]
                                        user_tasks_total2 = len(user_tasks2)
                                        user_completed_tasks = [task for task in user_tasks2 if "Yes" in task]
                                        total_user_completed_tasks = len(user_completed_tasks)
                                        user_complete_percentage = (total_user_completed_tasks/user_tasks_total2)*100
                                        user_overview.write(f"{user}: {user_complete_percentage}%\n")
                    
                                # percentage of total number of incompleted tasks per user
                                user_overview.write(f"\nPercentage of total number of incompleted tasks per user:\n\n")
                                for user in seen_users:
                                        user_tasks3 = [task for task in read_file6 if user in task]
                                        user_tasks_total3 = len(user_tasks3)
                                        user_incompleted_tasks = [task for task in user_tasks3 if "No" in task]
                                        total_user_incompleted_tasks = len(user_incompleted_tasks)
                                        user_incomplete_percentage = (total_user_incompleted_tasks/user_tasks_total3)*100
                                        user_overview.write(f"{user}: {user_incomplete_percentage}%\n")


                                # percentage of user's tasks that are incomplete and are overdue
                                user_overview.write(f"\nPercentage of user's tasks that are incomplete and are overdue:\n\n")
                                the_current_date = datetime.now()
                                for user in seen_users:
                                        user_tasks4 = [task for task in read_file6 if user in task]
                                        incompleted_user_tasks4 = [words for words in user_tasks4 if "No" in words]
                                        for line in incompleted_user_tasks4:
                                            line_search = line.split(",")
                                            if ("No" in lines for lines in incompleted_user_tasks4):
                                                line_date = datetime.strptime(line_search[4], " %d %b %Y")
                                                if the_current_date > line_date:
                                                    incomplete_overdue_tasks = []
                                                    total_user_tasks4 = len(user_tasks4)
                                                    incomplete_overdue_tasks.append(incompleted_user_tasks4)  
                                                    total_incomplete_overdue_tasks = len(incomplete_overdue_tasks)
                                                    percentage_incomplete_overdue_tasks = (total_incomplete_overdue_tasks/total_user_tasks4)*100

                                                    user_overview.write(f"{user}: {percentage_incomplete_overdue_tasks}%\n")
                                                    break
                                                # all the other users that have not appeared have 0 incomplete and overdue tasks

                        with open("user_overview.txt", "r") as user_statitics:
                             the_user_statistics = user_statitics.read()
                             print(the_user_statistics)
                         
                
        


    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made entered an invalid input. Please try again")