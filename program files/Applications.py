#we will impliment this projet with Qiskit this is only a prototype
# SimPy models for the Sending and Receiving Applications.
#
# The sending application:
#	- keeps creating new messages
#	- requests the lower-layer (rdt_sender)
#	  to deliver each message using the rdt_send() function
#
# The receiving application:
#	- receives the message delivered by the lower-layer to its
#	   deliver_data() method.
#	- does some basic validation.




import simpy
import random
from Packet import *
import sys

Qbit_val_collection = []
class SendingApplication(object):

	def __init__(self,env):
		# Initialize variables
		self.env=env 
		self.rdt_sender=None
		self.total_messages_sent=0
		# start behavior
		self.env.process(self.behavior())
		self.rdt_sender=None
		
		#self.packt=Packet(0,0)

	def behavior(self):

		while True:
		# wait for a random amount of time
			t=1
			yield self.env.timeout(t)

			# create a message (its just a number, for now.)
			msg = self.total_messages_sent
			
			packt=Packet(msg,self.rdt_sender.seq_num)
			# try to send it.
			
			if self.rdt_sender.rdt_send(packt):##############msg=packt
				# success.
				packt.QBIT()
				print("this is sender side:: QBIT VAL = ",packt.Q_bit)
				Qbit_val_collection.append(packt.Q_bit)
				print("this is original Qbit collections:: QBIT VAL = ",Qbit_val_collection)
				packt.ENCODE()
				print("this is sender side:: QBIT VAL = ",packt.Q_bit)
				self.total_messages_sent+=1
				
				print("TIME:",self.env.now,"SENDING APP: sent packet data with payload",msg)
			
			elif self.total_messages_sent==4:
				#print("T_avg:",self.rdt_sender.T_avg)
				
				
				break
			else:
				pass
		
			

class ReceivingApplication(object):

	def __init__(self,env):
		# Initialize variables
		self.env=env
		self.total_packets_received=0
		self.rdt_sender=None

	def deliver_data(self,packt): ###############packt=data
		# This function is called by the lower-layer (rdt_receiver)
		# to deliver data to the Receiving Application
		#packt.DECODE()
		print("TIME:",self.env.now,"RECEIVING APP: received data",packt.payload)#################packt=data

		# do some basic validation.
		if not (packt.payload==self.total_packets_received):
			print("ERROR!! RECEIVING APP: received wrong data:",packt,",expected:",self.total_packets_received)###########packt=data
			print("Halting simulation...")
			sys.exit(0)
		self.total_packets_received+=1
		#if self.total_packets_received==1000:
			#print("T_avg:",self.rdt_sender.T_avg)
			

