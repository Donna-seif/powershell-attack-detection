# PowerShell Attack Detection

This project demonstrates detection of suspicious PowerShell activity commonly used by attackers for execution and evasion.

## 🔍 Detection Approach

The detection identifies suspicious patterns such as:

- Encoded commands (`-enc`)
- Downloading external content (`Invoke-WebRequest`)
- In-memory execution (`IEX`)
- Execution policy bypass (`-ExecutionPolicy Bypass`)
- Use of `-NoProfile` to reduce visibility

## 🛠 Implementation

- Python-based detection using scoring logic
- Sample logs for testing detection

## 🧠 Detection Logic

Multiple behavioral signals are combined to improve detection accuracy and reduce false positives.

## ⚠️ Evasion Considerations

Attackers may:
- Obfuscate commands
- Use legitimate tools
- Combine multiple techniques to avoid detection

This detection focuses on identifying such patterns.
