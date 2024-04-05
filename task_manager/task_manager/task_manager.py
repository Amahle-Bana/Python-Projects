########### IMPORT LIBRARIES ##############
from datetime import datetime
import re

################### LOGIN SECTION #################

# GETTING USERNAME
username = str(input("Enter Your Username: ")).lower()
# READING AND LOOPING THROUGH 'user.txt' FOR USERNAME
with open("task_manager/user.txt", "r+") as username_file:
    # READING FILE LINES
    read_file1 = username_file.readlines()
    while read_file1:
        # LOOPING THROUGH THE FILE LINES AND INDEXING THE USERNAMES
        for word in read_file1:
            new_file = word.replace(",","")
            the_usernames = new_file.split()
            # USERNAME CONFIRMATION 
            if username == the_usernames[0]:
                break
        # USERNAME ERROR MESSAGE AND REPEATED INPUT
        if username != the_usernames[0]:
            print("You have entered the wrong username, please try again.")
            username = str(input("Enter Your Username: ")).lower()
        else:
            pass
        # USERNAME CONFIRMATION LOOP BREAK
        if username == the_usernames[0]:
            break



# GETTING PASSWORD
password = input("Enter Your Password: ").lower()
# STORING THE ENTERED DETAILS
details = f"{username}, {password}"
with open('task_manager/user.txt') as f:
    # READ THE FILE LINES AND LISTING THEM
    read_f = f.readlines()
    # RUNNING A WHILE LOOP
    while read_f:
        # LOOPING THROUGH THE LINES
        for line in read_f:
            new_file2 = line.replace("\n","")
        # USERNAME AND PASSWORD CONFIRMATION
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
    # PRESENTING MENU TO THE USER
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

            """This method is used to register users
            
                :param username: the username entered at the beginning
                :type username: str
                ...
                :return: writes a new username and password to the 'user.text'
                :rtype: str
            
            """

            if username == "admin":
            # WRITING 'user.text' FILE FOR REGISTERED USER
                with open("task_manager/user.txt", "r+") as register:
                    # NEW USERNAME INPUT
                    new_username = str(input("Enter Username: ")).lower()
                    # READING THE LINES OF THE FILE
                    read_register = register.readlines()
                    # LOOPING THROUGH EACH LINE ON THE FILE
                    for line in read_register:
                        # SPLITTING THE LISTS
                        split_register = line.split(",")
                        # INDEXING THE USERNAMES
                        the_username = split_register[0:1:2]
                        # LOOPING THE USERNAMES
                        for word in the_username:
                            # VALIDATING IF 'new username' EXISTS
                            existing_username = word
                            if new_username == existing_username:
                                print("Username Already Exists")
                            else:
                                pass
        
                        if new_username != existing_username:
                            pass
                        # VALIDATING IF 'new username' EXISTS
                        while new_username == existing_username:
                            print("Try Entering Another Username.")
                            new_username = str(input("Enter Username: ")).lower()
                            if new_username != existing_username:
                                break
                            else:
                                continue
                        else:
                            pass
                    # NEW PASSWORD INPUT
                    new_password = input("Enter Password: ").lower()
                    # PASSWORD CONFIRMATION
                    confirm_password = input("Confirm Password: ").lower()
                    while new_password != confirm_password:
                        confirm_password = input("Confirm Password: ").lower()
                    else:
                        # WRITING USER DETAILS INTO 'user.txt' FILE
                        register.write(f"\n{new_username}, {confirm_password}") 
            else:
                # ALERTING 'admin' PERMISSION
                print("Only Admin can register users\n")
        reg_user(username)




    elif menu == 'a':
        def add_task():

            """This method helps add a new task to 'tasks.txt'
            
            :return: writes a new tasks to 'tasks.txt'
            :rtype: str
            """

            # USERNAME INPUT
            task_username = str(input("Enter Username: ")).lower()
            # TITLE INPUT
            title = str(input("Enter Title: "))
            # DESCRIPTION INPUT
            description = str(input("Enter Description: "))
            # DUE DATE INPUT
            print("Please enter the due date in the the format stated (eg. 23 Oct 2023):")
            day = int(input("Day (eg. 23): "))
            month = (input("Month (eg. Oct): "))
            year = int(input("Year (eg. 2023): "))
            # CURRENT DATE REGISTRATION
            now = datetime.now()
            current_date = now.strftime("%d %b %Y")
            # TASK COMPLETION CHECKER
            task_completion = "No"
            # APPENDING THE ADDED TASK INTO THE 'tasks.txt' FILE
            with open("tasks.txt", "a+") as tasks:
                # WRITING THE DETAILS INTO 'tasks.txt' FILE
                tasks.write(f"\n{task_username}, {title}, {description}, {day} {month} {year}, {current_date}, {task_completion}")
        add_task()




    elif menu == 'va':
        def view_all():

            """this method reads and prints out the tasks in a specific format

            :return: prints out the tasks
            :rtype: str
            """
            # READING THE TASKS FROM 'tasks.txt' FILE
            with open("task_manager/tasks.txt", "r") as view_tasks:
                read_tasks = view_tasks.readlines()
                # LOOPING THROUGH THE TASKS REGISTERED
                for screening_all_tasks in read_tasks:
                    all_tasks = screening_all_tasks.split(",")
                    # PRINTING OUT 'output 2' FORMAT
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
        def view_my_tasks():

            """this method helps the user view their tasks

            :return: returns the users tasks
            :rtype: str
            """

            # READING FILE FOR USE
            with open("task_manager/tasks.txt", "r+") as my_tasks:

                # READING LINES AND CONVERTING THEM INTO A LIST
                read_file3 = my_tasks.readlines()
                # LOOPING THROUGH THE LIST FOR EACH ITEM
                for screening_task in read_file3:
                        # SPLITTING THE ITEM ON ITS COMMAS
                        screening = screening_task.split(",")
                        # INDEXING THE USERNAME
                        registered_username = screening[0]
                        # 'username' CONFIRMATION
                        if username == registered_username:
                                # SEARCHING THROUGH THE SENTENCES TO FIND 'username'
                                word_search = [ x for x in read_file3 if username in x]
                                # LOOPING THORUGH THE SENTENCES THAT THE 'username' IS IN
                                for count, real_task in enumerate(word_search, start=1):
                                        # SPLITTING THE SENTECES THAT HAVE 'username'
                                        screening_search = real_task.split(",")
                                        # PRINTING USING 'output 2' FORMAT
                                        print("___________________________________________\n")
                                        print(f"Task No.: {count}")
                                        print(f"Task:\t\t\t{screening_search[1]}")
                                        print(f"Assigned to: \t\t {screening_search[0]}")
                                        print(f"Date Assigned:\t\t{screening_search[3]}")
                                        print(f"Due Date:\t\t{screening_search[4]}")
                                        print(f"Task Complete?\t\t{screening_search[5]}")
                                        print(f"Task Description:\n {screening_search[2]}\n")
                                        print("___________________________________________\n")
                                # ASKING FOR TASK INPUT
                                task_selection = int(input("Select A Task: Type the number of your task, Type '-1' to return to main menu.\n"))
                                # VALIDATING TASK NUMBER 
                                for entry in range (1,len(read_file3)+1):
                                    # VALIDATING IF TASK NUMBER IS EQUAL TO RANGE
                                    if task_selection == entry:
                                        # GET TASK CHOICE
                                        task_choice = int(input("Edit Task(1) or Mark Task(2): "))
                                        if task_choice == 1:
                                            # LOOPING THROUGH THE TASKS
                                            for count, task_editor in enumerate(read_file3, start=1):
                                                # VALIDATING TASK SELECTION
                                                if task_selection == count:
                                                    # READING 'tasks.txt' FILE
                                                    with open("tasks.txt", "r") as task_editors:
                                                        # READING 'tasks.txt' LINES
                                                        read_file4 = task_editors.readlines()
                                                        # INDEXING STRING OF TASK SELECTED
                                                        for target_string in read_file4[task_selection-1:task_selection]:
                                                            # CHECKING IF TASK IS NOT COMPLETE
                                                            task_complete_marker = r"No"
                                                            # VALIDATING IF TASK IS UNCOMPLETED 
                                                            match = re.search(task_complete_marker, target_string)
                                                            # CONDITIONALS FOR UNCOMPLETED TASK
                                                            if match != None: 
                                                                # GETTING INPUT FOR TASK EDITING OPTIONS
                                                                changer = int(input("Change Person Responsible For Task(1) or Change Due Date(2):\n"))
                                                                if changer == 1:
                                                                    # GETTING NEW NAME FOR TASKS
                                                                    new_person = input("Enter A New Name: ")
                                                                    # OPENING THE FILE FOR WRITING
                                                                    with open("tasks.txt", "w") as the_tasks:
                                                                            # REPLACING THE 'No' WITH 'Yes'
                                                                            responsible_person = target_string.replace(screening_search[0],new_person)
                                                                            # LOOPING THROUGH THE LINE
                                                                            for sentence in read_file4:
                                                                                # WRITING AND REPLACE EXISTING LINE
                                                                                if line != task_selection:
                                                                                    the_tasks.write(sentence)
                                                                                    the_tasks.write(responsible_person)
                                                                                    break
                                                                elif changer == 2:
                                                                    # GETTING NEW DUE DATE INPUT
                                                                    print("Enter New Due Date:")
                                                                    day = int(input("Day (eg. 23): "))
                                                                    month = (input("Month (eg. Oct): "))
                                                                    year = int(input("Year (eg. 2023): "))
                                                                    # OPENING THE FILE FOR WRITING
                                                                    with open("tasks.txt", "w") as the_tasks:
                                                                            # REPLACING THE 'No' WITH 'Yes'
                                                                            new_due_date = target_string.replace(screening_search[4],f" {day} {month} {year}")
                                                                            # LOOPING THROUGH THE LINE
                                                                            for sentence in read_file4:
                                                                                # WRITING AND REPLACE EXISTING LINE
                                                                                if line != task_selection:
                                                                                    the_tasks.write(sentence)
                                                                                    the_tasks.write(new_due_date)
                                                                                    break

                                                            else:
                                                                print("Match Not found")                                                    

                                        elif task_choice == 2:
                                            # GETTING USER TO MARK TASK
                                            task_marker = input("Mark Task as complete(Yes/No): ").lower()
                                            # CONDITIONALS FOR 'YES'
                                            if task_marker == "yes":
                                                # LOOPING THROUGH THE TASKS 
                                                for count, checking_task in enumerate(read_file3, start=1):
                                                    # mMATCHING TASK SELECTION WITH TASK NUMBER 
                                                    if task_selection == count:
                                                        # OPENING THE FILE FOR WRITING
                                                        with open("tasks.txt", "w") as the_tasks:
                                                            # INDEXING THE TASK SELECTED
                                                            for exact_task in read_file3[task_selection-1:task_selection]:
                                                                # REPLACING THE 'No' WITH 'Yes'
                                                                marking_task = exact_task.replace("No","Yes")
                                                                # LOOPING THROUGH THE LINE
                                                                for line in read_file3:
                                                                    # WRITING THE REPLACE EXISTING LINE
                                                                    if line != task_selection:
                                                                        the_tasks.write(line)
                                                                        the_tasks.write(marking_task)
                                                                        break
                                            # CONDITIONALS FOR 'yes' OPTION
                                            elif task_marker == "no":
                                                # LOOPING THROUGH THE TASKS  
                                                for count, checking_task in enumerate(read_file3, start=1):
                                                    # SPLITTING THE SENTENCES THAT HAVE 'username'
                                                    if task_selection == count:
                                                        # OPENING THE FILE FOR WRITING
                                                        with open("tasks.txt", "w") as the_tasks:
                                                            # INDEXING THE TASK SELECTED
                                                            for exact_task in read_file3[task_selection-1:task_selection]:
                                                                # REPLACING THE 'No' WITH 'Yes'
                                                                marking_task = exact_task.replace("Yes","No")
                                                                # LOOPING THROUGH THE LINE
                                                                for line in read_file3:
                                                                    # WRITING AND REPLACING EXISTING LINE                                                                if line != task_selection:
                                                                        the_tasks.write(line)
                                                                        the_tasks.write(marking_task)
                                                                        break
                                                
                                    elif task_selection == -1:
                                        break
                                

                        # EXCEPTION HANDLING IF THERES NO TASKS
                        else:
                            ("No tasks available.")
                        break
        view_my_tasks()




    elif menu == "gr":
            def reports_generator():
            
                """this method helps generate reports on 'task_overview.txt'

                :return: this method prints out the report on tasks
                :rtype: str    
                """

                # CREATING THE 'task_overview.txt' FILE
                with open("task_manager/task_overview.txt", "w") as task_overview:
                # READING THE 'tasks.txt' FILE
                    with open("task_manager/tasks.txt", "r") as tasks_file:
                        # SPLITTING 'tasks.txt' LINES INTO A LIST
                        read_file5 = tasks_file.readlines()

                        # TOTAL NUMBER OF TASKS
                        total_no_tasks = len((read_file5))
                    
                        # TOTAL NUMBER OF COMPLETED TASKS
                        completed_tasks = sum("Yes" in lines for lines in read_file5)

                        # TOTAL NUMBER OF INCOMPLETED TASKS
                        incomplete_tasks = sum("No" in lines for lines in read_file5)

                        # TOTAL NUMBER OF TASKS THAT ARE INCOMPLETE AND ARE OVERDUE
                        the_current_date = datetime.now()
                        incomplete_and_overdue_tasks = 0
                        for line in read_file5:
                            line_search = line.split(",")
                            if ("No" in lines for lines in read_file5):
                                line_date = datetime.strptime(line_search[4], " %d %b %Y") 
                                if the_current_date > line_date:
                                    incomplete_and_overdue_tasks += 1

                        # PERCENTAGE OF TASKS THAT ARE COMPLETE
                        incomplete_tasks2 = sum("No" in lines for lines in read_file5)
                        percentage_incomplete_tasks = int((incomplete_tasks2/len(read_file5))*100)
                        # PERCENTAGE OF OVERDUE TASKS
                        overdue_tasks = 0
                        for line in read_file5:
                            if the_current_date > line_date:
                                overdue_tasks += 1
                                percentage_overdue_tasks = int((overdue_tasks/len(read_file5))*100)
                        
                        # WRITING TO 'task_overview.txt'
                        task_overview.write(f"TASK OVERVIEW REPORT\n\n")
                        task_overview.write(f"Total number of tasks: {total_no_tasks}\n")
                        task_overview.write(f"Total number of completed tasks: {completed_tasks}\n")
                        task_overview.write(f"Total number of incompleted tasks: {incomplete_tasks}\n")
                        task_overview.write(f"Total number of tasks that are incomplete and are overdue: {incomplete_and_overdue_tasks}\n")
                        task_overview.write(f"Percentage of tasks that are incomplete: {percentage_incomplete_tasks}%\n")
                        task_overview.write(f"Percentage of overdue tasks: {percentage_overdue_tasks}%")


                # WRITING TO 'user_overview.txt'
                with open("task_manager/user_overview.txt", "w") as user_overview:
                    
                    with open("task_manager/tasks.txt", "r") as users_file:
                        read_file6 = users_file.readlines()

                        user_overview.write(f"\nUSER OVERVIEW REPORT\n\n")
                        # TOTAL NUMBER OF USER REGISTERED
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

                        # TOTAL NUMBER OF TASKS REGISTERED
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



                        # USER STATISTICS
                        # NUMBER OF TASKS PER USER
                        user_overview.write(f"\nNumber of tasks per user:\n\n")
                        for user in seen_users:
                                user_tasks = [task for task in read_file6 if user in task]
                                user_tasks_total = len(user_tasks)
                                user_overview.write(f"{user}'s Tasks - {user_tasks_total}\n")
                    
                        # PERCENTAGE OF TOTAL NUMBER OF TASKS PER USER
                        user_overview.write(f"\nPercentage of total number of tasks per user:\n\n")
                        for user in seen_users:
                                user_tasks2 = [task for task in read_file6 if user in task]
                                user_tasks2_total = len(user_tasks2)
                                percentage_number_tasks = round((user_tasks2_total/len(read_file6))*100, 2)
                                user_overview.write(f"{user}'s Tasks: {percentage_number_tasks}%\n")

                        # PERCENTAGE OF TOTAL NUMBER OF COMPLETED TASKS PER USER
                        user_overview.write(f"\nPercentage of total number of completed tasks per user:\n\n")
                        for user in seen_users:
                                user_tasks2 = [task for task in read_file6 if user in task]
                                user_tasks_total2 = len(user_tasks2)
                                user_completed_tasks = [task for task in user_tasks2 if "Yes" in task]
                                total_user_completed_tasks = len(user_completed_tasks)
                                user_complete_percentage = (total_user_completed_tasks/user_tasks_total2)*100
                                user_overview.write(f"{user}: {user_complete_percentage}%\n")
                    
                        # PERCENTAGE OF TOTAL NUMBER OF COMPLETED TASKS PER USER
                        user_overview.write(f"\nPercentage of total number of incompleted tasks per user:\n\n")
                        for user in seen_users:
                                user_tasks3 = [task for task in read_file6 if user in task]
                                user_tasks_total3 = len(user_tasks3)
                                user_incompleted_tasks = [task for task in user_tasks3 if "No" in task]
                                total_user_incompleted_tasks = len(user_incompleted_tasks)
                                user_incomplete_percentage = (total_user_incompleted_tasks/user_tasks_total3)*100
                                user_overview.write(f"{user}: {user_incomplete_percentage}%\n")


                        # PERCENTAGE OF USER'S TASKS THAT ARE INCOMPLETE AND ARE OVERDUE
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
            reports_generator()
                    
                    
    elif menu == "s":
                def statistics():

                    """This method helps generate statistics

                    :return: prints out statistics of both tasks and users
                    :rtype: str    
                    """

                    try:
                        with open("task_manager/task_overview.txt", "r") as task_statitics:
                             the_task_statistics = task_statitics.read()
                             print(the_task_statistics)

                        with open("task_manager/user_overview.txt", "r") as user_statitics:
                             the_user_statistics = user_statitics.read()
                             print(the_user_statistics)
                    
                    except:
                        # WRITING TO 'task_overview.txt'
                        with open("task_manager/task_overview.txt", "w") as task_overview:
                        # READING FILE
                            with open("task_manager/tasks.txt", "r") as tasks_file:
                                # SPLITTING THE FILE LINES INTO A LIST
                                read_file5 = tasks_file.readlines()

                                # TOTAL NUMBER OF TASKS
                                total_no_tasks = len((read_file5))
                    
                                # TOTAL NUMBER OF COMPLETED TASKS
                                completed_tasks = sum("Yes" in lines for lines in read_file5)

                                # TOTAL NUMBER OF INCOMPETED TASKS
                                incomplete_tasks = sum("No" in lines for lines in read_file5)

                                # TOTAL NUMBER OF USER'S TASKS THAT ARE INCOMPLETE AND ARE OVERDUE
                                the_current_date = datetime.now()
                                incomplete_and_overdue_tasks = 0
                                for line in read_file5:
                                    line_search = line.split(",")
                                    if ("No" in lines for lines in read_file5):
                                        line_date = datetime.strptime(line_search[4], " %d %b %Y")
                                        if the_current_date > line_date:
                                            incomplete_and_overdue_tasks += 1

                                # PERCENTAGE OF TASKS that THAT ARE COMPLETE
                                incomplete_tasks2 = sum("No" in lines for lines in read_file5)
                                percentage_incomplete_tasks = int((incomplete_tasks2/len(read_file5))*100)
                                # PERCENTAGE OF OVERDUE TASKS
                                overdue_tasks = 0
                                for line in read_file5:
                                    if the_current_date > line_date:
                                        overdue_tasks += 1
                                        percentage_overdue_tasks = int((overdue_tasks/len(read_file5))*100)
                        
                                # WRITING TO 'task_overview.txt'
                                task_overview.write(f"TASK OVERVIEW REPORT\n\n")
                                task_overview.write(f"Total number of tasks: {total_no_tasks}\n")
                                task_overview.write(f"Total number of completed tasks: {completed_tasks}\n")
                                task_overview.write(f"Total number of incompleted tasks: {incomplete_tasks}\n")
                                task_overview.write(f"Total number of tasks that are incomplete and are overdue: {incomplete_and_overdue_tasks}\n")
                                task_overview.write(f"Percentage of tasks that are incomplete: {percentage_incomplete_tasks}%\n")
                                task_overview.write(f"Percentage of overdue tasks: {percentage_overdue_tasks}%")

                        # PRINTING THE 'tasks.txt statistics'
                        with open("task_manager/task_overview.txt", "r") as task_statitics:
                             the_task_statistics = task_statitics.read()
                             print(the_task_statistics)


                        # WRITING TO 'user_overview.txt'
                        with open("task_manager/user_overview.txt", "w") as user_overview:
                    
                            with open("task_manager/tasks.txt", "r") as users_file:
                                read_file6 = users_file.readlines()

                                user_overview.write(f"\nUSER OVERVIEW REPORT\n\n")
                                # TOTAL NUMBER OF USERS REGISTERED
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

                                # TOTAL NUMBER OF TASKS REGISTERED
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
                                # NUMBER OF TASKS PER USER
                                user_overview.write(f"\nNumber of tasks per user:\n\n")
                                for user in seen_users:
                                        user_tasks = [task for task in read_file6 if user in task]
                                        user_tasks_total = len(user_tasks)
                                        user_overview.write(f"{user}'s Tasks - {user_tasks_total}\n")
                    
                                # PERCENTAGE OF THE NUMBER OF TASKS PER USER
                                user_overview.write(f"\nPercentage of total number of tasks per user:\n\n")
                                for user in seen_users:
                                        user_tasks2 = [task for task in read_file6 if user in task]
                                        user_tasks2_total = len(user_tasks2)
                                        percentage_number_tasks = round((user_tasks2_total/len(read_file6))*100, 2)
                                        user_overview.write(f"{user}'s Tasks: {percentage_number_tasks}%\n")

                                # PERCENTAGE OF THE NUMBER OF COMPLETED TASKS PER USER
                                user_overview.write(f"\nPercentage of total number of completed tasks per user:\n\n")
                                for user in seen_users:
                                        user_tasks2 = [task for task in read_file6 if user in task]
                                        user_tasks_total2 = len(user_tasks2)
                                        user_completed_tasks = [task for task in user_tasks2 if "Yes" in task]
                                        total_user_completed_tasks = len(user_completed_tasks)
                                        user_complete_percentage = (total_user_completed_tasks/user_tasks_total2)*100
                                        user_overview.write(f"{user}: {user_complete_percentage}%\n")
                    
                                # PERCENTAGE OF USER'S NUMBER OF INCOMPLETED TASKS PER USER
                                user_overview.write(f"\nPercentage of total number of incompleted tasks per user:\n\n")
                                for user in seen_users:
                                        user_tasks3 = [task for task in read_file6 if user in task]
                                        user_tasks_total3 = len(user_tasks3)
                                        user_incompleted_tasks = [task for task in user_tasks3 if "No" in task]
                                        total_user_incompleted_tasks = len(user_incompleted_tasks)
                                        user_incomplete_percentage = (total_user_incompleted_tasks/user_tasks_total3)*100
                                        user_overview.write(f"{user}: {user_incomplete_percentage}%\n")


                                # PERCENTAGE OF USER'S NUMBER OF INCOMPLETED AND OVERDUE TASKS
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

                        with open("task_manager/user_overview.txt", "r") as user_statitics:
                             the_user_statistics = user_statitics.read()
                             print(the_user_statistics)
                statistics()         
                
        


    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made entered an invalid input. Please try again")