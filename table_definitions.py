from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Float

base = declarative_base()

# Each table being connected to needs a class which scaffolds it — otherwise SQLAlchemy
# can't tell what columns it contains.

class Class(base):
    __tablename__ = 'CLASS'

    allowRegistrationWithoutOrder = Column(Integer)
    classInstanceNumber = Column(Integer)
    courseID = Column(String)
    dateOpenForRegistration = Column(DateTime)
    deliveryMethod = Column(Integer)
    education = Column(Integer)
    endDate = Column(DateTime)
    eventCourse = Column(Integer)
    guestsAllowed = Column(Integer)
    instructorID = Column(String)
    maxAttendance = Column(Integer)
    maxNonBoardMembers = Column(Integer)
    minAttendance = Column(Integer)
    mmsiClassCode = Column(String, primary_key=True)
    name = Column(String)
    noComponents = Column(Integer)
    noComponentsNotCompleted = Column(Integer)
    noGuestSeatsTaken = Column(Integer)
    noGuestsAllowed = Column(Integer)
    noNonBoardMembersRegistered = Column(Integer)
    noRegistered = Column(Integer)
    registrationDeadline = Column(DateTime)
    reminderDateForClassContacts = Column(DateTime)
    restrictWhoCanTakeCourse = Column(Integer)
    ruleCancelDays = Column(Integer)
    ruleRegistrationDays = Column(Integer)
    sellOnWeb = Column(Integer)
    startDate = Column(DateTime)
    statusCode = Column(Integer)
    venueID = Column(String)
    viewOnWeb = Column(Integer)

class ClassAttendance(base):
    __tablename__ = 'CLASS_ATTENDANCE'

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
    __tablename__ = 'CLASS_ATTENDANCE_LOG'

    checkInOut = Column(Integer)
    checkInOutDateTime = Column(DateTime)
    classSessionID = Column(String)
    contactID = Column(String)
    name = Column(String, primary_key=True)
    classAttendanceID = Column(String)
    statusCode = Column(Integer)
    displayName = Column(String)

class ClassContact(base):
    __tablename__ = 'CLASS_CONTACT'

    classID = Column(String)
    contactID = Column(String)
    courseContactID = Column(String)
    courseID = Column(String)
    courseContactID = Column(String)
    name = Column(String, primary_key=True)
    roleForThisClass = Column(String)
    displayName = Column(String)

class ClassPriceRule(base):
    __tablename__ = 'CLASS_PRICE_RULE'

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
    __tablename__ = 'CLASS_SESSION'

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

class Compliance(base):
    __tablename__ = 'COMPLIANCE'

    name = Column(String, primary_key=True)

class ComplianceDetail(base):
    __tablename__ = 'COMPLIANCE_DETAIL'

    appliedUnits = Column(Integer)
    completed = Column(Integer)
    complianceID = Column(String)
    name = Column(String, primary_key=True)
    pending = Column(Integer)
    programAccreditationID = Column(String)
    unitType = Column(Integer)
    statusCode = Column(Integer)
    displayName = Column(String)

class ContactCourseDetail(base):
    __tablename__ = 'CONTACT_COURSE_DETAIL'

    alignmentDate = Column(DateTime)
    attendanceResult = Column(Integer)
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
    displayName = Column(String)
    externalCourseName = Column(String)

class Course(base):
    __tablename__ = 'COURSE'

    name = Column(String, primary_key=True)

class CourseAccreditation(base):
    __tablename__ = 'COURSE_ACCREDITATION'

    courseID = Column(String)
    name = Column(String, primary_key=True)

class CourseComponent(base):
    __tablename__ = 'COURSE_COMPONENT'

    classID = Column(String)
    courseID = Column(String)
    displayName = Column(String, primary_key=True)

class CourseContact(base):
    __tablename__ = 'COURSE_CONTACT'

    courseID = Column(String)
    name = Column(String, primary_key=True)

class CourseEducationProvider(base):
    __tablename__ = 'COURSE_EDUCATION_PROVIDER'

    courseID = Column(String)
    name = Column(String, primary_key=True)

class CourseRestriction(base):
    __tablename__ = 'COURSE_RESTRICTION'

    classID = Column(String)
    courseID = Column(String)
    name = Column(String, primary_key=True)

class EducationHistory(base):
    __tablename__ = 'EDUCATION_HISTORY'

    accredUnitType = Column(Integer)
    completedCourseUnits = Column(Integer)
    complianceDetailID = Column(String)
    complianceID = Column(String)
    contactID = Column(String)
    courseAccreditationID = Column(String)
    courseID = Column(String)
    courseUnits = Column(Float)
    eduHistoryID = Column(String)
    name = Column(String, primary_key=True)
    programAccreditationID = Column(String)
    programIterationID = Column(String)
    statusReason = Column(Integer)
    displayName = Column(String)
    applied = Column(Integer)
    applyCredits = Column(Integer)
    pending = Column(Integer)

class EventsClass(base):
    __tablename__ = 'EVENTS_CLASS'

    courseID = Column(String)
    mmsiClassCode = Column(String, primary_key=True)
    venueID = Column(String)

class NonComplianceNotification(base):
    __tablename__ = 'NON_COMPLIANCE_NOTIFICATION'

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

class Order(base):
    __tablename__ = 'ORDER'

    orderNo = Column(String, primary_key=True)

class OrderProduct(base):
    __tablename__ = 'ORDER_PRODUCT'

    classID = Column(String, primary_key=True)
    orderID = Column(String, primary_key=True)

class Registration(base):
    __tablename__ = 'REGISTRATION'

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

class RegistrationComponent(base):
    __tablename__ = 'REGISTRATION_COMPONENT'

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

class Venue(base):
    __tablename__ = 'VENUE'

    name = Column(String, primary_key=True)

