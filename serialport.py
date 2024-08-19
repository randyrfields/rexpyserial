import serial
import time

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
        port.write(b'!>busq\n')
        time.sleep(1)
        response = port.readline()
        if (len(response)) > 0:
            print(response.rstrip())
            time.sleep(2)
        else:
            time.sleep(1)


if __name__ == '__main__':
    main()