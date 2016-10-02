# Test program for MPU9250 changes for wipy board
import utime
from mpu9250 import MPU9250


imu = MPU9250()

utime.sleep(1)
#print("waiting one second")
print("Sensor: Accelerometer     Gyro      Magnetometer")
for count in range(20):
    utime.sleep_ms(1000)                      # Ensure an interrupt occurs to re-populate integer values
    scale = 6                     # Correction factors involve floating point
    imu.get_gyro_irq()
    imu.get_accel_irq()
    imu.get_mag_irq()
    mag = list(map(lambda x, y : x*y//scale, imu.mag.ixyz, imu.mag_correction))
    print("Sensor:", [x for x in imu.accel.ixyz], [x for x in imu.gyro.ixyz], mag)
    print()

print("Temp:%i °"%imu.temperature)
import machine
machine.reset()
