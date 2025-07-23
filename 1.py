# Step 1: Get the number of test cases from the user
test_cases = int(input("Enter number of test cases: "))

# Step 2: Loop through each test case
for i in range(test_cases):
    # Step 3: Get the input values for this test case
    # F = forward distance, B = backward distance, T = time per meter, D = distance to wall
    forward, backward, time_per_meter, distance_to_wall = map(int, input("Enter F B T D: ").split())

    # Step 4: Start from position 0 (initial position)
    current_position = 0
    total_time = 0

    # Step 5: Repeat the movement until car hits or crosses the wall
    while True:
        # Move backward
        current_position += backward
        total_time += backward * time_per_meter

        # Check if the car has reached or crossed the wall
        if current_position >= distance_to_wall:
            break  # Stop the loop because car hit the wall

        # Move forward
        current_position -= forward
        total_time += forward * time_per_meter

    # Step 6: Print total time taken before hitting the wall
    print("Time to hit the wall:", total_time)
