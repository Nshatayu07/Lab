import csv
from collections import defaultdict

def read_csv(file_path):
    transactions = defaultdict(list)
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            items = [item.strip() for item in row if item.strip()]
            if items:
                transactions[len(transactions) + 1] = items
    return list(transactions.values())

def calculate_support(itemset, transactions):
    count = 0
    for transaction in transactions:
        if set(itemset).issubset(set(transaction)):
            count += 1
    return count / len(transactions)

def apriori(transactions, min_support):
    frequent_itemsets = []
    unique_items = set(item for transaction in transactions for item in transaction)
   
    # Generate 1-itemsets
    candidates = [[item] for item in unique_items]
   
    k = 1
    while candidates:
        next_candidates = []
        for candidate in candidates:
            support = calculate_support(candidate, transactions)
            if support >= min_support:
                frequent_itemsets.append((candidate, support))
                next_candidates.extend([candidate + [item] for item in unique_items if item not in candidate])
        candidates = next_candidates
        k += 1
   
    return frequent_itemsets

def generate_association_rules(frequent_itemsets, min_confidence):
    association_rules = []
    for itemset, support in frequent_itemsets:
        if len(itemset) > 1:
            for i in range(1, len(itemset)):
                antecedent = itemset[:i]
                consequent = itemset[i:]
                confidence = support / calculate_support(antecedent, transactions)
                if confidence >= min_confidence:
                    association_rules.append((antecedent, consequent, confidence))
    return association_rules

# Read the CSV file containing transaction data
input_file_path = 'exp9/data9.csv'
transactions = read_csv(input_file_path)

# Get user input for the minimum support and confidence thresholds
min_support = float(input("Enter the minimum support threshold (a value between 0 and 1): "))
min_confidence = float(input("Enter the minimum confidence threshold (a value between 0 and 1): "))

# Find frequent itemsets using Apriori
frequent_itemsets = apriori(transactions, min_support)

# Print the frequent itemsets
print("\nFrequent Itemsets:")
for itemset, support in frequent_itemsets:
    print(f"{set(itemset)} - Support: {support}")

# Find association rules
association_rules = generate_association_rules(frequent_itemsets, min_confidence)

# Print the association rules
print("\nAssociation Rules:")
for antecedent, consequent, confidence in association_rules:
    print(f"{set(antecedent)} => {set(consequent)} - Confidence: {confidence}")

