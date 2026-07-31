# MSJS Framework - Collatz Conjecture Analyzer

A comprehensive Python tool for analyzing the Collatz conjecture through the MSJS (Modular Special Jump System) framework.

---

## 📖 Description

This program provides a complete analysis of any positive integer under the Collatz map, offering:

- The classical Collatz sequence.
- The MSJS Level 1 sequence (NEXT X1).
- The MSJS Extended Level 2 sequence (NEXT X2X1).
- Extraction of digit cycles and loops.
- A visual directed graph showing digit transitions with arrows.

---

## 📦 Requirements

- Python 3.7 or higher
- Libraries:
  - `matplotlib`
  - `networkx`

---

## 🚀 How to Run

1. **Clone or download** the repository.
2. **Install the required libraries**:
   ```bash
   pip install matplotlib networkx
Run the program:

bash
python MSJS_Framework.py
Follow the prompts:

Enter any positive integer.

Enter a digit (0–9) to extract loops.

📊 Example Output
n = 27
Classical Collatz Sequence:

text
[27, 82, 41, 124, 62, 31, 94, 47, 142, 71, 214, 107, 322, 161, 484, 242, 121, 364, 182, 91, 274, 137, 412, 206, 103, 310, 155, 466, 233, 700, 350, 175, 526, 263, 790, 395, 1186, 593, 1780, 890, 445, 1336, 668, 334, 167, 502, 251, 754, 377, 1132, 566, 283, 850, 425, 1276, 638, 319, 958, 479, 1438, 719, 2158, 1079, 3238, 1619, 4858, 2429, 7288, 3644, 1822, 911, 2734, 1367, 4102, 2051, 6154, 3077, 9232, 4616, 2308, 1154, 577, 1732, 866, 433, 1300, 650, 325, 976, 488, 244, 122, 61, 184, 92, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1]
MSJS Level 1 Sequence (NEXT X1):

text
[7, 2, 1, 4, 2, 1, 4, 7, 2, 1, 4, 7, 2, 1, 4, 2, 1, 4, 2, 1, 4, 7, 2, 6, 3, 0, 5, 6, 3, 0, 0, 5, 6, 3, 0, 5, 6, 3, 0, 0, 5, 6, 8, 4, 7, 2, 1, 4, 7, 2, 6, 3, 0, 5, 6, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 4, 2, 1, 4, 7, 2, 1, 4, 7, 2, 6, 8, 4, 7, 2, 6, 3, 0, 0, 5, 6, 8, 4, 2, 1, 4, 2, 6, 3, 0, 5, 6, 3, 0, 0, 0, 0, 0, 5, 6, 8, 4, 2, 1]
Loops Extracted (for digit 1):

text
loop number 1 : [7, 2]
loop number 2 : [1, 4, 2]
loop number 3 : [1, 4, 7, 2]
loop number 4 : [1, 4, 7, 2]
loop number 5 : [1, 4, 2]
loop number 6 : [1, 4, 2]
loop number 7 : [1, 4, 7, 2, 6, 3, 0, 5, 6, 3, 0, 0, 5, 6, 3, 0, 5, 6, 3, 0, 0, 5, 6, 8, 4, 7, 2]
loop number 8 : [1, 4, 7, 2, 6, 3, 0, 5, 6, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 4, 2]
loop number 9 : [1, 4, 7, 2]
loop number 10 : [1, 4, 7, 2, 6, 8, 4, 7, 2, 6, 3, 0, 0, 5, 6, 8, 4, 2]
loop number 11 : [1, 4, 2, 6, 3, 0, 5, 6, 3, 0, 0, 0, 0, 0, 5, 6, 8, 4, 2]
🖼️ Visual Output
The program generates a directed graph with arrows showing digit transitions. Red circles indicate repeated digits (cycles).

https://images/graph_27.png

📂 Repository Structure
text
MSJS_Framework/
├── MSJS_Framework.py          # Main program
├── README.md                  # This file
├── requirements.txt           # Required libraries
├── LICENSE                    # MIT License
├── examples/                  # Example outputs
│   └── output_27.txt
└── images/                    # Visual examples
    └── graph_27.png
🔗 Related Works
Zenodo (DOI): 10.5281/zenodo.21710622

ORCID: 0009-0008-9433-8446

Academia.edu: Mahmoud Sobeh

GitHub: https://github.com/mahmoud-soubeh/msjs-framework

📄 License
This project is licensed under the MIT License – see the LICENSE file for details.

👤 Author
Mahmoud Sabri Jaber Sobeh (Suobeh)
Email: mahsbh@yahoo.com, sbhmah8@gmail.com
