from connections import *
from program import *
from table_definitions import *

results = Connection.session.query(ClassAttendance)



# These tests verify there are no null values for these columns.

def test_reason():
    assert is_not_null(results, ClassAttendance.reason) == True

def test_passed():
    assert is_not_null(results, ClassAttendance.passed) == True

def test_classID():
    assert is_not_null(results, ClassAttendance.classID) == True

def test_classSessionID():
    assert is_not_null(results, ClassAttendance.classSessionID) == True

def test_contactID():
    assert is_not_null(results, ClassAttendance.contactID) == True

def test_statusReason():
    assert is_not_null(results, ClassAttendance.statusReason) == True

def test_name():
    assert is_not_null(results, ClassAttendance.name) == True

def test_displayName():
    assert is_not_null(results, ClassAttendance.displayName) == True

