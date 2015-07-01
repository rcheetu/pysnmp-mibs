#
# PySNMP MIB module JUNIPER-SMI (http://pysnmp.sf.net)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/JUNIPER-SMI
# Produced by pysmi-0.0.3 at Wed Jul  1 22:26:14 2015
# On host cray platform Linux version 2.6.37.6-smp by user ilya
# Using Python version 2.7.2 (default, Apr  2 2012, 20:32:47) 
#
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
( NotificationGroup, ModuleCompliance, ) = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
( Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, IpAddress, TimeTicks, Counter64, Unsigned32, enterprises, iso, Gauge32, ModuleIdentity, ObjectIdentity, Bits, Counter32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "IpAddress", "TimeTicks", "Counter64", "Unsigned32", "enterprises", "iso", "Gauge32", "ModuleIdentity", "ObjectIdentity", "Bits", "Counter32")
( DisplayString, TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniperMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636)).setRevisions(("2010-07-09 00:00", "2009-10-29 00:00", "2010-06-18 00:00", "2003-04-17 01:00", "2005-08-17 01:00", "2006-12-14 01:00", "2007-01-01 00:00", "2007-10-09 00:00", "2009-12-31 00:00", "2010-07-14 00:00", "2011-01-26 00:00", "2012-02-10 00:00", "2012-08-01 00:00", "2012-11-01 00:00", "2012-12-07 00:00", "2013-01-25 00:00", "2013-11-26 00:00",))
if mibBuilder.loadTexts: juniperMIB.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniperMIB.setContactInfo('        Juniper Technical Assistance Center\n\t\t     Juniper Networks, Inc.\n\t\t     1194 N. Mathilda Avenue\n\t\t     Sunnyvale, CA 94089\n\t\t     E-mail: support@juniper.net')
if mibBuilder.loadTexts: juniperMIB.setDescription('The Structure of Management Information for Juniper Networks.')
jnxProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 2636, 1))
if mibBuilder.loadTexts: jnxProducts.setDescription("The root of Juniper's Product OIDs.")
jnxMediaFlow = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 1, 2))
jnxJunosSpace = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 1, 3))
jnxReservedProducts3 = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 1, 4))
jnxReservedProducts4 = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 1, 5))
jnxReservedProducts5 = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 1, 6))
jnxSDKApplicationsRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 1, 7))
jnxJAB = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 1, 8))
jnxStrm = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 1, 9))
jnxServices = ObjectIdentity((1, 3, 6, 1, 4, 1, 2636, 2))
if mibBuilder.loadTexts: jnxServices.setDescription("The root of Juniper's Services OIDs.")
jnxMibs = ObjectIdentity((1, 3, 6, 1, 4, 1, 2636, 3))
if mibBuilder.loadTexts: jnxMibs.setDescription("The root of Juniper's MIB objects.")
jnxJsMibRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 39))
jnxExMibRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 40))
jnxWxMibRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 41))
jnxDcfMibRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 42))
jnxReservedMibs5 = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 43))
jnxPfeMibRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 44))
jnxBfdMibRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 45))
jnxXstpMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 46))
jnxUtilMibRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 47))
jnxl2aldMibRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 48))
jnxL2tpMibRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 49))
jnxRpmMibRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 50))
jnxUserAAAMibRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 51))
jnxIpSecMibRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 52))
jnxL2cpMibRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 53))
jnxPwTdmMibRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 54))
jnxPwTCMibRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 55))
jnxOtnMibRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 56))
jnxPsuMIBRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 58))
jnxSvcsMibRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 59))
jnxDomMibRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 60))
jnxJdhcpMibRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 61))
jnxJdhcpv6MibRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 62))
jnxLicenseMibRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 63))
jnxSubscriberMibRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 64))
jnxMagMibRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 65))
jnxMobileGatewayMibRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 66))
jnxPppoeMibRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 67))
jnxPppMibRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 68))
jnxJVAEMibRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 69))
jnxIfOtnMibRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 70))
jnxOpticsMibRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 71))
jnxAlarmExtMibRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 72))
jnxoptIfMibRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 73))
jnxFruMibRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 74))
jnxTimingNotfnsMIBRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 75))
jnxSnmpSetMibRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 76))
jnxTraps = ObjectIdentity((1, 3, 6, 1, 4, 1, 2636, 4))
if mibBuilder.loadTexts: jnxTraps.setDescription("The root of Juniper's Trap OIDs.")
jnxChassisTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 4, 1))
jnxChassisOKTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 4, 2))
jnxRmonTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 4, 3))
jnxLdpTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 4, 4))
jnxCmNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 4, 5))
jnxSonetNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 4, 6))
jnxPMonNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 4, 7))
jnxCollectorNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 4, 8))
jnxPingNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 4, 9))
jnxSpNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 4, 10))
jnxDfcNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 4, 11))
jnxSyslogNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 4, 12))
jnxEventNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 4, 13))
jnxVccpNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 4, 14))
jnxOtnNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 4, 15))
jnxSAIDPNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 4, 16))
jnxCosNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 4, 17))
jnxDomNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 4, 18))
jnxFabricChassisTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 4, 19))
jnxFabricChassisOKTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 4, 20))
jnxIfOtnNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 4, 21))
jnxOpticsNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 4, 22))
jnxFruTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 4, 23))
jnxSnmpSetTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 4, 24))
jnxExperiment = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 5))
jnxNsm = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 6))
jnxCA = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 7))
jnxAAA = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 8))
jnxAdvancedInsightMgr = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 9))
jnxBxMibRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 10))
mibBuilder.exportSymbols("JUNIPER-SMI", jnxPppMibRoot=jnxPppMibRoot, jnxOpticsMibRoot=jnxOpticsMibRoot, jnxPwTCMibRoot=jnxPwTCMibRoot, jnxMediaFlow=jnxMediaFlow, jnxNsm=jnxNsm, jnxXstpMibs=jnxXstpMibs, jnxRpmMibRoot=jnxRpmMibRoot, jnxDomNotifications=jnxDomNotifications, jnxL2cpMibRoot=jnxL2cpMibRoot, jnxVccpNotifications=jnxVccpNotifications, jnxJunosSpace=jnxJunosSpace, jnxPingNotifications=jnxPingNotifications, juniperMIB=juniperMIB, jnxMobileGatewayMibRoot=jnxMobileGatewayMibRoot, jnxFruMibRoot=jnxFruMibRoot, jnxFruTraps=jnxFruTraps, jnxJVAEMibRoot=jnxJVAEMibRoot, jnxTraps=jnxTraps, jnxoptIfMibRoot=jnxoptIfMibRoot, jnxPppoeMibRoot=jnxPppoeMibRoot, jnxIfOtnMibRoot=jnxIfOtnMibRoot, jnxIfOtnNotifications=jnxIfOtnNotifications, jnxMibs=jnxMibs, jnxJdhcpv6MibRoot=jnxJdhcpv6MibRoot, jnxServices=jnxServices, jnxFabricChassisOKTraps=jnxFabricChassisOKTraps, jnxProducts=jnxProducts, jnxChassisTraps=jnxChassisTraps, jnxEventNotifications=jnxEventNotifications, jnxPfeMibRoot=jnxPfeMibRoot, jnxSyslogNotifications=jnxSyslogNotifications, jnxPsuMIBRoot=jnxPsuMIBRoot, jnxDcfMibRoot=jnxDcfMibRoot, jnxBxMibRoot=jnxBxMibRoot, jnxOtnMibRoot=jnxOtnMibRoot, jnxAlarmExtMibRoot=jnxAlarmExtMibRoot, jnxReservedMibs5=jnxReservedMibs5, jnxCA=jnxCA, jnxSpNotifications=jnxSpNotifications, jnxTimingNotfnsMIBRoot=jnxTimingNotfnsMIBRoot, jnxBfdMibRoot=jnxBfdMibRoot, jnxSDKApplicationsRoot=jnxSDKApplicationsRoot, jnxDfcNotifications=jnxDfcNotifications, jnxl2aldMibRoot=jnxl2aldMibRoot, jnxJAB=jnxJAB, jnxLicenseMibRoot=jnxLicenseMibRoot, jnxMagMibRoot=jnxMagMibRoot, jnxLdpTraps=jnxLdpTraps, jnxSnmpSetTraps=jnxSnmpSetTraps, jnxCmNotifications=jnxCmNotifications, jnxDomMibRoot=jnxDomMibRoot, jnxReservedProducts4=jnxReservedProducts4, jnxOpticsNotifications=jnxOpticsNotifications, jnxUtilMibRoot=jnxUtilMibRoot, jnxExMibRoot=jnxExMibRoot, jnxSAIDPNotifications=jnxSAIDPNotifications, jnxSubscriberMibRoot=jnxSubscriberMibRoot, jnxSonetNotifications=jnxSonetNotifications, jnxJdhcpMibRoot=jnxJdhcpMibRoot, jnxPMonNotifications=jnxPMonNotifications, jnxOtnNotifications=jnxOtnNotifications, jnxFabricChassisTraps=jnxFabricChassisTraps, jnxIpSecMibRoot=jnxIpSecMibRoot, jnxJsMibRoot=jnxJsMibRoot, jnxWxMibRoot=jnxWxMibRoot, jnxCosNotifications=jnxCosNotifications, jnxPwTdmMibRoot=jnxPwTdmMibRoot, jnxExperiment=jnxExperiment, PYSNMP_MODULE_ID=juniperMIB, jnxReservedProducts5=jnxReservedProducts5, jnxSnmpSetMibRoot=jnxSnmpSetMibRoot, jnxCollectorNotifications=jnxCollectorNotifications, jnxAAA=jnxAAA, jnxAdvancedInsightMgr=jnxAdvancedInsightMgr, jnxRmonTraps=jnxRmonTraps, jnxReservedProducts3=jnxReservedProducts3, jnxChassisOKTraps=jnxChassisOKTraps, jnxUserAAAMibRoot=jnxUserAAAMibRoot, jnxL2tpMibRoot=jnxL2tpMibRoot, jnxSvcsMibRoot=jnxSvcsMibRoot, jnxStrm=jnxStrm)
