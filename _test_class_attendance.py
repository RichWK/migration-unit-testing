from program import *
from table_definitions import *

table = "ClassAttendance"
results = Connection.session.query(eval(table))
table += "."



# These tests verify there are no null values in each column.

def test_reason():
    assert is_not_null(results, table + "reason") == None

def test_passed():
    assert is_not_null(results, table + "passed") == None

def test_checkInDate():
    assert is_not_null(results, table + "checkInDate") == None

def test_checkOutDate():
    assert is_not_null(results, table + "checkOutDate") == None

def test_classID():
    assert is_not_null(results, table + "classID") == None

def test_classSessionID():
    assert is_not_null(results, table + "classSessionID") == None

def test_contactID():
    assert is_not_null(results, table + "contactID") == None

def test_statusReason():
    assert is_not_null(results, table + "statusReason") == None

def test_name():
    assert is_not_null(results, table + "name") == None

def test_attendanceNote():
    assert is_not_null(results, table + "attendanceNote") == None

def test_registrationComponent():
    assert is_not_null(results, table + "registrationComponent") == None

def test_registration():
    assert is_not_null(results, table + "registration") == None

def test_displayName():
    assert is_not_null(results, table + "displayName") == None
