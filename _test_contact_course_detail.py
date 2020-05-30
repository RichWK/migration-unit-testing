from program import *
from table_definitions import *

table = "ContactCourseDetail"
results = Connection.session.query(eval(table))
table += "."



# These tests verify there are no null values in each column.

def test_alignmentDate():
    assert is_not_null(results, table + "alignmentDate") == None

def test_attendanceResult():
    assert is_not_null(results, table + "attendanceResult") == None

def test_classID():
    assert is_not_null(results, table + "classID") == None

def test_completionDate():
    assert is_not_null(results, table + "completionDate") == None

def test_contactID():
    assert is_not_null(results, table + "contactID") == None

def test_courseID():
    assert is_not_null(results, table + "courseID") == None

def test_courseResult():
    assert is_not_null(results, table + "courseResult") == None

def test_deliveryMethod():
    assert is_not_null(results, table + "deliveryMethod") == None

def test_educationContactRole():
    assert is_not_null(results, table + "educationContactRole") == None

def test_name():
    assert is_not_null(results, table + "name") == None

def test_noComponentsPassed():
    assert is_not_null(results, table + "noComponentsPassed") == None

def test_providerForThisClassID():
    assert is_not_null(results, table + "providerForThisClassID") == None

def test_reasonForCourse():
    assert is_not_null(results, table + "reasonForCourse") == None

def test_registrationID():
    assert is_not_null(results, table + "registrationID") == None

def test_resultReason():
    assert is_not_null(results, table + "resultReason") == None

def test_source():
    assert is_not_null(results, table + "source") == None

def test_startDate():
    assert is_not_null(results, table + "startDate") == None

def test_statusReason():
    assert is_not_null(results, table + "statusReason") == None

def test_counter():
    assert is_not_null(results, table + "counter") == None

def test_components():
    assert is_not_null(results, table + "components") == None

def test_applyCredits():
    assert is_not_null(results, table + "applyCredits") == None

def test_displayName():
    assert is_not_null(results, table + "displayName") == None

