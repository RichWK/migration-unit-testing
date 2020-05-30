from program import *
from table_definitions import *

results = Connection.session.query(Registration)



# These tests verify there are no null values in each column.

def test_emailAddress():
    assert is_not_null(results, Registration.emailAddress) == None

def test_alternatePhoneNumber():
    assert is_not_null(results, Registration.alternatePhoneNumber) == None

def test_cancelOrderID():
    assert is_not_null(results, Registration.cancelOrderID) == None

def test_cancelOverride():
    assert is_not_null(results, Registration.cancelOverride) == None

def test_cancelReason():
    assert is_not_null(results, Registration.cancelReason) == None

def test_classID():
    assert is_not_null(results, Registration.classID) == None

def test_classPrice():
    assert is_not_null(results, Registration.classPrice) == None

def test_contactID():
    assert is_not_null(results, Registration.contactID) == None

def test_counter():
    assert is_not_null(results, Registration.counter) == None

def test_courseID():
    assert is_not_null(results, Registration.courseID) == None

def test_dateAddedToWaitlist():
    assert is_not_null(results, Registration.dateAddedToWaitlist) == None

def test_dateCancelledTransferred():
    assert is_not_null(results, Registration.dateCancelledTransferred) == None

def test_dateCourseEvalSent():
    assert is_not_null(results, Registration.dateCourseEvalSent) == None

def test_dateRegistered():
    assert is_not_null(results, Registration.dateRegistered) == None

def test_dateRemovedFromWaitList():
    assert is_not_null(results, Registration.dateRemovedFromWaitList) == None

def test_contactCourseDetailID():
    assert is_not_null(results, Registration.contactCourseDetailID) == None

def test_hold():
    assert is_not_null(results, Registration.hold) == None

def test_holdUntil():
    assert is_not_null(results, Registration.holdUntil) == None

def test_isNotABoardMember():
    assert is_not_null(results, Registration.isNotABoardMember) == None

def test_name():
    assert is_not_null(results, Registration.name) == None

def test_orderID():
    assert is_not_null(results, Registration.orderID) == None

def test_orderProductID():
    assert is_not_null(results, Registration.orderProductID) == None

def test_organizationID():
    assert is_not_null(results, Registration.organizationID) == None

def test_overrideAllowCourseToBeTaken():
    assert is_not_null(results, Registration.overrideAllowCourseToBeTaken) == None

def test_preClassActivityEmailProcessed():
    assert is_not_null(results, Registration.preClassActivityEmailProcessed) == None

def test_priceRuleID():
    assert is_not_null(results, Registration.priceRuleID) == None

def test_regID():
    assert is_not_null(results, Registration.regID) == None

def test_registered():
    assert is_not_null(results, Registration.registered) == None

def test_reasonForTaking():
    assert is_not_null(results, Registration.reasonForTaking) == None

def test_registrationSteps():
    assert is_not_null(results, Registration.registrationSteps) == None

def test_transferFromRegID():
    assert is_not_null(results, Registration.transferFromRegID) == None

def test_transferPending():
    assert is_not_null(results, Registration.transferPending) == None

def test_waitList():
    assert is_not_null(results, Registration.waitList) == None

def test_waitListStatus():
    assert is_not_null(results, Registration.waitListStatus) == None

def test_statusReason():
    assert is_not_null(results, Registration.statusReason) == None

def test_classStartDate():
    assert is_not_null(results, Registration.classStartDate) == None

def test_displayName():
    assert is_not_null(results, Registration.displayName) == None

