import sys;

# Defining Functions

employeeNames = ["Mayank", "Anshul", "Meha"]

def show_employee_list(emp_list):
    for employee in emp_list:
        print(employee)

if __name__ == '__main__':
    show_employee_list(employeeNames)
    print(sys.argv[1])


