from connections import *
from program import *
from table_definitions import *

results = Connection.session.query(RegistrationComponent)



# These tests verify there are no null values for these columns.

def test_classComponentID():
    assert is_not_null(results, RegistrationComponent.classComponentID) == True

def test_classID():
    assert is_not_null(results, RegistrationComponent.classID) == True

def test_componentResult():
    assert is_not_null(results, RegistrationComponent.componentResult) == True

def test_contactCourseDetailID():
    assert is_not_null(results, RegistrationComponent.contactCourseDetailID) == True

def test_contactID():
    assert is_not_null(results, RegistrationComponent.contactID) == True

def test_counterID():
    assert is_not_null(results, RegistrationComponent.counterID) == True

def test_deliveryMethod():
    assert is_not_null(results, RegistrationComponent.deliveryMethod) == True

def test_isPassed():
    assert is_not_null(results, RegistrationComponent.isPassed) == True

def test_markPercent():
    assert is_not_null(results, RegistrationComponent.markPercent) == True

def test_name():
    assert is_not_null(results, RegistrationComponent.name) == True

def test_noSessionsAttended():
    assert is_not_null(results, RegistrationComponent.noSessionsAttended) == True

def test_notCompleted():
    assert is_not_null(results, RegistrationComponent.notCompleted) == True

def test_registrationID():
    assert is_not_null(results, RegistrationComponent.registrationID) == True

def test_sequence():
    assert is_not_null(results, RegistrationComponent.sequence) == True

def test_statusReason():
    assert is_not_null(results, RegistrationComponent.statusReason) == True

def test_displayName():
    assert is_not_null(results, RegistrationComponent.displayName) == True

