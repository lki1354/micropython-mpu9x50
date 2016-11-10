from os import uname

__all__ = ["I2C"]

system_object = uname()

if hasattr(system_object, 'machine'):
    if 'edison' in system_object.release:
        from .i2cIntelEdison import I2CIntelEdison as I2C
    elif 'WiPy2' in system_object.machine:
        from .i2cWipy2 import I2CWiPy2 as I2C
    else:
        raise Exception("Micropython Board is not supported!")

else:
    raise Exception("No right platform is used! (Intel Edison, WiPy2 are supported)")

