from program import *
from table_definitions import *

table = "RegistrationComponent"
results = Connection.session.query(eval(table))
table += "."



# These tests verify there are no null values in each column.

def test_attendanceResult():
    assert is_not_null(results, table + "attendanceResult") == None

def test_classComponentID():
    assert is_not_null(results, table + "classComponentID") == None

def test_classID():
    assert is_not_null(results, table + "classID") == None

def test_componentResult():
    assert is_not_null(results, table + "componentResult") == None

def test_contactCourseDetailID():
    assert is_not_null(results, table + "contactCourseDetailID") == None

def test_contactID():
    assert is_not_null(results, table + "contactID") == None

def test_counterID():
    assert is_not_null(results, table + "counterID") == None

def test_dateCompleted():
    assert is_not_null(results, table + "dateCompleted") == None

def test_deliveryMethod():
    assert is_not_null(results, table + "deliveryMethod") == None

def test_isPassed():
    assert is_not_null(results, table + "isPassed") == None

def test_markPercent():
    assert is_not_null(results, table + "markPercent") == None

def test_name():
    assert is_not_null(results, table + "name") == None

def test_noSessionsAttended():
    assert is_not_null(results, table + "noSessionsAttended") == None

def test_notCompleted():
    assert is_not_null(results, table + "notCompleted") == None

def test_passFailReason():
    assert is_not_null(results, table + "passFailReason") == None

def test_registrationID():
    assert is_not_null(results, table + "registrationID") == None

def test_sequence():
    assert is_not_null(results, table + "sequence") == None

def test_statusReason():
    assert is_not_null(results, table + "statusReason") == None

def test_displayName():
    assert is_not_null(results, table + "displayName") == None

