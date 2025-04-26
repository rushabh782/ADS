#Stem-and-Leaf Plot

# Sample univariate data
data = [12, 14, 15, 15, 16, 18, 19, 20, 21, 22, 22, 23, 24, 25, 26, 28, 29, 30, 31, 33, 34, 35]

def stem_and_leaf(data):
    stems = {}
    for num in sorted(data):
        stem, leaf = divmod(num, 10)
        stems.setdefault(stem, []).append(leaf)

    print("Stem | Leaf")
    for stem, leaves in stems.items():
        print(f" {stem}   | {' '.join(map(str, leaves))}")

# Call the function
stem_and_leaf(data)
