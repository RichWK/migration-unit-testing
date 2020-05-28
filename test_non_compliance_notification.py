from connection import Connection as conn
from table_definitions import *

table = "NonComplianceNotification"
results = conn.session.query(eval(table))

# Helper functions.
# These are not tests.

def checkForNull(column):
    """Determines whether the provided column contains any null values.
    
    INPUT: String value, matching a column name for this table.
    OUTPUT: An object or None.
    """
    data = table + "." + column
    return results.filter(data == None).first()

# These tests verify that no null values are present in each column.

def test_complianceID():
    assert checkForNull("complianceID") == None

def test_contactID():
    assert checkForNull("contactID") == None

def test_name():
    assert checkForNull("name") == None

def test_nonComplianceRule():
    assert checkForNull("nonComplianceRule") == None

def test_notificationDate():
    assert checkForNull("notificationDate") == None

def test_notificationIssue():
    assert checkForNull("notificationIssue") == None

def test_stateCode():
    assert checkForNull("stateCode") == None

def test_statusReason():
    assert checkForNull("statuReason") == None

def test_displayName():
    assert checkForNull("displayName") == None

