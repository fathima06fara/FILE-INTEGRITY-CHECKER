# FILE-INTEGRITY-CHECKER

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: FATHIMA FARHANA M

*INTERN ID*: CT04DZ2242

*DOMAIN*: CYBERSECURITY AND ETHICAL HACKING

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH


## 🔐 Task 1 – File Integrity Checker

 CodTech Cyber Security Internship – Task Description

As part of the CodTech Cyber Security Internship, Task 1 involved developing a **File Integrity Checker** using Python. This tool is designed to monitor files in a specific folder and detect if any file has been **added, deleted, or modified** by comparing hash values across runs. The concept of **file integrity checking** is crucial in cybersecurity as it helps ensure that sensitive data remains unaltered and secure from unauthorized access or tampering.

The main idea behind this task is based on **hashing** — a technique where a unique digital fingerprint (hash value) is generated for every file. Even a tiny change in a file results in a completely different hash value, making it a reliable way to track file changes. In this task, the SHA-256 algorithm was used through Python’s `hashlib` module to compute the hashes.


 🧠 Script Overview

The Python script, named `file_integrity_checker.py`, is responsible for monitoring a folder called `files_to_monitor`. Inside this folder, I placed a file named `a.txt` as a test file.

Here’s how the script works:

* **First Run**: It scans the files in `files_to_monitor`, calculates their hash values, and stores them in a file called `file_hashes.json`.
* **Next Runs**: It recalculates the hash values and compares them with the stored ones. Based on the comparison, it reports:

  * 📁 Added files (new files since the last run)
  * ✏ Modified files (existing files that were changed)
  * ❌ Removed files (files deleted from the folder)

This process is fully automated. If the folder `files_to_monitor` doesn’t exist, the script creates it. Hash values are stored in JSON format, which makes it easy to read and reuse in future comparisons.



🔧 Key Features Implemented

* ✅ Uses **SHA-256** algorithm to ensure strong and secure hash calculation
* ✅ Automatically tracks changes in file content or structure
* ✅ Generates a clean and readable summary of added, removed, or modified files
* ✅ Uses `os.walk()` to scan all files in the folder recursively
* ✅ Uses `json` module to save and load previous hashes from `file_hashes.json`
* ✅ Cross-platform compatible (runs on Windows, Linux, macOS)



 📁 Folder Structure

After running the script once, the project folder looks like this:


file_integrity_checker/
│
├── file_integrity_checker.py        ← Main Python script
├── file_hashes.json                 ← Auto-generated hash record
└── files_to_monitor/
    └── a.txt                        ← Sample test file


This structure ensures that the script and data are organized, making it easy to submit and understand.

💡 Real-World Applications

This type of integrity checker is commonly used in:

* **Web servers** to detect unauthorized changes to code or configuration files
* **Financial systems** to ensure transaction logs remain unaltered
* **Government or defense systems** to detect tampering of classified files
* **Forensic investigations** to confirm if digital evidence was modified

In enterprise cybersecurity, such tools are often part of **File Integrity Monitoring (FIM)** solutions, which are required for compliance with standards like PCI-DSS, HIPAA, and ISO/IEC 27001.

 📌 Conclusion

Completing Task 1 was a valuable hands-on experience in applying cybersecurity fundamentals using Python. It helped strengthen my understanding of:

* Cryptographic hashing
* File system operations
* Real-time integrity monitoring

The final result is a reliable tool that can detect unauthorized file changes and contribute to a more secure digital environment. This task has not only fulfilled the internship requirements but has also deepened my practical knowledge in cyber defense and scripting.

#OUTPUT

PS C:\Users\Farhana\Downloads\file_integrity_checker> python file_integrity_checker.py
🔍 Checking file integrity...

📁 Added Files:
  + files_to_monitor\a.txt





