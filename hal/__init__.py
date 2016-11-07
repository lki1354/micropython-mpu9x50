from os import uname

__all__ = ["I2C"]

if uname().machine == 'intel edison':
    from .i2cIntelEdison import I2CIntelEdison as I2C
elif uname().machine == 'WiPy2':
    from .i2cWipy2 import I2CWiPy2 as I2C
else:
    raise Exception("No right platform is used! (Intel Edison, WiPy2 are supported)")

