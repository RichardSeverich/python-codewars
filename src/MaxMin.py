#In this little assignment you are given a string of space separated numbers, 
#and have to return the highest and lowest number.

def high_and_low(numbers):
    listNumbers = numbers.split()
    mayorMenor = (max(listNumbers, key=int)) + " " + (min(listNumbers, key=int))
    return mayorMenor