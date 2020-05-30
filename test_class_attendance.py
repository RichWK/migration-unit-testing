from program import *
from table_definitions import *

results = Connection.session.query(ClassAttendance)



# These tests verify there are no null values in each column.

def test_reason():
    assert is_not_null(results, ClassAttendance.reason) == True

def test_passed():
    assert is_not_null(results, ClassAttendance.passed) == True

def test_checkInDate():
    assert is_not_null(results, ClassAttendance.checkInDate) == True

def test_checkOutDate():
    assert is_not_null(results, ClassAttendance.checkOutDate) == True

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

def test_attendanceNote():
    assert is_not_null(results, ClassAttendance.attendanceNote) == True

def test_registrationComponent():
    assert is_not_null(results, ClassAttendance.registrationComponent) == True

def test_registration():
    assert is_not_null(results, ClassAttendance.registration) == True

def test_displayName():
    assert is_not_null(results, ClassAttendance.displayName) == True

