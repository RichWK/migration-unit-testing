from connections import *
from program import *
from table_definitions import *

session = MMSIMIGRATION.session
data = session.query(ClassAttendanceLog)

def test_duplicates():
    assert duplicates_exist(session, ClassAttendanceLog.name) == False

# Everything below checks for nulls:

def test_checkInOut():
    assert is_not_null(data, ClassAttendanceLog.checkInOut) == True

def test_checkInOutDateTime():
    assert is_not_null(data, ClassAttendanceLog.checkInOutDateTime) == True

def test_classSessionID():
    assert is_not_null(data, ClassAttendanceLog.classSessionID) == True

def test_contactID():
    assert is_not_null(data, ClassAttendanceLog.contactID) == True

def test_name():
    assert is_not_null(data, ClassAttendanceLog.name) == True

def test_classAttendanceID():
    assert is_not_null(data, ClassAttendanceLog.classAttendanceID) == True

def test_statusCode():
    assert is_not_null(data, ClassAttendanceLog.statusCode) == True

def test_displayName():
    assert is_not_null(data, ClassAttendanceLog.displayName) == True

