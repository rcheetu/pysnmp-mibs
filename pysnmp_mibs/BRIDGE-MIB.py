# PySNMP SMI module. Autogenerated from smidump -f python BRIDGE-MIB
# by libsmi2pysnmp-0.0.5-alpha at Fri Oct 28 00:30:32 2005,
# Python version (2, 4, 0, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( Bits, Counter32, Integer32, Integer32, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, TimeTicks, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Integer32", "Integer32", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "TimeTicks", "mib-2")

# Types

class BridgeId(OctetString):
    subtypeSpec = OctetString.subtypeSpec+constraint.ValueSizeConstraint(8,8)
    pass

class MacAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec+constraint.ValueSizeConstraint(6,6)
    pass

class Timeout(Integer32):
    pass


# Objects

dot1dBridge = MibIdentifier((1, 3, 6, 1, 2, 1, 17))
dot1dBase = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 1))
dot1dBaseBridgeAddress = MibScalar((1, 3, 6, 1, 2, 1, 17, 1, 1), MacAddress()).setMaxAccess("readonly")
dot1dBaseNumPorts = MibScalar((1, 3, 6, 1, 2, 1, 17, 1, 2), Integer32()).setMaxAccess("readonly")
dot1dBaseType = MibScalar((1, 3, 6, 1, 2, 1, 17, 1, 3), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(4,1,2,3,)).subtype(namedValues=namedval.NamedValues(("unknown", 1), ("transparent-only", 2), ("sourceroute-only", 3), ("srt", 4), ))).setMaxAccess("readonly")
dot1dBasePortTable = MibTable((1, 3, 6, 1, 2, 1, 17, 1, 4))
dot1dBasePortEntry = MibTableRow((1, 3, 6, 1, 2, 1, 17, 1, 4, 1)).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"))
dot1dBasePort = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
dot1dBasePortIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 1, 4, 1, 2), Integer32()).setMaxAccess("readonly")
dot1dBasePortCircuit = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 1, 4, 1, 3), ObjectIdentifier()).setMaxAccess("readonly")
dot1dBasePortDelayExceededDiscards = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 1, 4, 1, 4), Counter32()).setMaxAccess("readonly")
dot1dBasePortMtuExceededDiscards = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 1, 4, 1, 5), Counter32()).setMaxAccess("readonly")
dot1dStp = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 2))
dot1dStpProtocolSpecification = MibScalar((1, 3, 6, 1, 2, 1, 17, 2, 1), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(3,1,2,)).subtype(namedValues=namedval.NamedValues(("unknown", 1), ("decLb100", 2), ("ieee8021d", 3), ))).setMaxAccess("readonly")
dot1dStpPriority = MibScalar((1, 3, 6, 1, 2, 1, 17, 2, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
dot1dStpTimeSinceTopologyChange = MibScalar((1, 3, 6, 1, 2, 1, 17, 2, 3), TimeTicks()).setMaxAccess("readonly")
dot1dStpTopChanges = MibScalar((1, 3, 6, 1, 2, 1, 17, 2, 4), Counter32()).setMaxAccess("readonly")
dot1dStpDesignatedRoot = MibScalar((1, 3, 6, 1, 2, 1, 17, 2, 5), BridgeId()).setMaxAccess("readonly")
dot1dStpRootCost = MibScalar((1, 3, 6, 1, 2, 1, 17, 2, 6), Integer32()).setMaxAccess("readonly")
dot1dStpRootPort = MibScalar((1, 3, 6, 1, 2, 1, 17, 2, 7), Integer32()).setMaxAccess("readonly")
dot1dStpMaxAge = MibScalar((1, 3, 6, 1, 2, 1, 17, 2, 8), Timeout()).setMaxAccess("readonly")
dot1dStpHelloTime = MibScalar((1, 3, 6, 1, 2, 1, 17, 2, 9), Timeout()).setMaxAccess("readonly")
dot1dStpHoldTime = MibScalar((1, 3, 6, 1, 2, 1, 17, 2, 10), Integer32()).setMaxAccess("readonly")
dot1dStpForwardDelay = MibScalar((1, 3, 6, 1, 2, 1, 17, 2, 11), Timeout()).setMaxAccess("readonly")
dot1dStpBridgeMaxAge = MibScalar((1, 3, 6, 1, 2, 1, 17, 2, 12), Timeout().subtype(subtypeSpec=constraint.ValueRangeConstraint(600, 4000))).setMaxAccess("readwrite")
dot1dStpBridgeHelloTime = MibScalar((1, 3, 6, 1, 2, 1, 17, 2, 13), Timeout().subtype(subtypeSpec=constraint.ValueRangeConstraint(100, 1000))).setMaxAccess("readwrite")
dot1dStpBridgeForwardDelay = MibScalar((1, 3, 6, 1, 2, 1, 17, 2, 14), Timeout().subtype(subtypeSpec=constraint.ValueRangeConstraint(400, 3000))).setMaxAccess("readwrite")
dot1dStpPortTable = MibTable((1, 3, 6, 1, 2, 1, 17, 2, 15))
dot1dStpPortEntry = MibTableRow((1, 3, 6, 1, 2, 1, 17, 2, 15, 1)).setIndexNames((0, "BRIDGE-MIB", "dot1dStpPort"))
dot1dStpPort = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 2, 15, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
dot1dStpPortPriority = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 2, 15, 1, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
dot1dStpPortState = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 2, 15, 1, 3), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(3,1,6,4,5,2,)).subtype(namedValues=namedval.NamedValues(("disabled", 1), ("blocking", 2), ("listening", 3), ("learning", 4), ("forwarding", 5), ("broken", 6), ))).setMaxAccess("readonly")
dot1dStpPortEnable = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 2, 15, 1, 4), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("enabled", 1), ("disabled", 2), ))).setMaxAccess("readwrite")
dot1dStpPortPathCost = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 2, 15, 1, 5), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
dot1dStpPortDesignatedRoot = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 2, 15, 1, 6), BridgeId()).setMaxAccess("readonly")
dot1dStpPortDesignatedCost = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 2, 15, 1, 7), Integer32()).setMaxAccess("readonly")
dot1dStpPortDesignatedBridge = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 2, 15, 1, 8), BridgeId()).setMaxAccess("readonly")
dot1dStpPortDesignatedPort = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 2, 15, 1, 9), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(2, 2))).setMaxAccess("readonly")
dot1dStpPortForwardTransitions = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 2, 15, 1, 10), Counter32()).setMaxAccess("readonly")
dot1dSr = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 3))
dot1dTp = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 4))
dot1dTpLearnedEntryDiscards = MibScalar((1, 3, 6, 1, 2, 1, 17, 4, 1), Counter32()).setMaxAccess("readonly")
dot1dTpAgingTime = MibScalar((1, 3, 6, 1, 2, 1, 17, 4, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(10, 1000000))).setMaxAccess("readwrite")
dot1dTpFdbTable = MibTable((1, 3, 6, 1, 2, 1, 17, 4, 3))
dot1dTpFdbEntry = MibTableRow((1, 3, 6, 1, 2, 1, 17, 4, 3, 1)).setIndexNames((0, "BRIDGE-MIB", "dot1dTpFdbAddress"))
dot1dTpFdbAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 4, 3, 1, 1), MacAddress()).setMaxAccess("readonly")
dot1dTpFdbPort = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 4, 3, 1, 2), Integer32()).setMaxAccess("readonly")
dot1dTpFdbStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 4, 3, 1, 3), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(4,2,1,5,3,)).subtype(namedValues=namedval.NamedValues(("other", 1), ("invalid", 2), ("learned", 3), ("self", 4), ("mgmt", 5), ))).setMaxAccess("readonly")
dot1dTpPortTable = MibTable((1, 3, 6, 1, 2, 1, 17, 4, 4))
dot1dTpPortEntry = MibTableRow((1, 3, 6, 1, 2, 1, 17, 4, 4, 1)).setIndexNames((0, "BRIDGE-MIB", "dot1dTpPort"))
dot1dTpPort = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 4, 4, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
dot1dTpPortMaxInfo = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 4, 4, 1, 2), Integer32()).setMaxAccess("readonly")
dot1dTpPortInFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 4, 4, 1, 3), Counter32()).setMaxAccess("readonly")
dot1dTpPortOutFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 4, 4, 1, 4), Counter32()).setMaxAccess("readonly")
dot1dTpPortInDiscards = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 4, 4, 1, 5), Counter32()).setMaxAccess("readonly")
dot1dStatic = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 5))
dot1dStaticTable = MibTable((1, 3, 6, 1, 2, 1, 17, 5, 1))
dot1dStaticEntry = MibTableRow((1, 3, 6, 1, 2, 1, 17, 5, 1, 1)).setIndexNames((0, "BRIDGE-MIB", "dot1dStaticAddress"), (0, "BRIDGE-MIB", "dot1dStaticReceivePort"))
dot1dStaticAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 5, 1, 1, 1), MacAddress()).setMaxAccess("readwrite")
dot1dStaticReceivePort = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 5, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
dot1dStaticAllowedToGoTo = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 5, 1, 1, 3), OctetString()).setMaxAccess("readwrite")
dot1dStaticStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 5, 1, 1, 4), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,3,5,1,4,)).subtype(namedValues=namedval.NamedValues(("other", 1), ("invalid", 2), ("permanent", 3), ("deleteOnReset", 4), ("deleteOnTimeout", 5), ))).setMaxAccess("readwrite")

# Augmentions

# Notifications

newRoot = NotificationType((1, 3, 6, 1, 2, 1, 17, 0, 1)).setObjects()
topologyChange = NotificationType((1, 3, 6, 1, 2, 1, 17, 0, 2)).setObjects()

# Exports

# Types
mibBuilder.exportSymbols("BRIDGE-MIB", BridgeId=BridgeId, MacAddress=MacAddress, Timeout=Timeout)

# Objects
mibBuilder.exportSymbols("BRIDGE-MIB", dot1dBridge=dot1dBridge, dot1dBase=dot1dBase, dot1dBaseBridgeAddress=dot1dBaseBridgeAddress, dot1dBaseNumPorts=dot1dBaseNumPorts, dot1dBaseType=dot1dBaseType, dot1dBasePortTable=dot1dBasePortTable, dot1dBasePortEntry=dot1dBasePortEntry, dot1dBasePort=dot1dBasePort, dot1dBasePortIfIndex=dot1dBasePortIfIndex, dot1dBasePortCircuit=dot1dBasePortCircuit, dot1dBasePortDelayExceededDiscards=dot1dBasePortDelayExceededDiscards, dot1dBasePortMtuExceededDiscards=dot1dBasePortMtuExceededDiscards, dot1dStp=dot1dStp, dot1dStpProtocolSpecification=dot1dStpProtocolSpecification, dot1dStpPriority=dot1dStpPriority, dot1dStpTimeSinceTopologyChange=dot1dStpTimeSinceTopologyChange, dot1dStpTopChanges=dot1dStpTopChanges, dot1dStpDesignatedRoot=dot1dStpDesignatedRoot, dot1dStpRootCost=dot1dStpRootCost, dot1dStpRootPort=dot1dStpRootPort, dot1dStpMaxAge=dot1dStpMaxAge, dot1dStpHelloTime=dot1dStpHelloTime, dot1dStpHoldTime=dot1dStpHoldTime, dot1dStpForwardDelay=dot1dStpForwardDelay, dot1dStpBridgeMaxAge=dot1dStpBridgeMaxAge, dot1dStpBridgeHelloTime=dot1dStpBridgeHelloTime, dot1dStpBridgeForwardDelay=dot1dStpBridgeForwardDelay, dot1dStpPortTable=dot1dStpPortTable, dot1dStpPortEntry=dot1dStpPortEntry, dot1dStpPort=dot1dStpPort, dot1dStpPortPriority=dot1dStpPortPriority, dot1dStpPortState=dot1dStpPortState, dot1dStpPortEnable=dot1dStpPortEnable, dot1dStpPortPathCost=dot1dStpPortPathCost, dot1dStpPortDesignatedRoot=dot1dStpPortDesignatedRoot, dot1dStpPortDesignatedCost=dot1dStpPortDesignatedCost, dot1dStpPortDesignatedBridge=dot1dStpPortDesignatedBridge, dot1dStpPortDesignatedPort=dot1dStpPortDesignatedPort, dot1dStpPortForwardTransitions=dot1dStpPortForwardTransitions, dot1dSr=dot1dSr, dot1dTp=dot1dTp, dot1dTpLearnedEntryDiscards=dot1dTpLearnedEntryDiscards, dot1dTpAgingTime=dot1dTpAgingTime, dot1dTpFdbTable=dot1dTpFdbTable, dot1dTpFdbEntry=dot1dTpFdbEntry, dot1dTpFdbAddress=dot1dTpFdbAddress, dot1dTpFdbPort=dot1dTpFdbPort, dot1dTpFdbStatus=dot1dTpFdbStatus, dot1dTpPortTable=dot1dTpPortTable, dot1dTpPortEntry=dot1dTpPortEntry, dot1dTpPort=dot1dTpPort, dot1dTpPortMaxInfo=dot1dTpPortMaxInfo, dot1dTpPortInFrames=dot1dTpPortInFrames, dot1dTpPortOutFrames=dot1dTpPortOutFrames, dot1dTpPortInDiscards=dot1dTpPortInDiscards, dot1dStatic=dot1dStatic, dot1dStaticTable=dot1dStaticTable, dot1dStaticEntry=dot1dStaticEntry, dot1dStaticAddress=dot1dStaticAddress, dot1dStaticReceivePort=dot1dStaticReceivePort, dot1dStaticAllowedToGoTo=dot1dStaticAllowedToGoTo, dot1dStaticStatus=dot1dStaticStatus)

# Notifications
mibBuilder.exportSymbols("BRIDGE-MIB", newRoot=newRoot, topologyChange=topologyChange)

