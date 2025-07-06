class Sample:
    def __init__(self, name, data):
        self.name = name         # Used in __init__
        self.data = data         # A list, used for len and indexing

    def __str__(self):
        return f"Name: {self.name}"  # Friendly string

    def __repr__(self):
        return f"Sample('{self.name}', {self.data})"  # Developer string

    def __len__(self):
        return len(self.data)    # Length of data list

    def __getitem__(self, index):
        return self.data[index]  # Indexing

    def __add__(self, other):
        # Combine data lists and names
        return Sample(self.name + other.name, self.data + other.data)

    def __eq__(self, other):
        return self.name == other.name and self.data == other.data


# Test the class
s1 = Sample("A", [1, 2, 3])
s2 = Sample("B", [4, 5])

print(str(s1))          # __str__
print(repr(s1))         # __repr__
print(len(s1))          # __len__
print(s1[1])            # __getitem__

s3 = s1 + s2            # __add__
print(s3)               # uses __str__ again

print(s1 == s2)         # __eq__
print(s1 == Sample("A", [1, 2, 3]))  # True
