#Kim Asenbeck
#WHACK
#2-20-16
#findSeats.py

from hello import get_seats

#cinema = [[0, 0, 0, 1, 0], [0, 1, 0, 0, 1], [0, 1, 1, 0, 1], [1, 0, 1, 0, 1], [1, 1, 1, 0, 1]]
cinema = get_seats()

def findSeats(theater, num):
	if num > 5: return 
	seats = []
	for (i, row) in enumerate(theater): #for each row in the theater
		for (j, seat) in enumerate(row): #for each seat in the row
			need = num
			curr_seats = []
			while (need > 0) and (j < 5):
				if theater[i][j] == 0:
					curr_seats.append((i, j))
					need -= 1
					j += 1
				else: 
					curr_seats = []
					need = num
					j += 2
				if len(curr_seats) ==  num:
					if curr_seats not in seats:
						seats.append(curr_seats)
						curr_seats = []
						need = 0
	return seats 


def availableSeats(theater):
	#return the first seat in a sequence of n available seats
	seats = []
	for (i, row) in enumerate(theater): 
		for (j, seat) in enumerate(row):
			if theater[i][j] == 0:
				seats.append((i, j))
	return seats

def seatStatus(theater, row, col): 
	return  theater[row][col] #theater is a 2d array; return 0 if empty, 1 if seat is full

# # Changes status of seat from empty to full and vice versa, when the sensor status changes
def changeStatus(theater, row, col): 
	current = seatStatus(theater, row, col) #when we actually have a database running, we'll need to access the value from there
	theater[row][col] = 1 if current == 0 else 0 #but make sure to actually change the value in the database

#print findSeats(cinema, 2)
print findSeats(cinema, 1)


#available= availableSeats(theater) #get a list of all available seats
		# row = []
		# for seat in available: #in this loop, I create a list of available seats in each row.
		# 	if seat[0] == i: 
		# 		row.append(seat) 
		# #now we've created a list of the available seats in row i. 
		# #now, the task is: find combinations of n consecutive seats
		# for chair in row: 
