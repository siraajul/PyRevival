def create_mat_design(n, m):
    # Calculate the number of patterns in the upper half
    pattern_count = n // 2

    # Create the upper half of the design
    for i in range(pattern_count):
        pattern = ".|." * (2 * i + 1)  # Create the pattern
        print(pattern.center(m, '-'))  # Center the pattern with '-'

    # Print the welcome line
    print("WELCOME".center(m, '-'))

    # Create the lower half of the design
    for i in range(pattern_count - 1, -1, -1):
        pattern = ".|." * (2 * i + 1)  # Create the pattern
        print(pattern.center(m, '-'))  # Center the pattern with '-'

# Sample Input
n = 9
m = 27

# Generate the mat design
create_mat_design(n, m)
