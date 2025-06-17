# THBMTTNC_-0799

This repository contains laboratory exercises for a course on information security. It includes Python practice tasks, implementations of classical cryptography algorithms, GUI demonstrations and small networking examples.

## Labs Overview

### LAB-01: Python Basics
Simple Python scripts introducing the language and basic data structures.

### LAB-02: Classical Cipher Web Service
Flask application providing APIs and web pages for Caesar, Vigenère, Rail Fence, Playfair and Transposition ciphers.

### LAB-03: PyQt5 GUI Clients
GUI applications built with PyQt5 that interact with the LAB-02 API.

### LAB-04: Cryptography Demos
Various security related examples including AES/RSA socket communication, Diffie–Hellman key exchange, hashing algorithms and image steganography.

### LAB-05: Integration Test
Small Flask app demonstrating how to launch the PyQt5 clients and utilities for steganography.

## Getting Started
Each lab folder may provide a `requirements.txt` file describing its Python dependencies. Install them with pip before running a lab:

```bash
cd LAB-02
pip install -r requirements.txt
python api.py
```

Run the GUI programs in LAB-03 or other utilities similarly.

## Folder Structure
```
LAB-01/  # introductory Python exercises
LAB-02/  # Flask API and web interface
LAB-03/  # PyQt5 GUI applications
LAB-04/  # additional crypto demos
LAB-05/  # integration tests and tools
```

These labs serve as educational examples and are not intended for production use.
