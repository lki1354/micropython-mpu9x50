from mraa import I2c


class I2CIntelEdison(I2c):
    """
INTEL_EDISON_MRAA_I2C_BUS = {1,6}
# i2c mra mode for frequency
MRAA_I2C_STD = 0  #/**< up to 100Khz */
MRAA_I2C_FAST = 1 #/**< up to 400Khz */
MRAA_I2C_HIGH = 2  #/**< up to 3.4Mhz */
    """
    def __init__(self, address, bus=1, frequency=1):
        I2c.__init__(self,bus)
        #super().__init__(bus)
        self.address(address)
        self.frequency(frequency)

    @property
    def device_address(self):
        return self.address()

    @device_address.setter
    def device_address(self, value):
        self.address(value)

    def read_bsfr(self, memaddr, buf):
        buf[:] = self.readBytesReg(memaddr, len(buf))

    def write_btr(self, memaddr, data):
        self.writeReg(memaddr, data)

    def write_bstr(self, memaddr, data):
        self.write(data.insert(0, memaddr))

