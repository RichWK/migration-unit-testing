from connections import *
from program import *
from table_definitions import *

scribe_dev1 = SCRIBE_DEV1.session
data = scribe_dev1.query(ContactCourseDetail)

def test_duplicates():
    assert duplicates_exist(scribe_dev1, ContactCourseDetail.name) == False

# These tests verify that lookups to other entities actually exist in those entities.

def test_class_lookup():
    assert missing_from_target(
        ContactCourseDetail.classID
        ,Class.mmsiClassCode
        ,scribe_dev1
    ) == 0

def test_course_lookup():
    assert missing_from_target(
        ContactCourseDetail.courseID
        ,Course.name
        ,scribe_dev1
    ) == 0

def test_registration_lookup():
    assert missing_from_target(
        ContactCourseDetail.registrationID
        ,Registration.name
        ,scribe_dev1
    ) == 0

# Everything below checks for nulls:

def test_attendanceResult():
    assert is_not_null(data, ContactCourseDetail.attendanceResult) == True

def test_contactID():
    assert is_not_null(data, ContactCourseDetail.contactID) == True

def test_courseID():
    assert is_not_null(data, ContactCourseDetail.courseID) == True

def test_courseResult():
    assert is_not_null(data, ContactCourseDetail.courseResult) == True

def test_deliveryMethod():
    assert is_not_null(data, ContactCourseDetail.deliveryMethod) == True

def test_name():
    assert is_not_null(data, ContactCourseDetail.name) == True

def test_noComponentsPassed():
    assert is_not_null(data, ContactCourseDetail.noComponentsPassed) == True

def test_reasonForCourse():
    assert is_not_null(data, ContactCourseDetail.reasonForCourse) == True

def test_resultReason():
    assert is_not_null(data, ContactCourseDetail.resultReason) == True

def test_source():
    assert is_not_null(data, ContactCourseDetail.source) == True

def test_startDate():
    assert is_not_null(data, ContactCourseDetail.startDate) == True

def test_statusReason():
    assert is_not_null(data, ContactCourseDetail.statusReason) == True

def test_displayName():
    assert is_not_null(data, ContactCourseDetail.displayName) == True

