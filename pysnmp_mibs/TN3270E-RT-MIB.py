# PySNMP SMI module. Autogenerated from smidump -f python TN3270E-RT-MIB
# by libsmi2pysnmp-0.0.5-alpha at Fri Oct 28 00:30:54 2005,
# Python version (2, 4, 0, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( IANATn3270eAddrType, IANATn3270eAddress, ) = mibBuilder.importSymbols("IANATn3270eTC-MIB", "IANATn3270eAddrType", "IANATn3270eAddress")
( snanauMIB, ) = mibBuilder.importSymbols("SNA-NAU-MIB", "snanauMIB")
( ModuleCompliance, NotificationGroup, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
( Bits, Counter32, Gauge32, Integer32, ModuleIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Gauge32", "Integer32", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32")
( DateAndTime, RowStatus, TestAndIncr, TimeStamp, ) = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "RowStatus", "TestAndIncr", "TimeStamp")
( tn3270eClientGroupName, tn3270eResMapElementType, tn3270eSrvrConfIndex, ) = mibBuilder.importSymbols("TN3270E-MIB", "tn3270eClientGroupName", "tn3270eResMapElementType", "tn3270eSrvrConfIndex")

# Objects

tn3270eRtMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 34, 9))
tn3270eRtNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 9, 0))
tn3270eRtObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 9, 1))
tn3270eRtCollCtlTable = MibTable((1, 3, 6, 1, 2, 1, 34, 9, 1, 1))
tn3270eRtCollCtlEntry = MibTableRow((1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1)).setIndexNames((0, "TN3270E-MIB", "tn3270eSrvrConfIndex"), (0, "TN3270E-MIB", "tn3270eClientGroupName"))
tn3270eRtCollCtlType = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1, 2), Bits().subtype(namedValues=namedval.NamedValues(("aggregate", 0), ("excludeIpComponent", 1), ("ddr", 2), ("average", 3), ("buckets", 4), ("traps", 5), ))).setMaxAccess("readwrite")
tn3270eRtCollCtlSPeriod = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1, 3), Unsigned32().subtype(subtypeSpec=constraint.ValueRangeConstraint(15, 86400))).setMaxAccess("readwrite")
tn3270eRtCollCtlSPMult = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1, 4), Unsigned32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 5760))).setMaxAccess("readwrite")
tn3270eRtCollCtlThreshHigh = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readwrite")
tn3270eRtCollCtlThreshLow = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1, 6), Unsigned32()).setMaxAccess("readwrite")
tn3270eRtCollCtlIdleCount = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1, 7), Unsigned32()).setMaxAccess("readwrite")
tn3270eRtCollCtlBucketBndry1 = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1, 8), Unsigned32()).setMaxAccess("readwrite")
tn3270eRtCollCtlBucketBndry2 = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1, 9), Unsigned32()).setMaxAccess("readwrite")
tn3270eRtCollCtlBucketBndry3 = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1, 10), Unsigned32()).setMaxAccess("readwrite")
tn3270eRtCollCtlBucketBndry4 = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1, 11), Unsigned32()).setMaxAccess("readwrite")
tn3270eRtCollCtlRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1, 12), RowStatus()).setMaxAccess("readwrite")
tn3270eRtDataTable = MibTable((1, 3, 6, 1, 2, 1, 34, 9, 1, 2))
tn3270eRtDataEntry = MibTableRow((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1)).setIndexNames((0, "TN3270E-MIB", "tn3270eSrvrConfIndex"), (0, "TN3270E-MIB", "tn3270eClientGroupName"), (0, "TN3270E-RT-MIB", "tn3270eRtDataClientAddrType"), (0, "TN3270E-RT-MIB", "tn3270eRtDataClientAddress"), (0, "TN3270E-RT-MIB", "tn3270eRtDataClientPort"))
tn3270eRtDataClientAddrType = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 1), IANATn3270eAddrType()).setMaxAccess("noaccess")
tn3270eRtDataClientAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 2), IANATn3270eAddress()).setMaxAccess("noaccess")
tn3270eRtDataClientPort = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 3), Unsigned32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("noaccess")
tn3270eRtDataAvgRt = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 4), Gauge32()).setMaxAccess("readonly")
tn3270eRtDataAvgIpRt = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 5), Gauge32()).setMaxAccess("readonly")
tn3270eRtDataAvgCountTrans = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 6), Gauge32()).setMaxAccess("readonly")
tn3270eRtDataIntTimeStamp = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 7), DateAndTime()).setMaxAccess("readonly")
tn3270eRtDataTotalRts = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 8), Counter32()).setMaxAccess("readonly")
tn3270eRtDataTotalIpRts = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 9), Counter32()).setMaxAccess("readonly")
tn3270eRtDataCountTrans = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 10), Counter32()).setMaxAccess("readonly")
tn3270eRtDataCountDrs = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 11), Counter32()).setMaxAccess("readonly")
tn3270eRtDataElapsRndTrpSq = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 12), Unsigned32()).setMaxAccess("readonly")
tn3270eRtDataElapsIpRtSq = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 13), Unsigned32()).setMaxAccess("readonly")
tn3270eRtDataBucket1Rts = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 14), Counter32()).setMaxAccess("readonly")
tn3270eRtDataBucket2Rts = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 15), Counter32()).setMaxAccess("readonly")
tn3270eRtDataBucket3Rts = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 16), Counter32()).setMaxAccess("readonly")
tn3270eRtDataBucket4Rts = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 17), Counter32()).setMaxAccess("readonly")
tn3270eRtDataBucket5Rts = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 18), Counter32()).setMaxAccess("readonly")
tn3270eRtDataRtMethod = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 19), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(0,2,1,)).subtype(namedValues=namedval.NamedValues(("none", 0), ("responses", 1), ("timingMark", 2), ))).setMaxAccess("readonly")
tn3270eRtDataDiscontinuityTime = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 20), TimeStamp()).setMaxAccess("readonly")
tn3270eRtSpinLock = MibScalar((1, 3, 6, 1, 2, 1, 34, 9, 1, 3), TestAndIncr()).setMaxAccess("readwrite")
tn3270eRtConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 9, 3))
tn3270eRtGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 9, 3, 1))
tn3270eRtCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 9, 3, 2))

# Augmentions

# Notifications

tn3270eRtCollEnd = NotificationType((1, 3, 6, 1, 2, 1, 34, 9, 0, 4)).setObjects(("TN3270E-RT-MIB", "tn3270eRtDataBucket2Rts"), ("TN3270E-RT-MIB", "tn3270eRtDataTotalIpRts"), ("TN3270E-RT-MIB", "tn3270eRtDataRtMethod"), ("TN3270E-RT-MIB", "tn3270eRtDataBucket5Rts"), ("TN3270E-RT-MIB", "tn3270eRtDataCountTrans"), ("TN3270E-RT-MIB", "tn3270eRtDataBucket4Rts"), ("TN3270E-RT-MIB", "tn3270eRtDataBucket1Rts"), ("TN3270E-RT-MIB", "tn3270eRtDataBucket3Rts"), ("TN3270E-RT-MIB", "tn3270eRtDataElapsRndTrpSq"), ("TN3270E-RT-MIB", "tn3270eRtDataIntTimeStamp"), ("TN3270E-RT-MIB", "tn3270eRtDataDiscontinuityTime"), ("TN3270E-RT-MIB", "tn3270eRtDataAvgIpRt"), ("TN3270E-RT-MIB", "tn3270eRtDataTotalRts"), ("TN3270E-RT-MIB", "tn3270eRtDataAvgRt"), ("TN3270E-RT-MIB", "tn3270eRtDataAvgCountTrans"), ("TN3270E-RT-MIB", "tn3270eRtDataElapsIpRtSq"), ("TN3270E-RT-MIB", "tn3270eRtDataCountDrs"), )
tn3270eRtExceeded = NotificationType((1, 3, 6, 1, 2, 1, 34, 9, 0, 1)).setObjects(("TN3270E-RT-MIB", "tn3270eRtDataAvgRt"), ("TN3270E-RT-MIB", "tn3270eRtDataAvgCountTrans"), ("TN3270E-RT-MIB", "tn3270eRtDataRtMethod"), ("TN3270E-RT-MIB", "tn3270eRtDataAvgIpRt"), ("TN3270E-RT-MIB", "tn3270eRtDataIntTimeStamp"), )
tn3270eRtOkay = NotificationType((1, 3, 6, 1, 2, 1, 34, 9, 0, 2)).setObjects(("TN3270E-RT-MIB", "tn3270eRtDataAvgRt"), ("TN3270E-RT-MIB", "tn3270eRtDataAvgCountTrans"), ("TN3270E-RT-MIB", "tn3270eRtDataRtMethod"), ("TN3270E-RT-MIB", "tn3270eRtDataAvgIpRt"), ("TN3270E-RT-MIB", "tn3270eRtDataIntTimeStamp"), )
tn3270eRtCollStart = NotificationType((1, 3, 6, 1, 2, 1, 34, 9, 0, 3)).setObjects(("TN3270E-MIB", "tn3270eResMapElementType"), ("TN3270E-RT-MIB", "tn3270eRtDataRtMethod"), )

# Groups

tn3270eRtNotGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 34, 9, 3, 1, 2)).setObjects(("TN3270E-RT-MIB", "tn3270eRtCollEnd"), ("TN3270E-RT-MIB", "tn3270eRtExceeded"), ("TN3270E-RT-MIB", "tn3270eRtOkay"), ("TN3270E-RT-MIB", "tn3270eRtCollStart"), )
tn3270eRtGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 34, 9, 3, 1, 1)).setObjects(("TN3270E-RT-MIB", "tn3270eRtDataBucket2Rts"), ("TN3270E-RT-MIB", "tn3270eRtDataTotalIpRts"), ("TN3270E-RT-MIB", "tn3270eRtDataBucket5Rts"), ("TN3270E-RT-MIB", "tn3270eRtDataCountTrans"), ("TN3270E-RT-MIB", "tn3270eRtCollCtlIdleCount"), ("TN3270E-RT-MIB", "tn3270eRtSpinLock"), ("TN3270E-RT-MIB", "tn3270eRtDataBucket4Rts"), ("TN3270E-RT-MIB", "tn3270eRtDataCountDrs"), ("TN3270E-RT-MIB", "tn3270eRtCollCtlSPMult"), ("TN3270E-RT-MIB", "tn3270eRtDataDiscontinuityTime"), ("TN3270E-RT-MIB", "tn3270eRtCollCtlSPeriod"), ("TN3270E-RT-MIB", "tn3270eRtDataTotalRts"), ("TN3270E-RT-MIB", "tn3270eRtCollCtlThreshLow"), ("TN3270E-RT-MIB", "tn3270eRtDataRtMethod"), ("TN3270E-RT-MIB", "tn3270eRtCollCtlBucketBndry3"), ("TN3270E-RT-MIB", "tn3270eRtCollCtlBucketBndry2"), ("TN3270E-RT-MIB", "tn3270eRtCollCtlBucketBndry1"), ("TN3270E-RT-MIB", "tn3270eRtDataBucket1Rts"), ("TN3270E-RT-MIB", "tn3270eRtDataElapsRndTrpSq"), ("TN3270E-RT-MIB", "tn3270eRtDataElapsIpRtSq"), ("TN3270E-RT-MIB", "tn3270eRtDataAvgIpRt"), ("TN3270E-RT-MIB", "tn3270eRtDataAvgRt"), ("TN3270E-RT-MIB", "tn3270eRtCollCtlBucketBndry4"), ("TN3270E-RT-MIB", "tn3270eRtDataIntTimeStamp"), ("TN3270E-RT-MIB", "tn3270eRtDataBucket3Rts"), ("TN3270E-RT-MIB", "tn3270eRtCollCtlRowStatus"), ("TN3270E-RT-MIB", "tn3270eRtCollCtlThreshHigh"), ("TN3270E-RT-MIB", "tn3270eRtDataAvgCountTrans"), ("TN3270E-RT-MIB", "tn3270eRtCollCtlType"), )

# Exports

# Objects
mibBuilder.exportSymbols("TN3270E-RT-MIB", tn3270eRtMIB=tn3270eRtMIB, tn3270eRtNotifications=tn3270eRtNotifications, tn3270eRtObjects=tn3270eRtObjects, tn3270eRtCollCtlTable=tn3270eRtCollCtlTable, tn3270eRtCollCtlEntry=tn3270eRtCollCtlEntry, tn3270eRtCollCtlType=tn3270eRtCollCtlType, tn3270eRtCollCtlSPeriod=tn3270eRtCollCtlSPeriod, tn3270eRtCollCtlSPMult=tn3270eRtCollCtlSPMult, tn3270eRtCollCtlThreshHigh=tn3270eRtCollCtlThreshHigh, tn3270eRtCollCtlThreshLow=tn3270eRtCollCtlThreshLow, tn3270eRtCollCtlIdleCount=tn3270eRtCollCtlIdleCount, tn3270eRtCollCtlBucketBndry1=tn3270eRtCollCtlBucketBndry1, tn3270eRtCollCtlBucketBndry2=tn3270eRtCollCtlBucketBndry2, tn3270eRtCollCtlBucketBndry3=tn3270eRtCollCtlBucketBndry3, tn3270eRtCollCtlBucketBndry4=tn3270eRtCollCtlBucketBndry4, tn3270eRtCollCtlRowStatus=tn3270eRtCollCtlRowStatus, tn3270eRtDataTable=tn3270eRtDataTable, tn3270eRtDataEntry=tn3270eRtDataEntry, tn3270eRtDataClientAddrType=tn3270eRtDataClientAddrType, tn3270eRtDataClientAddress=tn3270eRtDataClientAddress, tn3270eRtDataClientPort=tn3270eRtDataClientPort, tn3270eRtDataAvgRt=tn3270eRtDataAvgRt, tn3270eRtDataAvgIpRt=tn3270eRtDataAvgIpRt, tn3270eRtDataAvgCountTrans=tn3270eRtDataAvgCountTrans, tn3270eRtDataIntTimeStamp=tn3270eRtDataIntTimeStamp, tn3270eRtDataTotalRts=tn3270eRtDataTotalRts, tn3270eRtDataTotalIpRts=tn3270eRtDataTotalIpRts, tn3270eRtDataCountTrans=tn3270eRtDataCountTrans, tn3270eRtDataCountDrs=tn3270eRtDataCountDrs, tn3270eRtDataElapsRndTrpSq=tn3270eRtDataElapsRndTrpSq, tn3270eRtDataElapsIpRtSq=tn3270eRtDataElapsIpRtSq, tn3270eRtDataBucket1Rts=tn3270eRtDataBucket1Rts, tn3270eRtDataBucket2Rts=tn3270eRtDataBucket2Rts, tn3270eRtDataBucket3Rts=tn3270eRtDataBucket3Rts, tn3270eRtDataBucket4Rts=tn3270eRtDataBucket4Rts, tn3270eRtDataBucket5Rts=tn3270eRtDataBucket5Rts, tn3270eRtDataRtMethod=tn3270eRtDataRtMethod, tn3270eRtDataDiscontinuityTime=tn3270eRtDataDiscontinuityTime, tn3270eRtSpinLock=tn3270eRtSpinLock, tn3270eRtConformance=tn3270eRtConformance, tn3270eRtGroups=tn3270eRtGroups, tn3270eRtCompliances=tn3270eRtCompliances)

# Notifications
mibBuilder.exportSymbols("TN3270E-RT-MIB", tn3270eRtCollEnd=tn3270eRtCollEnd, tn3270eRtExceeded=tn3270eRtExceeded, tn3270eRtOkay=tn3270eRtOkay, tn3270eRtCollStart=tn3270eRtCollStart)

# Groups
mibBuilder.exportSymbols("TN3270E-RT-MIB", tn3270eRtNotGroup=tn3270eRtNotGroup, tn3270eRtGroup=tn3270eRtGroup)
