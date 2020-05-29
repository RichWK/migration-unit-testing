from program import Connection as conn, check_for_null
from table_definitions import *

table = "NonComplianceNotification"
results = conn.session.query(eval(table))
table += "."



# These tests verify there are no null values in each column.

def test_complianceID():
    assert check_for_null(results, table + "complianceID") == None

def test_contactID():
    assert check_for_null(results, table + "contactID") == None

def test_name():
    assert check_for_null(results, table + "name") == None

def test_nonComplianceRule():
    assert check_for_null(results, table + "nonComplianceRule") == None

def test_notificationDate():
    assert check_for_null(results, table + "notificationDate") == None

def test_notificationIssue():
    assert check_for_null(results, table + "notificationIssue") == None

def test_stateCode():
    assert check_for_null(results, table + "stateCode") == None

def test_statusReason():
    assert check_for_null(results, table + "statuReason") == None

def test_displayName():
    assert check_for_null(results, table + "displayName") == None

