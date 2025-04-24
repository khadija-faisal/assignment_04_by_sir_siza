from time import sleep

def liftoff():
     # Loop from 10 to 1
    for i in range(10, 0, -1): # The range starts at 10, ends at 1, and decreases by 1
        sleep(1) # print each number in next line with 1 sec delay
        print(i)
    print("Liftoff 🚀 🎉")  # Output Liftoff after the countdown is complete

def main():
    liftoff()
   


if __name__ == '__main__':
    main()