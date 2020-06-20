from connections import *
from program import *
from table_definitions import *

scribe_dev1 = SCRIBE_DEV1.session
data = scribe_dev1.query(ComplianceDetail)

def test_duplicates():
    assert duplicates_exist(scribe_dev1, ComplianceDetail.name) == False

# These tests verify that lookups to other entities actually exist in those entities.

def test_compliance_lookup():
    assert missing_from_target(
        ComplianceDetail.complianceID
        ,Compliance.name
        ,scribe_dev1
    ) == 0

# Everything below checks for nulls:

def test_appliedUnits():
    assert is_not_null(data, ComplianceDetail.appliedUnits) == True

def test_completed():
    assert is_not_null(data, ComplianceDetail.completed) == True

def test_complianceID():
    assert is_not_null(data, ComplianceDetail.complianceID) == True

def test_name():
    assert is_not_null(data, ComplianceDetail.name) == True

def test_pending():
    assert is_not_null(data, ComplianceDetail.pending) == True

def test_programAccreditationID():
    assert is_not_null(data, ComplianceDetail.programAccreditationID) == True

def test_unitType():
    assert is_not_null(data, ComplianceDetail.unitType) == True

def test_statusCode():
    assert is_not_null(data, ComplianceDetail.statusCode) == True

def test_displayName():
    assert is_not_null(data, ComplianceDetail.displayName) == True

