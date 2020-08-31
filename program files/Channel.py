#we will impliment this projet with Qiskit this is only a prototype
# SimPy model for an unreliable communication channel.
#
#	A packet sent over this channel:
#		- can get corrupted, with probability Pc
#		- can get lost, with probability Pl
#		- reaches the other end after "delay" amount of time, if it is not lost.
#



import simpy
import random
from Packet import Packet
import copy
class UnreliableChannel(object):

	def __init__(self,env,Pc,Pl,delay,name):
		# Initialize variables
		self.env=env 
		self.Pc=Pc
		self.Pl=Pl
		self.delay=6
		self.receiver=None
		self.name=name
		self.sendingApplication=None
	def udt_send(self,packt_to_be_sent):
		
		# this function is called by the sending-side 
		# to send a new packet over the channel.
		#packt=copy.copy(packt_to_be_sent) #!!! BEWARE: Python uses pass-by-reference by default.Thus a copy() is necessary
		
		print("TIME:",self.env.now,self.name,": udt_send called for",packt_to_be_sent)
		# start a process to deliver this packet across the channel.
		self.env.process(self.deliver_packet_over_channel(self.delay, packt_to_be_sent)) 
		
		


	def deliver_packet_over_channel(self, delay, packt_to_be_delivered):
		#packt=copy.copy(packt_to_be_delivered)################self.sendingApplication=null
		# Is this packet lost?
		if random.random()<self.Pl:
			print("TIME:",self.env.now,self.name,":",packt_to_be_delivered,"was lost!")############packt_to_be_delivered=packt
		else:
			# Is this packet corrupted?
			if random.random()<self.Pc:
				packt.corrupt()
				print("TIME:",self.env.now,self.name,":",packt,"was corrupted!")#################packt_to_be_delivered=packt
			# Now wait for "delay" amount of time
			yield self.env.timeout(delay)
			# deliver the packet by calling the rdt_rcv()
			# function on the receiver side.
			#self.receiver.rdt_rcv(packt)###########self.sendingApplication=null########################packt_to_be_delivered=packt
			self.receiver.rdt_rcv(packt_to_be_delivered)
		
