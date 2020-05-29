from program import *
from table_definitions import *

table = "ClassAttendance"
results = Connection.session.query(eval(table))
table += "."



# These tests verify there are no null values in each column.

def test_reason():
    assert check_for_null(results, table + "reason") == None

def test_passed():
    assert check_for_null(results, table + "passed") == None

def test_checkInDate():
    assert check_for_null(results, table + "checkInDate") == None

def test_checkOutDate():
    assert check_for_null(results, table + "checkOutDate") == None

def test_classID():
    assert check_for_null(results, table + "classID") == None

def test_classSessionID():
    assert check_for_null(results, table + "classSessionID") == None

def test_contactID():
    assert check_for_null(results, table + "contactID") == None

def test_statusReason():
    assert check_for_null(results, table + "statusReason") == None

def test_name():
    assert check_for_null(results, table + "name") == None

def test_attendanceNote():
    assert check_for_null(results, table + "attendanceNote") == None

def test_registrationComponent():
    assert check_for_null(results, table + "registrationComponent") == None

def test_registration():
    assert check_for_null(results, table + "registration") == None

def test_displayName():
    assert check_for_null(results, table + "displayName") == None

