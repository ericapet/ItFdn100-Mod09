# ---------------------------------------------------------- #
# Title: IOClasses
# Description: A module of IO classes
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created starter script
# Erica Peterson, 9.6.22, edited grammatical and syntax errors
# ---------------------------------------------------------- #
if __name__ == "__main__":
    raise Exception("This file is not meant to be ran by itself")
else:
    import DataClasses as DC

class EmployeeIO:
    """  A class for performing Employee Input and Output

    methods:
        print_menu_items():

        print_current_list_items(list_of_rows):

        input_employee_data():

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class:
    """
    @staticmethod
    def print_menu_items():
        """ Print a menu of choices to the user  """
        try:
            print('''
            Menu of Options
            1) Show current employee data
            2) Add new employee data
            3) Save employee data to file
            4) Exit program
            ''')
            print()  # Add an extra line for looks
        except Exception as e:
            print(e)

    @staticmethod
    def input_menu_options():
        """ Gets the menu choice from a user

        :return: string
        """
        try:
            choice = str(input("Which option would you like to perform? [1 to 4]: ")).strip()
            print()  # Add an extra line for looks
        except Exception as e:
            print(e)
        return choice

    @staticmethod
    def print_current_list_items(list_of_rows: list):
        """ Print the current items in the list of Employee rows

        :param list_of_rows: (list) of rows you want to display
        """
        try:
            print("******* The current employees are: *******")
            print("Employee ID, First Name, Last Name")
            for row in list_of_rows:
                print(str(row))
            print("*******************************************")
            print()  # Add an extra line for looks
        except Exception as e:
            print(e)
    @staticmethod
    def input_employee_data():
        """ Gets data for an employee object

        :return: employee (object) with input data
        """
        try:
            employee_id = input("What is the employee's ID number? ").strip()
            first_name = str(input("What is the employee's First Name? ").strip())
            last_name = str(input("What is the employee's Last Name? ").strip())
            print()  # Add an extra line for looks
            emp = DC.Employee(employee_id, first_name, last_name)
        except Exception as e:
            print(e)
        return emp

