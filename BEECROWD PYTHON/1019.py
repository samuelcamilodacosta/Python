# Time Conversion

# Read an integer value, which is the duration in seconds of a certain event in a factory, 
# and inform it expressed in hours:minutes:seconds.

# The input file contains an integer N.

# Print the read time in the input file (seconds) converted in hours:minutes:seconds 
# like the following example.

durationSeconds = int(input())

if durationSeconds > 3600:
    hour = int(durationSeconds/3600)
    durationSeconds = durationSeconds-(hour*3600)
else:
    hour = int (0)

if durationSeconds > 60:
    minutes = int(durationSeconds/60)
    durationSeconds = durationSeconds - (minutes*60)
else:
    minutes = int (0)

print(f'{hour}:{minutes}:{durationSeconds}')