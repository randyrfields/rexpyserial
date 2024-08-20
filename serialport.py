import serial
import time
from cobs import cobs

port = '/dev/ttyS1'
baudrate = 115200
timeout = 1

def OpenSerialPort():

    ser = serial.Serial(port, baudrate, timeout=timeout)
    
    return ser


def main():
    """
    Setup Serial port
    Read system bus
    Populate database
    """

    port = OpenSerialPort()

    """
    Send request to SysControl
    """
    while True:
        encoded = cobs.encode(b'activate light\x00')
        port.write(encoded)
        time.sleep(1)
        # response = port.readline()
        time.sleep(2)
        print("rcv pass")


if __name__ == '__main__':
    main()