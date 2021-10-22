from datetime import datetime
import io
import serial


class Thermometer(object):

    def __init__(self):
        """
        Initialise the thermometer
        """
        self.ser = serial.Serial(
            port='/dev/ttyUSB0', 
            baudrate=9600) 
        self.sio = io.TextIOWrapper(
            io.BufferedRWPair(self.ser, self.ser, 1),
            encoding='ascii', newline='\r')
        self.sio._CHUNK_SIZE = 1


    def get_measurement(self):
        """
        Returns tuple of (temperature, when)
        temperature is float and when is datetime object
        """
        datastring = self.sio.readline().strip()
        temp = float(datastring[:6])
        when = datetime.utcnow()
        return (temp, when)


    def close(self):
        self.ser.close()
