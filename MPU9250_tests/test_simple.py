# Test program for IRQ based access to MPU9250
# Note there will be small differences between the lines because
# of drift or movement occurring between the readings
from machine import I2C
from mpu9250 import MPU9250
import utime

# Note: with a magnetometer read in the callback, a frequency of 1KHz hogged the CPU

#The default I2C pins are P9, G16 (SDA) and P10,G17 (SCL)
i2c = I2C(0, I2C.MASTER, baudrate=400000)
imu = MPU9250(i2c)
print("You should see slightly different values on each pair of readings.")


def delay(time_ms):
    time_continue = utime.ticks_ms() + time_ms
    time_now = utime.ticks_ms()
    while time_now < time_continue:
        time_now = utime.ticks_ms()


def run():

    print("            Accelerometer                               Gyro                                Magnetometer")
    for count in range(10):
        imu.get_gyro_irq()
        imu.get_accel_irq()
        imu.get_mag_irq()
        delay(400)                      # Ensure an interrupt occurs to re-populate integer values
        print("Normal:   ", imu.accel.xyz, imu.gyro.xyz, imu.mag.xyz)

