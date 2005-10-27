# PySNMP SMI module. Autogenerated from smidump -f python HCNUM-TC
# by libsmi2pysnmp-0.0.5-alpha at Fri Oct 28 00:30:39 2005,
# Python version (2, 4, 0, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( Bits, Counter64, Integer32, ModuleIdentity, MibIdentifier, TimeTicks, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter64", "Integer32", "ModuleIdentity", "MibIdentifier", "TimeTicks", "mib-2")
( TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention")

# Types

class CounterBasedGauge64(Counter64):
    pass

class ZeroBasedCounter64(Counter64):
    pass


# Objects

hcnumTC = ModuleIdentity((1, 3, 6, 1, 2, 1, 78))

# Augmentions

# Exports

# Types
mibBuilder.exportSymbols("HCNUM-TC", CounterBasedGauge64=CounterBasedGauge64, ZeroBasedCounter64=ZeroBasedCounter64)

# Objects
mibBuilder.exportSymbols("HCNUM-TC", hcnumTC=hcnumTC)

