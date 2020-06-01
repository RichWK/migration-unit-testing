from program import *
from table_definitions import *

results = Connection.session.query(ContactCourseDetail)



# These tests verify there are no null values in each column.

def test_alignmentDate():
    assert is_not_null(results, ContactCourseDetail.alignmentDate) == True

def test_attendanceResult():
    assert is_not_null(results, ContactCourseDetail.attendanceResult) == True

def test_classID():
    assert is_not_null(results, ContactCourseDetail.classID) == True

def test_completionDate():
    assert is_not_null(results, ContactCourseDetail.completionDate) == True

def test_contactID():
    assert is_not_null(results, ContactCourseDetail.contactID) == True

def test_courseID():
    assert is_not_null(results, ContactCourseDetail.courseID) == True

def test_courseResult():
    assert is_not_null(results, ContactCourseDetail.courseResult) == True

def test_deliveryMethod():
    assert is_not_null(results, ContactCourseDetail.deliveryMethod) == True

def test_educationContactRole():
    assert is_not_null(results, ContactCourseDetail.educationContactRole) == True

def test_name():
    assert is_not_null(results, ContactCourseDetail.name) == True

def test_noComponentsPassed():
    assert is_not_null(results, ContactCourseDetail.noComponentsPassed) == True

def test_providerForThisClassID():
    assert is_not_null(results, ContactCourseDetail.providerForThisClassID) == True

def test_reasonForCourse():
    assert is_not_null(results, ContactCourseDetail.reasonForCourse) == True

def test_registrationID():
    assert is_not_null(results, ContactCourseDetail.registrationID) == True

def test_resultReason():
    assert is_not_null(results, ContactCourseDetail.resultReason) == True

def test_source():
    assert is_not_null(results, ContactCourseDetail.source) == True

def test_startDate():
    assert is_not_null(results, ContactCourseDetail.startDate) == True

def test_statusReason():
    assert is_not_null(results, ContactCourseDetail.statusReason) == True

def test_counter():
    assert is_not_null(results, ContactCourseDetail.counter) == True

def test_components():
    assert is_not_null(results, ContactCourseDetail.components) == True

def test_applyCredits():
    assert is_not_null(results, ContactCourseDetail.applyCredits) == True

def test_displayName():
    assert is_not_null(results, ContactCourseDetail.displayName) == True
