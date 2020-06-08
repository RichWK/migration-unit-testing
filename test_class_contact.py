from connections import *
from program import *
from table_definitions import *

scribe_dev1 = SCRIBE_DEV1.session
data = scribe_dev1.query(ClassContact)

def test_duplicates():
    assert duplicates_exist(scribe_dev1, ClassContact.name) == False

# These tests verify that lookups to other entities actually exist in those entities.

def test_class_lookup():
    assert missing_from_target(
        ClassContact.classID
        ,Class.mmsiClassCode
        ,scribe_dev1
        ,EventsClass.mmsiClassCode
    ) == 0

def test_course_lookup():
    assert missing_from_target(
        ClassContact.courseID
        ,Course.name
        ,scribe_dev1
    ) == 0

def test_courseContact_lookup():
    assert missing_from_target(
        ClassContact.courseContactID
        ,CourseContact.name
        ,scribe_dev1
    ) == 0

# Everything below checks for nulls:

def test_classID():
    assert is_not_null(data, ClassContact.classID) == True

def test_contactID():
    assert is_not_null(data, ClassContact.contactID) == True

def test_courseID():
    assert is_not_null(data, ClassContact.courseID) == True

def test_roleForThisClass():
    assert is_not_null(data, ClassContact.roleForThisClass) == True

def test_courseContactID():
    assert is_not_null(data, ClassContact.courseContactID) == True

def test_displayName():
    assert is_not_null(data, ClassContact.displayName) == True

