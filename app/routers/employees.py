from fastapi import APIRouter, HTTPException
from app.models import EmployeeBase, EmployeeUpdate, EmployeeCreate
from app.database import *

router = APIRouter()
db = Database()
db.init_sample_data()


@router.get('/employees/')
def get_employees():
    employees = db.get_all_employees()
    return [employee.to_dict() for employee in employees]


@router.get('/employees/{id}')
def get_employee(id: int):
    employee = db.get_employee_by_id(id)
    if employee is None:
        raise HTTPException(status_code=400, detail='employee not found')
    return employee.model_dump()


@router.post('/employees/')
def insert_employee(employee: EmployeeCreate):
    result = db.add_employee(employee)
    if result is None:
        raise HTTPException(status_code=500, detail="Failed to create contact")
    return {
        "message": "Contact created successfully",
        "id": result.id
    }


@router.put('/employees/{id}')
def update_employee(id: int, data: EmployeeUpdate):
    update_data = data.model_dump(exclude_unset=True)

    if not update_data:
        raise HTTPException(status_code=400, detail="No fields provided for update")

    result = db.update_employee(id, **update_data)

    if not result:
        raise HTTPException(status_code=404, detail="Employee not found or no changes made")

    return {"message": "Employee updated successfully", "updated_fields": list(update_data.keys())}


@router.delete('/employees/{id}')
def remove_employee(id: int):
    result = db.delete_employee(id)
    if not result:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"message": "Employee removed successfully"}
