#we will impliment this projet with Qiskit this is only a prototype
# This is a Python class for a Packet.
#
# A packet has three fields:
#	payload: the data contained in the packet,
#	seq_num: the packet sequence number,
#	corrupted: a flag, which can be True or False
#

import random


collections2 = []
collections1 = []
decoded_value_collection =[]
key = []
#Qbit_val_collection=[]
#encode_val_collection=[]
class Packet(object):
	
	def __init__(self,payload, seq_num):
		self.payload=payload
		self.Q_bit=2	
		self.seq_num = seq_num
		self.corrupted=False
		self.enc_choice_for_one="XXX"
		self.enc_choice_for_zero="XXX"
		self.count=0
		self.arr=[0,1]
		self.c=2
		self.decoded_value=2
		
		#self.collections2 = []



	def QBIT(self):
		
		self.Q_bit = random.choice(self.arr)



	def ENCODE(self):
		self.count=self.count+1
		if self.count==1:
			self.Q_bit_VAL=self.Q_bit
			self.Q_bit=2
			#print("USE | or / for 1 and USE --- or \ for 0")
			print("=============================================")
			print("Encoding starts for bit no ",self.payload + 1)
			print("=============================================")
			if self.Q_bit_VAL==1:
				print("USE | or / for 1 ")
				#self.enc_choice_for_one = str(hash(input(">>")))
				self.enc_choice_for_one = input(">>")
				collections1.append(self.enc_choice_for_one)
				print("Symbols used for Encoding =",collections1)
				
			elif self.Q_bit_VAL==0:
				print("USE --- or \_ for 0 ")
				#self.enc_choice_for_zero = str(hash(input(">>")))
				self.enc_choice_for_zero = input(">>")
				collections1.append(self.enc_choice_for_zero)
				print("Symbols used for Encoding =",collections1)
			else:
				print("you can not encode becouse Q-BIT is in superposition state use QBIT() for observation first")
		else:
			print("u are reciever u can not use this method")
		print("=============================================")
		print("Encoding ends for bit no ",self.payload + 1)
		print("=============================================")

	def DECODE(self):
		print("=============================================")
		print("Decoding starts for bit no ",self.payload + 1)
		print("=============================================")
		print("USE X for mult method and USE + for add method")
		self.dmethod=input(">> ")
		collections2.append(self.dmethod)
		print("Symbols used for Decoding =",collections2)
		if self.dmethod=='X':
			if self.enc_choice_for_one=="/":#this is \
				self.decoded_value = 1
				print("decode value is =",self.decoded_value)
				decoded_value_collection.append(self.decoded_value +10)
				print("decoded value collections  =",decoded_value_collection)
				pass
			elif self.enc_choice_for_zero=="\_":# this is for /
				self.decoded_value = 0
				print("decode value is =",self.decoded_value)
				decoded_value_collection.append(self.decoded_value +10)
				print("decoded value collections  =",decoded_value_collection)
				pass
			elif self.enc_choice_for_one=="|":#this is |
				self.c = random.choice(self.arr)
				if self.c == 1:
					self.decoded_value = 1
					print("decode value is =",self.decoded_value)
					decoded_value_collection.append(self.decoded_value)
					print("decoded value collections  =",decoded_value_collection)
				if self.c == 0:
					self.decoded_value = 0
					print("decode value is =",self.decoded_value)
					decoded_value_collection.append(self.decoded_value)
					print("decoded value collections  =",decoded_value_collection)
			elif self.enc_choice_for_zero=="---":# this is for ---
				self.c = random.choice(self.arr)
				if self.c == 1:
					self.decoded_value = 1
					print("decode value is =",self.decoded_value)
					decoded_value_collection.append(self.decoded_value)
					print("decoded value collections  =",decoded_value_collection)
				if self.c == 0:
					self.decoded_value = 0
					print("decode value is =",self.decoded_value)
					decoded_value_collection.append(self.decoded_value)
					print("decoded value collections  =",decoded_value_collection)
			elif self.enc_choice_for_one=="XXX" and self.enc_choice_for_zero=="XXX":
				print("you have not used ENCODE() method for this Q-BIT")
			else:
				print("sender did not used right encoding characters")
		
			
		if self.dmethod=="+":
			if self.enc_choice_for_one=="\_":#this is \
				self.c = random.choice(self.arr)
				if self.c == 1:
					self.decoded_value = 1
					print("decode value is =",self.decoded_value)
					decoded_value_collection.append(self.decoded_value)
					print("decoded value collections  =",decoded_value_collection)
				if self.c == 0:
					self.decoded_value = 0
					print("decode value is =",self.decoded_value)
					decoded_value_collection.append(self.decoded_value)
					print("decoded value collections  =",decoded_value_collection)
			elif self.enc_choice_for_zero=="/":# this is for /
				self.c = random.choice(self.arr)
				if self.c == 1:
					self.decoded_value = 1
					print("decode value is =",self.decoded_value)
					decoded_value_collection.append(self.decoded_value)
					print("decoded value collections  =",decoded_value_collection)
				if self.c == 0:
					self.decoded_value = 0
					print("decode value is =",self.decoded_value)
					decoded_value_collection.append(self.decoded_value)
					print("decoded value collections  =",decoded_value_collection)
			elif self.enc_choice_for_one=="|":#this is |
				self.decoded_value = 1
				print("decode value is =",self.decoded_value)
				decoded_value_collection.append(self.decoded_value +10)
				print("decoded value collections  =",decoded_value_collection)
				pass
			elif self.enc_choice_for_zero=="---":# this is for ---
				self.decoded_value = 0
				print("decode value is =",self.decoded_value)
				decoded_value_collection.append(self.decoded_value +10)
				print("decoded value collections  =",decoded_value_collection)
				pass
			elif self.enc_choice_for_one=="XXX" and self.enc_choice_for_zero=="XXX":
				print("you have not used ENCODE() method for this Q-BIT")
			else:
				print("sender did not used right encoding characters")
		print("=============================================")
		print("Decoding ends for bit no",self.payload + 1)
		print("=============================================")
		
		if len(decoded_value_collection) == 4:
			for i in decoded_value_collection:
				if i == 1 or i == 0:
					key.append(0)
				elif i == 10:
					key.append(0)
				elif i == 11:
					key.append(1)
				else:
					key.append(404)
			print("==================================================================================>")
			print("Generated secret key = ",key)
			print("==================================================================================>")
			




	# this function can be called
	# to mark a packet as "corrupted".
	def corrupt(self):
		self.corrupted=True
		self.payload="$H!T"

	# this function can be used to print a packet
	def __str__(self):
		return "Packet(seq_num=%d, payload=%s, corrupted=%s ,Q_BIT=%s)"% (self.seq_num, self.payload, self.corrupted, self.Q_bit)


