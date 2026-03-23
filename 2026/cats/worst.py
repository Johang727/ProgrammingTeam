import random

def generate_worst_case(num_cases=20, num_cats=2000):
    print(num_cases)
    for _ in range(num_cases):
        # M = max milk, C = cats
        # Let's give it a tight milk budget
        print(f"100000 {num_cats}")
        
        # Every cat connected to every other cat
        for i in range(num_cats):
            for j in range(i + 1, num_cats):
                # Random weights between 1 and 100
                weight = random.randint(1, 100)
                print(f"{i} {j} {weight}")

# Run this and pipe it to a file: python generator.py > input.txt
if __name__ == "__main__":
    generate_worst_case(20, 2000)