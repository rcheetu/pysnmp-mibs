# PySNMP SMI module. Autogenerated from smidump -f python DIFFSERV-CONFIG-MIB
# by libsmi2pysnmp-0.0.5-alpha at Fri Oct 28 00:30:33 2005,
# Python version (2, 4, 0, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( SnmpAdminString, ) = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, mib_2, zeroDotZero, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "mib-2", "zeroDotZero")
( DateAndTime, RowPointer, RowStatus, StorageType, ) = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "RowPointer", "RowStatus", "StorageType")

# Objects

diffServConfigMib = ModuleIdentity((1, 3, 6, 1, 2, 1, 108))
diffServConfigMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 108, 1))
diffServConfigTable = MibTable((1, 3, 6, 1, 2, 1, 108, 1, 2))
diffServConfigEntry = MibTableRow((1, 3, 6, 1, 2, 1, 108, 1, 2, 1)).setIndexNames((0, "DIFFSERV-CONFIG-MIB", "diffServConfigId"))
diffServConfigId = MibTableColumn((1, 3, 6, 1, 2, 1, 108, 1, 2, 1, 1), SnmpAdminString().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 116))).setMaxAccess("noaccess")
diffServConfigDescr = MibTableColumn((1, 3, 6, 1, 2, 1, 108, 1, 2, 1, 2), SnmpAdminString()).setMaxAccess("readwrite")
diffServConfigOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 108, 1, 2, 1, 3), SnmpAdminString()).setMaxAccess("readwrite")
diffServConfigLastChange = MibTableColumn((1, 3, 6, 1, 2, 1, 108, 1, 2, 1, 4), DateAndTime()).setMaxAccess("readonly")
diffServConfigStart = MibTableColumn((1, 3, 6, 1, 2, 1, 108, 1, 2, 1, 5), RowPointer()).setMaxAccess("readwrite")
diffServConfigStorage = MibTableColumn((1, 3, 6, 1, 2, 1, 108, 1, 2, 1, 6), StorageType()).setMaxAccess("readwrite")
diffServConfigStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 108, 1, 2, 1, 7), RowStatus()).setMaxAccess("readwrite")
diffServConfigMIBConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 108, 2))
diffServConfigMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 108, 2, 1))
diffServConfigMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 108, 2, 2))

# Augmentions

# Groups

diffServConfigMIBConfigGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 108, 2, 2, 1)).setObjects(("DIFFSERV-CONFIG-MIB", "diffServConfigDescr"), ("DIFFSERV-CONFIG-MIB", "diffServConfigStatus"), ("DIFFSERV-CONFIG-MIB", "diffServConfigStorage"), ("DIFFSERV-CONFIG-MIB", "diffServConfigLastChange"), ("DIFFSERV-CONFIG-MIB", "diffServConfigOwner"), ("DIFFSERV-CONFIG-MIB", "diffServConfigStart"), )

# Exports

# Objects
mibBuilder.exportSymbols("DIFFSERV-CONFIG-MIB", diffServConfigMib=diffServConfigMib, diffServConfigMIBObjects=diffServConfigMIBObjects, diffServConfigTable=diffServConfigTable, diffServConfigEntry=diffServConfigEntry, diffServConfigId=diffServConfigId, diffServConfigDescr=diffServConfigDescr, diffServConfigOwner=diffServConfigOwner, diffServConfigLastChange=diffServConfigLastChange, diffServConfigStart=diffServConfigStart, diffServConfigStorage=diffServConfigStorage, diffServConfigStatus=diffServConfigStatus, diffServConfigMIBConformance=diffServConfigMIBConformance, diffServConfigMIBCompliances=diffServConfigMIBCompliances, diffServConfigMIBGroups=diffServConfigMIBGroups)

# Groups
mibBuilder.exportSymbols("DIFFSERV-CONFIG-MIB", diffServConfigMIBConfigGroup=diffServConfigMIBConfigGroup)
