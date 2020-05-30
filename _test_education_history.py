from program import *
from table_definitions import *

table = "EducationHistory"
results = Connection.session.query(eval(table))
table += "."



# These tests verify there are no null values in each column.

def test_accredUnitType():
    assert is_not_null(results, table + "accredUnitType") == None

def test_completedCourseUnits():
    assert is_not_null(results, table + "completedCourseUnits") == None

def test_complianceDetailID():
    assert is_not_null(results, table + "complianceDetailID") == None

def test_complianceID():
    assert is_not_null(results, table + "complianceID") == None

def test_contactID():
    assert is_not_null(results, table + "contactID") == None

def test_courseAccreditationID():
    assert is_not_null(results, table + "courseAccreditationID") == None

def test_courseID():
    assert is_not_null(results, table + "courseID") == None

def test_courseUnits():
    assert is_not_null(results, table + "courseUnits") == None

def test_eduHistoryID():
    assert is_not_null(results, table + "eduHistoryID") == None

def test_name():
    assert is_not_null(results, table + "name") == None

def test_programAccreditationID():
    assert is_not_null(results, table + "programAccreditationID") == None

def test_programIterationID():
    assert is_not_null(results, table + "programIterationID") == None

def test_statusReason():
    assert is_not_null(results, table + "statusReason") == None

def test_displayName():
    assert is_not_null(results, table + "displayName") == None

def test_applied():
    assert is_not_null(results, table + "applied") == None

def test_applyCredits():
    assert is_not_null(results, table + "applyCredits") == None

def test_pending():
    assert is_not_null(results, table + "pending") == None

