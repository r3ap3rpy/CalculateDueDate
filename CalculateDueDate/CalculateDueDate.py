from datetime import datetime
from datetime import timedelta
from .CalculateDueDateExceptions import *

def CalculateDueDate(SubmitDate: datetime, TurnaroundTime: int) -> datetime:
    if not SubmitDate.isoweekday() in range(1,6):
        raise OutOfWeekDays("The submit date is not a valid workday date!")
    if not SubmitDate.hour in range(9,17):
        raise OutOfWorkingHours("The submit date is not a valid working hour of the working day!")
    TurnaroundSeconds = TurnaroundTime * 3600
    while TurnaroundSeconds >= 0:
        if SubmitDate.isoweekday() in [6,7]:
            SubmitDate += timedelta(days=1)
        if SubmitDate.hour == 17:
            SubmitDate += timedelta(hours=16)
        
        SubmitDate += timedelta(seconds=1)
        TurnaroundSeconds -= 1
    return SubmitDate