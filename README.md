## Gift Vouncher Code Cracking
The objective is to identify the open port, generate valid gift voucher codes using client IDs, and eventually crack the MD5 hash to discover the components of the gift voucher code. The challenge is based on reverse-engineering the MD5 hashing process, where custom inputs (like the alphabet and symbol sets) are combined with the client ID to generate valid codes.

## What I learnt

1. **MD5 Hashing:**  
   - Used `hashlib` to calculate and compare hashes for validating voucher codes.

2. **Data Combination:**  
   - Combined inputs (`A`, `ClientID`, `B`) for hash generation.

3. **Scapy for Networking:**  
   - Created and sent UDP packets using Scapy, with random source ports.

4. **Response Handling:**  
   - Processed server responses to extract and display voucher codes.

5. **Practical Application:**  
   - Integrated hashing and networking to test server security.
