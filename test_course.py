from connections import *
from program import *
from table_definitions import *

scribe_dev1 = SCRIBE_DEV1.session
data = scribe_dev1.query(Course)

# These tests verify that lookups to other entities actually exist in those entities.

def test_primaryAccreditation_lookup():
    assert missing_from_target(
        Course.primaryAccreditation
        ,CourseAccreditation.name
        ,scribe_dev1
    ) == 0

# Everything below checks for nulls:

def test_name():
    assert is_not_null(data, Course.name) == True

