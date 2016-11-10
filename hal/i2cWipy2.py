from machine import I2C as I2c


class I2CWiPy2(I2c):
    """

    """
    def __init__(self, address, pins=('P9', 'P10'), baudrate=400000):
        super().__init__(0, pins=pins, baudrate=baudrate)
        self.__address = address
        self.buffer1 = bytearray(1)

    @property
    def device_address(self):
        return self.__address

    @device_address.setter
    def device_address(self, value):
        self.__address = value

    def read_bsfr(self, memaddr, buf):
        self.readfrom_mem_into(self.__address, memaddr, buf)

    def write_btr(self, memaddr, data):
        self.buffer1[0]=data
        self.writeto_mem(memaddr, self.buffer1)

    def write_bstr(self, memaddr, data):
        self.writeto_mem(self.__address, memaddr, data)

