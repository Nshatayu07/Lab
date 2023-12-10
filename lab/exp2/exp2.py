import csv
import math

def min_max_normalization(data, new_min, new_max):
    mini = min(data)
    maxi = max(data)
    normalized_data = []
    for value in data:
        normalized_value = ((value - mini) / (maxi - mini)) * (new_max - new_min) + new_min
        normalized_data.append(normalized_value)
    return normalized_data

def z_score_normalization(data):
    mean = sum(data) / len(data)
    standard_deviation = math.sqrt(sum((value - mean) ** 2 for value in data) / len(data))
    normalized_data = []
    for value in data:
        normalized_value = (value - mean) / standard_deviation
        normalized_data.append(normalized_value)
    return normalized_data

def main():
    data = []
    with open('exp2/data2.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(float(row[0]))
   
    opt = int(input("Enter option:\n1. Min-Max Normalization\n2. Z-Score Normalization\nOption: "))
   
    if opt == 1:
        new_min = float(input("Enter new min: "))
        new_max = float(input("Enter new max: "))
        normalized_data = min_max_normalization(data, new_min, new_max)
        with open('exp2/exp2_output_MinMax.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerow(['Data', 'Normalized Data'])
            for i in range(len(data)):
                writer.writerow([data[i], normalized_data[i]])
    elif opt == 2:
        normalized_data = z_score_normalization(data)
        with open('exp2/exp2_output_Zscore.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerow(['Data', 'Normalized Data'])
            for i in range(len(data)):
                writer.writerow([data[i], normalized_data[i]])
    else:
        print("Wrong Option")

if __name__ == "__main__":
    main()
