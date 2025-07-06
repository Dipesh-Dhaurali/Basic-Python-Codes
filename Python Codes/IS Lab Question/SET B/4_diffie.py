"""
Simulate Diffie-Hellman Key Exchange using a python program
"""
# Step 1: Input prime number q
q = int(input("Enter value for q (prime number): "))

# Check if q is a prime number using count logic
count = 0
for i in range(2, q):
    if q % i == 0:
        count += 1

if count != 0:
    print("Error: Only prime number allowed for q.")
    exit()

# Step 2: Input and validate primitive root a (alpha)
while True:
    a = int(input("Enter value for a (primitive root of q): "))

    # Check if a is a primitive root modulo q using your logic
    result_set = set()
    for i in range(1, q):
        val = pow(a, i) % q
        result_set.add(val)

    if len(result_set) == q - 1:
        break
    else:
        print("Error: Value of a is not a primitive root of q. Try again.")

# Step 3: Input private keys
Alice_key = int(input("Enter Alice's private key: "))
Bob_key = int(input("Enter Bob's private key: "))

# Step 4: Public key generation
if Alice_key < q:
    alice = pow(a, Alice_key) % q
else:
    print("Error: Alice's private key must be less than q.")
    exit()

if Bob_key < q:
    bob = pow(a, Bob_key) % q
else:
    print("Error: Bob's private key must be less than q.")
    exit()

# Step 5: Shared key computation
k1 = pow(bob, Alice_key) % q
k2 = pow(alice, Bob_key) % q

# Step 6: Display results
print("k1 (Alice's shared key):", k1)
print("k2 (Bob's shared key):", k2)

if k1 == k2:
    print("Success: Shared keys match!")
else:
    print("Error: Shared keys do not match.")
