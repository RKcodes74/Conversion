l1 = ["car", "bike", "animal"] 
l2 =["BMW","Yamaha","Dog"]
listtodict = dict(zip(l1, l2))
print(f"\n{listtodict}")

#conversion of binary search 
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  # target found at index mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # target not found

def main():
    # Example sorted list; you can modify it or read from input
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    print("Sorted list:", arr)
    
    # Ask user for target
    try:
        target = int(input("Enter the number to search for: "))
    except ValueError:
        print("Please enter a valid integer.")
        return

    result = binary_search(arr, target)
    if result != -1:
        print(f"✅ Found {target} at index {result}.")
    else:
        print(f"❌ {target} is not in the list.")

if __name__ == "__main__":
    main()
