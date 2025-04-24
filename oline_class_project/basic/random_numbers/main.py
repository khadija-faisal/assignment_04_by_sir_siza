import random



N_NUMBERS: int = 10  # constant count of numbers
MIN_VALUE: int = 1  # constant min value
MAX_VALUE: int = 100  # constant max value


def main():
   # generate 10 random numbers between 1 and 100
   for i in range(N_NUMBERS):
       number = random.randint(MIN_VALUE, MAX_VALUE)
       print(number, end=" ")

if __name__ == '__main__':
    main()