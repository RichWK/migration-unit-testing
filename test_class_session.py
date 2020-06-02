from connections import *
from program import *
from table_definitions import *

session = MMSIMIGRATION.session
results = session.query(ClassSession)

def test_duplicates():
    assert duplicates_exist(session, ClassSession.name) == False

# Everything below checks for nulls:

def test_courseID():
    assert is_not_null(results, ClassSession.courseID) == True

def test_courseClassLevel():
    assert is_not_null(results, ClassSession.courseClassLevel) == True

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

