from program import *
from table_definitions import *

table = "RegistrationComponent"
results = Connection.session.query(eval(table))
table += "."



# These tests verify there are no null values in each column.

def test_attendanceResult():
    assert check_for_null(results, table + "attendanceResult") == None

def test_classComponentID():
    assert check_for_null(results, table + "classComponentID") == None

def test_classID():
    assert check_for_null(results, table + "classID") == None

def test_componentResult():
    assert check_for_null(results, table + "componentResult") == None

def test_contactCourseDetailID():
    assert check_for_null(results, table + "contactCourseDetailID") == None

def test_contactID():
    assert check_for_null(results, table + "contactID") == None

def test_counterID():
    assert check_for_null(results, table + "counterID") == None

def test_dateCompleted():
    assert check_for_null(results, table + "dateCompleted") == None

def test_deliveryMethod():
    assert check_for_null(results, table + "deliveryMethod") == None

def test_isPassed():
    assert check_for_null(results, table + "isPassed") == None

def test_markPercent():
    assert check_for_null(results, table + "markPercent") == None

def test_name():
    assert check_for_null(results, table + "name") == None

def test_noSessionsAttended():
    assert check_for_null(results, table + "noSessionsAttended") == None

def test_notCompleted():
    assert check_for_null(results, table + "notCompleted") == None

def test_passFailReason():
    assert check_for_null(results, table + "passFailReason") == None

def test_registrationID():
    assert check_for_null(results, table + "registrationID") == None

def test_sequence():
    assert check_for_null(results, table + "sequence") == None

def test_statusReason():
    assert check_for_null(results, table + "statusReason") == None

def test_displayName():
    assert check_for_null(results, table + "displayName") == None

