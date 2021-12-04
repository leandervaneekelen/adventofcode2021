"""
Measure how many times a number is larger than the
previous number for an arbitrarily long list.
"""

from pathlib import Path

# Part one
# if __name__ == "__main__":

#     # Read numbers
#     input_file = Path("./input.txt")
#     with input_file.open() as file:
#         lines = [line.strip() for line in file.readlines()]
#         measurements = [int(measurement) for measurement in lines]

#     # Find number of increases
#     n_larger = 0
#     for i in range(1, len(measurements)):
#         before = measurements[i - 1]
#         current = measurements[i]
#         if current > before:
#             n_larger += 1
#     print(n_larger)

# Part two
if __name__ == "__main__":

    # Read numbers
    input_file = Path("./input.txt")
    with input_file.open() as file:
        lines = [line.strip() for line in file.readlines()]
        measurements = [int(measurement) for measurement in lines]

    # Find number of increases over sliding window
    n_larger = 0
    previous = sum(measurements[0:3])
    for i in range(2, len(measurements)):
        current = sum(measurements[i - 1: i + 2])
        if current > previous:
            n_larger += 1
        previous = current
    print(n_larger)