# ************** Binary search using iterative method **************


# Defining a function with parameter of array (as arr), target value (as x) and two pointers (as low and high)
def binarySearch(arr, x, low, high):
    # Using a while loop to check if the two pointers (high and low) meets
    while high >= low:
        # Finding the mid index of array by dividing into half
        mid = (high + low) // 2

        # Comparing the mid index value with target value
        if arr[mid] > x:
            # If value of mid index is greater than target value then assigning the index of mid - 1 to pointer high
            high = mid - 1

        elif arr[mid] < x:
            # If value of mid index is less than target value then assigning the index of mid + 1 to pointer low
            low = mid + 1

        else:
            # If mid index value is equal to target value then return index of mid
            return mid

    # Return -1 if two pointer meets
    return -1


# Let's test an array
testArray = [4, 7, 9, 11, 14, 20, 25, 27, 30]
targetValue = 27

# Call the function
result = binarySearch(testArray, targetValue, 0, len(testArray) - 1)

if result != -1:
    print("The target value is present at index of", str(result), "in given array.")
else:
    print("Target value is not present in given array")
