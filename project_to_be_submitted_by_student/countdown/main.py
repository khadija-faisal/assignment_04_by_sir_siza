import time
# countdown function
def countdown(t):
    while t:
        # divmod(t, 60) returns a tuple (mins, secs)
        mins, secs = divmod(t, 60)
        # format the timer as 02d:02d (2 digits for mins and secs)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        # end="\r" means print on the same line
        print(timer, end="\r")
        # wait for 1 second
        time.sleep(1)
        t -= 1
    print("Time's up run no more!")

# main function
def main():
    t = input("Enter the time in seconds: ")
    countdown(int(t))

if __name__ == '__main__':
    main()
