
# Recharge/Gift Card System
Fast resource-efficient algorithmic solution for generating, verifying, and redeeming gift or recharge cards requiring only **1.2 GB** of storage for **10 billion** unique cards.

## Description
A secure and efficient algorithmic solution for generating, verifying, and redeeming gift or recharge cards without relying on large-scale storage systems. The primary goal is to eliminate the need for extensive storage, focusing on security and rapid response times for read and write operations. The system is designed to support up to 10 billion unique cards, requiring only 1.2 GB of storage. The system is implemented in python and utilizes encryption algorithms to generate and verify card numbers.

## Key Features
- **Storage Efficiency**: By utilizing encryption, the system eliminates the need to store all card numbers and values centrally. This ensures a lightweight storage footprint while supporting up to 10 billion unique cards, requiring only 1.2 GB of storage.

- **Card Generation**: Encryption algorithms are employed to dynamically generate card numbers. Each card number includes a card serial and value, ensuring uniqueness and security.

- **Verification**: Card information can be securely verified by decrypting the card number, providing a reliable method for validation without the need for a central card database.

- **Redemption Tracking**: The redemption status of each card is stored in a file-based storage system. Each card's redemption state is represented as a binary value (0 or 1) at the corresponding bit position in the file, facilitating efficient low storage tracking without the need for a comprehensive database or large storage solution.

- **File Shredding**: To optimize read and write speeds and minimize storage overhead, the storage system shreds the data into 100 files. This strategy enhances overall system performance without compromising data integrity.
