from models import MissionCreate, MissionResponse


class Database:
    employees: list = []
    missions: list = []

    def add_mission(self,mission:MissionCreate)-> MissionCreate:
        self.missions.append(mission)
        return mission
    def get_all_missions(self)-> list[MissionCreate]:
        return self.missions

    def get_mission_by_id(self,mission_id:str)->MissionResponse | None:
        for mission in self.missions:
            if mission.id == mission_id:
                return mission
        return None

    def get_missions_by_employee(self, emp_id: str) -> list[MissionResponse] | None:
        for mission in self.missions:
            if mission.assigned_to == emp_id:
                return mission
        return None

    def update_mission(self,mission_id:str, data:dict):
        mission = self.get_mission_by_id(mission_id)
        if not mission:
            return None
        for key, value in data.items():
            setattr(mission,key,value)
        return mission

    def delete_mission(self, mission_id: str) -> bool:
        mission = self.get_mission_by_id(mission_id)
        if not mission:
            return False
        self.missions.remove(mission)
        return True