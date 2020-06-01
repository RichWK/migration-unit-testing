from program import *
from table_definitions import *

results = Connection.session.query(ClassPriceRule)



# These tests verify there are no null values for these columns.

def test_classID():
    assert is_not_null(results, ClassPriceRule.classID) == True

def test_courseID():
    assert is_not_null(results, ClassPriceRule.courseID) == True

def test_courseClassLevel():
    assert is_not_null(results, ClassPriceRule.courseClassLevel) == True

def test_name():
    assert is_not_null(results, ClassPriceRule.name) == True

def test_price():
    assert is_not_null(results, ClassPriceRule.price) == True

def test_statusCode():
    assert is_not_null(results, ClassPriceRule.statusCode) == True

# def test_hasThisLicenseLevel():
#     assert is_not_null(results, ClassPriceRule.hasThisLicenseLevel) == True

def test_usePriceListItem():
    assert is_not_null(results, ClassPriceRule.usePriceListItem) == True

def test_priceListID():
    assert is_not_null(results, ClassPriceRule.priceListID) == True

def test_displayName():
    assert is_not_null(results, ClassPriceRule.displayName) == True

