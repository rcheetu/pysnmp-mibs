# PySNMP SMI module. Autogenerated from smidump -f python DIFFSERV-DSCP-TC
# by libsmi2pysnmp-0.0.5-alpha at Fri Oct 28 00:30:33 2005,
# Python version (2, 4, 0, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( Bits, Integer32, Integer32, ModuleIdentity, MibIdentifier, TimeTicks, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "TimeTicks", "mib-2")
( TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention")

# Types

class Dscp(TextualConvention, Integer32):
    subtypeSpec = Integer32.subtypeSpec+constraint.ValueRangeConstraint(0,63)
    pass

class DscpOrAny(TextualConvention, Integer32):
    subtypeSpec = Integer32.subtypeSpec+constraint.ValueRangeConstraint(-1,63)
    pass


# Objects

diffServDSCPTC = ModuleIdentity((1, 3, 6, 1, 2, 1, 96))

# Augmentions

# Exports

# Types
mibBuilder.exportSymbols("DIFFSERV-DSCP-TC", Dscp=Dscp, DscpOrAny=DscpOrAny)

# Objects
mibBuilder.exportSymbols("DIFFSERV-DSCP-TC", diffServDSCPTC=diffServDSCPTC)

