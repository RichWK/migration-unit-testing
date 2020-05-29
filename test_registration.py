from program import *
from table_definitions import *

table = "Registration"
results = Connection.session.query(eval(table))
table += "."



# These tests verify there are no null values in each column.

def test_emailAddress():
    assert check_for_null(results, table + "emailAddress") == None

def test_alternatePhoneNumber():
    assert check_for_null(results, table + "alternatePhoneNumber") == None

def test_cancelOrderID():
    assert check_for_null(results, table + "cancelOrderID") == None

def test_cancelOverride():
    assert check_for_null(results, table + "cancelOverride") == None

def test_cancelReason():
    assert check_for_null(results, table + "cancelReason") == None

def test_classID():
    assert check_for_null(results, table + "classID") == None

def test_classPrice():
    assert check_for_null(results, table + "classPrice") == None

def test_contactID():
    assert check_for_null(results, table + "contactID") == None

def test_counter():
    assert check_for_null(results, table + "counter") == None

def test_courseID():
    assert check_for_null(results, table + "courseID") == None

def test_dateAddedToWaitlist():
    assert check_for_null(results, table + "dateAddedToWaitlist") == None

def test_contactCourseDetailID():
    assert check_for_null(results, table + "contactCourseDetailID") == None

def test_hold():
    assert check_for_null(results, table + "hold") == None

def test_holdUntil():
    assert check_for_null(results, table + "holdUntil") == None

def test_isNotABoardMember():
    assert check_for_null(results, table + "isNotABoardMember") == None

def test_name():
    assert check_for_null(results, table + "name") == None

def test_orderID():
    assert check_for_null(results, table + "orderID") == None

def test_orderProductID():
    assert check_for_null(results, table + "orderProductID") == None

def test_organizationID():
    assert check_for_null(results, table + "organizationID") == None

def test_overrideAllowCourseToBeTaken():
    assert check_for_null(results, table + "overrideAllowCourseToBeTaken") == None

def test_preClassActivityEmailProcessed():
    assert check_for_null(results, table + "preClassActivityEmailProcessed") == None

def test_priceRuleID():
    assert check_for_null(results, table + "priceRuleID") == None

def test_regID():
    assert check_for_null(results, table + "regID") == None

def test_registered():
    assert check_for_null(results, table + "registered") == None

def test_reasonForTaking():
    assert check_for_null(results, table + "reasonForTaking") == None

def test_registrationSteps():
    assert check_for_null(results, table + "registrationSteps") == None

def test_transferFromRegID():
    assert check_for_null(results, table + "transferFromRegID") == None

def test_transferPending():
    assert check_for_null(results, table + "transferPending") == None

def test_waitList():
    assert check_for_null(results, table + "waitList") == None

def test_waitListStatus():
    assert check_for_null(results, table + "waitListStatus") == None

def test_statusReason():
    assert check_for_null(results, table + "statusReason") == None

def test_classStartDate():
    assert check_for_null(results, table + "classStartDate") == None

def test_displayName():
    assert check_for_null(results, table + "displayName") == None

