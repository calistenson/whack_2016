#Kim Asenbeck
#WHACK
#2-20-16
#findSeats

cinema = [[0, 0, 0, 1, 0], [0, 1, 0, 0, 1], [0, 1, 1, 0, 1], [1, 0, 1, 0, 1], [1, 1, 1, 0, 1]]

def findSeats(theater, num):
	if num > 5: return #there are only 5 seats in each row (for now)
	result = [] 
	for i in range (5): #assess each row, looking for n consecutive seats.
		

	return result 


def availableSeats(theater):
	#return the first seat in a sequence of n available seats
	seats = []
	for (i, row) in enumerate(theater): 
		for (j, seat) in enumerate(row):
			if theater[i][j] == 0:
				seats.append((i, j))
	return seats;

def seatStatus(theater, row, col): 
	return  theater[row][col] #theater is a 2d array; return 0 if empty, 1 if seat is full

# # Changes status of seat from empty to full and vice versa, when the sensor status changes
def changeStatus(theater, row, col): 
	current = seatStatus(theater, row, col) #when we actually have a database running, we'll need to access the value from there
	theater[row][col] = 1 if current == 0 else 0 #but make sure to actually change the value in the database

print findSeats(cinema, 2)


#available= availableSeats(theater) #get a list of all available seats
		# row = []
		# for seat in available: #in this loop, I create a list of available seats in each row.
		# 	if seat[0] == i: 
		# 		row.append(seat) 
		# #now we've created a list of the available seats in row i. 
		# #now, the task is: find combinations of n consecutive seats
		# for chair in row: 