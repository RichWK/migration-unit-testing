from connections import *
from program import *
from table_definitions import *

# These variables are sets of results from SQLAlchemy.

session = MMSIMIGRATION.session
results = session.query(EducationHistory)

# Verifying that no duplicates exist for this entity's records.

def test_duplicates():
    assert duplicates_exist(session, EducationHistory.name) == False

# Verifying there aren't any invalid lookups.

def test_courseAccreditationLookup():
    assert exists_in(
        session
        ,EducationHistory.courseAccreditationID
        ,CourseAccreditation.name
        ) == True

# These tests verify there are no null values for these columns.

def test_accredUnitType():
    assert is_not_null(results, EducationHistory.accredUnitType) == True

def test_completedCourseUnits():
    assert is_not_null(results, EducationHistory.completedCourseUnits) == True

def test_contactID():
    assert is_not_null(results, EducationHistory.contactID) == True

def test_courseAccreditationID():
    assert is_not_null(results, EducationHistory.courseAccreditationID) == True

def test_courseID():
    assert is_not_null(results, EducationHistory.courseID) == True

def test_eduHistoryID():
    assert is_not_null(results, EducationHistory.eduHistoryID) == True

def test_name():
    assert is_not_null(results, EducationHistory.name) == True

def test_programAccreditationID():
    assert is_not_null(results, EducationHistory.programAccreditationID) == True

def test_programIterationID():
    assert is_not_null(results, EducationHistory.programIterationID) == True

def test_statusReason():
    assert is_not_null(results, EducationHistory.statusReason) == True

def test_displayName():
    assert is_not_null(results, EducationHistory.displayName) == True

def test_applied():
    assert is_not_null(results, EducationHistory.applied) == True

def test_applyCredits():
    assert is_not_null(results, EducationHistory.applyCredits) == True

def test_pending():
    assert is_not_null(results, EducationHistory.pending) == True

