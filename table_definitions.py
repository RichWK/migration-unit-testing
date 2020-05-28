from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

base = declarative_base()

# Each table we connect to needs to have a class scaffolding it.
# You only need to define the columns that you need.

class ClassPriceRule(base):
    __tablename__ = 'TEMP_CLASS_PRICE_RULE'

class ClassSession(base):
    __tablename__ = 'TEMP_CLASS_SESSION'

class Registration(base):
    __tablename__ = 'TEMP_REGISTRATION'

class ContactCourseDetail(base):
    __tablename__ = 'TEMP_CONTACT_COURSE_DETAIL'

class RegistrationComponent(base):
    __tablename__ = 'TEMP_REGISTRATION_COMPONENT'

class ClassAttendance(base):
    __tablename__ = 'TEMP_CLASS_ATTENDANCE'

class ClassAttendanceLog(base):
    __tablename__ = 'TEMP_CLASS_ATTENDANCE_LOG'

class EducationHistory(base):
    __tablename__ = 'TEMP_EDUCATION_HISTORY'

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

