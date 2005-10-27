# PySNMP SMI module. Autogenerated from smidump -f python IPOA-MIB
# by libsmi2pysnmp-0.0.5-alpha at Fri Oct 28 00:30:42 2005,
# Python version (2, 4, 0, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( InterfaceIndex, InterfaceIndexOrZero, ) = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "InterfaceIndexOrZero")
( ipAdEntAddr, ipNetToMediaIfIndex, ipNetToMediaNetAddress, ipNetToMediaPhysAddress, ) = mibBuilder.importSymbols("IP-MIB", "ipAdEntAddr", "ipNetToMediaIfIndex", "ipNetToMediaNetAddress", "ipNetToMediaPhysAddress")
( ModuleCompliance, NotificationGroup, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
( Bits, Counter32, Gauge32, Integer32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, transmission, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Gauge32", "Integer32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "transmission")
( RowStatus, TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention")

# Types

class IpoaAtmAddr(TextualConvention, OctetString):
    subtypeSpec = OctetString.subtypeSpec+constraint.ValueSizeConstraint(0,40)
    pass

class IpoaAtmConnKind(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(4,2,5,1,3,)
    namedValues = namedval.NamedValues(("pvc", 1), ("svcIncoming", 2), ("svcOutgoing", 3), ("spvcInitiator", 4), ("spvcTarget", 5), )
    pass

class IpoaEncapsType(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(3,1,2,)
    namedValues = namedval.NamedValues(("llcSnap", 1), ("vcMuxed", 2), ("other", 3), )
    pass

class IpoaVciInteger(Integer32):
    subtypeSpec = Integer32.subtypeSpec+constraint.ValueRangeConstraint(0,65535)
    pass

class IpoaVpiInteger(Integer32):
    subtypeSpec = Integer32.subtypeSpec+constraint.ValueRangeConstraint(0,255)
    pass


# Objects

ipoaMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 46))
ipoaObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 46, 1))
ipoaLisTrapEnable = MibScalar((1, 3, 6, 1, 2, 1, 10, 46, 1, 1), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("enabled", 1), ("disabled", 2), ))).setMaxAccess("readwrite")
ipoaLisTable = MibTable((1, 3, 6, 1, 2, 1, 10, 46, 1, 2))
ipoaLisEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 46, 1, 2, 1)).setIndexNames((0, "IPOA-MIB", "ipoaLisSubnetAddr"))
ipoaLisSubnetAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 2, 1, 1), IpAddress()).setMaxAccess("readonly")
ipoaLisDefaultMtu = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535)).clone(9180)).setMaxAccess("readwrite")
ipoaLisDefaultEncapsType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 2, 1, 3), IpoaEncapsType()).setMaxAccess("readwrite")
ipoaLisInactivityTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 2, 1, 4), Integer32().clone(1200)).setMaxAccess("readwrite")
ipoaLisMinHoldingTime = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535)).clone(60)).setMaxAccess("readwrite")
ipoaLisQDepth = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535)).clone(1)).setMaxAccess("readwrite")
ipoaLisMaxCalls = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535)).clone(500)).setMaxAccess("readwrite")
ipoaLisCacheEntryAge = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(60, 1200)).clone(900)).setMaxAccess("readwrite")
ipoaLisRetries = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 10)).clone(2)).setMaxAccess("readwrite")
ipoaLisTimeout = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 2, 1, 10), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 60)).clone(10)).setMaxAccess("readwrite")
ipoaLisDefaultPeakCellRate = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 2, 1, 11), Integer32()).setMaxAccess("readwrite")
ipoaLisActiveVcs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 2, 1, 12), Gauge32()).setMaxAccess("readonly")
ipoaLisRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 2, 1, 13), RowStatus()).setMaxAccess("readwrite")
ipoaLisIfMappingTable = MibTable((1, 3, 6, 1, 2, 1, 10, 46, 1, 3))
ipoaLisIfMappingEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 46, 1, 3, 1)).setIndexNames((0, "IPOA-MIB", "ipoaLisSubnetAddr"), (0, "IPOA-MIB", "ipoaLisIfMappingIfIndex"))
ipoaLisIfMappingIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 3, 1, 1), InterfaceIndex()).setMaxAccess("noaccess")
ipoaLisIfMappingRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 3, 1, 2), RowStatus()).setMaxAccess("readwrite")
ipoaArpClientTable = MibTable((1, 3, 6, 1, 2, 1, 10, 46, 1, 4))
ipoaArpClientEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1)).setIndexNames((0, "IP-MIB", "ipAdEntAddr"))
ipoaArpClientAtmAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1, 1), IpoaAtmAddr()).setMaxAccess("readwrite")
ipoaArpClientSrvrInUse = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1, 2), IpoaAtmAddr()).setMaxAccess("readonly")
ipoaArpClientInArpInReqs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1, 3), Counter32()).setMaxAccess("readonly")
ipoaArpClientInArpOutReqs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1, 4), Counter32()).setMaxAccess("readonly")
ipoaArpClientInArpInReplies = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1, 5), Counter32()).setMaxAccess("readonly")
ipoaArpClientInArpOutReplies = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1, 6), Counter32()).setMaxAccess("readonly")
ipoaArpClientInArpInvalidInReqs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1, 7), Counter32()).setMaxAccess("readonly")
ipoaArpClientInArpInvalidOutReqs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1, 8), Counter32()).setMaxAccess("readonly")
ipoaArpClientArpInReqs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1, 9), Counter32()).setMaxAccess("readonly")
ipoaArpClientArpOutReqs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1, 10), Counter32()).setMaxAccess("readonly")
ipoaArpClientArpInReplies = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1, 11), Counter32()).setMaxAccess("readonly")
ipoaArpClientArpOutReplies = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1, 12), Counter32()).setMaxAccess("readonly")
ipoaArpClientArpInNaks = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1, 13), Counter32()).setMaxAccess("readonly")
ipoaArpClientArpOutNaks = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1, 14), Counter32()).setMaxAccess("readonly")
ipoaArpClientArpUnknownOps = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1, 15), Counter32()).setMaxAccess("readonly")
ipoaArpClientArpNoSrvrResps = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1, 16), Counter32()).setMaxAccess("readonly")
ipoaArpClientRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 4, 1, 17), RowStatus()).setMaxAccess("readwrite")
ipoaArpSrvrTable = MibTable((1, 3, 6, 1, 2, 1, 10, 46, 1, 5))
ipoaArpSrvrEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 46, 1, 5, 1)).setIndexNames((0, "IP-MIB", "ipAdEntAddr"), (0, "IPOA-MIB", "ipoaArpSrvrAddr"))
ipoaArpSrvrAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 5, 1, 1), IpoaAtmAddr()).setMaxAccess("noaccess")
ipoaArpSrvrLis = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 5, 1, 2), IpAddress()).setMaxAccess("readwrite")
ipoaArpSrvrInArpInReqs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 5, 1, 3), Counter32()).setMaxAccess("readonly")
ipoaArpSrvrInArpOutReqs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 5, 1, 4), Counter32()).setMaxAccess("readonly")
ipoaArpSrvrInArpInReplies = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 5, 1, 5), Counter32()).setMaxAccess("readonly")
ipoaArpSrvrInArpOutReplies = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 5, 1, 6), Counter32()).setMaxAccess("readonly")
ipoaArpSrvrInArpInvalidInReqs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 5, 1, 7), Counter32()).setMaxAccess("readonly")
ipoaArpSrvrInArpInvalidOutReqs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 5, 1, 8), Counter32()).setMaxAccess("readonly")
ipoaArpSrvrArpInReqs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 5, 1, 9), Counter32()).setMaxAccess("readonly")
ipoaArpSrvrArpOutReplies = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 5, 1, 10), Counter32()).setMaxAccess("readonly")
ipoaArpSrvrArpOutNaks = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 5, 1, 11), Counter32()).setMaxAccess("readonly")
ipoaArpSrvrArpDupIpAddrs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 5, 1, 12), Counter32()).setMaxAccess("readonly")
ipoaArpSrvrArpUnknownOps = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 5, 1, 13), Counter32()).setMaxAccess("readonly")
ipoaArpSrvrRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 5, 1, 14), RowStatus()).setMaxAccess("readwrite")
ipoaArpRemoteSrvrTable = MibTable((1, 3, 6, 1, 2, 1, 10, 46, 1, 6))
ipoaArpRemoteSrvrEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 46, 1, 6, 1)).setIndexNames((0, "IPOA-MIB", "ipoaLisSubnetAddr"), (0, "IPOA-MIB", "ipoaArpRemoteSrvrAtmAddr"), (0, "IPOA-MIB", "ipoaArpRemoteSrvrIfIndex"))
ipoaArpRemoteSrvrAtmAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 6, 1, 1), IpoaAtmAddr()).setMaxAccess("noaccess")
ipoaArpRemoteSrvrRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 6, 1, 2), RowStatus()).setMaxAccess("readwrite")
ipoaArpRemoteSrvrIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 6, 1, 3), InterfaceIndexOrZero()).setMaxAccess("noaccess")
ipoaArpRemoteSrvrIpAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 6, 1, 4), IpAddress().clone("0.0.0.0")).setMaxAccess("readonly")
ipoaArpRemoteSrvrAdminStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 6, 1, 5), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("up", 1), ("down", 2), )).clone(2)).setMaxAccess("readwrite")
ipoaArpRemoteSrvrOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 6, 1, 6), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("up", 1), ("down", 2), )).clone(2)).setMaxAccess("readonly")
ipoaVcTable = MibTable((1, 3, 6, 1, 2, 1, 10, 46, 1, 7))
ipoaVcEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 46, 1, 7, 1)).setIndexNames((0, "IP-MIB", "ipNetToMediaIfIndex"), (0, "IP-MIB", "ipNetToMediaNetAddress"), (0, "IPOA-MIB", "ipoaVcVpi"), (0, "IPOA-MIB", "ipoaVcVci"))
ipoaVcVpi = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 7, 1, 1), IpoaVpiInteger()).setMaxAccess("noaccess")
ipoaVcVci = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 7, 1, 2), IpoaVciInteger()).setMaxAccess("noaccess")
ipoaVcType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 7, 1, 3), IpoaAtmConnKind()).setMaxAccess("readonly")
ipoaVcNegotiatedEncapsType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 7, 1, 4), IpoaEncapsType()).setMaxAccess("readonly")
ipoaVcNegotiatedMtu = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 7, 1, 5), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
ipoaConfigPvcTable = MibTable((1, 3, 6, 1, 2, 1, 10, 46, 1, 8))
ipoaConfigPvcEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 46, 1, 8, 1)).setIndexNames((0, "IPOA-MIB", "ipoaConfigPvcIfIndex"), (0, "IPOA-MIB", "ipoaConfigPvcVpi"), (0, "IPOA-MIB", "ipoaConfigPvcVci"))
ipoaConfigPvcIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 8, 1, 1), InterfaceIndex()).setMaxAccess("noaccess")
ipoaConfigPvcVpi = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 8, 1, 2), IpoaVpiInteger()).setMaxAccess("noaccess")
ipoaConfigPvcVci = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 8, 1, 3), IpoaVciInteger()).setMaxAccess("noaccess")
ipoaConfigPvcDefaultMtu = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 8, 1, 4), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535)).clone(9180)).setMaxAccess("readwrite")
ipoaConfigPvcRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 46, 1, 8, 1, 5), RowStatus()).setMaxAccess("readwrite")
ipoaNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 46, 2))
ipoaTrapPrefix = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 46, 2, 0))
ipoaConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 46, 3))
ipoaGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 46, 3, 1))
ipoaCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 46, 3, 2))

# Augmentions

# Notifications

ipoaMtuExceeded = NotificationType((1, 3, 6, 1, 2, 1, 10, 46, 2, 0, 1)).setObjects(("IPOA-MIB", "ipoaVcNegotiatedMtu"), )
ipoaLisCreate = NotificationType((1, 3, 6, 1, 2, 1, 10, 46, 2, 0, 3)).setObjects(("IPOA-MIB", "ipoaLisSubnetAddr"), )
ipoaDuplicateIpAddress = NotificationType((1, 3, 6, 1, 2, 1, 10, 46, 2, 0, 2)).setObjects(("IP-MIB", "ipNetToMediaPhysAddress"), ("IP-MIB", "ipNetToMediaNetAddress"), ("IP-MIB", "ipNetToMediaIfIndex"), )
ipoaLisDelete = NotificationType((1, 3, 6, 1, 2, 1, 10, 46, 2, 0, 4)).setObjects(("IPOA-MIB", "ipoaLisSubnetAddr"), )

# Groups

ipoaClientGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 46, 3, 1, 2)).setObjects(("IPOA-MIB", "ipoaArpClientAtmAddr"), ("IPOA-MIB", "ipoaArpClientArpOutNaks"), ("IPOA-MIB", "ipoaArpClientInArpInvalidInReqs"), ("IPOA-MIB", "ipoaArpClientArpOutReqs"), ("IPOA-MIB", "ipoaArpClientInArpInReplies"), ("IPOA-MIB", "ipoaArpClientArpOutReplies"), ("IPOA-MIB", "ipoaArpClientArpInReqs"), ("IPOA-MIB", "ipoaArpClientInArpInReqs"), ("IPOA-MIB", "ipoaArpClientArpInReplies"), ("IPOA-MIB", "ipoaArpClientArpUnknownOps"), ("IPOA-MIB", "ipoaArpClientInArpOutReqs"), ("IPOA-MIB", "ipoaArpClientSrvrInUse"), ("IPOA-MIB", "ipoaArpClientInArpOutReplies"), ("IPOA-MIB", "ipoaArpClientArpInNaks"), ("IPOA-MIB", "ipoaArpClientInArpInvalidOutReqs"), ("IPOA-MIB", "ipoaArpClientArpNoSrvrResps"), ("IPOA-MIB", "ipoaArpClientRowStatus"), )
ipoaSrvrGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 46, 3, 1, 3)).setObjects(("IPOA-MIB", "ipoaArpSrvrArpDupIpAddrs"), ("IPOA-MIB", "ipoaArpSrvrRowStatus"), ("IPOA-MIB", "ipoaArpSrvrArpInReqs"), ("IPOA-MIB", "ipoaArpSrvrInArpInvalidInReqs"), ("IPOA-MIB", "ipoaArpSrvrInArpInReplies"), ("IPOA-MIB", "ipoaArpSrvrInArpOutReqs"), ("IPOA-MIB", "ipoaArpSrvrArpOutReplies"), ("IPOA-MIB", "ipoaArpSrvrLis"), ("IPOA-MIB", "ipoaArpSrvrArpUnknownOps"), ("IPOA-MIB", "ipoaArpSrvrInArpInvalidOutReqs"), ("IPOA-MIB", "ipoaArpSrvrArpOutNaks"), ("IPOA-MIB", "ipoaArpSrvrInArpInReqs"), ("IPOA-MIB", "ipoaArpSrvrInArpOutReplies"), )
ipoaGeneralGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 46, 3, 1, 1)).setObjects(("IPOA-MIB", "ipoaVcNegotiatedMtu"), ("IPOA-MIB", "ipoaVcNegotiatedEncapsType"), ("IPOA-MIB", "ipoaVcType"), ("IPOA-MIB", "ipoaConfigPvcDefaultMtu"), ("IPOA-MIB", "ipoaConfigPvcRowStatus"), )
ipoaLisNotificationsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 46, 3, 1, 6)).setObjects(("IPOA-MIB", "ipoaLisCreate"), ("IPOA-MIB", "ipoaLisDelete"), )
ipoaLisTableGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 46, 3, 1, 7)).setObjects(("IPOA-MIB", "ipoaLisInactivityTimer"), ("IPOA-MIB", "ipoaLisQDepth"), ("IPOA-MIB", "ipoaLisDefaultPeakCellRate"), ("IPOA-MIB", "ipoaLisTrapEnable"), ("IPOA-MIB", "ipoaLisSubnetAddr"), ("IPOA-MIB", "ipoaArpRemoteSrvrOperStatus"), ("IPOA-MIB", "ipoaLisTimeout"), ("IPOA-MIB", "ipoaLisIfMappingRowStatus"), ("IPOA-MIB", "ipoaLisMinHoldingTime"), ("IPOA-MIB", "ipoaArpRemoteSrvrRowStatus"), ("IPOA-MIB", "ipoaLisDefaultMtu"), ("IPOA-MIB", "ipoaLisRowStatus"), ("IPOA-MIB", "ipoaArpRemoteSrvrIpAddr"), ("IPOA-MIB", "ipoaLisDefaultEncapsType"), ("IPOA-MIB", "ipoaArpRemoteSrvrAdminStatus"), ("IPOA-MIB", "ipoaLisRetries"), ("IPOA-MIB", "ipoaLisCacheEntryAge"), ("IPOA-MIB", "ipoaLisActiveVcs"), ("IPOA-MIB", "ipoaLisMaxCalls"), )
ipoaSrvrNotificationsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 46, 3, 1, 5)).setObjects(("IPOA-MIB", "ipoaDuplicateIpAddress"), )
ipoaBasicNotificationsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 46, 3, 1, 4)).setObjects(("IPOA-MIB", "ipoaMtuExceeded"), )

# Exports

# Types
mibBuilder.exportSymbols("IPOA-MIB", IpoaAtmAddr=IpoaAtmAddr, IpoaAtmConnKind=IpoaAtmConnKind, IpoaEncapsType=IpoaEncapsType, IpoaVciInteger=IpoaVciInteger, IpoaVpiInteger=IpoaVpiInteger)

# Objects
mibBuilder.exportSymbols("IPOA-MIB", ipoaMIB=ipoaMIB, ipoaObjects=ipoaObjects, ipoaLisTrapEnable=ipoaLisTrapEnable, ipoaLisTable=ipoaLisTable, ipoaLisEntry=ipoaLisEntry, ipoaLisSubnetAddr=ipoaLisSubnetAddr, ipoaLisDefaultMtu=ipoaLisDefaultMtu, ipoaLisDefaultEncapsType=ipoaLisDefaultEncapsType, ipoaLisInactivityTimer=ipoaLisInactivityTimer, ipoaLisMinHoldingTime=ipoaLisMinHoldingTime, ipoaLisQDepth=ipoaLisQDepth, ipoaLisMaxCalls=ipoaLisMaxCalls, ipoaLisCacheEntryAge=ipoaLisCacheEntryAge, ipoaLisRetries=ipoaLisRetries, ipoaLisTimeout=ipoaLisTimeout, ipoaLisDefaultPeakCellRate=ipoaLisDefaultPeakCellRate, ipoaLisActiveVcs=ipoaLisActiveVcs, ipoaLisRowStatus=ipoaLisRowStatus, ipoaLisIfMappingTable=ipoaLisIfMappingTable, ipoaLisIfMappingEntry=ipoaLisIfMappingEntry, ipoaLisIfMappingIfIndex=ipoaLisIfMappingIfIndex, ipoaLisIfMappingRowStatus=ipoaLisIfMappingRowStatus, ipoaArpClientTable=ipoaArpClientTable, ipoaArpClientEntry=ipoaArpClientEntry, ipoaArpClientAtmAddr=ipoaArpClientAtmAddr, ipoaArpClientSrvrInUse=ipoaArpClientSrvrInUse, ipoaArpClientInArpInReqs=ipoaArpClientInArpInReqs, ipoaArpClientInArpOutReqs=ipoaArpClientInArpOutReqs, ipoaArpClientInArpInReplies=ipoaArpClientInArpInReplies, ipoaArpClientInArpOutReplies=ipoaArpClientInArpOutReplies, ipoaArpClientInArpInvalidInReqs=ipoaArpClientInArpInvalidInReqs, ipoaArpClientInArpInvalidOutReqs=ipoaArpClientInArpInvalidOutReqs, ipoaArpClientArpInReqs=ipoaArpClientArpInReqs, ipoaArpClientArpOutReqs=ipoaArpClientArpOutReqs, ipoaArpClientArpInReplies=ipoaArpClientArpInReplies, ipoaArpClientArpOutReplies=ipoaArpClientArpOutReplies, ipoaArpClientArpInNaks=ipoaArpClientArpInNaks, ipoaArpClientArpOutNaks=ipoaArpClientArpOutNaks, ipoaArpClientArpUnknownOps=ipoaArpClientArpUnknownOps, ipoaArpClientArpNoSrvrResps=ipoaArpClientArpNoSrvrResps, ipoaArpClientRowStatus=ipoaArpClientRowStatus, ipoaArpSrvrTable=ipoaArpSrvrTable, ipoaArpSrvrEntry=ipoaArpSrvrEntry, ipoaArpSrvrAddr=ipoaArpSrvrAddr, ipoaArpSrvrLis=ipoaArpSrvrLis, ipoaArpSrvrInArpInReqs=ipoaArpSrvrInArpInReqs, ipoaArpSrvrInArpOutReqs=ipoaArpSrvrInArpOutReqs, ipoaArpSrvrInArpInReplies=ipoaArpSrvrInArpInReplies, ipoaArpSrvrInArpOutReplies=ipoaArpSrvrInArpOutReplies, ipoaArpSrvrInArpInvalidInReqs=ipoaArpSrvrInArpInvalidInReqs, ipoaArpSrvrInArpInvalidOutReqs=ipoaArpSrvrInArpInvalidOutReqs, ipoaArpSrvrArpInReqs=ipoaArpSrvrArpInReqs, ipoaArpSrvrArpOutReplies=ipoaArpSrvrArpOutReplies, ipoaArpSrvrArpOutNaks=ipoaArpSrvrArpOutNaks, ipoaArpSrvrArpDupIpAddrs=ipoaArpSrvrArpDupIpAddrs, ipoaArpSrvrArpUnknownOps=ipoaArpSrvrArpUnknownOps, ipoaArpSrvrRowStatus=ipoaArpSrvrRowStatus, ipoaArpRemoteSrvrTable=ipoaArpRemoteSrvrTable, ipoaArpRemoteSrvrEntry=ipoaArpRemoteSrvrEntry, ipoaArpRemoteSrvrAtmAddr=ipoaArpRemoteSrvrAtmAddr, ipoaArpRemoteSrvrRowStatus=ipoaArpRemoteSrvrRowStatus, ipoaArpRemoteSrvrIfIndex=ipoaArpRemoteSrvrIfIndex, ipoaArpRemoteSrvrIpAddr=ipoaArpRemoteSrvrIpAddr, ipoaArpRemoteSrvrAdminStatus=ipoaArpRemoteSrvrAdminStatus, ipoaArpRemoteSrvrOperStatus=ipoaArpRemoteSrvrOperStatus, ipoaVcTable=ipoaVcTable, ipoaVcEntry=ipoaVcEntry, ipoaVcVpi=ipoaVcVpi, ipoaVcVci=ipoaVcVci, ipoaVcType=ipoaVcType, ipoaVcNegotiatedEncapsType=ipoaVcNegotiatedEncapsType, ipoaVcNegotiatedMtu=ipoaVcNegotiatedMtu, ipoaConfigPvcTable=ipoaConfigPvcTable, ipoaConfigPvcEntry=ipoaConfigPvcEntry, ipoaConfigPvcIfIndex=ipoaConfigPvcIfIndex, ipoaConfigPvcVpi=ipoaConfigPvcVpi, ipoaConfigPvcVci=ipoaConfigPvcVci, ipoaConfigPvcDefaultMtu=ipoaConfigPvcDefaultMtu, ipoaConfigPvcRowStatus=ipoaConfigPvcRowStatus, ipoaNotifications=ipoaNotifications, ipoaTrapPrefix=ipoaTrapPrefix, ipoaConformance=ipoaConformance, ipoaGroups=ipoaGroups, ipoaCompliances=ipoaCompliances)

# Notifications
mibBuilder.exportSymbols("IPOA-MIB", ipoaMtuExceeded=ipoaMtuExceeded, ipoaLisCreate=ipoaLisCreate, ipoaDuplicateIpAddress=ipoaDuplicateIpAddress, ipoaLisDelete=ipoaLisDelete)

# Groups
mibBuilder.exportSymbols("IPOA-MIB", ipoaClientGroup=ipoaClientGroup, ipoaSrvrGroup=ipoaSrvrGroup, ipoaGeneralGroup=ipoaGeneralGroup, ipoaLisNotificationsGroup=ipoaLisNotificationsGroup, ipoaLisTableGroup=ipoaLisTableGroup, ipoaSrvrNotificationsGroup=ipoaSrvrNotificationsGroup, ipoaBasicNotificationsGroup=ipoaBasicNotificationsGroup)
