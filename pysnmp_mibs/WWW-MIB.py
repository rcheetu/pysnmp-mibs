# PySNMP SMI module. Autogenerated from smidump -f python WWW-MIB
# by libsmi2pysnmp-0.0.5-alpha at Fri Oct 28 00:30:55 2005,
# Python version (2, 4, 0, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Counter32, Counter64, Integer32, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, TimeTicks, Unsigned32, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "TimeTicks", "Unsigned32", "mib-2")
( DateAndTime, DisplayString, TextualConvention, TimeInterval, ) = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "DisplayString", "TextualConvention", "TimeInterval")
( Utf8String, ) = mibBuilder.importSymbols("SYSAPPL-MIB", "Utf8String")

# Types

class WwwDocName(TextualConvention, OctetString):
    subtypeSpec = OctetString.subtypeSpec+constraint.ValueSizeConstraint(0,255)
    pass

class WwwOperStatus(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(3,1,2,5,4,)
    namedValues = namedval.NamedValues(("down", 1), ("running", 2), ("halted", 3), ("congested", 4), ("restarting", 5), )
    pass

class WwwRequestType(OctetString):
    subtypeSpec = OctetString.subtypeSpec+constraint.ValueSizeConstraint(1,40)
    pass

class WwwResponseType(Integer32):
    subtypeSpec = Integer32.subtypeSpec+constraint.ValueRangeConstraint(0,2147483647L)
    pass


# Objects

wwwMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 65))
wwwMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 65, 1))
wwwService = MibIdentifier((1, 3, 6, 1, 2, 1, 65, 1, 1))
wwwServiceTable = MibTable((1, 3, 6, 1, 2, 1, 65, 1, 1, 1))
wwwServiceEntry = MibTableRow((1, 3, 6, 1, 2, 1, 65, 1, 1, 1, 1)).setIndexNames((0, "WWW-MIB", "wwwServiceIndex"))
wwwServiceIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 65, 1, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 4294967295L))).setMaxAccess("noaccess")
wwwServiceDescription = MibTableColumn((1, 3, 6, 1, 2, 1, 65, 1, 1, 1, 1, 2), Utf8String()).setMaxAccess("readonly")
wwwServiceContact = MibTableColumn((1, 3, 6, 1, 2, 1, 65, 1, 1, 1, 1, 3), Utf8String()).setMaxAccess("readonly")
wwwServiceProtocol = MibTableColumn((1, 3, 6, 1, 2, 1, 65, 1, 1, 1, 1, 4), ObjectIdentifier()).setMaxAccess("readonly")
wwwServiceName = MibTableColumn((1, 3, 6, 1, 2, 1, 65, 1, 1, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
wwwServiceType = MibTableColumn((1, 3, 6, 1, 2, 1, 65, 1, 1, 1, 1, 6), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(3,4,5,2,1,)).subtype(namedValues=namedval.NamedValues(("wwwOther", 1), ("wwwServer", 2), ("wwwClient", 3), ("wwwProxy", 4), ("wwwCachingProxy", 5), ))).setMaxAccess("readonly")
wwwServiceStartTime = MibTableColumn((1, 3, 6, 1, 2, 1, 65, 1, 1, 1, 1, 7), DateAndTime()).setMaxAccess("readonly")
wwwServiceOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 65, 1, 1, 1, 1, 8), WwwOperStatus()).setMaxAccess("readonly")
wwwServiceLastChange = MibTableColumn((1, 3, 6, 1, 2, 1, 65, 1, 1, 1, 1, 9), DateAndTime()).setMaxAccess("readonly")
wwwProtocolStatistics = MibIdentifier((1, 3, 6, 1, 2, 1, 65, 1, 2))
wwwSummaryTable = MibTable((1, 3, 6, 1, 2, 1, 65, 1, 2, 1))
wwwSummaryEntry = MibTableRow((1, 3, 6, 1, 2, 1, 65, 1, 2, 1, 1)).setIndexNames((0, "WWW-MIB", "wwwServiceIndex"))
wwwSummaryInRequests = MibTableColumn((1, 3, 6, 1, 2, 1, 65, 1, 2, 1, 1, 1), Counter32()).setMaxAccess("readonly")
wwwSummaryOutRequests = MibTableColumn((1, 3, 6, 1, 2, 1, 65, 1, 2, 1, 1, 2), Counter32()).setMaxAccess("readonly")
wwwSummaryInResponses = MibTableColumn((1, 3, 6, 1, 2, 1, 65, 1, 2, 1, 1, 3), Counter32()).setMaxAccess("readonly")
wwwSummaryOutResponses = MibTableColumn((1, 3, 6, 1, 2, 1, 65, 1, 2, 1, 1, 4), Counter32()).setMaxAccess("readonly")
wwwSummaryInBytes = MibTableColumn((1, 3, 6, 1, 2, 1, 65, 1, 2, 1, 1, 5), Counter64()).setMaxAccess("readonly")
wwwSummaryInLowBytes = MibTableColumn((1, 3, 6, 1, 2, 1, 65, 1, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
wwwSummaryOutBytes = MibTableColumn((1, 3, 6, 1, 2, 1, 65, 1, 2, 1, 1, 7), Counter64()).setMaxAccess("readonly")
wwwSummaryOutLowBytes = MibTableColumn((1, 3, 6, 1, 2, 1, 65, 1, 2, 1, 1, 8), Counter32()).setMaxAccess("readonly")
wwwRequestInTable = MibTable((1, 3, 6, 1, 2, 1, 65, 1, 2, 2))
wwwRequestInEntry = MibTableRow((1, 3, 6, 1, 2, 1, 65, 1, 2, 2, 1)).setIndexNames((0, "WWW-MIB", "wwwServiceIndex"), (0, "WWW-MIB", "wwwRequestInIndex"))
wwwRequestInIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 65, 1, 2, 2, 1, 1), WwwRequestType()).setMaxAccess("noaccess")
wwwRequestInRequests = MibTableColumn((1, 3, 6, 1, 2, 1, 65, 1, 2, 2, 1, 2), Counter32()).setMaxAccess("readonly")
wwwRequestInBytes = MibTableColumn((1, 3, 6, 1, 2, 1, 65, 1, 2, 2, 1, 3), Counter32()).setMaxAccess("readonly")
wwwRequestInLastTime = MibTableColumn((1, 3, 6, 1, 2, 1, 65, 1, 2, 2, 1, 4), DateAndTime()).setMaxAccess("readonly")
wwwRequestOutTable = MibTable((1, 3, 6, 1, 2, 1, 65, 1, 2, 3))
wwwRequestOutEntry = MibTableRow((1, 3, 6, 1, 2, 1, 65, 1, 2, 3, 1)).setIndexNames((0, "WWW-MIB", "wwwServiceIndex"), (0, "WWW-MIB", "wwwRequestOutIndex"))
wwwRequestOutIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 65, 1, 2, 3, 1, 1), WwwRequestType()).setMaxAccess("noaccess")
wwwRequestOutRequests = MibTableColumn((1, 3, 6, 1, 2, 1, 65, 1, 2, 3, 1, 2), Counter32()).setMaxAccess("readonly")
wwwRequestOutBytes = MibTableColumn((1, 3, 6, 1, 2, 1, 65, 1, 2, 3, 1, 3), Counter32()).setMaxAccess("readonly")
wwwRequestOutLastTime = MibTableColumn((1, 3, 6, 1, 2, 1, 65, 1, 2, 3, 1, 4), DateAndTime()).setMaxAccess("readonly")
wwwResponseInTable = MibTable((1, 3, 6, 1, 2, 1, 65, 1, 2, 4))
wwwResponseInEntry = MibTableRow((1, 3, 6, 1, 2, 1, 65, 1, 2, 4, 1)).setIndexNames((0, "WWW-MIB", "wwwServiceIndex"), (0, "WWW-MIB", "wwwResponseInIndex"))
wwwResponseInIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 65, 1, 2, 4, 1, 1), WwwResponseType()).setMaxAccess("noaccess")
wwwResponseInResponses = MibTableColumn((1, 3, 6, 1, 2, 1, 65, 1, 2, 4, 1, 2), Counter32()).setMaxAccess("readonly")
wwwResponseInBytes = MibTableColumn((1, 3, 6, 1, 2, 1, 65, 1, 2, 4, 1, 3), Counter32()).setMaxAccess("readonly")
wwwResponseInLastTime = MibTableColumn((1, 3, 6, 1, 2, 1, 65, 1, 2, 4, 1, 4), DateAndTime()).setMaxAccess("readonly")
wwwResponseOutTable = MibTable((1, 3, 6, 1, 2, 1, 65, 1, 2, 5))
wwwResponseOutEntry = MibTableRow((1, 3, 6, 1, 2, 1, 65, 1, 2, 5, 1)).setIndexNames((0, "WWW-MIB", "wwwServiceIndex"), (0, "WWW-MIB", "wwwResponseOutIndex"))
wwwResponseOutIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 65, 1, 2, 5, 1, 1), WwwResponseType()).setMaxAccess("noaccess")
wwwResponseOutResponses = MibTableColumn((1, 3, 6, 1, 2, 1, 65, 1, 2, 5, 1, 2), Counter32()).setMaxAccess("readonly")
wwwResponseOutBytes = MibTableColumn((1, 3, 6, 1, 2, 1, 65, 1, 2, 5, 1, 3), Counter32()).setMaxAccess("readonly")
wwwResponseOutLastTime = MibTableColumn((1, 3, 6, 1, 2, 1, 65, 1, 2, 5, 1, 4), DateAndTime()).setMaxAccess("readonly")
wwwDocumentStatistics = MibIdentifier((1, 3, 6, 1, 2, 1, 65, 1, 3))
wwwDocCtrlTable = MibTable((1, 3, 6, 1, 2, 1, 65, 1, 3, 1))
wwwDocCtrlEntry = MibTableRow((1, 3, 6, 1, 2, 1, 65, 1, 3, 1, 1)).setIndexNames((0, "WWW-MIB", "wwwServiceIndex"))
wwwDocCtrlLastNSize = MibTableColumn((1, 3, 6, 1, 2, 1, 65, 1, 3, 1, 1, 1), Unsigned32()).setMaxAccess("readwrite")
wwwDocCtrlLastNLock = MibTableColumn((1, 3, 6, 1, 2, 1, 65, 1, 3, 1, 1, 2), TimeTicks()).setMaxAccess("readwrite")
wwwDocCtrlBuckets = MibTableColumn((1, 3, 6, 1, 2, 1, 65, 1, 3, 1, 1, 3), Unsigned32()).setMaxAccess("readwrite")
wwwDocCtrlBucketTimeInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 65, 1, 3, 1, 1, 4), TimeInterval()).setMaxAccess("readwrite")
wwwDocCtrlTopNSize = MibTableColumn((1, 3, 6, 1, 2, 1, 65, 1, 3, 1, 1, 5), Unsigned32()).setMaxAccess("readwrite")
wwwDocLastNTable = MibTable((1, 3, 6, 1, 2, 1, 65, 1, 3, 2))
wwwDocLastNEntry = MibTableRow((1, 3, 6, 1, 2, 1, 65, 1, 3, 2, 1)).setIndexNames((0, "WWW-MIB", "wwwServiceIndex"), (0, "WWW-MIB", "wwwDocLastNIndex"))
wwwDocLastNIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 65, 1, 3, 2, 1, 1), Unsigned32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 4294967295L))).setMaxAccess("noaccess")
wwwDocLastNName = MibTableColumn((1, 3, 6, 1, 2, 1, 65, 1, 3, 2, 1, 2), WwwDocName()).setMaxAccess("readonly")
wwwDocLastNTimeStamp = MibTableColumn((1, 3, 6, 1, 2, 1, 65, 1, 3, 2, 1, 3), DateAndTime()).setMaxAccess("readonly")
wwwDocLastNRequestType = MibTableColumn((1, 3, 6, 1, 2, 1, 65, 1, 3, 2, 1, 4), WwwRequestType()).setMaxAccess("readonly")
wwwDocLastNResponseType = MibTableColumn((1, 3, 6, 1, 2, 1, 65, 1, 3, 2, 1, 5), WwwResponseType()).setMaxAccess("readonly")
wwwDocLastNStatusMsg = MibTableColumn((1, 3, 6, 1, 2, 1, 65, 1, 3, 2, 1, 6), Utf8String()).setMaxAccess("readonly")
wwwDocLastNBytes = MibTableColumn((1, 3, 6, 1, 2, 1, 65, 1, 3, 2, 1, 7), Unsigned32()).setMaxAccess("readonly")
wwwDocBucketTable = MibTable((1, 3, 6, 1, 2, 1, 65, 1, 3, 3))
wwwDocBucketEntry = MibTableRow((1, 3, 6, 1, 2, 1, 65, 1, 3, 3, 1)).setIndexNames((0, "WWW-MIB", "wwwServiceIndex"), (0, "WWW-MIB", "wwwDocBucketIndex"))
wwwDocBucketIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 65, 1, 3, 3, 1, 1), Unsigned32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 4294967295L))).setMaxAccess("noaccess")
wwwDocBucketTimeStamp = MibTableColumn((1, 3, 6, 1, 2, 1, 65, 1, 3, 3, 1, 2), DateAndTime()).setMaxAccess("readonly")
wwwDocBucketAccesses = MibTableColumn((1, 3, 6, 1, 2, 1, 65, 1, 3, 3, 1, 3), Unsigned32()).setMaxAccess("readonly")
wwwDocBucketDocuments = MibTableColumn((1, 3, 6, 1, 2, 1, 65, 1, 3, 3, 1, 4), Unsigned32()).setMaxAccess("readonly")
wwwDocBucketBytes = MibTableColumn((1, 3, 6, 1, 2, 1, 65, 1, 3, 3, 1, 5), Unsigned32()).setMaxAccess("readonly")
wwwDocAccessTopNTable = MibTable((1, 3, 6, 1, 2, 1, 65, 1, 3, 4))
wwwDocAccessTopNEntry = MibTableRow((1, 3, 6, 1, 2, 1, 65, 1, 3, 4, 1)).setIndexNames((0, "WWW-MIB", "wwwServiceIndex"), (0, "WWW-MIB", "wwwDocBucketIndex"), (0, "WWW-MIB", "wwwDocAccessTopNIndex"))
wwwDocAccessTopNIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 65, 1, 3, 4, 1, 1), Unsigned32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 4294967295L))).setMaxAccess("noaccess")
wwwDocAccessTopNName = MibTableColumn((1, 3, 6, 1, 2, 1, 65, 1, 3, 4, 1, 2), WwwDocName()).setMaxAccess("readonly")
wwwDocAccessTopNAccesses = MibTableColumn((1, 3, 6, 1, 2, 1, 65, 1, 3, 4, 1, 3), Unsigned32()).setMaxAccess("readonly")
wwwDocAccessTopNBytes = MibTableColumn((1, 3, 6, 1, 2, 1, 65, 1, 3, 4, 1, 4), Unsigned32()).setMaxAccess("readonly")
wwwDocAccessTopNLastResponseType = MibTableColumn((1, 3, 6, 1, 2, 1, 65, 1, 3, 4, 1, 5), WwwResponseType()).setMaxAccess("readonly")
wwwDocBytesTopNTable = MibTable((1, 3, 6, 1, 2, 1, 65, 1, 3, 5))
wwwDocBytesTopNEntry = MibTableRow((1, 3, 6, 1, 2, 1, 65, 1, 3, 5, 1)).setIndexNames((0, "WWW-MIB", "wwwServiceIndex"), (0, "WWW-MIB", "wwwDocBucketIndex"), (0, "WWW-MIB", "wwwDocBytesTopNIndex"))
wwwDocBytesTopNIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 65, 1, 3, 5, 1, 1), Unsigned32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 4294967295L))).setMaxAccess("noaccess")
wwwDocBytesTopNName = MibTableColumn((1, 3, 6, 1, 2, 1, 65, 1, 3, 5, 1, 2), WwwDocName()).setMaxAccess("readonly")
wwwDocBytesTopNAccesses = MibTableColumn((1, 3, 6, 1, 2, 1, 65, 1, 3, 5, 1, 3), Unsigned32()).setMaxAccess("readonly")
wwwDocBytesTopNBytes = MibTableColumn((1, 3, 6, 1, 2, 1, 65, 1, 3, 5, 1, 4), Unsigned32()).setMaxAccess("readonly")
wwwDocBytesTopNLastResponseType = MibTableColumn((1, 3, 6, 1, 2, 1, 65, 1, 3, 5, 1, 5), WwwResponseType()).setMaxAccess("readonly")
wwwMIBConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 65, 2))
wwwMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 65, 2, 1))
wwwMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 65, 2, 2))

# Augmentions

# Groups

wwwSummaryGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 65, 2, 2, 2)).setObjects(("WWW-MIB", "wwwSummaryInLowBytes"), ("WWW-MIB", "wwwSummaryOutLowBytes"), ("WWW-MIB", "wwwSummaryInRequests"), ("WWW-MIB", "wwwSummaryInBytes"), ("WWW-MIB", "wwwSummaryInResponses"), ("WWW-MIB", "wwwSummaryOutResponses"), ("WWW-MIB", "wwwSummaryOutBytes"), ("WWW-MIB", "wwwSummaryOutRequests"), )
wwwResponseOutGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 65, 2, 2, 6)).setObjects(("WWW-MIB", "wwwResponseOutLastTime"), ("WWW-MIB", "wwwResponseOutBytes"), ("WWW-MIB", "wwwResponseOutResponses"), )
wwwResponseInGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 65, 2, 2, 5)).setObjects(("WWW-MIB", "wwwResponseInResponses"), ("WWW-MIB", "wwwResponseInBytes"), ("WWW-MIB", "wwwResponseInLastTime"), )
wwwDocumentGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 65, 2, 2, 7)).setObjects(("WWW-MIB", "wwwDocLastNRequestType"), ("WWW-MIB", "wwwDocLastNResponseType"), ("WWW-MIB", "wwwDocBytesTopNAccesses"), ("WWW-MIB", "wwwDocLastNStatusMsg"), ("WWW-MIB", "wwwDocBucketDocuments"), ("WWW-MIB", "wwwDocLastNTimeStamp"), ("WWW-MIB", "wwwDocLastNName"), ("WWW-MIB", "wwwDocCtrlLastNSize"), ("WWW-MIB", "wwwDocAccessTopNLastResponseType"), ("WWW-MIB", "wwwDocAccessTopNName"), ("WWW-MIB", "wwwDocBytesTopNLastResponseType"), ("WWW-MIB", "wwwDocLastNBytes"), ("WWW-MIB", "wwwDocCtrlBuckets"), ("WWW-MIB", "wwwDocCtrlTopNSize"), ("WWW-MIB", "wwwDocCtrlBucketTimeInterval"), ("WWW-MIB", "wwwDocBucketAccesses"), ("WWW-MIB", "wwwDocAccessTopNAccesses"), ("WWW-MIB", "wwwDocBytesTopNName"), ("WWW-MIB", "wwwDocCtrlLastNLock"), ("WWW-MIB", "wwwDocAccessTopNBytes"), ("WWW-MIB", "wwwDocBytesTopNBytes"), ("WWW-MIB", "wwwDocBucketTimeStamp"), ("WWW-MIB", "wwwDocBucketBytes"), )
wwwRequestOutGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 65, 2, 2, 4)).setObjects(("WWW-MIB", "wwwRequestOutBytes"), ("WWW-MIB", "wwwRequestOutLastTime"), ("WWW-MIB", "wwwRequestOutRequests"), )
wwwServiceGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 65, 2, 2, 1)).setObjects(("WWW-MIB", "wwwServiceStartTime"), ("WWW-MIB", "wwwServiceProtocol"), ("WWW-MIB", "wwwServiceOperStatus"), ("WWW-MIB", "wwwServiceContact"), ("WWW-MIB", "wwwServiceName"), ("WWW-MIB", "wwwServiceType"), ("WWW-MIB", "wwwServiceDescription"), ("WWW-MIB", "wwwServiceLastChange"), )
wwwRequestInGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 65, 2, 2, 3)).setObjects(("WWW-MIB", "wwwRequestInLastTime"), ("WWW-MIB", "wwwRequestInRequests"), ("WWW-MIB", "wwwRequestInBytes"), )

# Exports

# Types
mibBuilder.exportSymbols("WWW-MIB", WwwDocName=WwwDocName, WwwOperStatus=WwwOperStatus, WwwRequestType=WwwRequestType, WwwResponseType=WwwResponseType)

# Objects
mibBuilder.exportSymbols("WWW-MIB", wwwMIB=wwwMIB, wwwMIBObjects=wwwMIBObjects, wwwService=wwwService, wwwServiceTable=wwwServiceTable, wwwServiceEntry=wwwServiceEntry, wwwServiceIndex=wwwServiceIndex, wwwServiceDescription=wwwServiceDescription, wwwServiceContact=wwwServiceContact, wwwServiceProtocol=wwwServiceProtocol, wwwServiceName=wwwServiceName, wwwServiceType=wwwServiceType, wwwServiceStartTime=wwwServiceStartTime, wwwServiceOperStatus=wwwServiceOperStatus, wwwServiceLastChange=wwwServiceLastChange, wwwProtocolStatistics=wwwProtocolStatistics, wwwSummaryTable=wwwSummaryTable, wwwSummaryEntry=wwwSummaryEntry, wwwSummaryInRequests=wwwSummaryInRequests, wwwSummaryOutRequests=wwwSummaryOutRequests, wwwSummaryInResponses=wwwSummaryInResponses, wwwSummaryOutResponses=wwwSummaryOutResponses, wwwSummaryInBytes=wwwSummaryInBytes, wwwSummaryInLowBytes=wwwSummaryInLowBytes, wwwSummaryOutBytes=wwwSummaryOutBytes, wwwSummaryOutLowBytes=wwwSummaryOutLowBytes, wwwRequestInTable=wwwRequestInTable, wwwRequestInEntry=wwwRequestInEntry, wwwRequestInIndex=wwwRequestInIndex, wwwRequestInRequests=wwwRequestInRequests, wwwRequestInBytes=wwwRequestInBytes, wwwRequestInLastTime=wwwRequestInLastTime, wwwRequestOutTable=wwwRequestOutTable, wwwRequestOutEntry=wwwRequestOutEntry, wwwRequestOutIndex=wwwRequestOutIndex, wwwRequestOutRequests=wwwRequestOutRequests, wwwRequestOutBytes=wwwRequestOutBytes, wwwRequestOutLastTime=wwwRequestOutLastTime, wwwResponseInTable=wwwResponseInTable, wwwResponseInEntry=wwwResponseInEntry, wwwResponseInIndex=wwwResponseInIndex, wwwResponseInResponses=wwwResponseInResponses, wwwResponseInBytes=wwwResponseInBytes, wwwResponseInLastTime=wwwResponseInLastTime, wwwResponseOutTable=wwwResponseOutTable, wwwResponseOutEntry=wwwResponseOutEntry, wwwResponseOutIndex=wwwResponseOutIndex, wwwResponseOutResponses=wwwResponseOutResponses, wwwResponseOutBytes=wwwResponseOutBytes, wwwResponseOutLastTime=wwwResponseOutLastTime, wwwDocumentStatistics=wwwDocumentStatistics, wwwDocCtrlTable=wwwDocCtrlTable, wwwDocCtrlEntry=wwwDocCtrlEntry, wwwDocCtrlLastNSize=wwwDocCtrlLastNSize, wwwDocCtrlLastNLock=wwwDocCtrlLastNLock, wwwDocCtrlBuckets=wwwDocCtrlBuckets, wwwDocCtrlBucketTimeInterval=wwwDocCtrlBucketTimeInterval, wwwDocCtrlTopNSize=wwwDocCtrlTopNSize, wwwDocLastNTable=wwwDocLastNTable, wwwDocLastNEntry=wwwDocLastNEntry, wwwDocLastNIndex=wwwDocLastNIndex, wwwDocLastNName=wwwDocLastNName, wwwDocLastNTimeStamp=wwwDocLastNTimeStamp, wwwDocLastNRequestType=wwwDocLastNRequestType, wwwDocLastNResponseType=wwwDocLastNResponseType, wwwDocLastNStatusMsg=wwwDocLastNStatusMsg, wwwDocLastNBytes=wwwDocLastNBytes, wwwDocBucketTable=wwwDocBucketTable, wwwDocBucketEntry=wwwDocBucketEntry, wwwDocBucketIndex=wwwDocBucketIndex, wwwDocBucketTimeStamp=wwwDocBucketTimeStamp, wwwDocBucketAccesses=wwwDocBucketAccesses, wwwDocBucketDocuments=wwwDocBucketDocuments, wwwDocBucketBytes=wwwDocBucketBytes, wwwDocAccessTopNTable=wwwDocAccessTopNTable, wwwDocAccessTopNEntry=wwwDocAccessTopNEntry, wwwDocAccessTopNIndex=wwwDocAccessTopNIndex, wwwDocAccessTopNName=wwwDocAccessTopNName, wwwDocAccessTopNAccesses=wwwDocAccessTopNAccesses, wwwDocAccessTopNBytes=wwwDocAccessTopNBytes, wwwDocAccessTopNLastResponseType=wwwDocAccessTopNLastResponseType, wwwDocBytesTopNTable=wwwDocBytesTopNTable, wwwDocBytesTopNEntry=wwwDocBytesTopNEntry, wwwDocBytesTopNIndex=wwwDocBytesTopNIndex, wwwDocBytesTopNName=wwwDocBytesTopNName, wwwDocBytesTopNAccesses=wwwDocBytesTopNAccesses, wwwDocBytesTopNBytes=wwwDocBytesTopNBytes, wwwDocBytesTopNLastResponseType=wwwDocBytesTopNLastResponseType, wwwMIBConformance=wwwMIBConformance, wwwMIBCompliances=wwwMIBCompliances, wwwMIBGroups=wwwMIBGroups)

# Groups
mibBuilder.exportSymbols("WWW-MIB", wwwSummaryGroup=wwwSummaryGroup, wwwResponseOutGroup=wwwResponseOutGroup, wwwResponseInGroup=wwwResponseInGroup, wwwDocumentGroup=wwwDocumentGroup, wwwRequestOutGroup=wwwRequestOutGroup, wwwServiceGroup=wwwServiceGroup, wwwRequestInGroup=wwwRequestInGroup)
