from __future__ import print_function
from rule import board
from copy import deepcopy as dc
from random import randint
import numpy as np
class node:
	def __init__(self,on,w,color):
		w=float(w)
		self.on=on
		self.n=0
		self.w=w
		self.q=w
		self.color=color
		self.under=[]
		self.x=8
		self.y=8
	def expand(self,b,turn):
		ok=[]
		for i in range(8):
			for j in range(8):
				if b.ok(i,j,turn):
					ok.append((i,j))
		if len(ok)==0:
			self.under.append(node(self,b.count(),0))#pass
			return
		t=dc(b)
		for i in ok:
			t.grid=dc(b.grid)
			t.play(i[0],i[1],turn)
			self.under.append(node(self,t.count(),turn))
			self.under[-1].x=i[0];self.under[-1].y=i[1]
	def select(self,b,d=0):
		while self.under!=[]:
			if self.color==1:
				qu=[i.q+10*np.sqrt(self.n)/(1+i.n) for i in self.under]
			else:
				qu=[-i.q+10*np.sqrt(self.n)/(1+i.n) for i in self.under]
			maxx=-100
			index=0
			for i in range(len(qu)):
				if qu[i]>maxx:
					maxx=qu[i]
					index=i
			#print(index)
			#index=max(xrange(len(qu)),key=qu.__getitem__)
			#print(index)
			self=self.under[index]
			if self.color!=0:
				b.play(self.x,self.y,self.color)
			if d:
				b.dump()
				print()
		return [self,b]
	def backup(self):
		while self.on!=0:
			self.n+=1
			self.w=0;
			for i in self.under:
				self.w+=i.w
			self.q=self.w/self.n
			self=self.on
	def mcts(self,b):
		self,b=self.select(b)
		self.expand(b,(not(self.color-1))+1)
		self.backup()
