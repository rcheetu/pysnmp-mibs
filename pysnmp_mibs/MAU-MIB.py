# PySNMP SMI module. Autogenerated from smidump -f python MAU-MIB
# by libsmi2pysnmp-0.0.5-alpha at Fri Oct 28 00:30:43 2005,
# Python version (2, 4, 0, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( InterfaceIndex, ) = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
( ModuleCompliance, NotificationGroup, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
( Bits, Counter32, Counter64, Integer32, Integer32, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "mib-2")
( AutonomousType, TextualConvention, TruthValue, ) = mibBuilder.importSymbols("SNMPv2-TC", "AutonomousType", "TextualConvention", "TruthValue")

# Types

class JackType(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(9,11,3,7,8,12,4,2,1,13,6,5,10,14,)
    namedValues = namedval.NamedValues(("other", 1), ("fiberST", 10), ("telco", 11), ("mtrj", 12), ("hssdc", 13), ("fiberLC", 14), ("rj45", 2), ("rj45S", 3), ("db9", 4), ("bnc", 5), ("fAUI", 6), ("mAUI", 7), ("fiberSC", 8), ("fiberMIC", 9), )
    pass


# Objects

snmpDot3MauMgt = MibIdentifier((1, 3, 6, 1, 2, 1, 26))
snmpDot3MauTraps = MibIdentifier((1, 3, 6, 1, 2, 1, 26, 0))
dot3RpMauBasicGroup = MibIdentifier((1, 3, 6, 1, 2, 1, 26, 1))
rpMauTable = MibTable((1, 3, 6, 1, 2, 1, 26, 1, 1))
rpMauEntry = MibTableRow((1, 3, 6, 1, 2, 1, 26, 1, 1, 1)).setIndexNames((0, "MAU-MIB", "rpMauGroupIndex"), (0, "MAU-MIB", "rpMauPortIndex"), (0, "MAU-MIB", "rpMauIndex"))
rpMauGroupIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("readonly")
rpMauPortIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("readonly")
rpMauIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("readonly")
rpMauType = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 1, 1, 1, 4), AutonomousType()).setMaxAccess("readonly")
rpMauStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 1, 1, 1, 5), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(6,4,2,3,1,5,)).subtype(namedValues=namedval.NamedValues(("other", 1), ("unknown", 2), ("operational", 3), ("standby", 4), ("shutdown", 5), ("reset", 6), ))).setMaxAccess("readwrite")
rpMauMediaAvailable = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 1, 1, 1, 6), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(3,7,6,11,2,9,1,5,4,10,8,)).subtype(namedValues=namedval.NamedValues(("other", 1), ("offline", 10), ("autoNegError", 11), ("unknown", 2), ("available", 3), ("notAvailable", 4), ("remoteFault", 5), ("invalidSignal", 6), ("remoteJabber", 7), ("remoteLinkLoss", 8), ("remoteTest", 9), ))).setMaxAccess("readonly")
rpMauMediaAvailableStateExits = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly")
rpMauJabberState = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 1, 1, 1, 8), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,4,3,)).subtype(namedValues=namedval.NamedValues(("other", 1), ("unknown", 2), ("noJabber", 3), ("jabbering", 4), ))).setMaxAccess("readonly")
rpMauJabberingStateEnters = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 1, 1, 1, 9), Counter32()).setMaxAccess("readonly")
rpMauFalseCarriers = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 1, 1, 1, 10), Counter32()).setMaxAccess("readonly")
rpJackTable = MibTable((1, 3, 6, 1, 2, 1, 26, 1, 2))
rpJackEntry = MibTableRow((1, 3, 6, 1, 2, 1, 26, 1, 2, 1)).setIndexNames((0, "MAU-MIB", "rpMauGroupIndex"), (0, "MAU-MIB", "rpMauPortIndex"), (0, "MAU-MIB", "rpMauIndex"), (0, "MAU-MIB", "rpJackIndex"))
rpJackIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("noaccess")
rpJackType = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 1, 2, 1, 2), JackType()).setMaxAccess("readonly")
dot3IfMauBasicGroup = MibIdentifier((1, 3, 6, 1, 2, 1, 26, 2))
ifMauTable = MibTable((1, 3, 6, 1, 2, 1, 26, 2, 1))
ifMauEntry = MibTableRow((1, 3, 6, 1, 2, 1, 26, 2, 1, 1)).setIndexNames((0, "MAU-MIB", "ifMauIfIndex"), (0, "MAU-MIB", "ifMauIndex"))
ifMauIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 2, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
ifMauIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("readonly")
ifMauType = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 2, 1, 1, 3), AutonomousType()).setMaxAccess("readonly")
ifMauStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 2, 1, 1, 4), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(6,4,2,3,1,5,)).subtype(namedValues=namedval.NamedValues(("other", 1), ("unknown", 2), ("operational", 3), ("standby", 4), ("shutdown", 5), ("reset", 6), ))).setMaxAccess("readwrite")
ifMauMediaAvailable = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 2, 1, 1, 5), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(3,7,15,6,11,2,17,9,13,16,1,5,14,4,10,12,18,8,)).subtype(namedValues=namedval.NamedValues(("other", 1), ("offline", 10), ("autoNegError", 11), ("pmdLinkFault", 12), ("wisFrameLoss", 13), ("wisSignalLoss", 14), ("pcsLinkFault", 15), ("excessiveBER", 16), ("dxsLinkFault", 17), ("pxsLinkFault", 18), ("unknown", 2), ("available", 3), ("notAvailable", 4), ("remoteFault", 5), ("invalidSignal", 6), ("remoteJabber", 7), ("remoteLinkLoss", 8), ("remoteTest", 9), ))).setMaxAccess("readonly")
ifMauMediaAvailableStateExits = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
ifMauJabberState = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 2, 1, 1, 7), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,4,3,)).subtype(namedValues=namedval.NamedValues(("other", 1), ("unknown", 2), ("noJabber", 3), ("jabbering", 4), ))).setMaxAccess("readonly")
ifMauJabberingStateEnters = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 2, 1, 1, 8), Counter32()).setMaxAccess("readonly")
ifMauFalseCarriers = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 2, 1, 1, 9), Counter32()).setMaxAccess("readonly")
ifMauTypeList = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 2, 1, 1, 10), Integer32()).setMaxAccess("readonly")
ifMauDefaultType = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 2, 1, 1, 11), AutonomousType()).setMaxAccess("readwrite")
ifMauAutoNegSupported = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 2, 1, 1, 12), TruthValue()).setMaxAccess("readonly")
ifMauTypeListBits = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 2, 1, 1, 13), Bits().subtype(namedValues=namedval.NamedValues(("bOther", 0), ("bAUI", 1), ("b10baseTHD", 10), ("b10baseTFD", 11), ("b10baseFLHD", 12), ("b10baseFLFD", 13), ("b100baseT4", 14), ("b100baseTXHD", 15), ("b100baseTXFD", 16), ("b100baseFXHD", 17), ("b100baseFXFD", 18), ("b100baseT2HD", 19), ("b10base5", 2), ("b100baseT2FD", 20), ("b1000baseXHD", 21), ("b1000baseXFD", 22), ("b1000baseLXHD", 23), ("b1000baseLXFD", 24), ("b1000baseSXHD", 25), ("b1000baseSXFD", 26), ("b1000baseCXHD", 27), ("b1000baseCXFD", 28), ("b1000baseTHD", 29), ("bFoirl", 3), ("b1000baseTFD", 30), ("b10GbaseX", 31), ("b10GbaseLX4", 32), ("b10GbaseR", 33), ("b10GbaseER", 34), ("b10GbaseLR", 35), ("b10GbaseSR", 36), ("b10GbaseW", 37), ("b10GbaseEW", 38), ("b10GbaseLW", 39), ("b10base2", 4), ("b10GbaseSW", 40), ("b10baseT", 5), ("b10baseFP", 6), ("b10baseFB", 7), ("b10baseFL", 8), ("b10broad36", 9), ))).setMaxAccess("readonly")
ifMauHCFalseCarriers = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 2, 1, 1, 14), Counter64()).setMaxAccess("readonly")
ifJackTable = MibTable((1, 3, 6, 1, 2, 1, 26, 2, 2))
ifJackEntry = MibTableRow((1, 3, 6, 1, 2, 1, 26, 2, 2, 1)).setIndexNames((0, "MAU-MIB", "ifMauIfIndex"), (0, "MAU-MIB", "ifMauIndex"), (0, "MAU-MIB", "ifJackIndex"))
ifJackIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("noaccess")
ifJackType = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 2, 2, 1, 2), JackType()).setMaxAccess("readonly")
dot3BroadMauBasicGroup = MibIdentifier((1, 3, 6, 1, 2, 1, 26, 3))
broadMauBasicTable = MibTable((1, 3, 6, 1, 2, 1, 26, 3, 1))
broadMauBasicEntry = MibTableRow((1, 3, 6, 1, 2, 1, 26, 3, 1, 1)).setIndexNames((0, "MAU-MIB", "broadMauIfIndex"), (0, "MAU-MIB", "broadMauIndex"))
broadMauIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 3, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
broadMauIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("readonly")
broadMauXmtRcvSplitType = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 3, 1, 1, 3), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,3,)).subtype(namedValues=namedval.NamedValues(("other", 1), ("single", 2), ("dual", 3), ))).setMaxAccess("readonly")
broadMauXmtCarrierFreq = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 3, 1, 1, 4), Integer32()).setMaxAccess("readonly")
broadMauTranslationFreq = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 3, 1, 1, 5), Integer32()).setMaxAccess("readonly")
dot3MauType = MibIdentifier((1, 3, 6, 1, 2, 1, 26, 4))
dot3MauTypeAUI = MibIdentifier((1, 3, 6, 1, 2, 1, 26, 4, 1))
dot3MauType10Base5 = MibIdentifier((1, 3, 6, 1, 2, 1, 26, 4, 2))
dot3MauTypeFoirl = MibIdentifier((1, 3, 6, 1, 2, 1, 26, 4, 3))
dot3MauType10Base2 = MibIdentifier((1, 3, 6, 1, 2, 1, 26, 4, 4))
dot3MauType10BaseT = MibIdentifier((1, 3, 6, 1, 2, 1, 26, 4, 5))
dot3MauType10BaseFP = MibIdentifier((1, 3, 6, 1, 2, 1, 26, 4, 6))
dot3MauType10BaseFB = MibIdentifier((1, 3, 6, 1, 2, 1, 26, 4, 7))
dot3MauType10BaseFL = MibIdentifier((1, 3, 6, 1, 2, 1, 26, 4, 8))
dot3MauType10Broad36 = MibIdentifier((1, 3, 6, 1, 2, 1, 26, 4, 9))
dot3MauType10BaseTHD = MibIdentifier((1, 3, 6, 1, 2, 1, 26, 4, 10))
dot3MauType10BaseTFD = MibIdentifier((1, 3, 6, 1, 2, 1, 26, 4, 11))
dot3MauType10BaseFLHD = MibIdentifier((1, 3, 6, 1, 2, 1, 26, 4, 12))
dot3MauType10BaseFLFD = MibIdentifier((1, 3, 6, 1, 2, 1, 26, 4, 13))
dot3MauType100BaseT4 = MibIdentifier((1, 3, 6, 1, 2, 1, 26, 4, 14))
dot3MauType100BaseTXHD = MibIdentifier((1, 3, 6, 1, 2, 1, 26, 4, 15))
dot3MauType100BaseTXFD = MibIdentifier((1, 3, 6, 1, 2, 1, 26, 4, 16))
dot3MauType100BaseFXHD = MibIdentifier((1, 3, 6, 1, 2, 1, 26, 4, 17))
dot3MauType100BaseFXFD = MibIdentifier((1, 3, 6, 1, 2, 1, 26, 4, 18))
dot3MauType100BaseT2HD = MibIdentifier((1, 3, 6, 1, 2, 1, 26, 4, 19))
dot3MauType100BaseT2FD = MibIdentifier((1, 3, 6, 1, 2, 1, 26, 4, 20))
dot3MauType1000BaseXHD = MibIdentifier((1, 3, 6, 1, 2, 1, 26, 4, 21))
dot3MauType1000BaseXFD = MibIdentifier((1, 3, 6, 1, 2, 1, 26, 4, 22))
dot3MauType1000BaseLXHD = MibIdentifier((1, 3, 6, 1, 2, 1, 26, 4, 23))
dot3MauType1000BaseLXFD = MibIdentifier((1, 3, 6, 1, 2, 1, 26, 4, 24))
dot3MauType1000BaseSXHD = MibIdentifier((1, 3, 6, 1, 2, 1, 26, 4, 25))
dot3MauType1000BaseSXFD = MibIdentifier((1, 3, 6, 1, 2, 1, 26, 4, 26))
dot3MauType1000BaseCXHD = MibIdentifier((1, 3, 6, 1, 2, 1, 26, 4, 27))
dot3MauType1000BaseCXFD = MibIdentifier((1, 3, 6, 1, 2, 1, 26, 4, 28))
dot3MauType1000BaseTHD = MibIdentifier((1, 3, 6, 1, 2, 1, 26, 4, 29))
dot3MauType1000BaseTFD = MibIdentifier((1, 3, 6, 1, 2, 1, 26, 4, 30))
dot3MauType10GigBaseX = MibIdentifier((1, 3, 6, 1, 2, 1, 26, 4, 31))
dot3MauType10GigBaseLX4 = MibIdentifier((1, 3, 6, 1, 2, 1, 26, 4, 32))
dot3MauType10GigBaseR = MibIdentifier((1, 3, 6, 1, 2, 1, 26, 4, 33))
dot3MauType10GigBaseER = MibIdentifier((1, 3, 6, 1, 2, 1, 26, 4, 34))
dot3MauType10GigBaseLR = MibIdentifier((1, 3, 6, 1, 2, 1, 26, 4, 35))
dot3MauType10GigBaseSR = MibIdentifier((1, 3, 6, 1, 2, 1, 26, 4, 36))
dot3MauType10GigBaseW = MibIdentifier((1, 3, 6, 1, 2, 1, 26, 4, 37))
dot3MauType10GigBaseEW = MibIdentifier((1, 3, 6, 1, 2, 1, 26, 4, 38))
dot3MauType10GigBaseLW = MibIdentifier((1, 3, 6, 1, 2, 1, 26, 4, 39))
dot3MauType10GigBaseSW = MibIdentifier((1, 3, 6, 1, 2, 1, 26, 4, 40))
dot3IfMauAutoNegGroup = MibIdentifier((1, 3, 6, 1, 2, 1, 26, 5))
ifMauAutoNegTable = MibTable((1, 3, 6, 1, 2, 1, 26, 5, 1))
ifMauAutoNegEntry = MibTableRow((1, 3, 6, 1, 2, 1, 26, 5, 1, 1)).setIndexNames((0, "MAU-MIB", "ifMauIfIndex"), (0, "MAU-MIB", "ifMauIndex"))
ifMauAutoNegAdminStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 5, 1, 1, 1), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("enabled", 1), ("disabled", 2), ))).setMaxAccess("readwrite")
ifMauAutoNegRemoteSignaling = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 5, 1, 1, 2), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,2,)).subtype(namedValues=namedval.NamedValues(("detected", 1), ("notdetected", 2), ))).setMaxAccess("readonly")
ifMauAutoNegConfig = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 5, 1, 1, 4), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(3,2,4,1,5,)).subtype(namedValues=namedval.NamedValues(("other", 1), ("configuring", 2), ("complete", 3), ("disabled", 4), ("parallelDetectFail", 5), ))).setMaxAccess("readonly")
ifMauAutoNegCapability = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 5, 1, 1, 5), Integer32()).setMaxAccess("readonly")
ifMauAutoNegCapAdvertised = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 5, 1, 1, 6), Integer32()).setMaxAccess("readwrite")
ifMauAutoNegCapReceived = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 5, 1, 1, 7), Integer32()).setMaxAccess("readonly")
ifMauAutoNegRestart = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 5, 1, 1, 8), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("restart", 1), ("norestart", 2), ))).setMaxAccess("readwrite")
ifMauAutoNegCapabilityBits = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 5, 1, 1, 9), Bits().subtype(namedValues=namedval.NamedValues(("bOther", 0), ("b10baseT", 1), ("bfdxSPause", 10), ("bfdxBPause", 11), ("b1000baseX", 12), ("b1000baseXFD", 13), ("b1000baseT", 14), ("b1000baseTFD", 15), ("b10baseTFD", 2), ("b100baseT4", 3), ("b100baseTX", 4), ("b100baseTXFD", 5), ("b100baseT2", 6), ("b100baseT2FD", 7), ("bfdxPause", 8), ("bfdxAPause", 9), ))).setMaxAccess("readonly")
ifMauAutoNegCapAdvertisedBits = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 5, 1, 1, 10), Bits().subtype(namedValues=namedval.NamedValues(("bOther", 0), ("b10baseT", 1), ("bFdxSPause", 10), ("bFdxBPause", 11), ("b1000baseX", 12), ("b1000baseXFD", 13), ("b1000baseT", 14), ("b1000baseTFD", 15), ("b10baseTFD", 2), ("b100baseT4", 3), ("b100baseTX", 4), ("b100baseTXFD", 5), ("b100baseT2", 6), ("b100baseT2FD", 7), ("bFdxPause", 8), ("bFdxAPause", 9), ))).setMaxAccess("readwrite")
ifMauAutoNegCapReceivedBits = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 5, 1, 1, 11), Bits().subtype(namedValues=namedval.NamedValues(("bOther", 0), ("b10baseT", 1), ("bFdxSPause", 10), ("bFdxBPause", 11), ("b1000baseX", 12), ("b1000baseXFD", 13), ("b1000baseT", 14), ("b1000baseTFD", 15), ("b10baseTFD", 2), ("b100baseT4", 3), ("b100baseTX", 4), ("b100baseTXFD", 5), ("b100baseT2", 6), ("b100baseT2FD", 7), ("bFdxPause", 8), ("bFdxAPause", 9), ))).setMaxAccess("readonly")
ifMauAutoNegRemoteFaultAdvertised = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 5, 1, 1, 12), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(4,3,1,2,)).subtype(namedValues=namedval.NamedValues(("noError", 1), ("offline", 2), ("linkFailure", 3), ("autoNegError", 4), ))).setMaxAccess("readwrite")
ifMauAutoNegRemoteFaultReceived = MibTableColumn((1, 3, 6, 1, 2, 1, 26, 5, 1, 1, 13), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(4,3,1,2,)).subtype(namedValues=namedval.NamedValues(("noError", 1), ("offline", 2), ("linkFailure", 3), ("autoNegError", 4), ))).setMaxAccess("readonly")
mauMod = ModuleIdentity((1, 3, 6, 1, 2, 1, 26, 6))
mauModConf = MibIdentifier((1, 3, 6, 1, 2, 1, 26, 6, 1))
mauModCompls = MibIdentifier((1, 3, 6, 1, 2, 1, 26, 6, 1, 1))
mauModObjGrps = MibIdentifier((1, 3, 6, 1, 2, 1, 26, 6, 1, 2))
mauModNotGrps = MibIdentifier((1, 3, 6, 1, 2, 1, 26, 6, 1, 3))

# Augmentions

# Notifications

ifMauJabberTrap = NotificationType((1, 3, 6, 1, 2, 1, 26, 0, 2)).setObjects(("MAU-MIB", "ifMauJabberState"), )
rpMauJabberTrap = NotificationType((1, 3, 6, 1, 2, 1, 26, 0, 1)).setObjects(("MAU-MIB", "rpMauJabberState"), )

# Groups

ifMauNotifications = ObjectGroup((1, 3, 6, 1, 2, 1, 26, 6, 1, 3, 2)).setObjects(("MAU-MIB", "ifMauJabberTrap"), )
mauIfGrpAutoNeg1000Mbps = ObjectGroup((1, 3, 6, 1, 2, 1, 26, 6, 1, 2, 11)).setObjects(("MAU-MIB", "ifMauAutoNegRemoteFaultAdvertised"), ("MAU-MIB", "ifMauAutoNegRemoteFaultReceived"), )
mauIfGrpJack = ObjectGroup((1, 3, 6, 1, 2, 1, 26, 6, 1, 2, 6)).setObjects(("MAU-MIB", "ifJackType"), )
mauRpGrpJack = ObjectGroup((1, 3, 6, 1, 2, 1, 26, 6, 1, 2, 3)).setObjects(("MAU-MIB", "rpJackType"), )
mauIfGrp100Mbs = ObjectGroup((1, 3, 6, 1, 2, 1, 26, 6, 1, 2, 5)).setObjects(("MAU-MIB", "ifMauFalseCarriers"), ("MAU-MIB", "ifMauAutoNegSupported"), ("MAU-MIB", "ifMauTypeList"), ("MAU-MIB", "ifMauDefaultType"), )
mauRpGrp100Mbs = ObjectGroup((1, 3, 6, 1, 2, 1, 26, 6, 1, 2, 2)).setObjects(("MAU-MIB", "rpMauFalseCarriers"), )
mauRpGrpBasic = ObjectGroup((1, 3, 6, 1, 2, 1, 26, 6, 1, 2, 1)).setObjects(("MAU-MIB", "rpMauType"), ("MAU-MIB", "rpMauJabberState"), ("MAU-MIB", "rpMauMediaAvailableStateExits"), ("MAU-MIB", "rpMauPortIndex"), ("MAU-MIB", "rpMauJabberingStateEnters"), ("MAU-MIB", "rpMauGroupIndex"), ("MAU-MIB", "rpMauIndex"), ("MAU-MIB", "rpMauMediaAvailable"), ("MAU-MIB", "rpMauStatus"), )
mauIfGrpBasic = ObjectGroup((1, 3, 6, 1, 2, 1, 26, 6, 1, 2, 4)).setObjects(("MAU-MIB", "ifMauMediaAvailable"), ("MAU-MIB", "ifMauType"), ("MAU-MIB", "ifMauIfIndex"), ("MAU-MIB", "ifMauJabberingStateEnters"), ("MAU-MIB", "ifMauStatus"), ("MAU-MIB", "ifMauIndex"), ("MAU-MIB", "ifMauJabberState"), ("MAU-MIB", "ifMauMediaAvailableStateExits"), )
rpMauNotifications = ObjectGroup((1, 3, 6, 1, 2, 1, 26, 6, 1, 3, 1)).setObjects(("MAU-MIB", "rpMauJabberTrap"), )
mauIfGrpHighCapacity = ObjectGroup((1, 3, 6, 1, 2, 1, 26, 6, 1, 2, 9)).setObjects(("MAU-MIB", "ifMauFalseCarriers"), ("MAU-MIB", "ifMauTypeListBits"), ("MAU-MIB", "ifMauAutoNegSupported"), ("MAU-MIB", "ifMauDefaultType"), )
mauBroadBasic = ObjectGroup((1, 3, 6, 1, 2, 1, 26, 6, 1, 2, 8)).setObjects(("MAU-MIB", "broadMauIndex"), ("MAU-MIB", "broadMauTranslationFreq"), ("MAU-MIB", "broadMauXmtCarrierFreq"), ("MAU-MIB", "broadMauIfIndex"), ("MAU-MIB", "broadMauXmtRcvSplitType"), )
mauIfGrpHCStats = ObjectGroup((1, 3, 6, 1, 2, 1, 26, 6, 1, 2, 12)).setObjects(("MAU-MIB", "ifMauHCFalseCarriers"), )
mauIfGrpAutoNeg = ObjectGroup((1, 3, 6, 1, 2, 1, 26, 6, 1, 2, 7)).setObjects(("MAU-MIB", "ifMauAutoNegRestart"), ("MAU-MIB", "ifMauAutoNegCapReceived"), ("MAU-MIB", "ifMauAutoNegCapAdvertised"), ("MAU-MIB", "ifMauAutoNegConfig"), ("MAU-MIB", "ifMauAutoNegRemoteSignaling"), ("MAU-MIB", "ifMauAutoNegCapability"), ("MAU-MIB", "ifMauAutoNegAdminStatus"), )
mauIfGrpAutoNeg2 = ObjectGroup((1, 3, 6, 1, 2, 1, 26, 6, 1, 2, 10)).setObjects(("MAU-MIB", "ifMauAutoNegRestart"), ("MAU-MIB", "ifMauAutoNegCapReceivedBits"), ("MAU-MIB", "ifMauAutoNegCapabilityBits"), ("MAU-MIB", "ifMauAutoNegRemoteSignaling"), ("MAU-MIB", "ifMauAutoNegCapAdvertisedBits"), ("MAU-MIB", "ifMauAutoNegConfig"), ("MAU-MIB", "ifMauAutoNegAdminStatus"), )

# Exports

# Types
mibBuilder.exportSymbols("MAU-MIB", JackType=JackType)

# Objects
mibBuilder.exportSymbols("MAU-MIB", snmpDot3MauMgt=snmpDot3MauMgt, snmpDot3MauTraps=snmpDot3MauTraps, dot3RpMauBasicGroup=dot3RpMauBasicGroup, rpMauTable=rpMauTable, rpMauEntry=rpMauEntry, rpMauGroupIndex=rpMauGroupIndex, rpMauPortIndex=rpMauPortIndex, rpMauIndex=rpMauIndex, rpMauType=rpMauType, rpMauStatus=rpMauStatus, rpMauMediaAvailable=rpMauMediaAvailable, rpMauMediaAvailableStateExits=rpMauMediaAvailableStateExits, rpMauJabberState=rpMauJabberState, rpMauJabberingStateEnters=rpMauJabberingStateEnters, rpMauFalseCarriers=rpMauFalseCarriers, rpJackTable=rpJackTable, rpJackEntry=rpJackEntry, rpJackIndex=rpJackIndex, rpJackType=rpJackType, dot3IfMauBasicGroup=dot3IfMauBasicGroup, ifMauTable=ifMauTable, ifMauEntry=ifMauEntry, ifMauIfIndex=ifMauIfIndex, ifMauIndex=ifMauIndex, ifMauType=ifMauType, ifMauStatus=ifMauStatus, ifMauMediaAvailable=ifMauMediaAvailable, ifMauMediaAvailableStateExits=ifMauMediaAvailableStateExits, ifMauJabberState=ifMauJabberState, ifMauJabberingStateEnters=ifMauJabberingStateEnters, ifMauFalseCarriers=ifMauFalseCarriers, ifMauTypeList=ifMauTypeList, ifMauDefaultType=ifMauDefaultType, ifMauAutoNegSupported=ifMauAutoNegSupported, ifMauTypeListBits=ifMauTypeListBits, ifMauHCFalseCarriers=ifMauHCFalseCarriers, ifJackTable=ifJackTable, ifJackEntry=ifJackEntry, ifJackIndex=ifJackIndex, ifJackType=ifJackType, dot3BroadMauBasicGroup=dot3BroadMauBasicGroup, broadMauBasicTable=broadMauBasicTable, broadMauBasicEntry=broadMauBasicEntry, broadMauIfIndex=broadMauIfIndex, broadMauIndex=broadMauIndex, broadMauXmtRcvSplitType=broadMauXmtRcvSplitType, broadMauXmtCarrierFreq=broadMauXmtCarrierFreq, broadMauTranslationFreq=broadMauTranslationFreq, dot3MauType=dot3MauType, dot3MauTypeAUI=dot3MauTypeAUI, dot3MauType10Base5=dot3MauType10Base5, dot3MauTypeFoirl=dot3MauTypeFoirl, dot3MauType10Base2=dot3MauType10Base2, dot3MauType10BaseT=dot3MauType10BaseT, dot3MauType10BaseFP=dot3MauType10BaseFP, dot3MauType10BaseFB=dot3MauType10BaseFB, dot3MauType10BaseFL=dot3MauType10BaseFL, dot3MauType10Broad36=dot3MauType10Broad36, dot3MauType10BaseTHD=dot3MauType10BaseTHD, dot3MauType10BaseTFD=dot3MauType10BaseTFD, dot3MauType10BaseFLHD=dot3MauType10BaseFLHD, dot3MauType10BaseFLFD=dot3MauType10BaseFLFD, dot3MauType100BaseT4=dot3MauType100BaseT4, dot3MauType100BaseTXHD=dot3MauType100BaseTXHD, dot3MauType100BaseTXFD=dot3MauType100BaseTXFD, dot3MauType100BaseFXHD=dot3MauType100BaseFXHD, dot3MauType100BaseFXFD=dot3MauType100BaseFXFD, dot3MauType100BaseT2HD=dot3MauType100BaseT2HD, dot3MauType100BaseT2FD=dot3MauType100BaseT2FD, dot3MauType1000BaseXHD=dot3MauType1000BaseXHD, dot3MauType1000BaseXFD=dot3MauType1000BaseXFD, dot3MauType1000BaseLXHD=dot3MauType1000BaseLXHD, dot3MauType1000BaseLXFD=dot3MauType1000BaseLXFD, dot3MauType1000BaseSXHD=dot3MauType1000BaseSXHD, dot3MauType1000BaseSXFD=dot3MauType1000BaseSXFD, dot3MauType1000BaseCXHD=dot3MauType1000BaseCXHD, dot3MauType1000BaseCXFD=dot3MauType1000BaseCXFD, dot3MauType1000BaseTHD=dot3MauType1000BaseTHD, dot3MauType1000BaseTFD=dot3MauType1000BaseTFD, dot3MauType10GigBaseX=dot3MauType10GigBaseX, dot3MauType10GigBaseLX4=dot3MauType10GigBaseLX4, dot3MauType10GigBaseR=dot3MauType10GigBaseR, dot3MauType10GigBaseER=dot3MauType10GigBaseER, dot3MauType10GigBaseLR=dot3MauType10GigBaseLR, dot3MauType10GigBaseSR=dot3MauType10GigBaseSR, dot3MauType10GigBaseW=dot3MauType10GigBaseW, dot3MauType10GigBaseEW=dot3MauType10GigBaseEW, dot3MauType10GigBaseLW=dot3MauType10GigBaseLW, dot3MauType10GigBaseSW=dot3MauType10GigBaseSW, dot3IfMauAutoNegGroup=dot3IfMauAutoNegGroup, ifMauAutoNegTable=ifMauAutoNegTable, ifMauAutoNegEntry=ifMauAutoNegEntry, ifMauAutoNegAdminStatus=ifMauAutoNegAdminStatus, ifMauAutoNegRemoteSignaling=ifMauAutoNegRemoteSignaling, ifMauAutoNegConfig=ifMauAutoNegConfig, ifMauAutoNegCapability=ifMauAutoNegCapability, ifMauAutoNegCapAdvertised=ifMauAutoNegCapAdvertised, ifMauAutoNegCapReceived=ifMauAutoNegCapReceived, ifMauAutoNegRestart=ifMauAutoNegRestart, ifMauAutoNegCapabilityBits=ifMauAutoNegCapabilityBits, ifMauAutoNegCapAdvertisedBits=ifMauAutoNegCapAdvertisedBits, ifMauAutoNegCapReceivedBits=ifMauAutoNegCapReceivedBits, ifMauAutoNegRemoteFaultAdvertised=ifMauAutoNegRemoteFaultAdvertised, ifMauAutoNegRemoteFaultReceived=ifMauAutoNegRemoteFaultReceived, mauMod=mauMod, mauModConf=mauModConf, mauModCompls=mauModCompls, mauModObjGrps=mauModObjGrps, mauModNotGrps=mauModNotGrps)

# Notifications
mibBuilder.exportSymbols("MAU-MIB", ifMauJabberTrap=ifMauJabberTrap, rpMauJabberTrap=rpMauJabberTrap)

# Groups
mibBuilder.exportSymbols("MAU-MIB", ifMauNotifications=ifMauNotifications, mauIfGrpAutoNeg1000Mbps=mauIfGrpAutoNeg1000Mbps, mauIfGrpJack=mauIfGrpJack, mauRpGrpJack=mauRpGrpJack, mauIfGrp100Mbs=mauIfGrp100Mbs, mauRpGrp100Mbs=mauRpGrp100Mbs, mauRpGrpBasic=mauRpGrpBasic, mauIfGrpBasic=mauIfGrpBasic, rpMauNotifications=rpMauNotifications, mauIfGrpHighCapacity=mauIfGrpHighCapacity, mauBroadBasic=mauBroadBasic, mauIfGrpHCStats=mauIfGrpHCStats, mauIfGrpAutoNeg=mauIfGrpAutoNeg, mauIfGrpAutoNeg2=mauIfGrpAutoNeg2)
