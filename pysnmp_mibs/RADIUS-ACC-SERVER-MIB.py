# PySNMP SMI module. Autogenerated from smidump -f python RADIUS-ACC-SERVER-MIB
# by libsmi2pysnmp-0.0.5-alpha at Fri Oct 28 00:30:49 2005,
# Python version (2, 4, 0, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( SnmpAdminString, ) = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Counter32, Integer32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, TimeTicks, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Integer32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "TimeTicks", "mib-2")

# Objects

radiusMIB = MibIdentifier((1, 3, 6, 1, 2, 1, 67))
radiusAccounting = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 2))
radiusAccServMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 67, 2, 1))
radiusAccServMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 2, 1, 1))
radiusAccServ = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1))
radiusAccServIdent = MibScalar((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 1), SnmpAdminString()).setMaxAccess("readonly")
radiusAccServUpTime = MibScalar((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 2), TimeTicks()).setMaxAccess("readonly")
radiusAccServResetTime = MibScalar((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 3), TimeTicks()).setMaxAccess("readonly")
radiusAccServConfigReset = MibScalar((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 4), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,3,4,1,)).subtype(namedValues=namedval.NamedValues(("other", 1), ("reset", 2), ("initializing", 3), ("running", 4), ))).setMaxAccess("readwrite")
radiusAccServTotalRequests = MibScalar((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 5), Counter32()).setMaxAccess("readonly")
radiusAccServTotalInvalidRequests = MibScalar((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 6), Counter32()).setMaxAccess("readonly")
radiusAccServTotalDupRequests = MibScalar((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly")
radiusAccServTotalResponses = MibScalar((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
radiusAccServTotalMalformedRequests = MibScalar((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 9), Counter32()).setMaxAccess("readonly")
radiusAccServTotalBadAuthenticators = MibScalar((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 10), Counter32()).setMaxAccess("readonly")
radiusAccServTotalPacketsDropped = MibScalar((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 11), Counter32()).setMaxAccess("readonly")
radiusAccServTotalNoRecords = MibScalar((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 12), Counter32()).setMaxAccess("readonly")
radiusAccServTotalUnknownTypes = MibScalar((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 13), Counter32()).setMaxAccess("readonly")
radiusAccClientTable = MibTable((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14))
radiusAccClientEntry = MibTableRow((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1)).setIndexNames((0, "RADIUS-ACC-SERVER-MIB", "radiusAccClientIndex"))
radiusAccClientIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("noaccess")
radiusAccClientAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1, 2), IpAddress()).setMaxAccess("readonly")
radiusAccClientID = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
radiusAccServPacketsDropped = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1, 4), Counter32()).setMaxAccess("readonly")
radiusAccServRequests = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1, 5), Counter32()).setMaxAccess("readonly")
radiusAccServDupRequests = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1, 6), Counter32()).setMaxAccess("readonly")
radiusAccServResponses = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1, 7), Counter32()).setMaxAccess("readonly")
radiusAccServBadAuthenticators = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1, 8), Counter32()).setMaxAccess("readonly")
radiusAccServMalformedRequests = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1, 9), Counter32()).setMaxAccess("readonly")
radiusAccServNoRecords = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1, 10), Counter32()).setMaxAccess("readonly")
radiusAccServUnknownTypes = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 2, 1, 1, 1, 14, 1, 11), Counter32()).setMaxAccess("readonly")
radiusAccServMIBConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 2, 1, 2))
radiusAccServMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 2, 1, 2, 1))
radiusAccServMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 2, 1, 2, 2))

# Augmentions

# Groups

radiusAccServMIBGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 67, 2, 1, 2, 2, 1)).setObjects(("RADIUS-ACC-SERVER-MIB", "radiusAccServResetTime"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServDupRequests"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServMalformedRequests"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalBadAuthenticators"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalUnknownTypes"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServIdent"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalMalformedRequests"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalDupRequests"), ("RADIUS-ACC-SERVER-MIB", "radiusAccClientAddress"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServConfigReset"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServUpTime"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalResponses"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServRequests"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServBadAuthenticators"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServResponses"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServPacketsDropped"), ("RADIUS-ACC-SERVER-MIB", "radiusAccClientID"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServNoRecords"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServUnknownTypes"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalRequests"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalPacketsDropped"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalInvalidRequests"), ("RADIUS-ACC-SERVER-MIB", "radiusAccServTotalNoRecords"), )

# Exports

# Objects
mibBuilder.exportSymbols("RADIUS-ACC-SERVER-MIB", radiusMIB=radiusMIB, radiusAccounting=radiusAccounting, radiusAccServMIB=radiusAccServMIB, radiusAccServMIBObjects=radiusAccServMIBObjects, radiusAccServ=radiusAccServ, radiusAccServIdent=radiusAccServIdent, radiusAccServUpTime=radiusAccServUpTime, radiusAccServResetTime=radiusAccServResetTime, radiusAccServConfigReset=radiusAccServConfigReset, radiusAccServTotalRequests=radiusAccServTotalRequests, radiusAccServTotalInvalidRequests=radiusAccServTotalInvalidRequests, radiusAccServTotalDupRequests=radiusAccServTotalDupRequests, radiusAccServTotalResponses=radiusAccServTotalResponses, radiusAccServTotalMalformedRequests=radiusAccServTotalMalformedRequests, radiusAccServTotalBadAuthenticators=radiusAccServTotalBadAuthenticators, radiusAccServTotalPacketsDropped=radiusAccServTotalPacketsDropped, radiusAccServTotalNoRecords=radiusAccServTotalNoRecords, radiusAccServTotalUnknownTypes=radiusAccServTotalUnknownTypes, radiusAccClientTable=radiusAccClientTable, radiusAccClientEntry=radiusAccClientEntry, radiusAccClientIndex=radiusAccClientIndex, radiusAccClientAddress=radiusAccClientAddress, radiusAccClientID=radiusAccClientID, radiusAccServPacketsDropped=radiusAccServPacketsDropped, radiusAccServRequests=radiusAccServRequests, radiusAccServDupRequests=radiusAccServDupRequests, radiusAccServResponses=radiusAccServResponses, radiusAccServBadAuthenticators=radiusAccServBadAuthenticators, radiusAccServMalformedRequests=radiusAccServMalformedRequests, radiusAccServNoRecords=radiusAccServNoRecords, radiusAccServUnknownTypes=radiusAccServUnknownTypes, radiusAccServMIBConformance=radiusAccServMIBConformance, radiusAccServMIBCompliances=radiusAccServMIBCompliances, radiusAccServMIBGroups=radiusAccServMIBGroups)

# Groups
mibBuilder.exportSymbols("RADIUS-ACC-SERVER-MIB", radiusAccServMIBGroup=radiusAccServMIBGroup)
