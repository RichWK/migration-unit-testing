from connections import *
from program import *
from table_definitions import *

scribe_dev1 = SCRIBE_DEV1.session

data = scribe_dev1.query(EducationHistory)

def test_duplicates():
    assert duplicates_exist(scribe_dev1, EducationHistory.name) == False

# These tests verify that lookups to other entities actually exist in those entities.

def test_compliance_lookup():
    assert missing_from_target(
        EducationHistory.complianceID
        ,Compliance.name
        ,scribe_dev1
    ) == 0

def test_complianceDetail_lookup():
    assert missing_from_target(
        EducationHistory.complianceDetailID
        ,ComplianceDetail.name
        ,scribe_dev1
    ) == 0

def test_contactCourseDetail_lookup():
    assert missing_from_target(
        EducationHistory.eduHistoryID
        ,ContactCourseDetail.name
        ,scribe_dev1
    ) == 0

def test_course_lookup():
    assert missing_from_target(EducationHistory.courseID,Course.name,scribe_dev1) == 0

def test_courseAccreditation_lookup():
    assert missing_from_target(
        EducationHistory.courseAccreditationID
        ,CourseAccreditation.name
        ,scribe_dev1
    ) == 0

# Everything below checks for nulls:

def test_accredUnitType():
    assert is_not_null(data, EducationHistory.accredUnitType) == True

def test_completedCourseUnits():
    assert is_not_null(data, EducationHistory.completedCourseUnits) == True

def test_contactID():
    assert is_not_null(data, EducationHistory.contactID) == True

def test_courseAccreditationID():
    assert is_not_null(data, EducationHistory.courseAccreditationID) == True

def test_courseID():
    assert is_not_null(data, EducationHistory.courseID) == True

def test_eduHistoryID():
    assert is_not_null(data, EducationHistory.eduHistoryID) == True

def test_name():
    assert is_not_null(data, EducationHistory.name) == True

def test_programAccreditationID():
    assert is_not_null(data, EducationHistory.programAccreditationID) == True

def test_programIterationID():
    assert is_not_null(data, EducationHistory.programIterationID) == True

def test_statusReason():
    assert is_not_null(data, EducationHistory.statusReason) == True

def test_displayName():
    assert is_not_null(data, EducationHistory.displayName) == True

def test_applied():
    assert is_not_null(data, EducationHistory.applied) == True

def test_applyCredits():
    assert is_not_null(data, EducationHistory.applyCredits) == True

def test_pending():
    assert is_not_null(data, EducationHistory.pending) == True

