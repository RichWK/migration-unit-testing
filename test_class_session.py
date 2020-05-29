from program import *
from table_definitions import *

table = "ClassSession"
results = Connection.session.query(eval(table))
table += "."



# These tests verify there are no null values in each column.

def test_attendanceGeneratedOn():
    assert check_for_null(results, table + "attendanceGeneratedOn") == None

def test_classID():
    assert check_for_null(results, table + "classID") == None

def test_courseID():
    assert check_for_null(results, table + "courseID") == None

def test_courseClassLevel():
    assert check_for_null(results, table + "courseClassLevel") == None

def test_endDate():
    assert check_for_null(results, table + "endDate") == None

def test_startDate():
    assert check_for_null(results, table + "startDate") == None

def test_statusCode():
    assert check_for_null(results, table + "statusCode") == None

def test_name():
    assert check_for_null(results, table + "name") == None

def test_sessionNumber():
    assert check_for_null(results, table + "sessionNumber") == None

def test_classComponentID():
    assert check_for_null(results, table + "classComponentID") == None

def test_displayName():
    assert check_for_null(results, table + "displayName") == None

