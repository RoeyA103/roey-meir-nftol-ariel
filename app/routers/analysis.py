from fastapi import APIRouter
from typing import List, Dict
from models import *
router = APIRouter()

# Endpoint 1: Employee statistics
@router.get("/stats/employees", response_model=Dict)
def employee_statistics():
    return get_employee_statistics()

# Endpoint 2: Mission statistics
@router.get("/stats/missions", response_model=Dict)
def mission_statistics():
    return get_mission_statistics()

# Endpoint 3: Employee workload
@router.get("/stats/workload", response_model=List[Dict])
def employee_workload():
    return get_employee_workload(employees, missions)
