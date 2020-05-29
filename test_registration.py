from program import *
from table_definitions import *

table = "Registration"
results = Connection.session.query(eval(table))
table += "."



# These tests verify there are no null values in each column.

def test_emailAddress():
    assert is_not_null(results, table + "emailAddress") == None

def test_alternatePhoneNumber():
    assert is_not_null(results, table + "alternatePhoneNumber") == None

def test_cancelOrderID():
    assert is_not_null(results, table + "cancelOrderID") == None

def test_cancelOverride():
    assert is_not_null(results, table + "cancelOverride") == None

def test_cancelReason():
    assert is_not_null(results, table + "cancelReason") == None

def test_classID():
    assert is_not_null(results, table + "classID") == None

def test_classPrice():
    assert is_not_null(results, table + "classPrice") == None

def test_contactID():
    assert is_not_null(results, table + "contactID") == None

def test_counter():
    assert is_not_null(results, table + "counter") == None

def test_courseID():
    assert is_not_null(results, table + "courseID") == None

def test_dateAddedToWaitlist():
    assert is_not_null(results, table + "dateAddedToWaitlist") == None

def test_contactCourseDetailID():
    assert is_not_null(results, table + "contactCourseDetailID") == None

def test_hold():
    assert is_not_null(results, table + "hold") == None

def test_holdUntil():
    assert is_not_null(results, table + "holdUntil") == None

def test_isNotABoardMember():
    assert is_not_null(results, table + "isNotABoardMember") == None

def test_name():
    assert is_not_null(results, table + "name") == None

def test_orderID():
    assert is_not_null(results, table + "orderID") == None

def test_orderProductID():
    assert is_not_null(results, table + "orderProductID") == None

def test_organizationID():
    assert is_not_null(results, table + "organizationID") == None

def test_overrideAllowCourseToBeTaken():
    assert is_not_null(results, table + "overrideAllowCourseToBeTaken") == None

def test_preClassActivityEmailProcessed():
    assert is_not_null(results, table + "preClassActivityEmailProcessed") == None

def test_priceRuleID():
    assert is_not_null(results, table + "priceRuleID") == None

def test_regID():
    assert is_not_null(results, table + "regID") == None

def test_registered():
    assert is_not_null(results, table + "registered") == None

def test_reasonForTaking():
    assert is_not_null(results, table + "reasonForTaking") == None

def test_registrationSteps():
    assert is_not_null(results, table + "registrationSteps") == None

def test_transferFromRegID():
    assert is_not_null(results, table + "transferFromRegID") == None

def test_transferPending():
    assert is_not_null(results, table + "transferPending") == None

def test_waitList():
    assert is_not_null(results, table + "waitList") == None

def test_waitListStatus():
    assert is_not_null(results, table + "waitListStatus") == None

def test_statusReason():
    assert is_not_null(results, table + "statusReason") == None

def test_classStartDate():
    assert is_not_null(results, table + "classStartDate") == None

def test_displayName():
    assert is_not_null(results, table + "displayName") == None

