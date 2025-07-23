# Step 1: Read input
N = int(input("Enter number of packets (N): "))

# Step 2: Read the array elements, one by one
arr = []
print("Enter the chocolate packets (use 0 for empty packets):")
for _ in range(N):
    arr.append(int(input()))

# Step 3: Move all non-zero elements to the front
pos = 0  # position to place the next non-zero element

for i in range(N):
    if arr[i] != 0:
        arr[pos] = arr[i]
        pos += 1

# Step 4: Fill the remaining positions with zeros
while pos < N:
    arr[pos] = 0
    pos += 1

# Step 5: Print the updated array
print("Rearranged packets:")
print(*arr)  # prints space-separated values
