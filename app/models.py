
def get_employee_statistics() -> dict:
    total_employees = len(emplyees)
    by_office = {}
    by_job_title = {}

    for emp in employees:
        full_name = f"{emp['first_name']} {emp['last_name']}"
        office = emp["office_name"]
        job = emp["job_title"]

        if office not in by_office:
            by_office[office] = [full_name]
        else:
            by_office[office].append(full_name)

        if job not in by_job_title:
            by_job_title[job] = [full_name]
        else:
            by_job_title[job].append(full_name)


    return {"total_employees":total_employees,"by_office":by_office.values(),"by_job_title":by_job_title.values()}

def get_mission_statistics() -> dict:
    total_missions = len(missions)
    by_status = {}
    by_priority = {}

    for miss in missions:
        status = miss["status"]
        priority = miss["priority"]

        if status not in by_status:
            by_status[status] = [miss["title"]]
        else:
            by_status[status].append(miss["title"])

        if priority not in by_priority:
            by_priority[priority] = [miss["title"]]
        else:
            by_priority[priority].append(miss["title"])

    return {
        "total_missions": total_missions,
        "by_status": by_status.values(),
        "by_priority": by_priority.values()
    }

def get_employee_workload(employees, missions) -> list[dict]:
    """
    Returns a list of dicts for each employee with:
    - employee_id
    - total_missions
    - active_missions (Pending + In Progress)
    - completed_missions (Completed)
    """
    workload = []

    for emp in employees:
        emp_id = emp["id"]
        total = 0
        active = 0
        completed = 0

        for miss in missions:
            if miss["assigned_to"] == emp_id:
                total += 1
                if miss["status"] in ("Pending", "In Progress"):
                    active += 1
                elif miss["status"] == "Completed":
                    completed += 1

        workload.append({
            "employee_id": emp_id,
            "total_missions": total,
            "active_missions": active,
            "completed_missions": completed
        })

    return workload
  
from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class EmployeeBase(BaseModel):
    first_name: str
    last_name: str
    office_name: str
    job_title: str


class EmployeeCreate(EmployeeBase):
    id: str


class EmployeeUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    office_name: Optional[str] = None
    job_title: Optional[str] = None



class EmployeeResponse(EmployeeBase):
    id: str
    created_at: datetime
    updated_at: datetime
