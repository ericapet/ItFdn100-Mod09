# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created starter script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# Erica Peterson, 9.7.22, added code to complete script
# ------------------------------------------------------------------------ #

if __name__ == "__main__":
    from DataClasses import Employee as Emp
    from ProcessingClasses import FileProcessor as FP
    from IOClasses import EmployeeIO as IO
else:
    raise Exception("This file was not created to be imported")

str_filename = "EmployeeData.txt"
obj_filehandle = None
lst_employeedata = []

# Main Body of Script  ---------------------------------------------------- #

# Load data from file into a list of employee objects when script starts
FP.create_file(file=obj_filehandle, file_name=str_filename)
lst_employeedata = FP.read_data_from_file(file_name=str_filename)

# Show user menu
try:
    while(True):
        IO.print_menu_items()

        # Get user's menu option choice
        strchoice = IO.input_menu_options()

        # Show user current data in the list of employee objects
        if strchoice.strip() == '1':
            IO.print_current_list_items(list_of_rows=lst_employeedata)
            continue  # return to the menu

        # Let user add data to the list of employee objects
        elif strchoice == '2':
            obj_employee = IO.input_employee_data()
            lst_employeedata.append(obj_employee)
            continue  # return to the menu

        # Let user save current data to file
        elif strchoice == '3':
            FP.save_data_to_file(file_name=str_filename, list_of_objects=lst_employeedata)
            print("Data Saved to EmployeeData.txt file!")
            continue  # return to the menu

        # Let user exit program
        elif strchoice == '4':
            print("Program exiting!")
            input() #for command prompt to not close immediately
            break  # exit loop


        else:
            print("Please enter a number between 1 and 4") # error if wrong number inputted
            continue

except Exception as e:
    print(e)
