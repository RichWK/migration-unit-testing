from connections import *
from program import *
from table_definitions import *

scribe_dev1 = SCRIBE_DEV1.session
data = scribe_dev1.query(NonComplianceNotification)

def test_duplicates():
    assert duplicates_exist(scribe_dev1, NonComplianceNotification.name) == False

# Everything below checks for nulls:

def test_complianceID():
    assert is_not_null(data, NonComplianceNotification.complianceID) == True

def test_contactID():
    assert is_not_null(data, NonComplianceNotification.contactID) == True

def test_name():
    assert is_not_null(data, NonComplianceNotification.name) == True

def test_nonComplianceRule():
    assert is_not_null(data, NonComplianceNotification.nonComplianceRule) == True

def test_notificationDate():
    assert is_not_null(data, NonComplianceNotification.notificationDate) == True

def test_notificationIssue():
    assert is_not_null(data, NonComplianceNotification.notificationIssue) == True

def test_stateCode():
    assert is_not_null(data, NonComplianceNotification.stateCode) == True

def test_statusReason():
    assert is_not_null(data, NonComplianceNotification.statuReason) == True

def test_displayName():
    assert is_not_null(data, NonComplianceNotification.displayName) == True

