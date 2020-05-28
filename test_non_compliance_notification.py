from connection import Connection as conn
from table_definitions import *

results = conn.session.query(NonComplianceNotification)

# Helper functions. These are not tests.

def checkForNull():
    return None

# Testing for absence of null values in various columns:

def test_complianceID():
    assert results\
        .filter(NonComplianceNotification.complianceID == None)\
        .first() == None

def test_contactID():
    assert results\
        .filter(NonComplianceNotification.contactID == None)\
        .first() == None

def test_name():
    assert results\
        .filter(NonComplianceNotification.name == None)\
        .first() == None

def test_nonComplianceRule():
    assert results\
        .filter(NonComplianceNotification.nonComplianceRule == None)\
        .first() == None

def test_notificationDate():
    assert results\
        .filter(NonComplianceNotification.notificationDate == None)\
        .first() == None

def test_notificationIssue():
    assert results\
        .filter(NonComplianceNotification.notificationIssue == None)\
        .first() == None

def test_stateCode():
    assert results\
        .filter(NonComplianceNotification.stateCode == None)\
        .first() == None

def test_statusReason():
    assert results\
        .filter(NonComplianceNotification.statuReason == None)\
        .first() == None

def test_displayName():
    assert results\
        .filter(NonComplianceNotification.displayName == None)\
        .first() == None

