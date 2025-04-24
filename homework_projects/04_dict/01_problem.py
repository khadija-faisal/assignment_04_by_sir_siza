def get_numbers():
    numbers = []
    n = input("enter a number")
      # Continuously prompt the user for input until they enter a blank line
    while n != "":
        numbers.append(int(n))
        n = input("enter a number")

    return numbers

def count_numbers(nums):
    
      # Create an empty dictionary to store counts of each number
    counts = {}
    for n in nums:
         #If number already exists, increment count; otherwise set it to 1
        counts[n] = counts.get(n, 0) + 1
    return counts



def counts_of_same_num(counts):
    # Loop through the dictionary and print each number with its count
    for num, count in counts.items():
        print(f"{num} appears {count} times.")

def main():
    counts_of_same_num(count_numbers(get_numbers()))

if __name__ == '__main__':
    main()
