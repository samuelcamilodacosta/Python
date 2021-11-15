# Class Dismissed!

# For each class will be defined a minimum number of attendants who must be in the room at 
# the scheduled time. If this number is not reached, training will be canceled.

# Given the total number of students in the class, the miminum number of attendants and the 
# expected arrival for each of them, determine if the training will happen or not. Consider 
# that if the expected arrival for a student Ai > 0, he is late.

# The first line of input consists of two integers N (1 <= N <= 106) and K (0 <= K <= 106) 
# representing the number of students and the minimum amount of students required to have 
# the class, respectively. The next input line is given by N integers A1, A2, ..., An (-104 <= An <= 104), 
# the time each student will arrive to the class.

# For each test case, your program should produce a single line with the word YES if the 
# training will happen or NO otherwise.


numberOfStudents, minimunNumberOfStudents = input().split()
numberOfStudents, minimunNumberOfStudents = [int(numberOfStudents), int(minimunNumberOfStudents)]
array = list(map(int,input().split()))
presentStudents = 0
for time in array:
    if(time <= 0):
        presentStudents += 1
if(minimunNumberOfStudents <= presentStudents):
    print("YES")
else:
    print("NO")