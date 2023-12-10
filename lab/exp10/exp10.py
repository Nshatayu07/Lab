import csv
import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def main():
    lines = []
    with open("exp10/data10.csv", "r") as infile:
        lines = infile.readlines()

    points = []
    for line in lines[1:]:
        x, y = map(int, line.strip().split(",")[1:])
        points.append((x, y))

    n = len(points)
   
    # Calculate mid point
    x_sum = sum(x for x, y in points)
    y_sum = sum(y for x, y in points)
    mid_x = x_sum / n
    mid_y = y_sum / n
    print(f"Mid Point: ({mid_x}, {mid_y})")

    # Write distance matrix to cluster_output.csv
    with open("exp10/cluster_output.csv", "w", newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["", "p1", "p2", "p3", "p4", "C"])
        for i in range(n):
            writer.writerow([f"p{i+1}"] + [distance(points[i][0], points[i][1], points[j][0], points[j][1]) for j in range(i + 1)] + [0])

        # Calculate nearest point to the center
        nearest_dist = float('inf')
        nearest_point = 0
        for i in range(n):
            dist = distance(mid_x, mid_y, points[i][0], points[i][1])
            print(f"Distance of p{i + 1} from centre: {dist}")
            writer.writerow([dist] + [0] * i + [dist] + [0] * (n - i - 1))
            if dist < nearest_dist:
                nearest_dist = dist
                nearest_point = i + 1

        print(f"Nearer Distance: {nearest_dist}")
        print(f"\nNearest point from Centre is: p{nearest_point}")

        # Calculate distance from new center to points
        writer.writerow([""])
        writer.writerow(["", "p1", "p2", "p3", "p4"])
        for i in range(n):
            writer.writerow([f"p{i+1}"] + [distance(points[i][0], points[i][1], points[j][0], points[j][1]) for j in range(i + 1)] + [0])

        x_new, y_new = points[nearest_point - 1]
        writer.writerow([f"p{nearest_point} (New Center)"] + [distance(x_new, y_new, points[j][0], points[j][1]) for j in range(n)])

if __name__ == "__main__":
    main()
