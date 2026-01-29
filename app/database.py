
employees = [
    
]

class Database:
    def __init__(self):
        self.employees = employees
        
    def add_employee(self, employee) -> EmployeeBase:
        self.employees.append(employee)
        return employee
    
    def get_all_employees(self):
        return self.employees
    
    def get_employee_by_id(emp_id) -> :
        for emp in employees:
            if emp['emp_id']:
                return emp
        return None