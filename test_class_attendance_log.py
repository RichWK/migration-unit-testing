from connections import *
from program import *
from table_definitions import *

primary_session = MMSIMIGRATION.session
data = primary_session.query(ClassAttendanceLog)

def test_duplicates():
    assert duplicates_exist(primary_session, ClassAttendanceLog.name) == False

# These tests verify that lookups to other entities actually exist in those entities.

def test_classSession_lookup():
    assert missing_from_target(
        ClassAttendanceLog.classSessionID
        ,ClassSession.name
        ,primary_session
    ) == 0

def test_classAttendance_lookup():
    assert missing_from_target(
        ClassAttendanceLog.classAttendanceID
        ,ClassAttendance.name
        ,primary_session
    ) == 0

# Everything below checks for nulls:

def test_checkInOut():
    assert is_not_null(data, ClassAttendanceLog.checkInOut) == True

def test_checkInOutDateTime():
    assert is_not_null(data, ClassAttendanceLog.checkInOutDateTime) == True

def test_classSessionID():
    assert is_not_null(data, ClassAttendanceLog.classSessionID) == True

def test_contactID():
    assert is_not_null(data, ClassAttendanceLog.contactID) == True

def test_name():
    assert is_not_null(data, ClassAttendanceLog.name) == True

def test_classAttendanceID():
    assert is_not_null(data, ClassAttendanceLog.classAttendanceID) == True

def test_statusCode():
    assert is_not_null(data, ClassAttendanceLog.statusCode) == True

def test_displayName():
    assert is_not_null(data, ClassAttendanceLog.displayName) == True

