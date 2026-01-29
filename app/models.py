from datetime import datetime
from pydantic import BaseModel
from  typing import Optional


class MissionBase(BaseModel):  #שדות בסיסים של מחלקת משימה
    title: str
    assigned_to: str
    status: str
    priority: str
    deadline: str

class MissionCreate(MissionBase):   #יצירת משימה
    id: str

class MissionUpdate(BaseModel):   #עדכון משימה
    title: Optional[str] = None
    assigned_to: Optional[str] = None
    status: Optional[str] = None
    priority: Optional[str] = None
    deadline: Optional[str] = None

class MissionResponse(MissionBase):    #השרת  מחזיר תגובה אחרי יצירה וכו
    id: str
    created_at: datetime