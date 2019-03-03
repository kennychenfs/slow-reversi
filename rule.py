class board:
	step=[[1,1],[1,0],[1,-1],[0,1],[0,-1],[-1,1],[-1,0],[-1,-1]]
	def __init__(self):
		self.grid=[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,2,1,0,0,0],[0,0,0,1,2,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
	def dump(self):
		for i in self.grid:
			for j in i:
				if j==0:
					print(" +", end="")
				elif j==1:
					print(" O", end="")
				elif j==2:
					print(" X", end="")
			print()
	def ok(self,x,y,color):
		if self.grid[x][y]!=0:
			return 0
		for i in self.step:
			a=0
			tx=x+i[0];ty=y+i[1]
			while tx<8 and ty<8 and tx>=0 and ty>=0 and self.grid[tx][ty]==(not(color-1))+1:
				tx+=i[0];ty+=i[1]
				a=1
			if not a:
				continue
			if tx<0 or ty<0 or tx>=8 or ty>=8 or self.grid[tx][ty]!=color:
				continue
			return 1
		return 0
	def play(self,x,y,color):
		self.grid[x][y]=color
		for i in self.step:
			tx=x+i[0];ty=y+i[1]
			if tx<0 or ty<0 or tx>=8 or ty>=8 or self.grid[tx][ty]!=(not(color-1))+1:
				continue
			tx=x+i[0];ty=y+i[1]
			while tx<8 and ty<8 and tx>=0 and ty>=0 and self.grid[tx][ty]==(not(color-1))+1:
				tx+=i[0];ty+=i[1]
			if tx<0 or ty<0 or tx>=8 or ty>=8 or self.grid[tx][ty]!=color:
				continue
			tx-=i[0];ty-=i[1]
			while tx<8 and ty<8 and tx>=0 and ty>=0 and self.grid[tx][ty]==(not(color-1))+1:
				self.grid[tx][ty]=color
				tx-=i[0];ty-=i[1]
