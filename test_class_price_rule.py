from program import *
from table_definitions import *

table = "ClassPriceRule"
results = Connection.session.query(eval(table))
table += "."



# These tests verify there are no null values in each column.

def test_classID():
    assert check_for_null(results, table + "classID") == None

def test_courseID():
    assert check_for_null(results, table + "courseID") == None

def test_courseClassLevel():
    assert check_for_null(results, table + "courseClassLevel") == None

def test_name():
    assert check_for_null(results, table + "name") == None

def test_price():
    assert check_for_null(results, table + "price") == None

def test_statusCode():
    assert check_for_null(results, table + "statusCode") == None

def test_hasThisLicenseLevel():
    assert check_for_null(results, table + "hasThisLicenseLevel") == None

def test_usePriceListItem():
    assert check_for_null(results, table + "usePriceListItem") == None

def test_priceListID():
    assert check_for_null(results, table + "priceListID") == None

def test_displayName():
    assert check_for_null(results, table + "displayName") == None

