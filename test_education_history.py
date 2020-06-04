from connections import *
from program import *
from table_definitions import *

session = MMSIMIGRATION.session
data = session.query(EducationHistory)

def test_duplicates():
    assert duplicates_exist(session, EducationHistory.name) == False

def test_contactCourseDetail_lookup():
    assert missing_from_target(
        EducationHistory.eduHistoryID
        ,ContactCourseDetail.name
        ,session
        ) == True

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

