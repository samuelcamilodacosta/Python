# Coding Competition

# A group of students decided to organize the GCC (Greatest Coding Competition), which will 
# be, obviously, the greatest coding competition that has ever happened. There are N universities 
# that can send students to participate in the form of teams of three. Now the organizers of 
# the GCC want to know: assuming that each student attends only one university and can be in 
# only one team and that teams can only be formed by students from the same university, what is 
# the maximum number of students could attend the GCC.

# The output must constain a single integer: the maximum number of students could attend the
# GCC given the constraints above.

universities = int(input())
array = list(map(int,input().split()))
sumOfMaximumStudents = 0
for value in array:
    while((value%3 != 0) & (value>2)):
        value = value-1
    if value%3 == 0:
        sumOfMaximumStudents += value
print(sumOfMaximumStudents)