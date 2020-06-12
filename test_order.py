from connections import *
from program import *
from table_definitions import *

scribe_dev1 = SCRIBE_DEV1.session

# These tests verify that lookups to other entities actually exist in those entities.

def test_order_lookup():
    assert missing_from_target(Order.orderNo, Registration.orderID, scribe_dev1) == 0

