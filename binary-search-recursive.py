# -- **************** Binary search program using recursive method **************** --
# Note: An array through to binary search must be sorted

# Define a func with four parameters - array (as arr), two pointers - high and low and target value (as x).


def binarySearch(arr, x, low, high):
    # Check if two pointers points to the same index

    if high >= low:
        # Find the middle index of array by halving.

        mid = (high + low) // 2

        # Check if the target value is same as the value pointed by mid

        if arr[mid] == x:
            return mid

        # If value of mid pointer is higher than target value, pointer high is changed to mid - 1
        # while pointer low remains unchanged
        elif arr[mid] > x:
            # Search on left sub-array
            return binarySearch(arr, x, low, mid - 1)

        else:
            # Search on right sub-array
            return binarySearch(arr, x, mid + 1, high)

    # If pointer high and low meets then target value is not present in the array and will return -1
    else:
        return -1


# Let's pass an array and target value to binarySearch function
arr = [1, 4, 7, 10, 15, 20, 27, 38, 49, 100]
x = 49

# Function call
result = binarySearch(arr, x, 0, len(arr) - 1)

if result != -1:
    print("Target value found in index", str(result))
else:
    print("Target value not present in array.")
