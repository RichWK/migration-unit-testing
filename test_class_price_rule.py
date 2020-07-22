from connections import *
from program import *
from table_definitions import *

scribe_dev1 = SCRIBE_DEV1.session
data = scribe_dev1.query(ClassPriceRule)

def test_duplicates():
    assert duplicates_exist(scribe_dev1, ClassPriceRule.name) == False

# These tests verify that lookups to other entities actually exist in those entities.

def test_class_lookup():
    assert missing_from_target(
        ClassPriceRule.classID
        ,Class.mmsiClassCode
        ,scribe_dev1
        ,EventsClass.mmsiClassCode
    ) == 0

def test_course_lookup():
    assert missing_from_target(
        ClassPriceRule.courseID
        ,Course.name
        ,scribe_dev1
    ) == 0

# These tests verify there are no null values for these columns.

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

