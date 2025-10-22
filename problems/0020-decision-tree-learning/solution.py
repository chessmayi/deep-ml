import math
from collections import Counter

def learn_decision_tree(x: list[dict], f: list[str], y: str) -> dict:
    def entropy(examples):
        """Calculate entropy of examples based on target class labels."""
        if not examples:
            return 0
        
        labels = [ex[y] for ex in examples]
        label_counts = Counter(labels)
        total = len(labels)
        
        ent = 0
        for count in label_counts.values():
            if count > 0:
                p = count / total
                ent -= p * math.log2(p)
        return ent
    
    def split_data(examples, attribute, value):
        return [ex for ex in examples if ex[attribute] == value]
    
    def information_gain(examples, attribute):
        total_entropy = entropy(examples)
        values = set(ex[attribute] for ex in examples)
        weighted_entropy = 0
        for value in values:
            subset = split_data(examples, attribute, value)
            weight = len(subset) / len(exampl