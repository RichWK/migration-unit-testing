from connections import *
from program import *
from table_definitions import *

results = Connection.session.query(NonComplianceNotification)



# These tests verify there are no null values for these columns.

def test_complianceID():
    assert is_not_null(results, NonComplianceNotification.complianceID) == True

def test_contactID():
    assert is_not_null(results, NonComplianceNotification.contactID) == True

def test_name():
    assert is_not_null(results, NonComplianceNotification.name) == True

def test_nonComplianceRule():
    assert is_not_null(results, NonComplianceNotification.nonComplianceRule) == True

def test_notificationDate():
    assert is_not_null(results, NonComplianceNotification.notificationDate) == True

def test_notificationIssue():
    assert is_not_null(results, NonComplianceNotification.notificationIssue) == True

def test_stateCode():
    assert is_not_null(results, NonComplianceNotification.stateCode) == True

def test_statusReason():
    assert is_not_null(results, NonComplianceNotification.statuReason) == True

def test_displayName():
    assert is_not_null(results, NonComplianceNotification.displayName) == True

