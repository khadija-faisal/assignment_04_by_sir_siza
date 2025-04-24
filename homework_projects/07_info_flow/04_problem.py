
fruit_stock = {
    "apple": 50,
    "banana": 100,
    "orange": 75,
    "pear": 1000,
    "grape": 30
}
	
def num_in_stock(fruit):
    return fruit_stock.get(fruit.lower())
def main():
    get_fruit : str = input("Enter a fruit name to know the number of stock: ")
    count = num_in_stock(get_fruit)
    if count is None or count == 0:
        print("This fruit is not in stock.")
    else:
        print("the number of stock is: ", count)
	
	

if __name__ == '__main__':
    main()