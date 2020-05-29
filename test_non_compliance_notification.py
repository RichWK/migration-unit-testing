from program import *
from table_definitions import *

table = "NonComplianceNotification"
results = Connection.session.query(eval(table))
table += "."



# These tests verify there are no null values in each column.

def test_complianceID():
    assert is_not_null(results, table + "complianceID") == None

def test_contactID():
    assert is_not_null(results, table + "contactID") == None

def test_name():
    assert is_not_null(results, table + "name") == None

def test_nonComplianceRule():
    assert is_not_null(results, table + "nonComplianceRule") == None

def test_notificationDate():
    assert is_not_null(results, table + "notificationDate") == None

def test_notificationIssue():
    assert is_not_null(results, table + "notificationIssue") == None

def test_stateCode():
    assert is_not_null(results, table + "stateCode") == None

def test_statusReason():
    assert is_not_null(results, table + "statuReason") == None

def test_displayName():
    assert is_not_null(results, table + "displayName") == None

