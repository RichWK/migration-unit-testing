from connections import *
from program import *
from table_definitions import *

scribe_dev1 = SCRIBE_DEV1.session

# These tests verify that lookups to other entities actually exist in those entities.

def test_class_lookup():
    assert missing_from_target(
        ClassContact.classID
        ,Class.mmsiClassCode
        ,scribe_dev1
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

