from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

base = declarative_base()

# Each table we connect to needs to have a class scaffolding it.
# You only need to define the columns that you need.

class NonComplianceNotification(base):
    __tablename__ = 'TEMP_NON_COMPLIANCE_NOTIFICATION'

    comment = Column(String)
    complianceID = Column(String)
    contactID = Column(String)
    name = Column(String, primary_key=True)
    nonComplianceRule = Column(String)
    notificationDate = Column(DateTime)
    notificationIssue = Column(Integer)
    stateCode = Column(Integer)
    statuReason = Column(Integer)
    displayName = Column(Integer)

