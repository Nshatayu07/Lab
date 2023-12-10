import csv
from collections import defaultdict
from itertools import combinations 

# Read the CSV file containing transaction data
input_file_path = 'exp8/data8.csv'

# Dictionary to store transactions
transactions = defaultdict(list)

# Read and process the CSV file
with open(input_file_path, 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        # Filter out empty values
        items = [item.strip() for item in row if item.strip()]
        # Skip empty rows
        if items:
            transactions[len(transactions) + 1] = items

# Print transactions for inspection
print("Transactions:")
print(transactions)

# Get user input for the minimum support threshold
min_support = float(input("Enter the minimum support threshold (a value between 0 and 1): "))

# Function to generate candidate itemsets
def generate_candidates(itemsets, length):
    candidates = set()
    for itemset1 in itemsets:
        for itemset2 in itemsets:
            union_set = itemset1.union(itemset2)
            if len(union_set) == length:
                candidates.add(union_set)
    return candidates

# Function to prune infrequent itemsets
def prune_itemsets(itemsets, min_support, transactions):
    pruned_itemsets = set()
    for itemset in itemsets:
        support_count = sum(1 for transaction in transactions.values() if itemset.issubset(transaction))
        support = support_count / len(transactions)
        if support >= min_support:
            pruned_itemsets.add(itemset)
    return pruned_itemsets

# Find frequent itemsets using the Apriori algorithm
itemsets = set(frozenset([item]) for items in transactions.values() for item in items)
frequent_itemsets = set()

while itemsets:
    pruned_itemsets = prune_itemsets(itemsets, min_support, transactions)
    frequent_itemsets.update(pruned_itemsets)
    itemsets = generate_candidates(pruned_itemsets, len(pruned_itemsets))

# Convert frozensets to sets for a more readable output
frequent_itemsets = [set(itemset) for itemset in frequent_itemsets]

# Print the frequent itemsets
print("\nFrequent Itemsets:")
for itemset in frequent_itemsets:
    print(itemset)

# Get user input for the minimum confidence threshold
min_confidence = float(input("Enter the minimum confidence threshold (a value between 0 and 1): "))

# Find association rules
association_rules = []
for itemset in frequent_itemsets:
    for antecedent_length in range(1, len(itemset)):
        for antecedent in combinations(itemset, antecedent_length):
            antecedent_set = set(antecedent)
            consequent_set = itemset - antecedent_set
            antecedent_support = sum(1 for transaction in transactions.values() if antecedent_set.issubset(transaction)) / len(transactions)
            rule_support = sum(1 for transaction in transactions.values() if itemset.issubset(transaction)) / len(transactions)
            confidence = rule_support / antecedent_support
            if confidence >= min_confidence:
                association_rules.append((antecedent_set, consequent_set, confidence))

# Print the association rules
print("\nAssociation Rules:")
for antecedent_set, consequent_set, confidence in association_rules:
    print(f"{antecedent_set} => {consequent_set} (Confidence: {confidence:.2f})")

# Save the association rules to a new CSV file
output_rules_file_path = 'exp8/output_association_rules.csv'
with open(output_rules_file_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(association_rules)

print(f"\nAssociation rules saved to {output_rules_file_path}")
