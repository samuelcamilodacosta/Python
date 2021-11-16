# Correct Answer

# Roumes was an above average student. In math tests, he always got a maximum score, getting all the 
# maths right, but his secret wasn't in doing the math correctly. He interpreted what he saw in the 
# environment around him and he could deduce the answers to the questions. You too can be someone 
# special, just like Roumes.

# For each question asked, print the word 'resposta', followed by a space, then the question number, 
# a colon, a space and the answer.

cases = int(input())
for index in range(1,cases+1):
    answer = input()
    print(f'resposta {index}: {answer}')
