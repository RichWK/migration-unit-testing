from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Float

base = declarative_base()

# Each table we connect to needs to have a class which scaffolds it — otherwise
# SQLAlchemy doesn't know what columns it contains.

# These are ordered according to the sequence they need to be inserted into Dynamics.

class ClassPriceRule(base):
    __tablename__ = 'TEMP_CLASS_PRICE_RULE'

    classID = Column(String)
    courseID = Column(String)
    courseClassLevel = Column(Integer)
    name = Column(String, primary_key=True)
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
    name = Column(String, primary_key=True)
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
    name = Column(String, primary_key=True)
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
    name = Column(String, primary_key=True)
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
    name = Column(String, primary_key=True)
    noSessionsAttended = Column(Integer)
    notCompleted = Column(Integer)
    passFailReason = Column(Integer)
    registrationID = Column(String)
    sequence = Column(Integer)
    statusReason = Column(Integer)
    displayName = Column(String)

class ClassAttendance(base):
    __tablename__ = 'TEMP_CLASS_ATTENDANCE'

    reason = Column(Integer)
    passed = Column(Integer)
    checkInDate = Column(DateTime)
    checkOutDate = Column(DateTime)
    classID = Column(String)
    classSessionID = Column(String)
    contactID = Column(String)
    statusReason = Column(Integer)
    name = Column(String, primary_key=True)
    attendanceNote = Column(String)
    registrationComponent = Column(String)
    registration = Column(String)
    displayName = Column(String)

class ClassAttendanceLog(base):
    __tablename__ = 'TEMP_CLASS_ATTENDANCE_LOG'

    checkInOut = Column(Integer)
    checkInOutDateTime = Column(DateTime)
    classSessionID = Column(String)
    contactID = Column(String)
    name = Column(String)
    classAttendanceID = Column(String)
    statusCode = Column(Integer)
    displayName = Column(String)

class EducationHistory(base):
    __tablename__ = 'TEMP_EDUCATION_HISTORY'

    accredUnitType = Column(Integer)
    completedCourseUnits = Column(Integer)
    complianceDetailID = Column(String)
    complianceID = Column(String)
    contactID = Column(String)
    courseAccreditationID = Column(String)
    courseID = Column(String)
    courseUnits = Column(Float)
    eduHistoryID = Column(String)
    name = Column(String)
    programAccreditationID = Column(String)
    programIterationID = Column(String)
    statusReason = Column(Integer)
    displayName = Column(String)
    applied = Column(Integer)
    applyCredits = Column(Integer)
    pending = Column(Integer)

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

