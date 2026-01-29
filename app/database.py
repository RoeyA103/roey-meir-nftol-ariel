from models import *

employees = [

]


class Database:
    def __init__(self):
        self.employees = employees

    def add_employee(self, employee) -> EmployeeBase:
        self.employees.append(employee)
        return employee

    def get_all_employees(self) -> list[EmployeeResponse]:
        response = []
        response.extend(EmployeeResponse(emp) for emp in employees)

        return response

    def get_employee_by_id(emp_id) -> EmployeeResponse | None:
        for emp in employees:
            if emp['emp_id']:
                return EmployeeResponse(emp)
        return None

    def update_employee(self, id: str, employee: EmployeeUpdate) -> EmployeeUpdate:
        for emp in self.employees:
            pass

    def delete_employee(self, emp_id: str) -> bool:
        for emp in self.employees:
            if emp.id == emp_id:
                self.employees.remove(emp)
                return True
        return False


