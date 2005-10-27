# PySNMP SMI module. Autogenerated from smidump -f python GSMP-MIB
# by libsmi2pysnmp-0.0.5-alpha at Fri Oct 28 00:30:39 2005,
# Python version (2, 4, 0, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( AtmVcIdentifier, AtmVpIdentifier, ) = mibBuilder.importSymbols("ATM-TC-MIB", "AtmVcIdentifier", "AtmVpIdentifier")
( InterfaceIndex, ) = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
( InetAddress, InetAddressType, InetPortNumber, ) = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType", "InetPortNumber")
( ZeroBasedCounter32, ) = mibBuilder.importSymbols("RMON2-MIB", "ZeroBasedCounter32")
( ModuleCompliance, NotificationGroup, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
( Bits, Integer32, Integer32, ModuleIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "mib-2")
( RowStatus, StorageType, TextualConvention, TimeStamp, TruthValue, ) = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "StorageType", "TextualConvention", "TimeStamp", "TruthValue")

# Types

class GsmpLabelType(OctetString):
    pass

class GsmpNameType(OctetString):
    subtypeSpec = OctetString.subtypeSpec+constraint.ValueSizeConstraint(6,6)
    pass

class GsmpPartitionIdType(OctetString):
    subtypeSpec = OctetString.subtypeSpec+constraint.ValueSizeConstraint(1,1)
    pass

class GsmpPartitionType(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(3,2,1,)
    namedValues = namedval.NamedValues(("noPartition", 1), ("fixedPartitionRequest", 2), ("fixedPartitionAssigned", 3), )
    pass

class GsmpVersion(Unsigned32):
    pass


# Objects

gsmpMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 98))
gsmpNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 98, 0))
gsmpObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 98, 1))
gsmpControllerTable = MibTable((1, 3, 6, 1, 2, 1, 98, 1, 1))
gsmpControllerEntry = MibTableRow((1, 3, 6, 1, 2, 1, 98, 1, 1, 1)).setIndexNames((0, "GSMP-MIB", "gsmpControllerEntityId"))
gsmpControllerEntityId = MibTableColumn((1, 3, 6, 1, 2, 1, 98, 1, 1, 1, 1), GsmpNameType()).setMaxAccess("noaccess")
gsmpControllerMaxVersion = MibTableColumn((1, 3, 6, 1, 2, 1, 98, 1, 1, 1, 2), GsmpVersion()).setMaxAccess("readwrite")
gsmpControllerTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 98, 1, 1, 1, 3), Unsigned32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 255))).setMaxAccess("readwrite")
gsmpControllerPort = MibTableColumn((1, 3, 6, 1, 2, 1, 98, 1, 1, 1, 4), Unsigned32()).setMaxAccess("readwrite")
gsmpControllerInstance = MibTableColumn((1, 3, 6, 1, 2, 1, 98, 1, 1, 1, 5), Unsigned32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 16777215))).setMaxAccess("readonly")
gsmpControllerPartitionType = MibTableColumn((1, 3, 6, 1, 2, 1, 98, 1, 1, 1, 6), GsmpPartitionType()).setMaxAccess("readwrite")
gsmpControllerPartitionId = MibTableColumn((1, 3, 6, 1, 2, 1, 98, 1, 1, 1, 7), GsmpPartitionIdType()).setMaxAccess("readwrite")
gsmpControllerDoResync = MibTableColumn((1, 3, 6, 1, 2, 1, 98, 1, 1, 1, 8), TruthValue()).setMaxAccess("readwrite")
gsmpControllerNotificationMap = MibTableColumn((1, 3, 6, 1, 2, 1, 98, 1, 1, 1, 9), Bits().subtype(namedValues=namedval.NamedValues(("sessionDown", 0), ("sessionUp", 1), ("sendFailureIndication", 2), ("receivedFailureIndication", 3), ("portUpEvent", 4), ("portDownEvent", 5), ("invalidLabelEvent", 6), ("newPortEvent", 7), ("deadPortEvent", 8), ("adjacencyUpdateEvent", 9), )).clone(("sessionDown","sessionUp","sendFailureIndication","receivedFailureIndication",))).setMaxAccess("readwrite")
gsmpControllerSessionState = MibTableColumn((1, 3, 6, 1, 2, 1, 98, 1, 1, 1, 10), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(4,1,2,3,)).subtype(namedValues=namedval.NamedValues(("null", 1), ("synsent", 2), ("synrcvd", 3), ("estab", 4), ))).setMaxAccess("readonly")
gsmpControllerStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 98, 1, 1, 1, 11), StorageType()).setMaxAccess("readwrite")
gsmpControllerRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 98, 1, 1, 1, 12), RowStatus()).setMaxAccess("readwrite")
gsmpSwitchTable = MibTable((1, 3, 6, 1, 2, 1, 98, 1, 2))
gsmpSwitchEntry = MibTableRow((1, 3, 6, 1, 2, 1, 98, 1, 2, 1)).setIndexNames((0, "GSMP-MIB", "gsmpSwitchEntityId"))
gsmpSwitchEntityId = MibTableColumn((1, 3, 6, 1, 2, 1, 98, 1, 2, 1, 1), GsmpNameType()).setMaxAccess("noaccess")
gsmpSwitchMaxVersion = MibTableColumn((1, 3, 6, 1, 2, 1, 98, 1, 2, 1, 2), GsmpVersion()).setMaxAccess("readwrite")
gsmpSwitchTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 98, 1, 2, 1, 3), Unsigned32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 255))).setMaxAccess("readwrite")
gsmpSwitchName = MibTableColumn((1, 3, 6, 1, 2, 1, 98, 1, 2, 1, 4), GsmpNameType()).setMaxAccess("readwrite")
gsmpSwitchPort = MibTableColumn((1, 3, 6, 1, 2, 1, 98, 1, 2, 1, 5), Unsigned32()).setMaxAccess("readwrite")
gsmpSwitchInstance = MibTableColumn((1, 3, 6, 1, 2, 1, 98, 1, 2, 1, 6), Unsigned32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 16777215))).setMaxAccess("readonly")
gsmpSwitchPartitionType = MibTableColumn((1, 3, 6, 1, 2, 1, 98, 1, 2, 1, 7), GsmpPartitionType()).setMaxAccess("readwrite")
gsmpSwitchPartitionId = MibTableColumn((1, 3, 6, 1, 2, 1, 98, 1, 2, 1, 8), GsmpPartitionIdType()).setMaxAccess("readwrite")
gsmpSwitchNotificationMap = MibTableColumn((1, 3, 6, 1, 2, 1, 98, 1, 2, 1, 9), Bits().subtype(namedValues=namedval.NamedValues(("sessionDown", 0), ("sessionUp", 1), ("sendFailureIndication", 2), ("receivedFailureIndication", 3), ("portUpEvent", 4), ("portDownEvent", 5), ("invalidLabelEvent", 6), ("newPortEvent", 7), ("deadPortEvent", 8), ("adjacencyUpdateEvent", 9), )).clone(("sessionDown","sessionUp","sendFailureIndication","receivedFailureIndication",))).setMaxAccess("readwrite")
gsmpSwitchSwitchType = MibTableColumn((1, 3, 6, 1, 2, 1, 98, 1, 2, 1, 10), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(2, 2))).setMaxAccess("readwrite")
gsmpSwitchWindowSize = MibTableColumn((1, 3, 6, 1, 2, 1, 98, 1, 2, 1, 11), Unsigned32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
gsmpSwitchSessionState = MibTableColumn((1, 3, 6, 1, 2, 1, 98, 1, 2, 1, 12), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(4,1,2,3,)).subtype(namedValues=namedval.NamedValues(("null", 1), ("synsent", 2), ("synrcvd", 3), ("estab", 4), ))).setMaxAccess("readonly")
gsmpSwitchStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 98, 1, 2, 1, 13), StorageType()).setMaxAccess("readwrite")
gsmpSwitchRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 98, 1, 2, 1, 14), RowStatus()).setMaxAccess("readwrite")
gsmpAtmEncapTable = MibTable((1, 3, 6, 1, 2, 1, 98, 1, 3))
gsmpAtmEncapEntry = MibTableRow((1, 3, 6, 1, 2, 1, 98, 1, 3, 1)).setIndexNames((0, "GSMP-MIB", "gsmpAtmEncapEntityId"))
gsmpAtmEncapEntityId = MibTableColumn((1, 3, 6, 1, 2, 1, 98, 1, 3, 1, 1), GsmpNameType()).setMaxAccess("noaccess")
gsmpAtmEncapIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 98, 1, 3, 1, 2), InterfaceIndex()).setMaxAccess("readwrite")
gsmpAtmEncapVpi = MibTableColumn((1, 3, 6, 1, 2, 1, 98, 1, 3, 1, 3), AtmVpIdentifier()).setMaxAccess("readwrite")
gsmpAtmEncapVci = MibTableColumn((1, 3, 6, 1, 2, 1, 98, 1, 3, 1, 4), AtmVcIdentifier()).setMaxAccess("readwrite")
gsmpAtmEncapStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 98, 1, 3, 1, 5), StorageType()).setMaxAccess("readwrite")
gsmpAtmEncapRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 98, 1, 3, 1, 6), RowStatus()).setMaxAccess("readwrite")
gsmpTcpIpEncapTable = MibTable((1, 3, 6, 1, 2, 1, 98, 1, 4))
gsmpTcpIpEncapEntry = MibTableRow((1, 3, 6, 1, 2, 1, 98, 1, 4, 1)).setIndexNames((0, "GSMP-MIB", "gsmpTcpIpEncapEntityId"))
gsmpTcpIpEncapEntityId = MibTableColumn((1, 3, 6, 1, 2, 1, 98, 1, 4, 1, 1), GsmpNameType()).setMaxAccess("noaccess")
gsmpTcpIpEncapAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 98, 1, 4, 1, 2), InetAddressType()).setMaxAccess("readwrite")
gsmpTcpIpEncapAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 98, 1, 4, 1, 3), InetAddress()).setMaxAccess("readwrite")
gsmpTcpIpEncapPortNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 98, 1, 4, 1, 4), InetPortNumber()).setMaxAccess("readwrite")
gsmpTcpIpEncapStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 98, 1, 4, 1, 5), StorageType()).setMaxAccess("readwrite")
gsmpTcpIpEncapRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 98, 1, 4, 1, 6), RowStatus()).setMaxAccess("readwrite")
gsmpSessionTable = MibTable((1, 3, 6, 1, 2, 1, 98, 1, 5))
gsmpSessionEntry = MibTableRow((1, 3, 6, 1, 2, 1, 98, 1, 5, 1)).setIndexNames((0, "GSMP-MIB", "gsmpSessionThisSideId"), (0, "GSMP-MIB", "gsmpSessionFarSideId"))
gsmpSessionThisSideId = MibTableColumn((1, 3, 6, 1, 2, 1, 98, 1, 5, 1, 1), GsmpNameType()).setMaxAccess("noaccess")
gsmpSessionFarSideId = MibTableColumn((1, 3, 6, 1, 2, 1, 98, 1, 5, 1, 2), GsmpNameType()).setMaxAccess("noaccess")
gsmpSessionVersion = MibTableColumn((1, 3, 6, 1, 2, 1, 98, 1, 5, 1, 3), GsmpVersion()).setMaxAccess("readonly")
gsmpSessionTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 98, 1, 5, 1, 4), Integer32()).setMaxAccess("readonly")
gsmpSessionPartitionId = MibTableColumn((1, 3, 6, 1, 2, 1, 98, 1, 5, 1, 5), GsmpPartitionIdType()).setMaxAccess("readonly")
gsmpSessionAdjacencyCount = MibTableColumn((1, 3, 6, 1, 2, 1, 98, 1, 5, 1, 6), Unsigned32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
gsmpSessionFarSideName = MibTableColumn((1, 3, 6, 1, 2, 1, 98, 1, 5, 1, 7), GsmpNameType()).setMaxAccess("readonly")
gsmpSessionFarSidePort = MibTableColumn((1, 3, 6, 1, 2, 1, 98, 1, 5, 1, 8), Unsigned32()).setMaxAccess("readonly")
gsmpSessionFarSideInstance = MibTableColumn((1, 3, 6, 1, 2, 1, 98, 1, 5, 1, 9), Unsigned32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 16777215))).setMaxAccess("readonly")
gsmpSessionLastFailureCode = MibTableColumn((1, 3, 6, 1, 2, 1, 98, 1, 5, 1, 10), Unsigned32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
gsmpSessionDiscontinuityTime = MibTableColumn((1, 3, 6, 1, 2, 1, 98, 1, 5, 1, 11), TimeStamp()).setMaxAccess("readonly")
gsmpSessionStartUptime = MibTableColumn((1, 3, 6, 1, 2, 1, 98, 1, 5, 1, 12), TimeStamp()).setMaxAccess("readonly")
gsmpSessionStatSentMessages = MibTableColumn((1, 3, 6, 1, 2, 1, 98, 1, 5, 1, 13), ZeroBasedCounter32()).setMaxAccess("readonly")
gsmpSessionStatFailureInds = MibTableColumn((1, 3, 6, 1, 2, 1, 98, 1, 5, 1, 14), ZeroBasedCounter32()).setMaxAccess("readonly")
gsmpSessionStatReceivedMessages = MibTableColumn((1, 3, 6, 1, 2, 1, 98, 1, 5, 1, 15), ZeroBasedCounter32()).setMaxAccess("readonly")
gsmpSessionStatReceivedFailures = MibTableColumn((1, 3, 6, 1, 2, 1, 98, 1, 5, 1, 16), ZeroBasedCounter32()).setMaxAccess("readonly")
gsmpSessionStatPortUpEvents = MibTableColumn((1, 3, 6, 1, 2, 1, 98, 1, 5, 1, 17), ZeroBasedCounter32()).setMaxAccess("readonly")
gsmpSessionStatPortDownEvents = MibTableColumn((1, 3, 6, 1, 2, 1, 98, 1, 5, 1, 18), ZeroBasedCounter32()).setMaxAccess("readonly")
gsmpSessionStatInvLabelEvents = MibTableColumn((1, 3, 6, 1, 2, 1, 98, 1, 5, 1, 19), ZeroBasedCounter32()).setMaxAccess("readonly")
gsmpSessionStatNewPortEvents = MibTableColumn((1, 3, 6, 1, 2, 1, 98, 1, 5, 1, 20), ZeroBasedCounter32()).setMaxAccess("readonly")
gsmpSessionStatDeadPortEvents = MibTableColumn((1, 3, 6, 1, 2, 1, 98, 1, 5, 1, 21), ZeroBasedCounter32()).setMaxAccess("readonly")
gsmpSessionStatAdjUpdateEvents = MibTableColumn((1, 3, 6, 1, 2, 1, 98, 1, 5, 1, 22), ZeroBasedCounter32()).setMaxAccess("readonly")
gsmpNotificationsObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 98, 2))
gsmpEventPort = MibScalar((1, 3, 6, 1, 2, 1, 98, 2, 1), Unsigned32()).setMaxAccess("notifyonly")
gsmpEventPortSessionNumber = MibScalar((1, 3, 6, 1, 2, 1, 98, 2, 2), Unsigned32()).setMaxAccess("notifyonly")
gsmpEventSequenceNumber = MibScalar((1, 3, 6, 1, 2, 1, 98, 2, 3), Unsigned32()).setMaxAccess("notifyonly")
gsmpEventLabel = MibScalar((1, 3, 6, 1, 2, 1, 98, 2, 4), GsmpLabelType()).setMaxAccess("notifyonly")
gsmpConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 98, 3))
gsmpGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 98, 3, 1))
gsmpCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 98, 3, 2))

# Augmentions

# Notifications

gsmpInvalidLabelEvent = NotificationType((1, 3, 6, 1, 2, 1, 98, 0, 7)).setObjects(("GSMP-MIB", "gsmpEventLabel"), ("GSMP-MIB", "gsmpEventSequenceNumber"), ("GSMP-MIB", "gsmpSessionStatInvLabelEvents"), ("GSMP-MIB", "gsmpEventPort"), )
gsmpPortUpEvent = NotificationType((1, 3, 6, 1, 2, 1, 98, 0, 5)).setObjects(("GSMP-MIB", "gsmpEventPortSessionNumber"), ("GSMP-MIB", "gsmpSessionStatPortUpEvents"), ("GSMP-MIB", "gsmpEventSequenceNumber"), ("GSMP-MIB", "gsmpEventPort"), )
gsmpSentFailureInd = NotificationType((1, 3, 6, 1, 2, 1, 98, 0, 3)).setObjects(("GSMP-MIB", "gsmpSessionLastFailureCode"), ("GSMP-MIB", "gsmpSessionStatFailureInds"), )
gsmpDeadPortEvent = NotificationType((1, 3, 6, 1, 2, 1, 98, 0, 9)).setObjects(("GSMP-MIB", "gsmpEventSequenceNumber"), ("GSMP-MIB", "gsmpEventPortSessionNumber"), ("GSMP-MIB", "gsmpSessionStatDeadPortEvents"), ("GSMP-MIB", "gsmpEventPort"), )
gsmpSessionUp = NotificationType((1, 3, 6, 1, 2, 1, 98, 0, 2)).setObjects(("GSMP-MIB", "gsmpSessionFarSideInstance"), )
gsmpAdjacencyUpdateEvent = NotificationType((1, 3, 6, 1, 2, 1, 98, 0, 10)).setObjects(("GSMP-MIB", "gsmpSessionAdjacencyCount"), ("GSMP-MIB", "gsmpSessionStatAdjUpdateEvents"), ("GSMP-MIB", "gsmpEventSequenceNumber"), )
gsmpSessionDown = NotificationType((1, 3, 6, 1, 2, 1, 98, 0, 1)).setObjects(("GSMP-MIB", "gsmpSessionStatPortUpEvents"), ("GSMP-MIB", "gsmpSessionStatReceivedMessages"), ("GSMP-MIB", "gsmpSessionStatDeadPortEvents"), ("GSMP-MIB", "gsmpSessionStatNewPortEvents"), ("GSMP-MIB", "gsmpSessionStatPortDownEvents"), ("GSMP-MIB", "gsmpSessionStatAdjUpdateEvents"), ("GSMP-MIB", "gsmpSessionStartUptime"), ("GSMP-MIB", "gsmpSessionStatFailureInds"), ("GSMP-MIB", "gsmpSessionStatInvLabelEvents"), ("GSMP-MIB", "gsmpSessionStatReceivedFailures"), ("GSMP-MIB", "gsmpSessionStatSentMessages"), )
gsmpReceivedFailureInd = NotificationType((1, 3, 6, 1, 2, 1, 98, 0, 4)).setObjects(("GSMP-MIB", "gsmpSessionLastFailureCode"), ("GSMP-MIB", "gsmpSessionStatReceivedFailures"), )
gsmpNewPortEvent = NotificationType((1, 3, 6, 1, 2, 1, 98, 0, 8)).setObjects(("GSMP-MIB", "gsmpEventPortSessionNumber"), ("GSMP-MIB", "gsmpSessionStatNewPortEvents"), ("GSMP-MIB", "gsmpEventSequenceNumber"), ("GSMP-MIB", "gsmpEventPort"), )
gsmpPortDownEvent = NotificationType((1, 3, 6, 1, 2, 1, 98, 0, 6)).setObjects(("GSMP-MIB", "gsmpEventPortSessionNumber"), ("GSMP-MIB", "gsmpEventSequenceNumber"), ("GSMP-MIB", "gsmpSessionStatPortDownEvents"), ("GSMP-MIB", "gsmpEventPort"), )

# Groups

gsmpControllerGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 98, 3, 1, 2)).setObjects(("GSMP-MIB", "gsmpControllerRowStatus"), ("GSMP-MIB", "gsmpControllerSessionState"), ("GSMP-MIB", "gsmpControllerStorageType"), ("GSMP-MIB", "gsmpControllerPort"), ("GSMP-MIB", "gsmpControllerNotificationMap"), ("GSMP-MIB", "gsmpControllerDoResync"), ("GSMP-MIB", "gsmpControllerTimer"), ("GSMP-MIB", "gsmpControllerPartitionType"), ("GSMP-MIB", "gsmpControllerMaxVersion"), ("GSMP-MIB", "gsmpControllerInstance"), ("GSMP-MIB", "gsmpControllerPartitionId"), )
gsmpTcpIpEncapGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 98, 3, 1, 5)).setObjects(("GSMP-MIB", "gsmpTcpIpEncapAddress"), ("GSMP-MIB", "gsmpTcpIpEncapPortNumber"), ("GSMP-MIB", "gsmpTcpIpEncapAddressType"), ("GSMP-MIB", "gsmpTcpIpEncapStorageType"), ("GSMP-MIB", "gsmpTcpIpEncapRowStatus"), )
gsmpNotificationObjectsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 98, 3, 1, 6)).setObjects(("GSMP-MIB", "gsmpEventLabel"), ("GSMP-MIB", "gsmpEventPortSessionNumber"), ("GSMP-MIB", "gsmpEventSequenceNumber"), ("GSMP-MIB", "gsmpEventPort"), )
gsmpSwitchGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 98, 3, 1, 3)).setObjects(("GSMP-MIB", "gsmpSwitchSwitchType"), ("GSMP-MIB", "gsmpSwitchRowStatus"), ("GSMP-MIB", "gsmpSwitchStorageType"), ("GSMP-MIB", "gsmpSwitchInstance"), ("GSMP-MIB", "gsmpSwitchPartitionId"), ("GSMP-MIB", "gsmpSwitchSessionState"), ("GSMP-MIB", "gsmpSwitchName"), ("GSMP-MIB", "gsmpSwitchNotificationMap"), ("GSMP-MIB", "gsmpSwitchPort"), ("GSMP-MIB", "gsmpSwitchWindowSize"), ("GSMP-MIB", "gsmpSwitchTimer"), ("GSMP-MIB", "gsmpSwitchPartitionType"), ("GSMP-MIB", "gsmpSwitchMaxVersion"), )
gsmpAtmEncapGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 98, 3, 1, 4)).setObjects(("GSMP-MIB", "gsmpAtmEncapIfIndex"), ("GSMP-MIB", "gsmpAtmEncapVci"), ("GSMP-MIB", "gsmpAtmEncapVpi"), ("GSMP-MIB", "gsmpAtmEncapStorageType"), ("GSMP-MIB", "gsmpAtmEncapRowStatus"), )
gsmpGeneralGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 98, 3, 1, 1)).setObjects(("GSMP-MIB", "gsmpSessionLastFailureCode"), ("GSMP-MIB", "gsmpSessionStartUptime"), ("GSMP-MIB", "gsmpSessionStatReceivedMessages"), ("GSMP-MIB", "gsmpSessionFarSidePort"), ("GSMP-MIB", "gsmpSessionStatDeadPortEvents"), ("GSMP-MIB", "gsmpSessionTimer"), ("GSMP-MIB", "gsmpSessionStatNewPortEvents"), ("GSMP-MIB", "gsmpSessionStatPortDownEvents"), ("GSMP-MIB", "gsmpSessionPartitionId"), ("GSMP-MIB", "gsmpSessionFarSideName"), ("GSMP-MIB", "gsmpSessionFarSideInstance"), ("GSMP-MIB", "gsmpSessionStatAdjUpdateEvents"), ("GSMP-MIB", "gsmpSessionStatPortUpEvents"), ("GSMP-MIB", "gsmpSessionStatFailureInds"), ("GSMP-MIB", "gsmpSessionStatInvLabelEvents"), ("GSMP-MIB", "gsmpSessionDiscontinuityTime"), ("GSMP-MIB", "gsmpSessionAdjacencyCount"), ("GSMP-MIB", "gsmpSessionStatReceivedFailures"), ("GSMP-MIB", "gsmpSessionVersion"), ("GSMP-MIB", "gsmpSessionStatSentMessages"), )
gsmpNotificationsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 98, 3, 1, 7)).setObjects(("GSMP-MIB", "gsmpInvalidLabelEvent"), ("GSMP-MIB", "gsmpPortUpEvent"), ("GSMP-MIB", "gsmpSentFailureInd"), ("GSMP-MIB", "gsmpDeadPortEvent"), ("GSMP-MIB", "gsmpSessionUp"), ("GSMP-MIB", "gsmpAdjacencyUpdateEvent"), ("GSMP-MIB", "gsmpSessionDown"), ("GSMP-MIB", "gsmpReceivedFailureInd"), ("GSMP-MIB", "gsmpNewPortEvent"), ("GSMP-MIB", "gsmpPortDownEvent"), )

# Exports

# Types
mibBuilder.exportSymbols("GSMP-MIB", GsmpLabelType=GsmpLabelType, GsmpNameType=GsmpNameType, GsmpPartitionIdType=GsmpPartitionIdType, GsmpPartitionType=GsmpPartitionType, GsmpVersion=GsmpVersion)

# Objects
mibBuilder.exportSymbols("GSMP-MIB", gsmpMIB=gsmpMIB, gsmpNotifications=gsmpNotifications, gsmpObjects=gsmpObjects, gsmpControllerTable=gsmpControllerTable, gsmpControllerEntry=gsmpControllerEntry, gsmpControllerEntityId=gsmpControllerEntityId, gsmpControllerMaxVersion=gsmpControllerMaxVersion, gsmpControllerTimer=gsmpControllerTimer, gsmpControllerPort=gsmpControllerPort, gsmpControllerInstance=gsmpControllerInstance, gsmpControllerPartitionType=gsmpControllerPartitionType, gsmpControllerPartitionId=gsmpControllerPartitionId, gsmpControllerDoResync=gsmpControllerDoResync, gsmpControllerNotificationMap=gsmpControllerNotificationMap, gsmpControllerSessionState=gsmpControllerSessionState, gsmpControllerStorageType=gsmpControllerStorageType, gsmpControllerRowStatus=gsmpControllerRowStatus, gsmpSwitchTable=gsmpSwitchTable, gsmpSwitchEntry=gsmpSwitchEntry, gsmpSwitchEntityId=gsmpSwitchEntityId, gsmpSwitchMaxVersion=gsmpSwitchMaxVersion, gsmpSwitchTimer=gsmpSwitchTimer, gsmpSwitchName=gsmpSwitchName, gsmpSwitchPort=gsmpSwitchPort, gsmpSwitchInstance=gsmpSwitchInstance, gsmpSwitchPartitionType=gsmpSwitchPartitionType, gsmpSwitchPartitionId=gsmpSwitchPartitionId, gsmpSwitchNotificationMap=gsmpSwitchNotificationMap, gsmpSwitchSwitchType=gsmpSwitchSwitchType, gsmpSwitchWindowSize=gsmpSwitchWindowSize, gsmpSwitchSessionState=gsmpSwitchSessionState, gsmpSwitchStorageType=gsmpSwitchStorageType, gsmpSwitchRowStatus=gsmpSwitchRowStatus, gsmpAtmEncapTable=gsmpAtmEncapTable, gsmpAtmEncapEntry=gsmpAtmEncapEntry, gsmpAtmEncapEntityId=gsmpAtmEncapEntityId, gsmpAtmEncapIfIndex=gsmpAtmEncapIfIndex, gsmpAtmEncapVpi=gsmpAtmEncapVpi, gsmpAtmEncapVci=gsmpAtmEncapVci, gsmpAtmEncapStorageType=gsmpAtmEncapStorageType, gsmpAtmEncapRowStatus=gsmpAtmEncapRowStatus, gsmpTcpIpEncapTable=gsmpTcpIpEncapTable, gsmpTcpIpEncapEntry=gsmpTcpIpEncapEntry, gsmpTcpIpEncapEntityId=gsmpTcpIpEncapEntityId, gsmpTcpIpEncapAddressType=gsmpTcpIpEncapAddressType, gsmpTcpIpEncapAddress=gsmpTcpIpEncapAddress, gsmpTcpIpEncapPortNumber=gsmpTcpIpEncapPortNumber, gsmpTcpIpEncapStorageType=gsmpTcpIpEncapStorageType, gsmpTcpIpEncapRowStatus=gsmpTcpIpEncapRowStatus, gsmpSessionTable=gsmpSessionTable, gsmpSessionEntry=gsmpSessionEntry, gsmpSessionThisSideId=gsmpSessionThisSideId, gsmpSessionFarSideId=gsmpSessionFarSideId, gsmpSessionVersion=gsmpSessionVersion, gsmpSessionTimer=gsmpSessionTimer, gsmpSessionPartitionId=gsmpSessionPartitionId, gsmpSessionAdjacencyCount=gsmpSessionAdjacencyCount, gsmpSessionFarSideName=gsmpSessionFarSideName, gsmpSessionFarSidePort=gsmpSessionFarSidePort, gsmpSessionFarSideInstance=gsmpSessionFarSideInstance, gsmpSessionLastFailureCode=gsmpSessionLastFailureCode, gsmpSessionDiscontinuityTime=gsmpSessionDiscontinuityTime, gsmpSessionStartUptime=gsmpSessionStartUptime, gsmpSessionStatSentMessages=gsmpSessionStatSentMessages, gsmpSessionStatFailureInds=gsmpSessionStatFailureInds, gsmpSessionStatReceivedMessages=gsmpSessionStatReceivedMessages, gsmpSessionStatReceivedFailures=gsmpSessionStatReceivedFailures, gsmpSessionStatPortUpEvents=gsmpSessionStatPortUpEvents, gsmpSessionStatPortDownEvents=gsmpSessionStatPortDownEvents, gsmpSessionStatInvLabelEvents=gsmpSessionStatInvLabelEvents, gsmpSessionStatNewPortEvents=gsmpSessionStatNewPortEvents, gsmpSessionStatDeadPortEvents=gsmpSessionStatDeadPortEvents, gsmpSessionStatAdjUpdateEvents=gsmpSessionStatAdjUpdateEvents, gsmpNotificationsObjects=gsmpNotificationsObjects, gsmpEventPort=gsmpEventPort, gsmpEventPortSessionNumber=gsmpEventPortSessionNumber, gsmpEventSequenceNumber=gsmpEventSequenceNumber, gsmpEventLabel=gsmpEventLabel, gsmpConformance=gsmpConformance, gsmpGroups=gsmpGroups, gsmpCompliances=gsmpCompliances)

# Notifications
mibBuilder.exportSymbols("GSMP-MIB", gsmpInvalidLabelEvent=gsmpInvalidLabelEvent, gsmpPortUpEvent=gsmpPortUpEvent, gsmpSentFailureInd=gsmpSentFailureInd, gsmpDeadPortEvent=gsmpDeadPortEvent, gsmpSessionUp=gsmpSessionUp, gsmpAdjacencyUpdateEvent=gsmpAdjacencyUpdateEvent, gsmpSessionDown=gsmpSessionDown, gsmpReceivedFailureInd=gsmpReceivedFailureInd, gsmpNewPortEvent=gsmpNewPortEvent, gsmpPortDownEvent=gsmpPortDownEvent)

# Groups
mibBuilder.exportSymbols("GSMP-MIB", gsmpControllerGroup=gsmpControllerGroup, gsmpTcpIpEncapGroup=gsmpTcpIpEncapGroup, gsmpNotificationObjectsGroup=gsmpNotificationObjectsGroup, gsmpSwitchGroup=gsmpSwitchGroup, gsmpAtmEncapGroup=gsmpAtmEncapGroup, gsmpGeneralGroup=gsmpGeneralGroup, gsmpNotificationsGroup=gsmpNotificationsGroup)
