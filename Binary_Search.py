"""
Binary Search Program
author: Akshit Gupta
"""

#Bianry Search Function
def binary_search (arr, len, number):
    start = 0
    end = len - 1
    
    while end >= start:
        mid = (start + end)//2
        if arr[mid] == number:
            return print (f'Number {number} is found at index {mid}')     
        if number > arr [mid]:
            start = mid + 1
        else:
            end = mid - 1
    return print("Number not found")   

#Main function
if __name__ == "__main__":
    #taking input from user
    list_input = input('Enter the number of integers in the string followed by space ')
    list1 = list_input.split()

    #Converting string to integer
    list1 = [int (i) for i in list1]
    
    #Taking the  iser input dynamically
    number = int (input ("Enter a number you want to search in the list "))
    
    #Calling the binary search function
    binary_search(list1, len(list1), number)




