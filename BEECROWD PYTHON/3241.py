# Help a PhD Candidate Out!

# Jon Marius forgot how to add two numbers while doing research for his PhD. And now he has a long list 
# of addition problems that he needs to solve, in addition to his computer science ones! Can you help him?

# Output the result of each addition. For lines containing “P=NP”, output “skipped”.

cases = int(input())
while(cases > 0):
    string = input().split('+')
    if(len(string) == 1):
        print("skipped")
    else:
        sum = 0
        for element in string:
            sum += int(element)
        print(sum)
    cases -= 1