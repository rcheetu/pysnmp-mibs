# PySNMP SMI module. Autogenerated from smidump -f python POWER-ETHERNET-MIB
# by libsmi2pysnmp-0.0.5-alpha at Fri Oct 28 00:30:47 2005,
# Python version (2, 4, 0, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( SnmpAdminString, ) = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
( ModuleCompliance, NotificationGroup, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
( Bits, Counter32, Gauge32, Integer32, Integer32, ModuleIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Gauge32", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "mib-2")
( TruthValue, ) = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue")

# Objects

powerEthernetMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 105))
pethNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 105, 0))
pethObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 105, 1))
pethPsePortTable = MibTable((1, 3, 6, 1, 2, 1, 105, 1, 1))
pethPsePortEntry = MibTableRow((1, 3, 6, 1, 2, 1, 105, 1, 1, 1)).setIndexNames((0, "POWER-ETHERNET-MIB", "pethPsePortGroupIndex"), (0, "POWER-ETHERNET-MIB", "pethPsePortIndex"))
pethPsePortGroupIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("noaccess")
pethPsePortIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("noaccess")
pethPsePortAdminEnable = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 1, 1, 3), TruthValue()).setMaxAccess("readwrite")
pethPsePortPowerPairsControlAbility = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 1, 1, 4), TruthValue()).setMaxAccess("readonly")
pethPsePortPowerPairs = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 1, 1, 5), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,2,)).subtype(namedValues=namedval.NamedValues(("signal", 1), ("spare", 2), ))).setMaxAccess("readwrite")
pethPsePortDetectionStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 1, 1, 6), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(6,4,2,3,1,5,)).subtype(namedValues=namedval.NamedValues(("disabled", 1), ("searching", 2), ("deliveringPower", 3), ("fault", 4), ("test", 5), ("otherFault", 6), ))).setMaxAccess("readonly")
pethPsePortPowerPriority = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 1, 1, 7), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,3,)).subtype(namedValues=namedval.NamedValues(("critical", 1), ("high", 2), ("low", 3), ))).setMaxAccess("readwrite")
pethPsePortMPSAbsentCounter = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
pethPsePortType = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 1, 1, 9), SnmpAdminString()).setMaxAccess("readwrite")
pethPsePortPowerClassifications = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 1, 1, 10), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(5,3,4,1,2,)).subtype(namedValues=namedval.NamedValues(("class0", 1), ("class1", 2), ("class2", 3), ("class3", 4), ("class4", 5), ))).setMaxAccess("readonly")
pethPsePortInvalidSignatureCounter = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 1, 1, 11), Counter32()).setMaxAccess("readonly")
pethPsePortPowerDeniedCounter = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 1, 1, 12), Counter32()).setMaxAccess("readonly")
pethPsePortOverLoadCounter = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 1, 1, 13), Counter32()).setMaxAccess("readonly")
pethPsePortShortCounter = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 1, 1, 14), Counter32()).setMaxAccess("readonly")
pethMainPseObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 105, 1, 3))
pethMainPseTable = MibTable((1, 3, 6, 1, 2, 1, 105, 1, 3, 1))
pethMainPseEntry = MibTableRow((1, 3, 6, 1, 2, 1, 105, 1, 3, 1, 1)).setIndexNames((0, "POWER-ETHERNET-MIB", "pethMainPseGroupIndex"))
pethMainPseGroupIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("noaccess")
pethMainPsePower = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 3, 1, 1, 2), Gauge32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
pethMainPseOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 3, 1, 1, 3), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,3,2,)).subtype(namedValues=namedval.NamedValues(("on", 1), ("off", 2), ("faulty", 3), ))).setMaxAccess("readonly")
pethMainPseConsumptionPower = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 3, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
pethMainPseUsageThreshold = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 99))).setMaxAccess("readwrite")
pethNotificationControl = MibIdentifier((1, 3, 6, 1, 2, 1, 105, 1, 4))
pethNotificationControlTable = MibTable((1, 3, 6, 1, 2, 1, 105, 1, 4, 1))
pethNotificationControlEntry = MibTableRow((1, 3, 6, 1, 2, 1, 105, 1, 4, 1, 1)).setIndexNames((0, "POWER-ETHERNET-MIB", "pethNotificationControlGroupIndex"))
pethNotificationControlGroupIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("noaccess")
pethNotificationControlEnable = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 4, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
pethConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 105, 2))
pethCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 105, 2, 1))
pethGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 105, 2, 2))

# Augmentions

# Notifications

pethPsePortOnOffNotification = NotificationType((1, 3, 6, 1, 2, 1, 105, 0, 1)).setObjects(("POWER-ETHERNET-MIB", "pethPsePortDetectionStatus"), )
pethMainPowerUsageOnNotification = NotificationType((1, 3, 6, 1, 2, 1, 105, 0, 2)).setObjects(("POWER-ETHERNET-MIB", "pethMainPseConsumptionPower"), )
pethMainPowerUsageOffNotification = NotificationType((1, 3, 6, 1, 2, 1, 105, 0, 3)).setObjects(("POWER-ETHERNET-MIB", "pethMainPseConsumptionPower"), )

# Groups

pethPsePortNotificationGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 105, 2, 2, 4)).setObjects(("POWER-ETHERNET-MIB", "pethPsePortOnOffNotification"), )
pethMainPowerNotificationGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 105, 2, 2, 5)).setObjects(("POWER-ETHERNET-MIB", "pethMainPowerUsageOffNotification"), ("POWER-ETHERNET-MIB", "pethMainPowerUsageOnNotification"), )
pethMainPseGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 105, 2, 2, 2)).setObjects(("POWER-ETHERNET-MIB", "pethMainPseUsageThreshold"), ("POWER-ETHERNET-MIB", "pethMainPseOperStatus"), ("POWER-ETHERNET-MIB", "pethMainPsePower"), ("POWER-ETHERNET-MIB", "pethMainPseConsumptionPower"), )
pethNotificationControlGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 105, 2, 2, 3)).setObjects(("POWER-ETHERNET-MIB", "pethNotificationControlEnable"), )
pethPsePortGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 105, 2, 2, 1)).setObjects(("POWER-ETHERNET-MIB", "pethPsePortPowerPairsControlAbility"), ("POWER-ETHERNET-MIB", "pethPsePortShortCounter"), ("POWER-ETHERNET-MIB", "pethPsePortPowerPriority"), ("POWER-ETHERNET-MIB", "pethPsePortDetectionStatus"), ("POWER-ETHERNET-MIB", "pethPsePortAdminEnable"), ("POWER-ETHERNET-MIB", "pethPsePortType"), ("POWER-ETHERNET-MIB", "pethPsePortOverLoadCounter"), ("POWER-ETHERNET-MIB", "pethPsePortPowerDeniedCounter"), ("POWER-ETHERNET-MIB", "pethPsePortPowerClassifications"), ("POWER-ETHERNET-MIB", "pethPsePortPowerPairs"), ("POWER-ETHERNET-MIB", "pethPsePortMPSAbsentCounter"), ("POWER-ETHERNET-MIB", "pethPsePortInvalidSignatureCounter"), )

# Exports

# Objects
mibBuilder.exportSymbols("POWER-ETHERNET-MIB", powerEthernetMIB=powerEthernetMIB, pethNotifications=pethNotifications, pethObjects=pethObjects, pethPsePortTable=pethPsePortTable, pethPsePortEntry=pethPsePortEntry, pethPsePortGroupIndex=pethPsePortGroupIndex, pethPsePortIndex=pethPsePortIndex, pethPsePortAdminEnable=pethPsePortAdminEnable, pethPsePortPowerPairsControlAbility=pethPsePortPowerPairsControlAbility, pethPsePortPowerPairs=pethPsePortPowerPairs, pethPsePortDetectionStatus=pethPsePortDetectionStatus, pethPsePortPowerPriority=pethPsePortPowerPriority, pethPsePortMPSAbsentCounter=pethPsePortMPSAbsentCounter, pethPsePortType=pethPsePortType, pethPsePortPowerClassifications=pethPsePortPowerClassifications, pethPsePortInvalidSignatureCounter=pethPsePortInvalidSignatureCounter, pethPsePortPowerDeniedCounter=pethPsePortPowerDeniedCounter, pethPsePortOverLoadCounter=pethPsePortOverLoadCounter, pethPsePortShortCounter=pethPsePortShortCounter, pethMainPseObjects=pethMainPseObjects, pethMainPseTable=pethMainPseTable, pethMainPseEntry=pethMainPseEntry, pethMainPseGroupIndex=pethMainPseGroupIndex, pethMainPsePower=pethMainPsePower, pethMainPseOperStatus=pethMainPseOperStatus, pethMainPseConsumptionPower=pethMainPseConsumptionPower, pethMainPseUsageThreshold=pethMainPseUsageThreshold, pethNotificationControl=pethNotificationControl, pethNotificationControlTable=pethNotificationControlTable, pethNotificationControlEntry=pethNotificationControlEntry, pethNotificationControlGroupIndex=pethNotificationControlGroupIndex, pethNotificationControlEnable=pethNotificationControlEnable, pethConformance=pethConformance, pethCompliances=pethCompliances, pethGroups=pethGroups)

# Notifications
mibBuilder.exportSymbols("POWER-ETHERNET-MIB", pethPsePortOnOffNotification=pethPsePortOnOffNotification, pethMainPowerUsageOnNotification=pethMainPowerUsageOnNotification, pethMainPowerUsageOffNotification=pethMainPowerUsageOffNotification)

# Groups
mibBuilder.exportSymbols("POWER-ETHERNET-MIB", pethPsePortNotificationGroup=pethPsePortNotificationGroup, pethMainPowerNotificationGroup=pethMainPowerNotificationGroup, pethMainPseGroup=pethMainPseGroup, pethNotificationControlGroup=pethNotificationControlGroup, pethPsePortGroup=pethPsePortGroup)
