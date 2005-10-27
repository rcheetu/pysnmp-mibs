# PySNMP SMI module. Autogenerated from smidump -f python ATM-ACCOUNTING-INFORMATION-MIB
# by libsmi2pysnmp-0.0.5-alpha at Fri Oct 28 00:30:31 2005,
# Python version (2, 4, 0, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( AtmAddr, ) = mibBuilder.importSymbols("ATM-TC-MIB", "AtmAddr")
( Bits, Counter64, Integer32, Integer32, ModuleIdentity, MibIdentifier, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter64", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "mib-2")
( DateAndTime, DisplayString, ) = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "DisplayString")

# Objects

atmAccountingInformationMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 59))
atmAcctngMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 59, 1))
atmAcctngDataObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 59, 1, 1))
atmAcctngConnectionType = MibScalar((1, 3, 6, 1, 2, 1, 59, 1, 1, 1), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,10,7,3,8,1,9,6,5,4,)).subtype(namedValues=namedval.NamedValues(("pvc", 1), ("spvpTarget", 10), ("pvp", 2), ("svcIncoming", 3), ("svcOutgoing", 4), ("svpIncoming", 5), ("svpOutgoing", 6), ("spvcInitiator", 7), ("spvcTarget", 8), ("spvpInitiator", 9), ))).setMaxAccess("noaccess")
atmAcctngCastType = MibScalar((1, 3, 6, 1, 2, 1, 59, 1, 1, 2), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,2,)).subtype(namedValues=namedval.NamedValues(("p2p", 1), ("p2mp", 2), ))).setMaxAccess("noaccess")
atmAcctngIfName = MibScalar((1, 3, 6, 1, 2, 1, 59, 1, 1, 3), DisplayString()).setMaxAccess("noaccess")
atmAcctngIfAlias = MibScalar((1, 3, 6, 1, 2, 1, 59, 1, 1, 4), DisplayString()).setMaxAccess("noaccess")
atmAcctngVpi = MibScalar((1, 3, 6, 1, 2, 1, 59, 1, 1, 5), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 4095))).setMaxAccess("noaccess")
atmAcctngVci = MibScalar((1, 3, 6, 1, 2, 1, 59, 1, 1, 6), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("noaccess")
atmAcctngCallingParty = MibScalar((1, 3, 6, 1, 2, 1, 59, 1, 1, 7), AtmAddr()).setMaxAccess("noaccess")
atmAcctngCalledParty = MibScalar((1, 3, 6, 1, 2, 1, 59, 1, 1, 8), AtmAddr()).setMaxAccess("noaccess")
atmAcctngCallReference = MibScalar((1, 3, 6, 1, 2, 1, 59, 1, 1, 9), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 3))).setMaxAccess("noaccess")
atmAcctngStartTime = MibScalar((1, 3, 6, 1, 2, 1, 59, 1, 1, 10), DateAndTime()).setMaxAccess("noaccess")
atmAcctngCollectionTime = MibScalar((1, 3, 6, 1, 2, 1, 59, 1, 1, 11), DateAndTime()).setMaxAccess("noaccess")
atmAcctngCollectMode = MibScalar((1, 3, 6, 1, 2, 1, 59, 1, 1, 12), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,2,3,)).subtype(namedValues=namedval.NamedValues(("onRelease", 1), ("periodically", 2), ("onCommand", 3), ))).setMaxAccess("noaccess")
atmAcctngReleaseCause = MibScalar((1, 3, 6, 1, 2, 1, 59, 1, 1, 13), Integer32()).setMaxAccess("noaccess")
atmAcctngServiceCategory = MibScalar((1, 3, 6, 1, 2, 1, 59, 1, 1, 14), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(6,7,2,5,1,4,3,)).subtype(namedValues=namedval.NamedValues(("other", 1), ("cbr", 2), ("vbrRt", 3), ("vbrNrt", 4), ("abr", 5), ("ubr", 6), ("unknown", 7), ))).setMaxAccess("noaccess")
atmAcctngTransmittedCells = MibScalar((1, 3, 6, 1, 2, 1, 59, 1, 1, 15), Counter64()).setMaxAccess("noaccess")
atmAcctngTransmittedClp0Cells = MibScalar((1, 3, 6, 1, 2, 1, 59, 1, 1, 16), Counter64()).setMaxAccess("noaccess")
atmAcctngReceivedCells = MibScalar((1, 3, 6, 1, 2, 1, 59, 1, 1, 17), Counter64()).setMaxAccess("noaccess")
atmAcctngReceivedClp0Cells = MibScalar((1, 3, 6, 1, 2, 1, 59, 1, 1, 18), Counter64()).setMaxAccess("noaccess")
atmAcctngTransmitTrafficDescriptorType = MibScalar((1, 3, 6, 1, 2, 1, 59, 1, 1, 19), ObjectIdentifier()).setMaxAccess("noaccess")
atmAcctngTransmitTrafficDescriptorParam1 = MibScalar((1, 3, 6, 1, 2, 1, 59, 1, 1, 20), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 2147483647L))).setMaxAccess("noaccess")
atmAcctngTransmitTrafficDescriptorParam2 = MibScalar((1, 3, 6, 1, 2, 1, 59, 1, 1, 21), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 2147483647L))).setMaxAccess("noaccess")
atmAcctngTransmitTrafficDescriptorParam3 = MibScalar((1, 3, 6, 1, 2, 1, 59, 1, 1, 22), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 2147483647L))).setMaxAccess("noaccess")
atmAcctngTransmitTrafficDescriptorParam4 = MibScalar((1, 3, 6, 1, 2, 1, 59, 1, 1, 23), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 2147483647L))).setMaxAccess("noaccess")
atmAcctngTransmitTrafficDescriptorParam5 = MibScalar((1, 3, 6, 1, 2, 1, 59, 1, 1, 24), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 2147483647L))).setMaxAccess("noaccess")
atmAcctngReceiveTrafficDescriptorType = MibScalar((1, 3, 6, 1, 2, 1, 59, 1, 1, 25), ObjectIdentifier()).setMaxAccess("noaccess")
atmAcctngReceiveTrafficDescriptorParam1 = MibScalar((1, 3, 6, 1, 2, 1, 59, 1, 1, 26), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 2147483647L))).setMaxAccess("noaccess")
atmAcctngReceiveTrafficDescriptorParam2 = MibScalar((1, 3, 6, 1, 2, 1, 59, 1, 1, 27), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 2147483647L))).setMaxAccess("noaccess")
atmAcctngReceiveTrafficDescriptorParam3 = MibScalar((1, 3, 6, 1, 2, 1, 59, 1, 1, 28), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 2147483647L))).setMaxAccess("noaccess")
atmAcctngReceiveTrafficDescriptorParam4 = MibScalar((1, 3, 6, 1, 2, 1, 59, 1, 1, 29), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 2147483647L))).setMaxAccess("noaccess")
atmAcctngReceiveTrafficDescriptorParam5 = MibScalar((1, 3, 6, 1, 2, 1, 59, 1, 1, 30), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 2147483647L))).setMaxAccess("noaccess")
atmAcctngCallingPartySubAddress = MibScalar((1, 3, 6, 1, 2, 1, 59, 1, 1, 31), AtmAddr()).setMaxAccess("noaccess")
atmAcctngCalledPartySubAddress = MibScalar((1, 3, 6, 1, 2, 1, 59, 1, 1, 32), AtmAddr()).setMaxAccess("noaccess")
atmAcctngRecordCrc16 = MibScalar((1, 3, 6, 1, 2, 1, 59, 1, 1, 33), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(2, 2))).setMaxAccess("noaccess")

# Augmentions

# Exports

# Objects
mibBuilder.exportSymbols("ATM-ACCOUNTING-INFORMATION-MIB", atmAccountingInformationMIB=atmAccountingInformationMIB, atmAcctngMIBObjects=atmAcctngMIBObjects, atmAcctngDataObjects=atmAcctngDataObjects, atmAcctngConnectionType=atmAcctngConnectionType, atmAcctngCastType=atmAcctngCastType, atmAcctngIfName=atmAcctngIfName, atmAcctngIfAlias=atmAcctngIfAlias, atmAcctngVpi=atmAcctngVpi, atmAcctngVci=atmAcctngVci, atmAcctngCallingParty=atmAcctngCallingParty, atmAcctngCalledParty=atmAcctngCalledParty, atmAcctngCallReference=atmAcctngCallReference, atmAcctngStartTime=atmAcctngStartTime, atmAcctngCollectionTime=atmAcctngCollectionTime, atmAcctngCollectMode=atmAcctngCollectMode, atmAcctngReleaseCause=atmAcctngReleaseCause, atmAcctngServiceCategory=atmAcctngServiceCategory, atmAcctngTransmittedCells=atmAcctngTransmittedCells, atmAcctngTransmittedClp0Cells=atmAcctngTransmittedClp0Cells, atmAcctngReceivedCells=atmAcctngReceivedCells, atmAcctngReceivedClp0Cells=atmAcctngReceivedClp0Cells, atmAcctngTransmitTrafficDescriptorType=atmAcctngTransmitTrafficDescriptorType, atmAcctngTransmitTrafficDescriptorParam1=atmAcctngTransmitTrafficDescriptorParam1, atmAcctngTransmitTrafficDescriptorParam2=atmAcctngTransmitTrafficDescriptorParam2, atmAcctngTransmitTrafficDescriptorParam3=atmAcctngTransmitTrafficDescriptorParam3, atmAcctngTransmitTrafficDescriptorParam4=atmAcctngTransmitTrafficDescriptorParam4, atmAcctngTransmitTrafficDescriptorParam5=atmAcctngTransmitTrafficDescriptorParam5, atmAcctngReceiveTrafficDescriptorType=atmAcctngReceiveTrafficDescriptorType, atmAcctngReceiveTrafficDescriptorParam1=atmAcctngReceiveTrafficDescriptorParam1, atmAcctngReceiveTrafficDescriptorParam2=atmAcctngReceiveTrafficDescriptorParam2, atmAcctngReceiveTrafficDescriptorParam3=atmAcctngReceiveTrafficDescriptorParam3, atmAcctngReceiveTrafficDescriptorParam4=atmAcctngReceiveTrafficDescriptorParam4, atmAcctngReceiveTrafficDescriptorParam5=atmAcctngReceiveTrafficDescriptorParam5, atmAcctngCallingPartySubAddress=atmAcctngCallingPartySubAddress, atmAcctngCalledPartySubAddress=atmAcctngCalledPartySubAddress, atmAcctngRecordCrc16=atmAcctngRecordCrc16)

