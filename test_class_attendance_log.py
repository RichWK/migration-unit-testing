from program import *
from table_definitions import *

table = "ClassAttendanceLog"
results = Connection.session.query(eval(table))
table += "."



# These tests verify there are no null values in each column.

def test_checkInOut():
    assert check_for_null(results, table + "checkInOut") == None

def test_checkInOutDateTime():
    assert check_for_null(results, table + "checkInOutDateTime") == None

def test_classSessionID():
    assert check_for_null(results, table + "classSessionID") == None

def test_contactID():
    assert check_for_null(results, table + "contactID") == None

def test_name():
    assert check_for_null(results, table + "name") == None

def test_classAttendanceID():
    assert check_for_null(results, table + "classAttendanceID") == None

def test_statusCode():
    assert check_for_null(results, table + "statusCode") == None

def test_displayName():
    assert check_for_null(results, table + "displayName") == None

