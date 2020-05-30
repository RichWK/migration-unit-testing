from program import *
from table_definitions import *

results = Connection.session.query(Registration)



# These tests verify there are no null values in each column.

def test_emailAddress():
    assert is_not_null(results, Registration.emailAddress) == True

def test_alternatePhoneNumber():
    assert is_not_null(results, Registration.alternatePhoneNumber) == True

def test_cancelOrderID():
    assert is_not_null(results, Registration.cancelOrderID) == True

def test_cancelOverride():
    assert is_not_null(results, Registration.cancelOverride) == True

def test_cancelReason():
    assert is_not_null(results, Registration.cancelReason) == True

def test_classID():
    assert is_not_null(results, Registration.classID) == True

def test_classPrice():
    assert is_not_null(results, Registration.classPrice) == True

def test_contactID():
    assert is_not_null(results, Registration.contactID) == True

def test_counter():
    assert is_not_null(results, Registration.counter) == True

def test_courseID():
    assert is_not_null(results, Registration.courseID) == True

def test_dateAddedToWaitlist():
    assert is_not_null(results, Registration.dateAddedToWaitlist) == True

def test_dateCancelledTransferred():
    assert is_not_null(results, Registration.dateCancelledTransferred) == True

def test_dateCourseEvalSent():
    assert is_not_null(results, Registration.dateCourseEvalSent) == True

def test_dateRegistered():
    assert is_not_null(results, Registration.dateRegistered) == True

def test_dateRemovedFromWaitList():
    assert is_not_null(results, Registration.dateRemovedFromWaitList) == True

def test_contactCourseDetailID():
    assert is_not_null(results, Registration.contactCourseDetailID) == True

def test_hold():
    assert is_not_null(results, Registration.hold) == True

def test_holdUntil():
    assert is_not_null(results, Registration.holdUntil) == True

def test_isNotABoardMember():
    assert is_not_null(results, Registration.isNotABoardMember) == True

def test_name():
    assert is_not_null(results, Registration.name) == True

def test_orderID():
    assert is_not_null(results, Registration.orderID) == True

def test_orderProductID():
    assert is_not_null(results, Registration.orderProductID) == True

def test_organizationID():
    assert is_not_null(results, Registration.organizationID) == True

def test_overrideAllowCourseToBeTaken():
    assert is_not_null(results, Registration.overrideAllowCourseToBeTaken) == True

def test_preClassActivityEmailProcessed():
    assert is_not_null(results, Registration.preClassActivityEmailProcessed) == True

def test_priceRuleID():
    assert is_not_null(results, Registration.priceRuleID) == True

def test_regID():
    assert is_not_null(results, Registration.regID) == True

def test_registered():
    assert is_not_null(results, Registration.registered) == True

def test_reasonForTaking():
    assert is_not_null(results, Registration.reasonForTaking) == True

def test_registrationSteps():
    assert is_not_null(results, Registration.registrationSteps) == True

def test_transferFromRegID():
    assert is_not_null(results, Registration.transferFromRegID) == True

def test_transferPending():
    assert is_not_null(results, Registration.transferPending) == True

def test_waitList():
    assert is_not_null(results, Registration.waitList) == True

def test_waitListStatus():
    assert is_not_null(results, Registration.waitListStatus) == True

def test_statusReason():
    assert is_not_null(results, Registration.statusReason) == True

def test_classStartDate():
    assert is_not_null(results, Registration.classStartDate) == True

def test_displayName():
    assert is_not_null(results, Registration.displayName) == True
