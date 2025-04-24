def main():
   numbers_list : list[int] = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
   total_sum_of_list : int = 0
   for num in numbers_list :
       total_sum_of_list = total_sum_of_list + num
   print("the total sum of list is " +str(total_sum_of_list))
       
      
if __name__ == '__main__':
    main()