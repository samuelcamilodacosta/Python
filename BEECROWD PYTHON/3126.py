# Training List

# Input
# The first line of each test is a single integer C (1 <= C <= 1000), representing the amount 
# of registered candidates. The next line is composed of C integers separated by a space, 
# each being 1 if the corresponding candidate joined the event, and 0 if he didn't.

# Output
# The output should be a single integer, representing the amount of candidates that joined 
# the event.

totalCandidates = int(input())
array = list(map(int,input().split()))
joinedTheEvent = 0
for value in array:
    if value == 1:
        joinedTheEvent += 1
print(joinedTheEvent)