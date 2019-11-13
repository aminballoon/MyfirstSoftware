from startup import setting
from startup import serial_read
if __name__ == '__main__':
    try:
        if (input("debug? (y or N)").lower() == 'y'):
            print("program is run with debug mode")
            debug = True
        setting(debug)
        serial_read(input("Enter your serial port name (EX : com6) : "),debug)
        # serial_read("com22")
    except KeyboardInterrupt:
        print("\n\n\n\nShutdown ...\n\n\n\n")
        # something before end this program