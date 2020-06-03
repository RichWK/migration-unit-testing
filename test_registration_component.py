from connections import *
from program import *
from table_definitions import *

session = MMSIMIGRATION.session
data = session.query(RegistrationComponent)

def test_duplicates():
    assert duplicates_exist(session, RegistrationComponent.name) == False

# Everything below checks for nulls:

def test_classComponentID():
    assert is_not_null(data, RegistrationComponent.classComponentID) == True

def test_classID():
    assert is_not_null(data, RegistrationComponent.classID) == True

def test_componentResult():
    assert is_not_null(data, RegistrationComponent.componentResult) == True

def test_contactCourseDetailID():
    assert is_not_null(data, RegistrationComponent.contactCourseDetailID) == True

def test_contactID():
    assert is_not_null(data, RegistrationComponent.contactID) == True

def test_counterID():
    assert is_not_null(data, RegistrationComponent.counterID) == True

def test_deliveryMethod():
    assert is_not_null(data, RegistrationComponent.deliveryMethod) == True

def test_isPassed():
    assert is_not_null(data, RegistrationComponent.isPassed) == True

def test_markPercent():
    assert is_not_null(data, RegistrationComponent.markPercent) == True

def test_name():
    assert is_not_null(data, RegistrationComponent.name) == True

def test_noSessionsAttended():
    assert is_not_null(data, RegistrationComponent.noSessionsAttended) == True

def test_notCompleted():
    assert is_not_null(data, RegistrationComponent.notCompleted) == True

def test_registrationID():
    assert is_not_null(data, RegistrationComponent.registrationID) == True

def test_sequence():
    assert is_not_null(data, RegistrationComponent.sequence) == True

def test_statusReason():
    assert is_not_null(data, RegistrationComponent.statusReason) == True

def test_displayName():
    assert is_not_null(data, RegistrationComponent.displayName) == True

