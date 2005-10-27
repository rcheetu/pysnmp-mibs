# PySNMP SMI module. Autogenerated from smidump -f python ATM-TC-MIB
# by libsmi2pysnmp-0.0.5-alpha at Fri Oct 28 00:30:32 2005,
# Python version (2, 4, 0, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( Bits, Integer32, ModuleIdentity, MibIdentifier, ObjectIdentity, TimeTicks, TimeTicks, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "ObjectIdentity", "TimeTicks", "TimeTicks", "mib-2")
( TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention")

# Types

class AtmAddr(TextualConvention, OctetString):
    subtypeSpec = OctetString.subtypeSpec+constraint.ValueSizeConstraint(0,40)
    pass

class AtmConnCastType(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(3,2,1,)
    namedValues = namedval.NamedValues(("p2p", 1), ("p2mpRoot", 2), ("p2mpLeaf", 3), )
    pass

class AtmConnKind(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(4,2,5,1,3,)
    namedValues = namedval.NamedValues(("pvc", 1), ("svcIncoming", 2), ("svcOutgoing", 3), ("spvcInitiator", 4), ("spvcTarget", 5), )
    pass

class AtmIlmiNetworkPrefix(OctetString):
    subtypeSpec = OctetString.subtypeSpec+constraint.ValueSizeConstraint(13,13)
    pass

class AtmInterfaceType(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(4,5,8,7,12,10,1,3,13,11,9,2,6,)
    namedValues = namedval.NamedValues(("other", 1), ("atmfPnni1Dot0", 10), ("atmfBici2Dot0", 11), ("atmfUniPvcOnly", 12), ("atmfNniPvcOnly", 13), ("autoConfig", 2), ("ituDss2", 3), ("atmfUni3Dot0", 4), ("atmfUni3Dot1", 5), ("atmfUni4Dot0", 6), ("atmfIispUni3Dot0", 7), ("atmfIispUni3Dot1", 8), ("atmfIispUni4Dot0", 9), )
    pass

class AtmServiceCategory(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(3,6,2,5,1,4,)
    namedValues = namedval.NamedValues(("other", 1), ("cbr", 2), ("rtVbr", 3), ("nrtVbr", 4), ("abr", 5), ("ubr", 6), )
    pass

class AtmSigDescrParamIndex(Integer32):
    subtypeSpec = Integer32.subtypeSpec+constraint.ValueRangeConstraint(0,2147483647L)
    pass

class AtmTrafficDescrParamIndex(Integer32):
    subtypeSpec = Integer32.subtypeSpec+constraint.ValueRangeConstraint(0,2147483647L)
    pass

class AtmVcIdentifier(Integer32):
    subtypeSpec = Integer32.subtypeSpec+constraint.ValueRangeConstraint(0,65535)
    pass

class AtmVorXAdminStatus(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(2,1,)
    namedValues = namedval.NamedValues(("up", 1), ("down", 2), )
    pass

class AtmVorXLastChange(TimeTicks):
    pass

class AtmVorXOperStatus(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(3,1,2,)
    namedValues = namedval.NamedValues(("up", 1), ("down", 2), ("unknown", 3), )
    pass

class AtmVpIdentifier(Integer32):
    subtypeSpec = Integer32.subtypeSpec+constraint.ValueRangeConstraint(0,4095)
    pass


# Objects

atmTrafficDescriptorTypes = MibIdentifier((1, 3, 6, 1, 2, 1, 37, 1, 1))
atmNoTrafficDescriptor = MibIdentifier((1, 3, 6, 1, 2, 1, 37, 1, 1, 1))
atmNoClpNoScr = MibIdentifier((1, 3, 6, 1, 2, 1, 37, 1, 1, 2))
atmClpNoTaggingNoScr = MibIdentifier((1, 3, 6, 1, 2, 1, 37, 1, 1, 3))
atmClpTaggingNoScr = MibIdentifier((1, 3, 6, 1, 2, 1, 37, 1, 1, 4))
atmNoClpScr = MibIdentifier((1, 3, 6, 1, 2, 1, 37, 1, 1, 5))
atmClpNoTaggingScr = MibIdentifier((1, 3, 6, 1, 2, 1, 37, 1, 1, 6))
atmClpTaggingScr = MibIdentifier((1, 3, 6, 1, 2, 1, 37, 1, 1, 7))
atmClpNoTaggingMcr = MibIdentifier((1, 3, 6, 1, 2, 1, 37, 1, 1, 8))
atmClpTransparentNoScr = MibIdentifier((1, 3, 6, 1, 2, 1, 37, 1, 1, 9))
atmClpTransparentScr = MibIdentifier((1, 3, 6, 1, 2, 1, 37, 1, 1, 10))
atmNoClpTaggingNoScr = MibIdentifier((1, 3, 6, 1, 2, 1, 37, 1, 1, 11))
atmNoClpNoScrCdvt = MibIdentifier((1, 3, 6, 1, 2, 1, 37, 1, 1, 12))
atmNoClpScrCdvt = MibIdentifier((1, 3, 6, 1, 2, 1, 37, 1, 1, 13))
atmClpNoTaggingScrCdvt = MibIdentifier((1, 3, 6, 1, 2, 1, 37, 1, 1, 14))
atmClpTaggingScrCdvt = MibIdentifier((1, 3, 6, 1, 2, 1, 37, 1, 1, 15))
atmTCMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 37, 3))
atmObjectIdentities = MibIdentifier((1, 3, 6, 1, 2, 1, 37, 3, 1))

# Augmentions

# Exports

# Types
mibBuilder.exportSymbols("ATM-TC-MIB", AtmAddr=AtmAddr, AtmConnCastType=AtmConnCastType, AtmConnKind=AtmConnKind, AtmIlmiNetworkPrefix=AtmIlmiNetworkPrefix, AtmInterfaceType=AtmInterfaceType, AtmServiceCategory=AtmServiceCategory, AtmSigDescrParamIndex=AtmSigDescrParamIndex, AtmTrafficDescrParamIndex=AtmTrafficDescrParamIndex, AtmVcIdentifier=AtmVcIdentifier, AtmVorXAdminStatus=AtmVorXAdminStatus, AtmVorXLastChange=AtmVorXLastChange, AtmVorXOperStatus=AtmVorXOperStatus, AtmVpIdentifier=AtmVpIdentifier)

# Objects
mibBuilder.exportSymbols("ATM-TC-MIB", atmTrafficDescriptorTypes=atmTrafficDescriptorTypes, atmNoTrafficDescriptor=atmNoTrafficDescriptor, atmNoClpNoScr=atmNoClpNoScr, atmClpNoTaggingNoScr=atmClpNoTaggingNoScr, atmClpTaggingNoScr=atmClpTaggingNoScr, atmNoClpScr=atmNoClpScr, atmClpNoTaggingScr=atmClpNoTaggingScr, atmClpTaggingScr=atmClpTaggingScr, atmClpNoTaggingMcr=atmClpNoTaggingMcr, atmClpTransparentNoScr=atmClpTransparentNoScr, atmClpTransparentScr=atmClpTransparentScr, atmNoClpTaggingNoScr=atmNoClpTaggingNoScr, atmNoClpNoScrCdvt=atmNoClpNoScrCdvt, atmNoClpScrCdvt=atmNoClpScrCdvt, atmClpNoTaggingScrCdvt=atmClpNoTaggingScrCdvt, atmClpTaggingScrCdvt=atmClpTaggingScrCdvt, atmTCMIB=atmTCMIB, atmObjectIdentities=atmObjectIdentities)

