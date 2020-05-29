from program import *
from table_definitions import *

table = "ContactCourseDetail"
results = Connection.session.query(eval(table))
table += "."



# These tests verify there are no null values in each column.

def test_alignmentDate():
    assert check_for_null(results, table + "alignmentDate") == None

def test_attendanceResult():
    assert check_for_null(results, table + "attendanceResult") == None

def test_classID():
    assert check_for_null(results, table + "classID") == None

def test_completionDate():
    assert check_for_null(results, table + "completionDate") == None

def test_contactID():
    assert check_for_null(results, table + "contactID") == None

def test_courseID():
    assert check_for_null(results, table + "courseID") == None

def test_courseResult():
    assert check_for_null(results, table + "courseResult") == None

def test_deliveryMethod():
    assert check_for_null(results, table + "deliveryMethod") == None

def test_educationContactRole():
    assert check_for_null(results, table + "educationContactRole") == None

def test_name():
    assert check_for_null(results, table + "name") == None

def test_noComponentsPassed():
    assert check_for_null(results, table + "noComponentsPassed") == None

def test_providerForThisClassID():
    assert check_for_null(results, table + "providerForThisClassID") == None

def test_reasonForCourse():
    assert check_for_null(results, table + "reasonForCourse") == None

def test_registrationID():
    assert check_for_null(results, table + "registrationID") == None

def test_resultReason():
    assert check_for_null(results, table + "resultReason") == None

def test_source():
    assert check_for_null(results, table + "source") == None

def test_startDate():
    assert check_for_null(results, table + "startDate") == None

def test_statusReason():
    assert check_for_null(results, table + "statusReason") == None

def test_counter():
    assert check_for_null(results, table + "counter") == None

def test_components():
    assert check_for_null(results, table + "components") == None

def test_applyCredits():
    assert check_for_null(results, table + "applyCredits") == None

def test_displayName():
    assert check_for_null(results, table + "displayName") == None

