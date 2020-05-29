from program import *
from table_definitions import *

table = "ClassPriceRule"
results = Connection.session.query(eval(table))
table += "."



# These tests verify there are no null values in each column.

def test_classID():
    assert is_not_null(results, table + "classID") == None

def test_courseID():
    assert is_not_null(results, table + "courseID") == None

def test_courseClassLevel():
    assert is_not_null(results, table + "courseClassLevel") == None

def test_name():
    assert is_not_null(results, table + "name") == None

def test_price():
    assert is_not_null(results, table + "price") == None

def test_statusCode():
    assert is_not_null(results, table + "statusCode") == None

def test_hasThisLicenseLevel():
    assert is_not_null(results, table + "hasThisLicenseLevel") == None

def test_usePriceListItem():
    assert is_not_null(results, table + "usePriceListItem") == None

def test_priceListID():
    assert is_not_null(results, table + "priceListID") == None

def test_displayName():
    assert is_not_null(results, table + "displayName") == None

