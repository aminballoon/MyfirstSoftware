from startup import setting
from startup import serial_read
if __name__ == '__main__':
    try:
        setting()
        serial_read(input("Enter your serial port name (EX : com6) : "))
    except KeyboardInterrupt:
        print("\n\nShutdows ...\n\n")
        # something for end this program