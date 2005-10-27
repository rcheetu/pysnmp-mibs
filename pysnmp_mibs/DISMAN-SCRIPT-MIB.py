# PySNMP SMI module. Autogenerated from smidump -f python DISMAN-SCRIPT-MIB
# by libsmi2pysnmp-0.0.5-alpha at Fri Oct 28 00:30:34 2005,
# Python version (2, 4, 0, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( SnmpAdminString, ) = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
( ModuleCompliance, NotificationGroup, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
( Bits, Integer32, Integer32, ModuleIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "mib-2")
( DateAndTime, DisplayString, RowStatus, StorageType, TimeInterval, ) = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "DisplayString", "RowStatus", "StorageType", "TimeInterval")

# Objects

scriptMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 64))
smObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 64, 1))
smLangTable = MibTable((1, 3, 6, 1, 2, 1, 64, 1, 1))
smLangEntry = MibTableRow((1, 3, 6, 1, 2, 1, 64, 1, 1, 1)).setIndexNames((0, "DISMAN-SCRIPT-MIB", "smLangIndex"))
smLangIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("noaccess")
smLangLanguage = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 1, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
smLangVersion = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 1, 1, 3), SnmpAdminString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
smLangVendor = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 1, 1, 4), ObjectIdentifier()).setMaxAccess("readonly")
smLangRevision = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 1, 1, 5), SnmpAdminString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
smLangDescr = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 1, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
smExtsnTable = MibTable((1, 3, 6, 1, 2, 1, 64, 1, 2))
smExtsnEntry = MibTableRow((1, 3, 6, 1, 2, 1, 64, 1, 2, 1)).setIndexNames((0, "DISMAN-SCRIPT-MIB", "smLangIndex"), (0, "DISMAN-SCRIPT-MIB", "smExtsnIndex"))
smExtsnIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("noaccess")
smExtsnExtension = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 2, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
smExtsnVersion = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 2, 1, 3), SnmpAdminString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
smExtsnVendor = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 2, 1, 4), ObjectIdentifier()).setMaxAccess("readonly")
smExtsnRevision = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 2, 1, 5), SnmpAdminString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
smExtsnDescr = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 2, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
smScriptObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 64, 1, 3))
smScriptTable = MibTable((1, 3, 6, 1, 2, 1, 64, 1, 3, 1))
smScriptEntry = MibTableRow((1, 3, 6, 1, 2, 1, 64, 1, 3, 1, 1)).setIndexNames((0, "DISMAN-SCRIPT-MIB", "smScriptOwner"), (0, "DISMAN-SCRIPT-MIB", "smScriptName"))
smScriptOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 3, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 32))).setMaxAccess("noaccess")
smScriptName = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 3, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 32))).setMaxAccess("noaccess")
smScriptDescr = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 3, 1, 1, 3), SnmpAdminString()).setMaxAccess("readwrite")
smScriptLanguage = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 2147483647L))).setMaxAccess("readwrite")
smScriptSource = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 3, 1, 1, 5), DisplayString()).setMaxAccess("readwrite")
smScriptAdminStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 3, 1, 1, 6), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,3,1,)).subtype(namedValues=namedval.NamedValues(("enabled", 1), ("disabled", 2), ("editing", 3), )).clone(2)).setMaxAccess("readwrite")
smScriptOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 3, 1, 1, 7), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(14,10,8,13,4,1,12,2,9,5,6,3,11,7,)).subtype(namedValues=namedval.NamedValues(("enabled", 1), ("compilationFailed", 10), ("noResourcesLeft", 11), ("unknownProtocol", 12), ("protocolFailure", 13), ("genericError", 14), ("disabled", 2), ("editing", 3), ("retrieving", 4), ("compiling", 5), ("noSuchScript", 6), ("accessDenied", 7), ("wrongLanguage", 8), ("wrongVersion", 9), )).clone(2)).setMaxAccess("readonly")
smScriptStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 3, 1, 1, 8), StorageType()).setMaxAccess("readwrite")
smScriptRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 3, 1, 1, 9), RowStatus()).setMaxAccess("readwrite")
smScriptError = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 3, 1, 1, 10), SnmpAdminString()).setMaxAccess("readonly")
smScriptLastChange = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 3, 1, 1, 11), DateAndTime()).setMaxAccess("readonly")
smCodeTable = MibTable((1, 3, 6, 1, 2, 1, 64, 1, 3, 2))
smCodeEntry = MibTableRow((1, 3, 6, 1, 2, 1, 64, 1, 3, 2, 1)).setIndexNames((0, "DISMAN-SCRIPT-MIB", "smScriptOwner"), (0, "DISMAN-SCRIPT-MIB", "smScriptName"), (0, "DISMAN-SCRIPT-MIB", "smCodeIndex"))
smCodeIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 3, 2, 1, 1), Unsigned32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 4294967295L))).setMaxAccess("noaccess")
smCodeText = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 3, 2, 1, 2), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 1024))).setMaxAccess("readwrite")
smCodeRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 3, 2, 1, 3), RowStatus()).setMaxAccess("readwrite")
smRunObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 64, 1, 4))
smLaunchTable = MibTable((1, 3, 6, 1, 2, 1, 64, 1, 4, 1))
smLaunchEntry = MibTableRow((1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1)).setIndexNames((0, "DISMAN-SCRIPT-MIB", "smLaunchOwner"), (0, "DISMAN-SCRIPT-MIB", "smLaunchName"))
smLaunchOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 32))).setMaxAccess("noaccess")
smLaunchName = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 32))).setMaxAccess("noaccess")
smLaunchScriptOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 3), SnmpAdminString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
smLaunchScriptName = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 4), SnmpAdminString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 32)).clone('')).setMaxAccess("readwrite")
smLaunchArgument = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 5), OctetString().clone('')).setMaxAccess("readwrite")
smLaunchMaxRunning = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 6), Unsigned32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 4294967295L))).setMaxAccess("readwrite")
smLaunchMaxCompleted = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 7), Unsigned32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 4294967295L))).setMaxAccess("readwrite")
smLaunchLifeTime = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 8), TimeInterval()).setMaxAccess("readwrite")
smLaunchExpireTime = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 9), TimeInterval()).setMaxAccess("readwrite")
smLaunchStart = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 10), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 2147483647L)).clone(0)).setMaxAccess("readwrite")
smLaunchControl = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 11), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,4,3,)).subtype(namedValues=namedval.NamedValues(("abort", 1), ("suspend", 2), ("resume", 3), ("nop", 4), )).clone(4)).setMaxAccess("readwrite")
smLaunchAdminStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 12), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,3,)).subtype(namedValues=namedval.NamedValues(("enabled", 1), ("disabled", 2), ("autostart", 3), )).clone(2)).setMaxAccess("readwrite")
smLaunchOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 13), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,3,1,)).subtype(namedValues=namedval.NamedValues(("enabled", 1), ("disabled", 2), ("expired", 3), )).clone(2)).setMaxAccess("readonly")
smLaunchRunIndexNext = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 14), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("readonly")
smLaunchStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 15), StorageType()).setMaxAccess("readwrite")
smLaunchRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 16), RowStatus()).setMaxAccess("readwrite")
smLaunchError = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 17), SnmpAdminString()).setMaxAccess("readonly")
smLaunchLastChange = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 18), DateAndTime()).setMaxAccess("readonly")
smLaunchRowExpireTime = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 19), TimeInterval()).setMaxAccess("readwrite")
smRunTable = MibTable((1, 3, 6, 1, 2, 1, 64, 1, 4, 2))
smRunEntry = MibTableRow((1, 3, 6, 1, 2, 1, 64, 1, 4, 2, 1)).setIndexNames((0, "DISMAN-SCRIPT-MIB", "smLaunchOwner"), (0, "DISMAN-SCRIPT-MIB", "smLaunchName"), (0, "DISMAN-SCRIPT-MIB", "smRunIndex"))
smRunIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 4, 2, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("noaccess")
smRunArgument = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 4, 2, 1, 2), OctetString().clone('')).setMaxAccess("readonly")
smRunStartTime = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 4, 2, 1, 3), DateAndTime()).setMaxAccess("readonly")
smRunEndTime = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 4, 2, 1, 4), DateAndTime()).setMaxAccess("readonly")
smRunLifeTime = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 4, 2, 1, 5), TimeInterval()).setMaxAccess("readwrite")
smRunExpireTime = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 4, 2, 1, 6), TimeInterval()).setMaxAccess("readwrite")
smRunExitCode = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 4, 2, 1, 7), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(6,7,3,8,2,1,5,4,9,)).subtype(namedValues=namedval.NamedValues(("noError", 1), ("halted", 2), ("lifeTimeExceeded", 3), ("noResourcesLeft", 4), ("languageError", 5), ("runtimeError", 6), ("invalidArgument", 7), ("securityViolation", 8), ("genericError", 9), )).clone(1)).setMaxAccess("readonly")
smRunResult = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 4, 2, 1, 8), OctetString().clone('')).setMaxAccess("readonly")
smRunControl = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 4, 2, 1, 9), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,4,3,)).subtype(namedValues=namedval.NamedValues(("abort", 1), ("suspend", 2), ("resume", 3), ("nop", 4), )).clone(4)).setMaxAccess("readwrite")
smRunState = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 4, 2, 1, 10), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(7,6,3,2,5,4,1,)).subtype(namedValues=namedval.NamedValues(("initializing", 1), ("executing", 2), ("suspending", 3), ("suspended", 4), ("resuming", 5), ("aborting", 6), ("terminated", 7), ))).setMaxAccess("readonly")
smRunError = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 4, 2, 1, 11), SnmpAdminString()).setMaxAccess("readonly")
smRunResultTime = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 4, 2, 1, 12), DateAndTime()).setMaxAccess("readonly")
smRunErrorTime = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 4, 2, 1, 13), DateAndTime()).setMaxAccess("readonly")
smNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 64, 2))
smTraps = MibIdentifier((1, 3, 6, 1, 2, 1, 64, 2, 0))
smConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 64, 3))
smCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 64, 3, 1))
smGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 64, 3, 2))

# Augmentions

# Notifications

smScriptResult = NotificationType((1, 3, 6, 1, 2, 1, 64, 2, 0, 2)).setObjects(("DISMAN-SCRIPT-MIB", "smRunResult"), )
smScriptAbort = NotificationType((1, 3, 6, 1, 2, 1, 64, 2, 0, 1)).setObjects(("DISMAN-SCRIPT-MIB", "smRunEndTime"), ("DISMAN-SCRIPT-MIB", "smRunExitCode"), ("DISMAN-SCRIPT-MIB", "smRunError"), )
smScriptException = NotificationType((1, 3, 6, 1, 2, 1, 64, 2, 0, 3)).setObjects(("DISMAN-SCRIPT-MIB", "smRunError"), )

# Groups

smScriptGroup2 = ObjectGroup((1, 3, 6, 1, 2, 1, 64, 3, 2, 7)).setObjects(("DISMAN-SCRIPT-MIB", "smScriptLastChange"), ("DISMAN-SCRIPT-MIB", "smScriptSource"), ("DISMAN-SCRIPT-MIB", "smScriptDescr"), ("DISMAN-SCRIPT-MIB", "smScriptError"), ("DISMAN-SCRIPT-MIB", "smScriptOperStatus"), ("DISMAN-SCRIPT-MIB", "smScriptLanguage"), ("DISMAN-SCRIPT-MIB", "smScriptRowStatus"), ("DISMAN-SCRIPT-MIB", "smScriptAdminStatus"), ("DISMAN-SCRIPT-MIB", "smScriptStorageType"), )
smNotificationsGroup2 = ObjectGroup((1, 3, 6, 1, 2, 1, 64, 3, 2, 10)).setObjects(("DISMAN-SCRIPT-MIB", "smScriptResult"), ("DISMAN-SCRIPT-MIB", "smScriptAbort"), ("DISMAN-SCRIPT-MIB", "smScriptException"), )
smLaunchGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 64, 3, 2, 4)).setObjects(("DISMAN-SCRIPT-MIB", "smLaunchExpireTime"), ("DISMAN-SCRIPT-MIB", "smLaunchRunIndexNext"), ("DISMAN-SCRIPT-MIB", "smLaunchLifeTime"), ("DISMAN-SCRIPT-MIB", "smLaunchArgument"), ("DISMAN-SCRIPT-MIB", "smLaunchScriptOwner"), ("DISMAN-SCRIPT-MIB", "smLaunchOperStatus"), ("DISMAN-SCRIPT-MIB", "smLaunchStart"), ("DISMAN-SCRIPT-MIB", "smLaunchScriptName"), ("DISMAN-SCRIPT-MIB", "smLaunchRowStatus"), ("DISMAN-SCRIPT-MIB", "smLaunchControl"), ("DISMAN-SCRIPT-MIB", "smLaunchMaxRunning"), ("DISMAN-SCRIPT-MIB", "smLaunchAdminStatus"), ("DISMAN-SCRIPT-MIB", "smLaunchMaxCompleted"), ("DISMAN-SCRIPT-MIB", "smLaunchStorageType"), )
smRunGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 64, 3, 2, 5)).setObjects(("DISMAN-SCRIPT-MIB", "smRunArgument"), ("DISMAN-SCRIPT-MIB", "smRunControl"), ("DISMAN-SCRIPT-MIB", "smRunLifeTime"), ("DISMAN-SCRIPT-MIB", "smRunEndTime"), ("DISMAN-SCRIPT-MIB", "smRunResult"), ("DISMAN-SCRIPT-MIB", "smRunState"), ("DISMAN-SCRIPT-MIB", "smRunError"), ("DISMAN-SCRIPT-MIB", "smRunStartTime"), ("DISMAN-SCRIPT-MIB", "smRunExpireTime"), ("DISMAN-SCRIPT-MIB", "smRunExitCode"), )
smCodeGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 64, 3, 2, 3)).setObjects(("DISMAN-SCRIPT-MIB", "smCodeRowStatus"), ("DISMAN-SCRIPT-MIB", "smCodeText"), )
smLaunchGroup2 = ObjectGroup((1, 3, 6, 1, 2, 1, 64, 3, 2, 8)).setObjects(("DISMAN-SCRIPT-MIB", "smLaunchExpireTime"), ("DISMAN-SCRIPT-MIB", "smLaunchRunIndexNext"), ("DISMAN-SCRIPT-MIB", "smLaunchLifeTime"), ("DISMAN-SCRIPT-MIB", "smLaunchArgument"), ("DISMAN-SCRIPT-MIB", "smLaunchScriptOwner"), ("DISMAN-SCRIPT-MIB", "smLaunchError"), ("DISMAN-SCRIPT-MIB", "smLaunchOperStatus"), ("DISMAN-SCRIPT-MIB", "smLaunchStart"), ("DISMAN-SCRIPT-MIB", "smLaunchScriptName"), ("DISMAN-SCRIPT-MIB", "smLaunchRowStatus"), ("DISMAN-SCRIPT-MIB", "smLaunchControl"), ("DISMAN-SCRIPT-MIB", "smLaunchMaxRunning"), ("DISMAN-SCRIPT-MIB", "smLaunchRowExpireTime"), ("DISMAN-SCRIPT-MIB", "smLaunchLastChange"), ("DISMAN-SCRIPT-MIB", "smLaunchAdminStatus"), ("DISMAN-SCRIPT-MIB", "smLaunchMaxCompleted"), ("DISMAN-SCRIPT-MIB", "smLaunchStorageType"), )
smScriptGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 64, 3, 2, 2)).setObjects(("DISMAN-SCRIPT-MIB", "smScriptSource"), ("DISMAN-SCRIPT-MIB", "smScriptDescr"), ("DISMAN-SCRIPT-MIB", "smScriptOperStatus"), ("DISMAN-SCRIPT-MIB", "smScriptLanguage"), ("DISMAN-SCRIPT-MIB", "smScriptRowStatus"), ("DISMAN-SCRIPT-MIB", "smScriptAdminStatus"), ("DISMAN-SCRIPT-MIB", "smScriptStorageType"), )
smNotificationsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 64, 3, 2, 6)).setObjects(("DISMAN-SCRIPT-MIB", "smScriptResult"), ("DISMAN-SCRIPT-MIB", "smScriptAbort"), )
smRunGroup2 = ObjectGroup((1, 3, 6, 1, 2, 1, 64, 3, 2, 9)).setObjects(("DISMAN-SCRIPT-MIB", "smRunArgument"), ("DISMAN-SCRIPT-MIB", "smRunErrorTime"), ("DISMAN-SCRIPT-MIB", "smRunControl"), ("DISMAN-SCRIPT-MIB", "smRunLifeTime"), ("DISMAN-SCRIPT-MIB", "smRunEndTime"), ("DISMAN-SCRIPT-MIB", "smRunResult"), ("DISMAN-SCRIPT-MIB", "smRunState"), ("DISMAN-SCRIPT-MIB", "smRunError"), ("DISMAN-SCRIPT-MIB", "smRunStartTime"), ("DISMAN-SCRIPT-MIB", "smRunResultTime"), ("DISMAN-SCRIPT-MIB", "smRunExpireTime"), ("DISMAN-SCRIPT-MIB", "smRunExitCode"), )
smLanguageGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 64, 3, 2, 1)).setObjects(("DISMAN-SCRIPT-MIB", "smExtsnVersion"), ("DISMAN-SCRIPT-MIB", "smExtsnExtension"), ("DISMAN-SCRIPT-MIB", "smLangVersion"), ("DISMAN-SCRIPT-MIB", "smLangLanguage"), ("DISMAN-SCRIPT-MIB", "smExtsnVendor"), ("DISMAN-SCRIPT-MIB", "smExtsnDescr"), ("DISMAN-SCRIPT-MIB", "smLangRevision"), ("DISMAN-SCRIPT-MIB", "smLangDescr"), ("DISMAN-SCRIPT-MIB", "smExtsnRevision"), ("DISMAN-SCRIPT-MIB", "smLangVendor"), )

# Exports

# Objects
mibBuilder.exportSymbols("DISMAN-SCRIPT-MIB", scriptMIB=scriptMIB, smObjects=smObjects, smLangTable=smLangTable, smLangEntry=smLangEntry, smLangIndex=smLangIndex, smLangLanguage=smLangLanguage, smLangVersion=smLangVersion, smLangVendor=smLangVendor, smLangRevision=smLangRevision, smLangDescr=smLangDescr, smExtsnTable=smExtsnTable, smExtsnEntry=smExtsnEntry, smExtsnIndex=smExtsnIndex, smExtsnExtension=smExtsnExtension, smExtsnVersion=smExtsnVersion, smExtsnVendor=smExtsnVendor, smExtsnRevision=smExtsnRevision, smExtsnDescr=smExtsnDescr, smScriptObjects=smScriptObjects, smScriptTable=smScriptTable, smScriptEntry=smScriptEntry, smScriptOwner=smScriptOwner, smScriptName=smScriptName, smScriptDescr=smScriptDescr, smScriptLanguage=smScriptLanguage, smScriptSource=smScriptSource, smScriptAdminStatus=smScriptAdminStatus, smScriptOperStatus=smScriptOperStatus, smScriptStorageType=smScriptStorageType, smScriptRowStatus=smScriptRowStatus, smScriptError=smScriptError, smScriptLastChange=smScriptLastChange, smCodeTable=smCodeTable, smCodeEntry=smCodeEntry, smCodeIndex=smCodeIndex, smCodeText=smCodeText, smCodeRowStatus=smCodeRowStatus, smRunObjects=smRunObjects, smLaunchTable=smLaunchTable, smLaunchEntry=smLaunchEntry, smLaunchOwner=smLaunchOwner, smLaunchName=smLaunchName, smLaunchScriptOwner=smLaunchScriptOwner, smLaunchScriptName=smLaunchScriptName, smLaunchArgument=smLaunchArgument, smLaunchMaxRunning=smLaunchMaxRunning, smLaunchMaxCompleted=smLaunchMaxCompleted, smLaunchLifeTime=smLaunchLifeTime, smLaunchExpireTime=smLaunchExpireTime, smLaunchStart=smLaunchStart, smLaunchControl=smLaunchControl, smLaunchAdminStatus=smLaunchAdminStatus, smLaunchOperStatus=smLaunchOperStatus, smLaunchRunIndexNext=smLaunchRunIndexNext, smLaunchStorageType=smLaunchStorageType, smLaunchRowStatus=smLaunchRowStatus, smLaunchError=smLaunchError, smLaunchLastChange=smLaunchLastChange, smLaunchRowExpireTime=smLaunchRowExpireTime, smRunTable=smRunTable, smRunEntry=smRunEntry, smRunIndex=smRunIndex, smRunArgument=smRunArgument, smRunStartTime=smRunStartTime, smRunEndTime=smRunEndTime, smRunLifeTime=smRunLifeTime, smRunExpireTime=smRunExpireTime, smRunExitCode=smRunExitCode, smRunResult=smRunResult, smRunControl=smRunControl, smRunState=smRunState, smRunError=smRunError, smRunResultTime=smRunResultTime, smRunErrorTime=smRunErrorTime, smNotifications=smNotifications, smTraps=smTraps, smConformance=smConformance, smCompliances=smCompliances, smGroups=smGroups)

# Notifications
mibBuilder.exportSymbols("DISMAN-SCRIPT-MIB", smScriptResult=smScriptResult, smScriptAbort=smScriptAbort, smScriptException=smScriptException)

# Groups
mibBuilder.exportSymbols("DISMAN-SCRIPT-MIB", smScriptGroup2=smScriptGroup2, smNotificationsGroup2=smNotificationsGroup2, smLaunchGroup=smLaunchGroup, smRunGroup=smRunGroup, smCodeGroup=smCodeGroup, smLaunchGroup2=smLaunchGroup2, smScriptGroup=smScriptGroup, smNotificationsGroup=smNotificationsGroup, smRunGroup2=smRunGroup2, smLanguageGroup=smLanguageGroup)
