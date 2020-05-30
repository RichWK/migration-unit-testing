from program import *
from table_definitions import *

results = Connection.session.query(ClassSession)



# These tests verify there are no null values in each column.

def test_attendanceGeneratedOn():
    assert is_not_null(results, ClassSession.attendanceGeneratedOn) == True

def test_classID():
    assert is_not_null(results, ClassSession.classID) == True

def test_courseID():
    assert is_not_null(results, ClassSession.courseID) == True

def test_courseClassLevel():
    assert is_not_null(results, ClassSession.courseClassLevel) == True

def test_endDate():
    assert is_not_null(results, ClassSession.endDate) == True

def test_startDate():
    assert is_not_null(results, ClassSession.startDate) == True

def test_statusCode():
    assert is_not_null(results, ClassSession.statusCode) == True

def test_name():
    assert is_not_null(results, ClassSession.name) == True

def test_sessionNumber():
    assert is_not_null(results, ClassSession.sessionNumber) == True

def test_classComponentID():
    assert is_not_null(results, ClassSession.classComponentID) == True

def test_displayName():
    assert is_not_null(results, ClassSession.displayName) == True

