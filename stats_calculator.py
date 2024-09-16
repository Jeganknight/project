# stats_calculator.py
import statistics
import sys

def calculate_statistics(data):
    mean = statistics.mean(data)
    median = statistics.median(data)
    std_dev = statistics.stdev(data)
    return mean, median, std_dev

def read_data_from_file(filename):
    with open(filename, 'r') as file:
        return [float(line.strip()) for line in file]

if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        data = read_data_from_file(filename)
    else:
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    mean, median, std_dev = calculate_statistics(data)
    print(f"Mean: {mean}, Median: {median}, Standard Deviation: {std_dev}")
print("Succesflly Done!")
print("Completed")
