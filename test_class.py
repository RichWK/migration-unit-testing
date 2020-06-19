from connections import *
from program import *
from table_definitions import *

scribe_dev1 = SCRIBE_DEV1.session
data = scribe_dev1.query(Class)

# These tests verify that lookups to other entities actually exist in those entities.

def test_course_lookup():
    assert missing_from_target(
        Class.courseID
        ,Course.name
        ,scribe_dev1
    ) == 0

def test_venue_lookup():
    assert missing_from_target(
        Class.venueID
        ,Venue.name
        ,scribe_dev1
    ) == 0

# Everything below checks for nulls:

def test_allowRegistrationWithoutOrder():
    assert is_not_null(data, Class.allowRegistrationWithoutOrder) == True

def test_mmsiClassCode():
    assert is_not_null(data, Class.mmsiClassCode) == True

def test_classInstanceNumber():
    assert is_not_null(data, Class.classInstanceNumber) == True

def test_dateOpenForRegistration():
    assert is_not_null(data, Class.dateOpenForRegistration) == True

def test_deliveryMethod():
    assert is_not_null(data, Class.deliveryMethod) == True

def test_endDate():
    assert is_not_null(data, Class.endDate) == True

def test_instructorID():
    assert is_not_null(data, Class.instructorID) == True

def test_maxAttendance():
    assert is_not_null(data, Class.maxAttendance) == True

def test_maxNonBoardMembers():
    assert is_not_null(data, Class.maxNonBoardMembers) == True

def test_minAttendance():
    assert is_not_null(data, Class.minAttendance) == True

def test_name():
    assert is_not_null(data, Class.name) == True

def test_noComponents():
    assert is_not_null(data, Class.noComponents) == True

def test_noComponentsNotCompleted():
    assert is_not_null(data, Class.noComponentsNotCompleted) == True

def test_noNonBoardMembersRegistered():
    assert is_not_null(data, Class.noNonBoardMembersRegistered) == True

def test_noRegistered():
    assert is_not_null(data, Class.noRegistered) == True

def test_registrationDeadline():
    assert is_not_null(data, Class.registrationDeadline) == True

def test_reminderDateForClassContacts():
    assert is_not_null(data, Class.reminderDateForClassContacts) == True

def test_restrictWhoCanTakeCourse():
    assert is_not_null(data, Class.restrictWhoCanTakeCourse) == True

def test_ruleRegistrationDays():
    assert is_not_null(data, Class.ruleRegistrationDays) == True

def test_sellOnWeb():
    assert is_not_null(data, Class.sellOnWeb) == True

def test_startDate():
    assert is_not_null(data, Class.startDate) == True

def test_venueID():
    assert is_not_null(data, Class.venueID) == True

def test_classID():
    assert is_not_null(data, Class.classID) == True

def test_viewOnWeb():
    assert is_not_null(data, Class.viewOnWeb) == True

def test_statusCode():
    assert is_not_null(data, Class.statusCode) == True

def test_education():
    assert is_not_null(data, Class.education) == True

def test_eventCourse():
    assert is_not_null(data, Class.eventCourse) == True

def test_guestsAllowed():
    assert is_not_null(data, Class.guestsAllowed) == True

def test_noGuestsAllowed():
    assert is_not_null(data, Class.noGuestsAllowed) == True

def test_noGuestSeatsTaken():
    assert is_not_null(data, Class.noGuestSeatsTaken) == True

def test_ruleCancelDays():
    assert is_not_null(data, Class.ruleCancelDays) == True

