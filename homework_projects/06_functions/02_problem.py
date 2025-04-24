import random

# Probability of stopping the counting at any step (20%)
DONE_LIKELIHOOD = 0.2
def chaotic_counting():
    """
    Counts from 1 to 10, but might stop early if done() returns True.
    """
    i = 0
    while (i < 10):
        i += 1
        # Check if we should stop counting
        if done():
            return # Exit the function early
        # Print the current number if not done
        print(i) 
      
def done():
    """ Returns True with a probability of DONE_LIKELIHOOD """
    if random.random() < DONE_LIKELIHOOD:
        return True
    return False

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("I'm done")

if __name__ == "__main__":
    main()