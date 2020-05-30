from program import *
from table_definitions import *

results = Connection.session.query(ClassAttendanceLog)



# These tests verify there are no null values in each column.

def test_checkInOut():
    assert is_not_null(results, ClassAttendanceLog.checkInOut) == True

def test_checkInOutDateTime():
    assert is_not_null(results, ClassAttendanceLog.checkInOutDateTime) == True

def test_classSessionID():
    assert is_not_null(results, ClassAttendanceLog.classSessionID) == True

def test_contactID():
    assert is_not_null(results, ClassAttendanceLog.contactID) == True

def test_name():
    assert is_not_null(results, ClassAttendanceLog.name) == True

def test_classAttendanceID():
    assert is_not_null(results, ClassAttendanceLog.classAttendanceID) == True

def test_statusCode():
    assert is_not_null(results, ClassAttendanceLog.statusCode) == True

def test_displayName():
    assert is_not_null(results, ClassAttendanceLog.displayName) == True

