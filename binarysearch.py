def find_range_with_difference_of_two(start, end):
    if start > end:
        return []

    if start % 2 == 1:
        start += 1

    if end % 2 == 1:
        end -= 1

    if start > end:
        return []

    return list(range(start, end + 1, 2))

# Example usage:
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

result = find_range_with_difference_of_two(start, end)

if result:
    print("Range with a difference of two:", result)
else:
    print("No such range found in the specified range.")
