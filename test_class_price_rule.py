from connections import *
from program import *
from table_definitions import *

mmsimigration = MMSIMIGRATION.session
data = mmsimigration.query(ClassPriceRule)

def test_duplicates():
    assert duplicates_exist(mmsimigration, ClassPriceRule.name) == False

# These tests verify there are no null values for these columns.

def test_classID():
    assert is_not_null(data, ClassPriceRule.classID) == True

def test_courseID():
    assert is_not_null(data, ClassPriceRule.courseID) == True

def test_courseClassLevel():
    assert is_not_null(data, ClassPriceRule.courseClassLevel) == True

def test_name():
    assert is_not_null(data, ClassPriceRule.name) == True

def test_price():
    assert is_not_null(data, ClassPriceRule.price) == True

def test_statusCode():
    assert is_not_null(data, ClassPriceRule.statusCode) == True

def test_usePriceListItem():
    assert is_not_null(data, ClassPriceRule.usePriceListItem) == True

def test_priceListID():
    assert is_not_null(data, ClassPriceRule.priceListID) == True

def test_displayName():
    assert is_not_null(data, ClassPriceRule.displayName) == True

