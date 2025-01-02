import hashlib

# Gift Voucher code
voucher_code = '218b9a79afd071d8c7291ed3be603c93'

# Components to be used in hash calculation
A = 'nh'        	# Two-alphabet characters from set A
ClientID = '8039276'  	# Example client ID
B = '#`'        	# Two-symbol characters from set B

# Combine components into a single string
input_string = A + ClientID + B

# Calculate the MD5 hash of the combined string
calculated_hash = hashlib.md5(input_string.encode()).hexdigest()

# Output the results
print("Gift Voucher Code:", voucher_code)
print("Calculated Hash:", calculated_hash)

# Compare the calculated hash with the voucher code
if calculated_hash == voucher_code:
    print("Success! The hashes match.")
else:
    print("Failure! The hashes do not match.")
