from connections import *
from program import *
from table_definitions import *

session = MMSIMIGRATION.session
data = session.query(ClassAttendance)

def test_duplicates():
    assert duplicates_exist(session, ClassAttendance.name) == False

# Everything below checks for nulls:

def test_reason():
    assert is_not_null(data, ClassAttendance.reason) == True

def test_passed():
    assert is_not_null(data, ClassAttendance.passed) == True

def test_classID():
    assert is_not_null(data, ClassAttendance.classID) == True

def test_classSessionID():
    assert is_not_null(data, ClassAttendance.classSessionID) == True

def test_contactID():
    assert is_not_null(data, ClassAttendance.contactID) == True

def test_statusReason():
    assert is_not_null(data, ClassAttendance.statusReason) == True

def test_name():
    assert is_not_null(data, ClassAttendance.name) == True

def test_displayName():
    assert is_not_null(data, ClassAttendance.displayName) == True

