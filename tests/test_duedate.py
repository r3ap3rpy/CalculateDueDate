from CalculateDueDate import CalculateDueDateExceptions
import pytest
from datetime import datetime
from CalculateDueDate.CalculateDueDate import CalculateDueDate
from CalculateDueDate.CalculateDueDateExceptions import *


def test_outofworkinghours():
    with pytest.raises(OutOfWorkingHours) as exc:
        CalculateDueDate(datetime(2021, 11, 11, 19, 10, 55),10)

def test_outofworkingdays():
    with pytest.raises(OutOfWeekDays) as exc:
        CalculateDueDate(datetime(2021, 12, 4, 19, 10, 55),14)

def test_duedate():
    assert CalculateDueDate(datetime(2021, 12, 3, 13, 10, 55),16) == datetime(2021, 12, 7, 13, 10, 55)

def test_invalidturnaroundtime():
    with pytest.raises(ValueError) as exc:
        CalculateDueDate(datetime(2021, 12, 3, 13, 10, 55),'asd')

def test_negativeturnaroundtime():
    with pytest.raises(ValueError) as exc:
        CalculateDueDate(datetime(2021, 12, 3, 13, 10, 55),-1)