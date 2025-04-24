
fruits = {'strawberry': 1.5, 'melon': 50, 'pomegranate': 80, 'kiwi': 1, 'dragonfruit': 1.5, 'mango': 5}
def main():
    total_cost = 0
    for fruit in fruits:
        price = fruits[fruit]
        user_fruit_budget = int(input(f" how many {fruit} do you want? enter quantity:"))
        total_cost += price * user_fruit_budget
        
    print(f"total cost of fruits is ${total_cost}")    

      

if __name__ == '__main__':
    main()