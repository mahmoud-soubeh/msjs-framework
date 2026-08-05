# ============================================================
# MSJS Framework - Collatz Conjecture Analyzer
# Author: Mahmoud Sabri Jaber Sobeh (Suobeh)
# Email: mahsbh@yahoo.com, sbhmah8@gmail.com
# ============================================================
# Zenodo (DOI): https://doi.org/10.5281/zenodo.21558635
# ORCID: https://orcid.org/0009-0008-9433-8446
# Academia.edu: https://independent.academia.edu/MahmoudSobeh
# GitHub: https://github.com/mahmoud-sobeh/msjs-framework
# ============================================================

import matplotlib.pyplot as plt
import networkx as nx
import sys

# Allow very large numbers
sys.set_int_max_str_digits(1000000)

print("\n" + "="*60)
print("# ==========================================================")
print("# MSJS Framework - Collatz Conjecture Analyzer")
print("# Author: Mahmoud Sabri Jaber Sobeh (Suobeh)")
print("# Email: mahsbh@yahoo.com, sbhmah8@gmail.com")
print("# ==========================================================")
print("# Zenodo (DOI): https://doi.org/10.5281/zenodo.21558635")
print("# ORCID: https://orcid.org/0009-0008-9433-8446")
print("# Academia.edu: https://independent.academia.edu/MahmoudSobeh")
print("# GitHub: https://github.com/mahmoud-sobeh/msjs-framework")
print("# ==========================================================")
print("="*60 + "\n")

# ------------------------------------------------------------
# 1. Compute the classical Collatz sequence
# ------------------------------------------------------------

p7 = []
n = int(input("Enter any positive integer >= 1 : "))
start_number = n
p7.append(start_number)

while start_number != 1:
    if start_number % 2 == 0:
        start_number = start_number // 2
        p7.append(start_number)
    else:
        start_number = start_number * 3 + 1
        p7.append(start_number)

print("\n" + "_" * 20)
print("AS COLLATZ CONJECTURE SAY :", p7)
print("_" * 20)

# ------------------------------------------------------------
# 2. Compute MSJS (NEXT X2X1) - Extended Level 2
# ------------------------------------------------------------

p_answer = []
p_answer.append(n % 100)

for i in range(len(p7) - 1):
    y = int(p7[i]) % 100
    g = (int(p7[i]) // 100) % 10

    if g % 2 == 0 and y % 2 == 0:
        if y == 0: p_answer.append(0)
        elif y == 10: p_answer.append(5)
        elif y == 20: p_answer.append(10)
        elif y == 30: p_answer.append(15)
        elif y == 40: p_answer.append(20)
        elif y == 50: p_answer.append(25)
        elif y == 60: p_answer.append(30)
        elif y == 70: p_answer.append(35)
        elif y == 80: p_answer.append(40)
        elif y == 90: p_answer.append(45)
        elif y == 2: p_answer.append(1)
        elif y == 12: p_answer.append(6)
        elif y == 22: p_answer.append(11)
        elif y == 32: p_answer.append(16)
        elif y == 42: p_answer.append(21)
        elif y == 52: p_answer.append(26)
        elif y == 62: p_answer.append(31)
        elif y == 72: p_answer.append(36)
        elif y == 82: p_answer.append(41)
        elif y == 92: p_answer.append(46)
        elif y == 4: p_answer.append(2)
        elif y == 14: p_answer.append(7)
        elif y == 24: p_answer.append(12)
        elif y == 34: p_answer.append(17)
        elif y == 44: p_answer.append(22)
        elif y == 54: p_answer.append(27)
        elif y == 64: p_answer.append(32)
        elif y == 74: p_answer.append(37)
        elif y == 84: p_answer.append(42)
        elif y == 94: p_answer.append(47)
        elif y == 6: p_answer.append(3)
        elif y == 16: p_answer.append(8)
        elif y == 26: p_answer.append(13)
        elif y == 36: p_answer.append(18)
        elif y == 46: p_answer.append(23)
        elif y == 56: p_answer.append(28)
        elif y == 66: p_answer.append(33)
        elif y == 76: p_answer.append(38)
        elif y == 86: p_answer.append(43)
        elif y == 96: p_answer.append(48)
        elif y == 8: p_answer.append(4)
        elif y == 18: p_answer.append(9)
        elif y == 28: p_answer.append(14)
        elif y == 38: p_answer.append(19)
        elif y == 48: p_answer.append(24)
        elif y == 58: p_answer.append(29)
        elif y == 68: p_answer.append(34)
        elif y == 78: p_answer.append(39)
        elif y == 88: p_answer.append(44)
        elif y == 98: p_answer.append(49)

    elif g % 2 != 0 and y % 2 == 0:
        if y == 0: p_answer.append(50)
        elif y == 10: p_answer.append(55)
        elif y == 20: p_answer.append(60)
        elif y == 30: p_answer.append(65)
        elif y == 40: p_answer.append(70)
        elif y == 50: p_answer.append(75)
        elif y == 60: p_answer.append(80)
        elif y == 70: p_answer.append(85)
        elif y == 80: p_answer.append(90)
        elif y == 90: p_answer.append(95)
        elif y == 2: p_answer.append(51)
        elif y == 12: p_answer.append(56)
        elif y == 22: p_answer.append(61)
        elif y == 32: p_answer.append(66)
        elif y == 42: p_answer.append(71)
        elif y == 52: p_answer.append(76)
        elif y == 62: p_answer.append(81)
        elif y == 72: p_answer.append(86)
        elif y == 82: p_answer.append(91)
        elif y == 92: p_answer.append(96)
        elif y == 4: p_answer.append(52)
        elif y == 14: p_answer.append(57)
        elif y == 24: p_answer.append(62)
        elif y == 34: p_answer.append(67)
        elif y == 44: p_answer.append(72)
        elif y == 54: p_answer.append(77)
        elif y == 64: p_answer.append(82)
        elif y == 74: p_answer.append(87)
        elif y == 84: p_answer.append(92)
        elif y == 94: p_answer.append(97)
        elif y == 6: p_answer.append(53)
        elif y == 16: p_answer.append(58)
        elif y == 26: p_answer.append(63)
        elif y == 36: p_answer.append(68)
        elif y == 46: p_answer.append(73)
        elif y == 56: p_answer.append(78)
        elif y == 66: p_answer.append(83)
        elif y == 76: p_answer.append(88)
        elif y == 86: p_answer.append(93)
        elif y == 96: p_answer.append(98)
        elif y == 8: p_answer.append(54)
        elif y == 18: p_answer.append(59)
        elif y == 28: p_answer.append(64)
        elif y == 38: p_answer.append(69)
        elif y == 48: p_answer.append(74)
        elif y == 58: p_answer.append(79)
        elif y == 68: p_answer.append(84)
        elif y == 78: p_answer.append(89)
        elif y == 88: p_answer.append(94)
        elif y == 98: p_answer.append(99)

    if y % 2 != 0:
        if y == 1: p_answer.append(4)
        elif y == 11: p_answer.append(34)
        elif y == 21: p_answer.append(64)
        elif y == 31: p_answer.append(94)
        elif y == 41: p_answer.append(24)
        elif y == 51: p_answer.append(54)
        elif y == 61: p_answer.append(84)
        elif y == 71: p_answer.append(14)
        elif y == 81: p_answer.append(44)
        elif y == 91: p_answer.append(74)
        elif y == 3: p_answer.append(10)
        elif y == 13: p_answer.append(40)
        elif y == 23: p_answer.append(70)
        elif y == 33: p_answer.append(0)
        elif y == 43: p_answer.append(30)
        elif y == 53: p_answer.append(60)
        elif y == 63: p_answer.append(90)
        elif y == 73: p_answer.append(20)
        elif y == 83: p_answer.append(50)
        elif y == 93: p_answer.append(80)
        elif y == 5: p_answer.append(16)
        elif y == 15: p_answer.append(46)
        elif y == 25: p_answer.append(76)
        elif y == 35: p_answer.append(6)
        elif y == 45: p_answer.append(36)
        elif y == 55: p_answer.append(66)
        elif y == 65: p_answer.append(96)
        elif y == 75: p_answer.append(26)
        elif y == 85: p_answer.append(56)
        elif y == 95: p_answer.append(86)
        elif y == 7: p_answer.append(22)
        elif y == 17: p_answer.append(52)
        elif y == 27: p_answer.append(82)
        elif y == 37: p_answer.append(12)
        elif y == 47: p_answer.append(42)
        elif y == 57: p_answer.append(72)
        elif y == 67: p_answer.append(2)
        elif y == 77: p_answer.append(32)
        elif y == 87: p_answer.append(62)
        elif y == 97: p_answer.append(92)
        elif y == 9: p_answer.append(28)
        elif y == 19: p_answer.append(58)
        elif y == 29: p_answer.append(88)
        elif y == 39: p_answer.append(18)
        elif y == 49: p_answer.append(48)
        elif y == 59: p_answer.append(78)
        elif y == 69: p_answer.append(8)
        elif y == 79: p_answer.append(38)
        elif y == 89: p_answer.append(68)
        elif y == 99: p_answer.append(98)

print("\n" + "_" * 30)
print("AS MSJS(NEXT(X2X1)) SAY :", p_answer)
print("_" * 30)

# ------------------------------------------------------------
# 3. Compute MSJS (NEXT X1) - Level 1
# ------------------------------------------------------------

list_of_ones = []
for i in range(len(p7) - 1):
    list_of_ones.append(int(p7[i]) % 10)

list_of_ones.append(1)
print("\n" + "_" * 30)
print("AS MSJS(NEXT(X1)) SAY :", list_of_ones)
print("_" * 30)

print(f"LENGTH OF STEPS IS : {len(p7) - 1}")
print("_" * 50)

# ------------------------------------------------------------
# 4. Extract loops
# ------------------------------------------------------------

digit = int(input("\nEnter a digit (0-9) to extract loops : "))
print("_" * 50)

loops = []
current_loop = []
for num in list_of_ones:
    if num == digit:
        if current_loop:
            loops.append(current_loop)
            current_loop = []
    current_loop.append(num)

if current_loop:
    loops.append(current_loop)

for i, loop in enumerate(loops, 1):
    if loop:
        print(f"loop number {i} : {loop}")
        print("_" * 20)

# ------------------------------------------------------------
# 5. Draw the graph with arrows and title
# ------------------------------------------------------------

print("\n" + "_" * 50)
print("SEE THE FIGURE AS - MSJS(NEXT(X1)) - SAY EXACTLY.")
print("The Red Circle Means That This Number Has Been Entered Repeatedly.")
print("_" * 50)



'''
def draw_number_sequence(numbers):
    G = nx.DiGraph()
    
    for i in range(len(numbers) - 1):
        G.add_edge(numbers[i], numbers[i+1])

    # ✅ استخدام circular_layout لتوزيع العقد على شكل دائرة
    pos = nx.circular_layout(G)
    
    plt.figure(figsize=(12, 10))

    nx.draw_networkx_nodes(G, pos, node_size=2500, node_color='lightblue')
    nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')
    
    # ✅ أسهم مستقيمة (بدون انحناء)
    nx.draw_networkx_edges(G, pos, 
                           edge_color='gray', 
                           arrows=True,
                           arrowsize=50,
                           arrowstyle='->',
                           connectionstyle='arc3,rad=0.0')

    # رسم دوائر حمراء حول الأرقام المتكررة
    repeat_numbers = set([num for num in numbers if numbers.count(num) > 1])
    for num in repeat_numbers:
        if num in pos:
            circle = plt.Circle((pos[num][0], pos[num][1]), 0.12,
                                color='red', fill=False, linewidth=2.5)
            plt.gca().add_patch(circle)

    # ✅ العنوان
    plt.title(f'MSJS(NEXT(X1)) for n = {n}', fontsize=14, fontweight='bold')
    plt.axis('off')
    plt.subplots_adjust(top=0.90)
    plt.show()

draw_number_sequence(list_of_ones)
'''
def draw_number_sequence(numbers):
    G = nx.DiGraph()
    
    for i in range(len(numbers) - 1):
        G.add_edge(numbers[i], numbers[i+1])

    pos = nx.spring_layout(G, seed=42, k=2, iterations=50)
    
    plt.figure(figsize=(14, 12))

    # رسم العقد (الدوائر)
    nx.draw_networkx_nodes(G, pos, node_size=3000, node_color='lightblue')
    nx.draw_networkx_labels(G, pos, font_size=14, font_weight='bold')

    # ✅ رسم الأسهم باستخدام plt.annotate (طريقة مضمونة)
    for u, v in G.edges():
        x1, y1 = pos[u]
        x2, y2 = pos[v]
        plt.annotate("",
                     xy=(x2, y2), xytext=(x1, y1),
                     arrowprops=dict(arrowstyle="->", color='green', lw=2, shrinkA=20, shrinkB=20))

    # رسم دوائر حمراء حول الأرقام المتكررة
    repeat_numbers = set([num for num in numbers if numbers.count(num) > 1])
    for num in repeat_numbers:
        if num in pos:
            circle = plt.Circle((pos[num][0], pos[num][1]), 0.13,
                                color='red', fill=False, linewidth=3)
            plt.gca().add_patch(circle)

    # العنوان
    plt.title(f'MSJS(NEXT(X1)) for n = {n}', fontsize=16, fontweight='bold')
    plt.axis('off')
    plt.subplots_adjust(top=0.92)
    plt.show()
draw_number_sequence(list_of_ones)
#gray
