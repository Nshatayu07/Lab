import csv
import math

def main():
    with open('exp4/data4.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        choice = int(input("Enter Child Column Number : "))
        parent = {}
        child = {}
        for row in reader:
            day = row[0]
            level = row[1]
            routine = row[2]
            playGame = row[3]
            value = row[4]
            if choice == 1:
                childName = day
            elif choice == 2:
                childName = level
            elif choice == 3:
                childName = routine
            elif choice == 4:
                childName = value
            else:
                childName = routine
            if playGame in parent:
                parent[playGame] += 1
            else:
                parent[playGame] = 1
            if childName in child:
                if playGame in child[childName]:
                    child[childName][playGame] += 1
                else:
                    child[childName][playGame] = 1
            else:
                child[childName] = {playGame: 1}
   
    pos = parent.get("Yes", 0)
    neg = parent.get("No", 0)
    total = pos + neg
   
    parent_entropy = -((pos / total) * math.log2(pos / total) +
                       (neg / total) * math.log2(neg / total))
    print("Parent Entropy:", parent_entropy)
   
    child_entropy = 0
    for childName, games in child.items():
        pR = games.get("Yes", 0)
        nR = games.get("No", 0)
        tR = pR + nR
        child_entropy += -((pR + nR) / total) * ((pR / tR) * math.log2(pR / tR) +
                                                 (nR / tR) * math.log2(nR / tR))
    print("Child Entropy * Their proportion:", child_entropy)
    print("Info gain:", parent_entropy - child_entropy)

if __name__ == "__main__":
    main()


