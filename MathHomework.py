print("MathHomework.py")
problem = input ("Enter a Math Problem, or 'q' to Quit: ")
while (problem != "q"):
    print("The answer to ", problem, "is:", eval(problem))
    problem = input ("Enter another Math Problem, or 'q' to Quit: ")
