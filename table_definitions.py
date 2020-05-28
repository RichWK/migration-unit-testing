from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Float

base = declarative_base()

# Each table we connect to needs to have a class scaffolding it — otherwise SQLAlchemy
# doesn't know what columns it contains.

class ClassPriceRule(base):
    __tablename__ = 'TEMP_CLASS_PRICE_RULE'

    classID = Column(String)
    courseID = Column(String)
    courseClassLevel = Column(Integer)
    name = Column(String)
    price = Column(Integer)
    statusCode = Column(Integer)
    hasThisLicenseLevel = Column(Integer)
    usePriceListItem = Column(Integer)
    priceListID = Column(String)
    displayName = Column(String)

class ClassSession(base):
    __tablename__ = 'TEMP_CLASS_SESSION'

    attendanceGeneratedOn = Column(DateTime)
    classID = Column(String)
    courseID = Column(String)
    courseClassLevel = Column(Integer)
    endDate = Column(DateTime)
    startDate = Column(DateTime)
    statusCode = Column(Integer)
    name = Column(String)
    sessionNumber = Column(Integer)
    classComponentID = Column(String)
    displayName = Column(String)

class Registration(base):
    __tablename__ = 'TEMP_REGISTRATION'

    emailAddress = Column(String)
    alternatePhoneNumber = Column(String)
    cancelOrderID = Column(String)
    cancelOverride = Column(Integer)
    cancelReason = Column(Integer)
    classID = Column(String)
    classPrice = Column(Float)
    contactID = Column(String)
    counter = Column(Integer)
    courseID = Column(String)
    dateAddedToWaitlist = Column(DateTime)
    dateCancelledTransferred = Column(DateTime)
    dateCourseEvalSent = Column(DateTime)
    dateRegistered = Column(DateTime)
    dateRemovedFromWaitList = Column(DateTime)
    contactCourseDetailID = Column(String)
    hold = Column(Integer)
    holdUntil = Column(DateTime)
    isNotABoardMember = Column(Integer)
    name = Column(String)
    orderID = Column(Integer)
    orderProductID = Column(Integer)
    organizationID = Column(String)
    overrideAllowCourseToBeTaken = Column(Integer)
    preClassActivityEmailProcessed = Column(Integer)
    priceRuleID = Column(String)
    regID = Column(String)
    registered = Column(Integer)
    reasonForTaking = Column(Integer)
    registrationSteps = Column(Integer)
    transferFromRegID = Column(Integer)
    transferPending = Column(Integer)
    waitList = Column(Integer)
    waitListStatus = Column(Integer)
    statusReason = Column(Integer)
    classStartDate = Column(DateTime)
    displayName = Column(String)

class ContactCourseDetail(base):
    __tablename__ = 'TEMP_CONTACT_COURSE_DETAIL'

    alignmentDate = Column(DateTime)
    attendaceResult = Column(Integer)
    classID = Column(String)
    completionDate = Column(DateTime)
    contactID = Column(String)
    courseID = Column(String)
    courseResult = Column(Integer)
    deliveryMethod = Column(Integer)
    educationContactRole = Column(Integer)
    name = Column(String)
    noComponentsPassed = Column(Integer)
    providerForThisClassID = Column(String)
    reasonForCourse = Column(Integer)
    registrationID = Column(String)
    resultReason = Column(Integer)
    source = Column(Integer)
    startDate = Column(DateTime)
    statusReason = Column(Integer)
    counter = Column(Integer)
    components = Column(Integer)
    applyCredits = Column(Integer)
    displayName = Column(String)

class RegistrationComponent(base):
    __tablename__ = 'TEMP_REGISTRATION_COMPONENT'

    attendanceResult = Column(Integer)
    classComponentID = Column(String)
    classID = Column(String)
    componentResult = Column(Integer)
    contactCourseDetailID = Column(String)
    contactID = Column(String)
    counterID = Column(Integer)
    dateCompleted = Column(DateTime)
    deliveryMethod = Column(Integer)
    isPassed = Column(Integer)
    markPercent = Column(Float)
    name = Column(String)
    noSessionsAttended = Column(Integer)
    notCompleted = Column(Integer)
    passFailReason = Column(Integer)
    registrationID = Column(String)
    sequence = Column(Integer)
    statusReason = Column(Integer)
    displayName = Column(String)

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

