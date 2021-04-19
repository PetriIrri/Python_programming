
def bubble_sort(numbers):
    for passnum in range(len(numbers)-1,0,-1):
        swapped = False
        for i in range(passnum):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                swapped = True
        if not swapped:
            break
    return numbers

numbers = [6,2,8,10,1,3,2,4,5,6]
numbers = bubble_sort(numbers)
print(numbers)