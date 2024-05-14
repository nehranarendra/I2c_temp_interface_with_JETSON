import smbus2
import time

# ADT7420 I2C address
ADT7420_ADDR = 0x48

# ADT7420 registers
ADT7420_REG_CONFIG = 0x01
ADT7420_REG_TEMP_MSB = 0x00

# Initialize I2C bus
bus = smbus2.SMBus(1)

# Configure the ADT7420
bus.write_byte_data(ADT7420_ADDR, ADT7420_REG_CONFIG, 0x80)

while True:
    # Read temperature data
    temp_data = bus.read_i2c_block_data(ADT7420_ADDR, ADT7420_REG_TEMP_MSB, 3)

    print(temp_data)
    
    # Convert temperature data to temperature in degrees Celsius
    temp_celsius = ((temp_data[0] << 9) | temp_data[1]) / 256.0

    print("Temperature: {:.2f}°C".format(temp_celsius))

    # Wait for 1 second before reading again
    time.sleep(1)

















































