#we will impliment this projet with Qiskit this is only a prototype
#for running protocol_rdt22.py just change imported protocol file name in Testbench.py 

# SimPy model for the Reliable Data Transport (rdt) Protocol 2.2 (Using ACK and sequence number 0, 1)

#
# Sender-side (rdt_Sender)
#	- receives messages to be delivered from the upper layer 
#	  (SendingApplication) 
#	- Implements the protocol for reliable transport
#	 using the udt_send() function provided by an unreliable channel.
#
# Receiver-side (rdt_Receiver)
#	- receives packets from the unrealible channel via calls to its
#	rdt_rcv() function.
#	- implements the receiver-side protocol and delivers the collected
#	data to the receiving application.




import simpy
import random
from Packet import Packet
import sys
import time

# sender side states
WAITING_FOR_CALL_FROM_ABOVE_0 = 0
WAITING_FOR_CALL_FROM_ABOVE_1 = 2
WAIT_FOR_ACK_0 = 1
WAIT_FOR_ACK_1 = 3


#receiver side states
WAITING_FOR_CALL_FROM_BELOW_0 = 0
WAITING_FOR_CALL_FROM_BELOW_1 = 1

class rdt_Sender(object):

	def __init__(self,env):
		# Initialize variables
		self.env=env 
		self.channel=None
		# some state variables
		self.state = WAITING_FOR_CALL_FROM_ABOVE_0
		self.seq_num=0
		self.packet_to_be_sent=None
		# additional timer-related variables
		self.timeout_value=6
		self.timer_is_running=False
		self.timer=None
		#for T_avg
		self.T_avg=0
		self.Total_time_spent=0
		self.total_packt_sent_n_received=0
		self.initial_time=0
		self.ending_time=0
		self.sendingApplication=None
		#self.collections1 = []
		#self.collections2 = []
		
	# This function models a Timer's behavior.	
	def timer_behavior(self):
		try:
			# Start
			self.timer_is_running=True
			yield self.env.timeout(self.timeout_value)
			# Stop
			self.timer_is_running=False
			
			# take some actions
			self.timeout_action()
		except simpy.Interrupt:
			# upon interrupt, stop the timer
			self.timer_is_running=False


	# This function can be called to start the timer
	def start_timer(self):
		assert(self.timer_is_running==False)		
		self.timer=self.env.process(self.timer_behavior())
	# This function can be called to stop the timer
	def stop_timer(self):
		assert(self.timer_is_running==True)
		self.timer.interrupt()
	def timeout_action(self):
		# add here the actions to be performed
		# upon a timeout
		self.channel.udt_send(self.packet_to_be_sent)
		self.start_timer()
	
	def rdt_send(self,packt):	###########packt=msg
		if self.state==WAITING_FOR_CALL_FROM_ABOVE_0:
			#self.packet_to_be_sent = Packet(seq_num=self.seq_num, payload=msg)#############
			self.packet_to_be_sent = packt ##############
			#packt.QBIT()
			#print("this is sender side:: QBIT VAL = ",packt.Q_bit)
			#packt.ENCODE()
			#print("this is sender side:: QBIT VAL = ",packt.Q_bit)
			
			self.channel.udt_send(self.packet_to_be_sent)
			#starting clock T_avg
			self.initial_time = time.time()
			self.seq_num+=1
			#start timer
			self.start_timer()
			self.state=WAIT_FOR_ACK_0
			return False
						
		elif self.state==WAITING_FOR_CALL_FROM_ABOVE_1:
			
			#self.packet_to_be_sent = Packet(seq_num=self.seq_num, payload=msg)
			self.packet_to_be_sent=packt
			self.seq_num-=1
			self.channel.udt_send(self.packet_to_be_sent)
			self.start_timer()
			self.state=WAIT_FOR_ACK_1
			return True
		else:
			return False
			
			
	def rdt_rcv(self,packt):
		if self.state==WAIT_FOR_ACK_0:
			if(packt.payload=="ACK" and packt.seq_num == 1):
				self.state==WAIT_FOR_ACK_0
			elif(packt.corrupted):
				self.state==WAIT_FOR_ACK_0
			elif(packt.payload=="ACK" and packt.seq_num == 0):
				#state change
				self.state = WAITING_FOR_CALL_FROM_ABOVE_1
				self.stop_timer()
			else:
				print("ERROR!!!")
				print("Halting simulation...")
				sys.exit(0)
			
		if self.state==WAIT_FOR_ACK_1:
			if(packt.payload=="ACK" and packt.seq_num == 0):
				self.state==WAIT_FOR_ACK_1
			elif(packt.corrupted):
				self.state==WAIT_FOR_ACK_1
			elif(packt.payload=="ACK" and packt.seq_num == 1):
				self.state = WAITING_FOR_CALL_FROM_ABOVE_0
				self.stop_timer()
				self.total_packt_sent_n_received+=1
				self.ending_time=time.time()
				self.Total_time_spent += (self.ending_time - self.initial_time)
				self.T_avg=(self.Total_time_spent/self.total_packt_sent_n_received)
				
			else:
				print("ERROR!!!")
				print("Halting simulation...")
				sys.exit(0)
			

			
class rdt_Receiver(object):
	def __init__(self,env):
		# Initialize variables
		self.env=env 
		self.receiving_app=None
		self.channel=None
		self.state = WAITING_FOR_CALL_FROM_BELOW_0
		self.sendingApplication=None
		

	def rdt_rcv(self,packt):
		if self.state==WAITING_FOR_CALL_FROM_BELOW_0:
			if(packt.corrupted or packt.seq_num == 1):
				response = Packet(seq_num=1, payload="ACK") 
				self.channel.udt_send(response)
			else:
				response = Packet(seq_num=0, payload="ACK") 
				self.channel.udt_send(response)
				#state change
				self.state = WAITING_FOR_CALL_FROM_BELOW_1
			
		if self.state==WAITING_FOR_CALL_FROM_BELOW_1:
			if(packt.corrupted or packt.seq_num == 0):
				response = Packet(seq_num=0, payload="ACK")
				self.channel.udt_send(response)
			else:
				response = Packet(seq_num=1, payload="ACK") 
				#state change
				self.state = WAITING_FOR_CALL_FROM_BELOW_0
				self.channel.udt_send(response)
				self.receiving_app.deliver_data(packt)###############
				packt.DECODE()
				
				#print("this is sender side:: QBIT VAL = ",self.packet_to_be_sent.Q_bit)
			
