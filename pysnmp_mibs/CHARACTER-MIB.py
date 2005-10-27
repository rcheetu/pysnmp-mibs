# PySNMP SMI module. Autogenerated from smidump -f python CHARACTER-MIB
# by libsmi2pysnmp-0.0.5-alpha at Fri Oct 28 00:30:32 2005,
# Python version (2, 4, 0, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( InterfaceIndex, ) = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
( transmission, ) = mibBuilder.importSymbols("RFC1213-MIB", "transmission")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Counter32, Gauge32, Integer32, Integer32, ModuleIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, TimeTicks, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Gauge32", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "TimeTicks", "mib-2")
( AutonomousType, DisplayString, InstancePointer, TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "AutonomousType", "DisplayString", "InstancePointer", "TextualConvention")

# Types

class PortIndex(TextualConvention, Integer32):
    pass


# Objects

char = ModuleIdentity((1, 3, 6, 1, 2, 1, 19))
charNumber = MibScalar((1, 3, 6, 1, 2, 1, 19, 1), Integer32()).setMaxAccess("readonly")
charPortTable = MibTable((1, 3, 6, 1, 2, 1, 19, 2))
charPortEntry = MibTableRow((1, 3, 6, 1, 2, 1, 19, 2, 1)).setIndexNames((0, "CHARACTER-MIB", "charPortIndex"))
charPortIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 2, 1, 1), PortIndex()).setMaxAccess("readonly")
charPortName = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 2, 1, 2), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
charPortType = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 2, 1, 3), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,2,)).subtype(namedValues=namedval.NamedValues(("physical", 1), ("virtual", 2), ))).setMaxAccess("readonly")
charPortHardware = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 2, 1, 4), AutonomousType()).setMaxAccess("readonly")
charPortReset = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 2, 1, 5), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,2,)).subtype(namedValues=namedval.NamedValues(("ready", 1), ("execute", 2), ))).setMaxAccess("readwrite")
charPortAdminStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 2, 1, 6), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,3,1,4,)).subtype(namedValues=namedval.NamedValues(("enabled", 1), ("disabled", 2), ("off", 3), ("maintenance", 4), ))).setMaxAccess("readwrite")
charPortOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 2, 1, 7), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(4,1,2,3,5,)).subtype(namedValues=namedval.NamedValues(("up", 1), ("down", 2), ("maintenance", 3), ("absent", 4), ("active", 5), ))).setMaxAccess("readonly")
charPortLastChange = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 2, 1, 8), TimeTicks()).setMaxAccess("readonly")
charPortInFlowType = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 2, 1, 9), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,2,3,5,4,)).subtype(namedValues=namedval.NamedValues(("none", 1), ("xonXoff", 2), ("hardware", 3), ("ctsRts", 4), ("dsrDtr", 5), ))).setMaxAccess("readwrite")
charPortOutFlowType = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 2, 1, 10), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,2,3,5,4,)).subtype(namedValues=namedval.NamedValues(("none", 1), ("xonXoff", 2), ("hardware", 3), ("ctsRts", 4), ("dsrDtr", 5), ))).setMaxAccess("readwrite")
charPortInFlowState = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 2, 1, 11), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(4,2,1,3,)).subtype(namedValues=namedval.NamedValues(("none", 1), ("unknown", 2), ("stop", 3), ("go", 4), ))).setMaxAccess("readonly")
charPortOutFlowState = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 2, 1, 12), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(4,2,1,3,)).subtype(namedValues=namedval.NamedValues(("none", 1), ("unknown", 2), ("stop", 3), ("go", 4), ))).setMaxAccess("readonly")
charPortInCharacters = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 2, 1, 13), Counter32()).setMaxAccess("readonly")
charPortOutCharacters = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 2, 1, 14), Counter32()).setMaxAccess("readonly")
charPortAdminOrigin = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 2, 1, 15), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(3,4,1,2,)).subtype(namedValues=namedval.NamedValues(("dynamic", 1), ("network", 2), ("local", 3), ("none", 4), ))).setMaxAccess("readwrite")
charPortSessionMaximum = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 2, 1, 16), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(-1, 2147483647L))).setMaxAccess("readwrite")
charPortSessionNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 2, 1, 17), Gauge32()).setMaxAccess("readonly")
charPortSessionIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 2, 1, 18), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 2147483647L))).setMaxAccess("readonly")
charPortInFlowTypes = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 2, 1, 19), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 1))).setMaxAccess("readwrite")
charPortOutFlowTypes = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 2, 1, 20), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 1))).setMaxAccess("readwrite")
charPortLowerIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 2, 1, 21), InterfaceIndex()).setMaxAccess("readonly")
charSessTable = MibTable((1, 3, 6, 1, 2, 1, 19, 3))
charSessEntry = MibTableRow((1, 3, 6, 1, 2, 1, 19, 3, 1)).setIndexNames((0, "CHARACTER-MIB", "charSessPortIndex"), (0, "CHARACTER-MIB", "charSessIndex"))
charSessPortIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 3, 1, 1), PortIndex()).setMaxAccess("readonly")
charSessIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 3, 1, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("readonly")
charSessKill = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 3, 1, 3), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,2,)).subtype(namedValues=namedval.NamedValues(("ready", 1), ("execute", 2), ))).setMaxAccess("readwrite")
charSessState = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 3, 1, 4), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,3,1,)).subtype(namedValues=namedval.NamedValues(("connecting", 1), ("connected", 2), ("disconnecting", 3), ))).setMaxAccess("readonly")
charSessProtocol = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 3, 1, 5), AutonomousType()).setMaxAccess("readonly")
charSessOperOrigin = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 3, 1, 6), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,3,2,)).subtype(namedValues=namedval.NamedValues(("unknown", 1), ("network", 2), ("local", 3), ))).setMaxAccess("readonly")
charSessInCharacters = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 3, 1, 7), Counter32()).setMaxAccess("readonly")
charSessOutCharacters = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 3, 1, 8), Counter32()).setMaxAccess("readonly")
charSessConnectionId = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 3, 1, 9), InstancePointer()).setMaxAccess("readonly")
charSessStartTime = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 3, 1, 10), TimeTicks()).setMaxAccess("readonly")
wellKnownProtocols = MibIdentifier((1, 3, 6, 1, 2, 1, 19, 4))
protocolOther = MibIdentifier((1, 3, 6, 1, 2, 1, 19, 4, 1))
protocolTelnet = MibIdentifier((1, 3, 6, 1, 2, 1, 19, 4, 2))
protocolRlogin = MibIdentifier((1, 3, 6, 1, 2, 1, 19, 4, 3))
protocolLat = MibIdentifier((1, 3, 6, 1, 2, 1, 19, 4, 4))
protocolX29 = MibIdentifier((1, 3, 6, 1, 2, 1, 19, 4, 5))
protocolVtp = MibIdentifier((1, 3, 6, 1, 2, 1, 19, 4, 6))
charConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 19, 5))
charGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 19, 5, 1))
charCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 19, 5, 2))

# Augmentions

# Groups

charGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 19, 5, 1, 1)).setObjects(("CHARACTER-MIB", "charPortInCharacters"), ("CHARACTER-MIB", "charPortOutFlowTypes"), ("CHARACTER-MIB", "charPortSessionMaximum"), ("CHARACTER-MIB", "charPortAdminOrigin"), ("CHARACTER-MIB", "charSessProtocol"), ("CHARACTER-MIB", "charSessPortIndex"), ("CHARACTER-MIB", "charSessIndex"), ("CHARACTER-MIB", "charSessInCharacters"), ("CHARACTER-MIB", "charPortOperStatus"), ("CHARACTER-MIB", "charPortSessionIndex"), ("CHARACTER-MIB", "charPortAdminStatus"), ("CHARACTER-MIB", "charPortInFlowState"), ("CHARACTER-MIB", "charSessKill"), ("CHARACTER-MIB", "charPortLastChange"), ("CHARACTER-MIB", "charSessState"), ("CHARACTER-MIB", "charPortOutCharacters"), ("CHARACTER-MIB", "charPortLowerIfIndex"), ("CHARACTER-MIB", "charPortSessionNumber"), ("CHARACTER-MIB", "charPortType"), ("CHARACTER-MIB", "charPortReset"), ("CHARACTER-MIB", "charPortHardware"), ("CHARACTER-MIB", "charPortName"), ("CHARACTER-MIB", "charPortIndex"), ("CHARACTER-MIB", "charSessOperOrigin"), ("CHARACTER-MIB", "charSessOutCharacters"), ("CHARACTER-MIB", "charSessConnectionId"), ("CHARACTER-MIB", "charSessStartTime"), ("CHARACTER-MIB", "charNumber"), ("CHARACTER-MIB", "charPortOutFlowState"), ("CHARACTER-MIB", "charPortInFlowTypes"), )

# Exports

# Types
mibBuilder.exportSymbols("CHARACTER-MIB", PortIndex=PortIndex)

# Objects
mibBuilder.exportSymbols("CHARACTER-MIB", char=char, charNumber=charNumber, charPortTable=charPortTable, charPortEntry=charPortEntry, charPortIndex=charPortIndex, charPortName=charPortName, charPortType=charPortType, charPortHardware=charPortHardware, charPortReset=charPortReset, charPortAdminStatus=charPortAdminStatus, charPortOperStatus=charPortOperStatus, charPortLastChange=charPortLastChange, charPortInFlowType=charPortInFlowType, charPortOutFlowType=charPortOutFlowType, charPortInFlowState=charPortInFlowState, charPortOutFlowState=charPortOutFlowState, charPortInCharacters=charPortInCharacters, charPortOutCharacters=charPortOutCharacters, charPortAdminOrigin=charPortAdminOrigin, charPortSessionMaximum=charPortSessionMaximum, charPortSessionNumber=charPortSessionNumber, charPortSessionIndex=charPortSessionIndex, charPortInFlowTypes=charPortInFlowTypes, charPortOutFlowTypes=charPortOutFlowTypes, charPortLowerIfIndex=charPortLowerIfIndex, charSessTable=charSessTable, charSessEntry=charSessEntry, charSessPortIndex=charSessPortIndex, charSessIndex=charSessIndex, charSessKill=charSessKill, charSessState=charSessState, charSessProtocol=charSessProtocol, charSessOperOrigin=charSessOperOrigin, charSessInCharacters=charSessInCharacters, charSessOutCharacters=charSessOutCharacters, charSessConnectionId=charSessConnectionId, charSessStartTime=charSessStartTime, wellKnownProtocols=wellKnownProtocols, protocolOther=protocolOther, protocolTelnet=protocolTelnet, protocolRlogin=protocolRlogin, protocolLat=protocolLat, protocolX29=protocolX29, protocolVtp=protocolVtp, charConformance=charConformance, charGroups=charGroups, charCompliances=charCompliances)

# Groups
mibBuilder.exportSymbols("CHARACTER-MIB", charGroup=charGroup)
