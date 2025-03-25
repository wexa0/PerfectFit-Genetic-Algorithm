# PerfectFit - A GA-Based Solution for Optimal Outfit Selection

## 📘 Introduction
**PerfectFit** is a Python-based application that leverages Genetic Algorithms (GA) to help users optimize their outfit selection based on specific criteria such as dress code, color palette, comfort level, and budget. The goal of the project is to simplify the decision-making process when choosing an outfit by automatically suggesting the best combination of items from the user's wardrobe, adhering to their defined preferences.

---

## 🧩 Problem Statement
Choosing the right outfit for various occasions can be a complex task due to multiple considerations like:
- Dress code
- Budget constraints
- Color palette
- Comfort level

Many individuals struggle with this decision-making process, especially when faced with a diverse wardrobe. **PerfectFit** addresses this by using a Genetic Algorithm to suggest the optimal outfit for any given situation, taking into account all user preferences and constraints.

---

## 💡 Solution
**PerfectFit** employs a genetic algorithm to optimize the process of outfit selection:
1. The user provides input for preferences (dress code, color, comfort, and budget).
2. The genetic algorithm generates a population of outfit combinations.
3. It then evolves the population over multiple generations, applying selection, crossover, mutation, and replacement operations.
4. The best outfits are selected based on a fitness function that evaluates how well they meet the user’s preferences.

The outcome is a tailored outfit recommendation that maximizes the fitness score across all defined factors.

---

## 💻 Technology Stack
- **Programming Language:** Python
- **Algorithm:** Genetic Algorithm (GA) using 2-point crossover, mutation, binary tournament selection, and replacement.

---

## 🚀 Launching Instructions

1. **📥 Clone the Repository**
   - Open the Command Prompt or Terminal.
   - Clone this repository by running:

     ```bash
     git clone https://github.com/yourusername/PerfectFit.git
     ```

2. **🔧 Install Prerequisites**
   - Make sure you have Python 3.x installed.
   - Install required Python packages:

     ```bash
     pip install -r requirements.txt
     ```

3. **▶️ Run the Application**
   - After installation, navigate to the project directory and run the script:

     ```bash
     python PerfectFit.py
     ```

