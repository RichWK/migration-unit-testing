from connections import *
from program import *
from table_definitions import *

scribe_dev1 = SCRIBE_DEV1.session
data = scribe_dev1.query(ClassSession)

def test_duplicates():
    assert duplicates_exist(scribe_dev1, ClassSession.name) == False

# Everything below checks for nulls:

def test_courseID():
    assert is_not_null(data, ClassSession.courseID) == True

def test_courseClassLevel():
    assert is_not_null(data, ClassSession.courseClassLevel) == True

def test_statusCode():
    assert is_not_null(data, ClassSession.statusCode) == True

def test_name():
    assert is_not_null(data, ClassSession.name) == True

def test_sessionNumber():
    assert is_not_null(data, ClassSession.sessionNumber) == True

def test_classComponentID():
    assert is_not_null(data, ClassSession.classComponentID) == True

def test_displayName():
    assert is_not_null(data, ClassSession.displayName) == True

