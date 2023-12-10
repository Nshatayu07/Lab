import csv
import sys

op = 1
fwtr = open("exp11/exp11_output.csv", "w")
algomerative_output_file = None

def algomerative(input_file):
    global op
    global algomerative_output_file

    dm = {}
    with open(input_file, 'r') as file:
        lines = file.readlines()
        points = lines[0].strip().split(',')[1:]
        
        for line in lines[1:]:
            values = line.strip().split(',')
            point = values[0]
            dm[point] = {points[i]: int(dist) for i, dist in enumerate(values[1:]) if dist}

    pt1, pt2, min_dist = find_closest_clusters(dm)
    print("Clusters Chosen :", pt1, pt2)

    up, down = (pt2, pt1) if pt1[0] > pt2[0] else (pt1, pt2)
    new_pt = down + up

    for point, distances in dm.items():
        if point[0] > new_pt[0]:
            dm.setdefault(point, {})
            dm[point][new_pt] = min(dm[point].get(up, sys.maxsize), dm[point].get(down, sys.maxsize))

    for point, d1 in dm[down].items():
        if point[0] < up[0]:
            dm.setdefault(new_pt, {})
            dm[new_pt][point] = min(d1, dm[up].get(point, sys.maxsize))
        else:
            dm.setdefault(new_pt, {})
            dm[new_pt][point] = min(d1, dm[point].get(up, sys.maxsize))

    for point, mtemp in dm.items():
        if point[0] >= up[0]:
            dm.setdefault(new_pt, {})
            d1 = dm[point].get(up, sys.maxsize)
            if down[0] > point[0]:
                d1 = min(d1, dm[down].get(point, sys.maxsize))
            else:
                d1 = min(d1, dm[point].get(down, sys.maxsize))
            dm[point][new_pt] = d1
            dm[point].pop(up, None)
            if point[0] >= down[0]:
                dm[point].pop(down, None)

    dm.pop(up, None)
    dm.pop(down, None)

    output = f"exp11/output{op}.csv"
    op += 1

    with open(output, 'w') as fw:
        fw.write(',')
        fw.write(','.join(dm.keys()))
        fw.write('\n')
        for point, distances in dm.items():
            fw.write(point + ',')
            fw.write(','.join(map(str, distances.values())))
            fw.write('\n')

    fwtr.write(f"{down} & {up}\n")

    algomerative_output_file = output
    return output

def find_closest_clusters(dm):
    points = list(dm.keys())
    pt1, pt2 = '', ''
    min_dist = sys.maxsize

    for p in dm:
        for pp, dist in dm[p].items():
            if p != pp and dist < min_dist:
                pt1 = p
                pt2 = pp
                min_dist = dist

    return pt1, pt2, min_dist

def main():
    global algomerative_output_file

    input_file = "exp11/data11.csv"
    with open(input_file, 'r') as file1:
        lines = file1.readlines()
        points = lines[0].strip().split(',')[1:]
        len_points = len(points)

    for i in range(1, len_points - 1):
        algomerative_output_file = algomerative(input_file)
        input_file = algomerative_output_file

    fwtr.close()

if __name__ == "__main__":
    main()
