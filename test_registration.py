from connections import *
from program import *
from table_definitions import *

mmsimigration = MMSIMIGRATION.session
data = mmsimigration.query(Registration)

def test_duplicates():
    assert duplicates_exist(mmsimigration, Registration.name) == False

# These tests verify that lookups to other entities actually exist in those entities.

def test_contactCourseDetail_lookup():
    assert missing_from_target(
        Registration.contactCourseDetailID
        ,ContactCourseDetail.name
        ,mmsimigration
    ) == 0

def test_classPriceRule_lookup():
    assert missing_from_target(
        Registration.priceRuleID
        ,ClassPriceRule.name
        ,mmsimigration
    ) == 0

# Everything below checks for nulls:

def test_emailAddress():
    assert is_not_null(data, Registration.emailAddress) == True

def test_alternatePhoneNumber():
    assert is_not_null(data, Registration.alternatePhoneNumber) == True

def test_cancelOverride():
    assert is_not_null(data, Registration.cancelOverride) == True

def test_cancelReason():
    assert is_not_null(data, Registration.cancelReason) == True

def test_classID():
    assert is_not_null(data, Registration.classID) == True

def test_contactID():
    assert is_not_null(data, Registration.contactID) == True

def test_counter():
    assert is_not_null(data, Registration.counter) == True

def test_courseID():
    assert is_not_null(data, Registration.courseID) == True

def test_dateRegistered():
    assert is_not_null(data, Registration.dateRegistered) == True

def test_contactCourseDetailID():
    assert is_not_null(data, Registration.contactCourseDetailID) == True

def test_hold():
    assert is_not_null(data, Registration.hold) == True

def test_holdUntil():
    assert is_not_null(data, Registration.holdUntil) == True

def test_name():
    assert is_not_null(data, Registration.name) == True

def test_orderID():
    assert is_not_null(data, Registration.orderID) == True

def test_orderProductID():
    assert is_not_null(data, Registration.orderProductID) == True

def test_organizationID():
    assert is_not_null(data, Registration.organizationID) == True

def test_overrideAllowCourseToBeTaken():
    assert is_not_null(data, Registration.overrideAllowCourseToBeTaken) == True

def test_priceRuleID():
    assert is_not_null(data, Registration.priceRuleID) == True

def test_regID():
    assert is_not_null(data, Registration.regID) == True

def test_registered():
    assert is_not_null(data, Registration.registered) == True

def test_reasonForTaking():
    assert is_not_null(data, Registration.reasonForTaking) == True

def test_registrationSteps():
    assert is_not_null(data, Registration.registrationSteps) == True

def test_statusReason():
    assert is_not_null(data, Registration.statusReason) == True

def test_classStartDate():
    assert is_not_null(data, Registration.classStartDate) == True

def test_displayName():
    assert is_not_null(data, Registration.displayName) == True

