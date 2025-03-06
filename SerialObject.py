import glob
import threading
import time
import platform
import serial
from pydispatch import dispatcher


class SerialObject(threading.Thread):
	def __init__(self, port_name, baud_rate=9600, parity=serial.PARITY_NONE, stop_bits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=0, block_size=1000, read_callback_function=None, start=True):
		threading.Thread.__init__(self)
		self.serialPort = None
		self.portName = port_name
		self.baudRate = baud_rate
		self.parityBits = parity
		self.stopBits = stop_bits
		self.dataBits = bytesize
		self.timeOut = timeout
		self.blockSize = block_size
		self.readExitFlag = False
		self.readCallbackFunction = False
		if read_callback_function:
			dispatcher.connect(read_callback_function, signal="SerialReceive", sender=dispatcher.Any)
			self.readCallbackFunction = True
			
		self.received_data = ""
		if start:
			self.open_COM()
		
	def open_COM(self):
		try:
			self.serialPort = serial.Serial(self.portName, self.baudRate, parity=self.parityBits,
		                                 stopbits=self.stopBits, bytesize=self.dataBits, timeout=self.timeOut)
		except Exception as e:
			print("Error opening Serial port: ", str(e))
			return str(e)
		else:
			print(f"Port {self.portName} opened successfully")
	
	@property
	def port_name(self):
		return self.portName
	
	@port_name.setter
	def port_name(self, port_name):
		self.portName = port_name
	
	@property
	def baud_rate(self):
		return self.baudRate
	
	@baud_rate.setter
	def baud_rate(self, baud_rate):
		self.baudRate = baud_rate
	
	@property
	def stop_bits(self):
		return self.stopBits
	
	@stop_bits.setter
	def stop_bits(self, stop_bits):
		self.stopBits = stop_bits
	
	@property
	def byte_size(self):
		return self.dataBits
	
	@byte_size.setter
	def byte_size(self, byte_size):
		self.dataBits = byte_size
	
	@property
	def time_out(self):
		return self.timeOut
	
	@time_out.setter
	def time_out(self, time_out):
		self.timeOut = time_out
	
	@property
	def parity_bits(self):
		return self.parityBits
	
	@parity_bits.setter
	def parity_bits(self, parity_bits):
		self.parityBits = parity_bits
	
	@property
	def block_size(self):
		return self.blockSize
	
	@block_size.setter
	def block_size(self, block_size):
		self.blockSize = block_size
		
	def send_data(self, data):
		self.serialPort.write(data.encode())
		
	def get_data(self):
		return self.received_data
	
	def get_inWaiting(self):
		self.serialPort.inWaiting()
	
	def run(self) -> None:
		self.__start_read_thread()
	
	# ------------------------------------------------------------------------------
	def __start_read_thread(self):
		""" Reads the serial port and 'dispatches' the data to the subscribers """
		print("Read Thread Started: Listening...")
		while not self.readExitFlag:
			try:
				self.received_data = self.serialPort.read(self.blockSize)
			except Exception as e:
				print("Error reading Serial Port: ", str(e))
				return str(e)
			
			if self.received_data and self.readCallbackFunction:
				dispatcher.send("SerialReceive", message=self.received_data)
				self.received_data = ""
			time.sleep(0.01)
	
	# ------------------------------------------------------------------------------
	def stop(self):
		""" Object read loop is stopped by this method """
		self.readExitFlag = 1
		self.serialPort.close()
		print("Closed Serial Port: ", self.portName)
	
	@staticmethod
	def scan_for_serial_ports():
		available_ports = []
		if platform.system() == "Windows":
			key = 0
			for i in range(256):
				try:
					s = serial.Serial("COM" + str(i))
				except serial.SerialException:
					pass
				else:
					available_ports.append("COM" + str(i))
					s.close()
		elif platform.system() == "Linux":
			key = 0
			s = glob.glob('/dev/ttyUSB*')
			print("Detected USB Ports:", s)
			for i in range(s.__len__() - 1, -1, -1):
				available_ports.append(s[i])
			
			s = glob.glob('/dev/ttyS[0-2]')
			print("Detected Serial Ports:", s)
			for i in range(s.__len__() - 1, -1, -1):
				available_ports.append(s[i])
		
		return available_ports

