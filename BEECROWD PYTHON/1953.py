# Robert and Rampant Room

# All classroom students should give the registration name and abbreviation of the course on a 
# sheet, and the call will be computed later. They need to know how many students from each 
# course attended. It has the data, but unfortunately does not have the required proficiency in 
# programming for "CODE" it. You could help you to know, given a list of students, how many of 
# EPR, how many of EHD and how many intruders?

# Your program should print three lines containing the number of students who are EPR, EHD and 
# INTRUSOS in the format: "acronym: quantity." (See example output).

while True:
    try:
        cases = int(input())
        epr = 0
        ehd = 0
        intruders = 0
        while(cases > 0):
            registrationNumber, course = input().split()
            if course == 'EHD': ehd += 1
            elif course == 'EPR': epr += 1
            else: intruders += 1
            cases -= 1
        print("EPR:", epr)
        print("EHD:", ehd)
        print("INTRUSOS:", intruders)
    except EOFError:
        break