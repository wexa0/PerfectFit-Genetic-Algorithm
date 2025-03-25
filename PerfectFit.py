import random
import matplotlib.pyplot as plt


# Define the search space as a dictionary
search_space = {

    "Top": [
        {"Item": "T-shirt", "Price": 0.0, "Dress Code": "Casual", "Color": "Bright", "Comfort Level": 5},
        {"Item": "Formal Shirt", "Price": 120.0, "Dress Code": "Business", "Color": "Dark", "Comfort Level": 3},
        {"Item": "Polo Shirt", "Price": 80.0, "Dress Code": "Sportswear", "Color": "Bright", "Comfort Level": 4},
        {"Item": "Evening Blouse", "Price": 150.0, "Dress Code": "Evening", "Color": "Dark", "Comfort Level": 3},
        {"Item": "Sweater", "Price": 0.0, "Dress Code": "Casual", "Color": "Dark", "Comfort Level": 5},
        {"Item": "Hoodie", "Price": 60.0, "Dress Code": "Casual", "Color": "Bright", "Comfort Level": 4},
        {"Item": "Tank Top", "Price": 0.0, "Dress Code": "Sportswear", "Color": "Bright", "Comfort Level": 4},
        {"Item": "Silk Blouse", "Price": 200.0, "Dress Code": "Evening", "Color": "Dark", "Comfort Level": 3},
    ],
    
    "Bottom": [
        {"Item": "Jeans", "Price": 0.0, "Dress Code": "Casual", "Color": "Dark", "Comfort Level": 4},
        {"Item": "Formal Trousers", "Price": 150.0, "Dress Code": "Business", "Color": "Dark", "Comfort Level": 3},
        {"Item": "Sports Shorts", "Price": 0.0, "Dress Code": "Sportswear", "Color": "Bright", "Comfort Level": 5},
        {"Item": "Skirt", "Price": 100.0, "Dress Code": "Evening", "Color": "Bright", "Comfort Level": 3},
        {"Item": "Chinos", "Price": 90.0, "Dress Code": "Business", "Color": "Dark", "Comfort Level": 4},
        {"Item": "Leggings", "Price": 60.0, "Dress Code": "Casual", "Color": "Dark", "Comfort Level": 5},
        {"Item": "Athletic Pants", "Price": 80.0, "Dress Code": "Sportswear", "Color": "Bright", "Comfort Level": 5},
        {"Item": "Evening Gown Bottom", "Price": 250.0, "Dress Code": "Evening", "Color": "Dark", "Comfort Level": 1},
    ],
    
    "Shoes": [
        {"Item": "Sneakers", "Price": 0.0, "Dress Code": "Sportswear", "Color": "Bright", "Comfort Level": 5},
        {"Item": "Leather Shoes", "Price": 180.0, "Dress Code": "Business", "Color": "Dark", "Comfort Level": 2},
        {"Item": "Running Shoes", "Price": 120.0, "Dress Code": "Sportswear", "Color": "Bright", "Comfort Level": 5},
        {"Item": "Ballet Flats", "Price": 90.0, "Dress Code": "Casual", "Color": "Dark", "Comfort Level": 4},
        {"Item": "High Heels", "Price": 250.0, "Dress Code": "Evening", "Color": "Dark", "Comfort Level": 2},
        {"Item": "Sandals", "Price": 0.0, "Dress Code": "Casual", "Color": "Bright", "Comfort Level": 5},
        {"Item": "Loafers", "Price": 150.0, "Dress Code": "Business", "Color": "Dark", "Comfort Level": 3},
        {"Item": "Evening Pumps", "Price": 220.0, "Dress Code": "Evening", "Color": "Bright", "Comfort Level": 2},
    ],
    
    "Neck": [
        {"Item": "Silk Scarf", "Price": 70.0, "Dress Code": "Business", "Color": "Dark", "Comfort Level": 3},
        {"Item": "Sports Scarf", "Price": 0.0, "Dress Code": "Sportswear", "Color": "Bright", "Comfort Level": 4},
        {"Item": "Necklace", "Price": 220.0, "Dress Code": "Evening", "Color": "Dark", "Comfort Level": 3},
        {"Item": "Casual Scarf", "Price": 0.0, "Dress Code": "Casual", "Color": "Bright", "Comfort Level": 5},
        {"Item": "Bow Tie", "Price": 80.0, "Dress Code": "Evening", "Color": "Dark", "Comfort Level": 3},
        {"Item": "Athletic Headband", "Price": 50.0, "Dress Code": "Sportswear", "Color": "Bright", "Comfort Level": 5},
        {"Item": "Diamond Necklace", "Price": 750.0, "Dress Code": "Evening", "Color": "Bright", "Comfort Level": 3},
        {"Item": "Choker", "Price": 0.0, "Dress Code": "Evening", "Color": "Dark", "Comfort Level": 4},
    ],
    
    "Purse": [{"Item": "Clutch Bag", "Price": 100.0, "Dress Code": "Evening", "Color": "Dark", "Comfort Level": 3},
        {"Item": "Canvas Bag", "Price": 0.0, "Dress Code": "Casual", "Color": "Bright", "Comfort Level": 5},
        {"Item": "Leather Briefcase", "Price": 180.0, "Dress Code": "Business", "Color": "Dark", "Comfort Level": 1},
        {"Item": "Sports Backpack", "Price": 80.0, "Dress Code": "Sportswear", "Color": "Bright", "Comfort Level": 5},
        {"Item": "Tote Bag", "Price": 0.0, "Dress Code": "Casual", "Color": "Bright", "Comfort Level": 4},
        {"Item": "Wristlet", "Price": 150.0, "Dress Code": "Evening", "Color": "Dark", "Comfort Level": 3},
        {"Item": "Fanny Pack", "Price": 50.0, "Dress Code": "Sportswear", "Color": "Bright", "Comfort Level": 4},
        {"Item": "Elegant Handbag", "Price": 250.0, "Dress Code": "Evening", "Color": "Dark", "Comfort Level": 3},
    ]
}

# Collects user preference
def get_user_preferences():
    print("Welcome to PerfectFit!\n")
    name = input("What is your name?\n").strip()
    
    while not name.isalpha():
        print("Invalid input! Name should only contain letters.")
        name = input("Please enter a valid name:\n").strip()
    
    valid_dress_codes = ["Casual", "Sportswear", "Business", "Evening"]
    print(f"Hi {name}!")
    dress_code = input(f"Please enter your dress code preference ({', '.join(valid_dress_codes)}):\n").strip()
    
    while dress_code not in valid_dress_codes:
        print(f"Invalid input! Please choose from the following options: {', '.join(valid_dress_codes)}.")
        dress_code = input(f"Enter your dress code preference ({', '.join(valid_dress_codes)}):\n").strip()
    
    valid_color_palettes = ["Dark", "Bright"]
    color_palette = input(f"\nPlease enter your color palette preference ({', '.join(valid_color_palettes)}):\n").strip()
    
    while color_palette not in valid_color_palettes:
        print(f"Invalid input! Please choose from the following options: {', '.join(valid_color_palettes)}.")
        color_palette = input(f"Enter your color palette preference ({', '.join(valid_color_palettes)}):\n").strip()
    
    comfort_level = input("\nPlease enter your comfort level (1 (least comfortable) to 5 (most comfortable)):\n").strip()
    
    while not comfort_level.isdigit() or int(comfort_level) < 1 or int(comfort_level) > 5:
        print("Invalid input! Comfort level must be a number between 1 and 5.")
        comfort_level = input("Please enter your comfort level (1 to 5):\n").strip()
    
    budget = input("\nPlease enter your budget (in SAR):\n").strip()
    
    while not budget.replace('.', '', 1).isdigit() or float(budget) <= 0:
        print("Invalid input! Budget must be a positive number.")
        budget = input("Please enter your budget (in SAR):\n").strip()
    
    print("\nWe Are Working on preparing your optimal outfit...")
    return name, dress_code, color_palette, int(comfort_level), float(budget)


# Function to generate the initial population
def generate_population(pop_size, chromosome_length):
    population = []
    for _ in range(pop_size):
        # A chromosome is a random selection of items (one per category)
        chromosome = [random.randint(0, len(search_space[category])-1) for category in search_space] # generates one chromosome by randomly selecting an item from each category
        population.append(chromosome)
    return population


# Function to calculate fitness (Fitness function)
def calculate_fitness(chromosome, search_space, desired_dress_code, desired_color_palette, desired_comfort, budget, weights):
    w1, w2, w3, w4 = weights  # Dress code, Color palette, Comfort, Budget

    categories = ["Top", "Bottom", "Shoes", "Neck", "Purse"]
    
    dress_code_score = 0
    color_palette_score = 0
    comfort_sum = 0
    total_cost = 0
     
    for idx, selected_item in enumerate(chromosome):
        category = categories[idx]
        item = search_space[category][selected_item]
        
        if item["Dress Code"] == desired_dress_code:
            dress_code_score += 1
        
        if item["Color"] == desired_color_palette:
            color_palette_score += 1
        
        comfort_sum += item["Comfort Level"]
        total_cost += item["Price"]
    
    dress_code_score /= len(categories)
    color_palette_score /= len(categories)
    avg_comfort = comfort_sum / len(categories)
    comfort_score = 1 - abs(avg_comfort - desired_comfort) / 4  # Scale to [0, 1]
    budget_score = 1 if total_cost <= budget else budget / total_cost
    
    # Return the weighted fitness score
    fitness = (w1 * dress_code_score +
               w2 * color_palette_score +
               w3 * comfort_score +
               w4 * budget_score)
    
    return fitness


# Function for binary tournament selection
def binary_tournament_selection(population, fitness_scores):
    def tournament():
        # Randomly select two chromosomes
        a = random.randint(0, len(population) - 1)
        b = random.randint(0, len(population) - 1)
          # Select the fittest chromosome (break ties randomly)
        if fitness_scores[a] > fitness_scores[b]:
            return population[a]
        elif fitness_scores[b] > fitness_scores[a]:
            return population[b]
        else:
            # If both have the same fitness, randomly select one
            return random.choice([population[a], population[b]])

    parent1 = tournament()
    parent2 = tournament()
    

    return parent1, parent2


# Crossover: 2-Point Crossover
def crossover(parent1, parent2):
    point1 = random.randint(0, len(parent1) - 1)
    point2 = random.randint(0, len(parent1) - 1)
    
    # Ensure point1 is not equal to point2
    while point1 == point2:
        point2 = random.randint(0, len(parent1) - 1)
    
    # Ensure point1 is less than point2
    if point1 > point2:
        point1, point2 = point2, point1
    
    child1 = parent1[:point1] + parent2[point1:point2] + parent1[point2:]
    child2 = parent2[:point1] + parent1[point1:point2] + parent2[point2:]
    
    return child1, child2


# Function to mutate a chromosome by randomly changing its genes.
def mutate(chromosome, mutation_rate, search_space):
  
    # Copy the chromosome to avoid modifying the original
    mutated_chromosome = chromosome[:]

    for i in range(len(chromosome)):
        # Apply mutation with a given probability
        if random.random() < mutation_rate:

            # Mutate by replacing the gene with another valid random value from the category
            category = list(search_space.keys())[i]
            mutated_chromosome[i] = random.randint(0, len(search_space[category]) - 1)
    
    return mutated_chromosome   


# Replacement: Replace least-fit individuals
def replacement(population, fitness_scores, new_solution, new_solution_fitness):

    # Find the index of the weakest individual
    weakest_index = min(range(len(fitness_scores)), key=lambda i: fitness_scores[i])

    # Replace the weakest individual if the new solution is better
    if new_solution_fitness > fitness_scores[weakest_index]:
        population[weakest_index] = new_solution
        fitness_scores[weakest_index] = new_solution_fitness

    return population, fitness_scores


# Implements the main Genetic Algorithm for optimizing outfit selection based on user preferences.
def genetic_algorithm(dress_code, color_palette, comfort_level, budget, weights, 
                      pop_size=10, generations=300, mutation_rate=0.2):
    
    # Initialize population
    chromosome_length = len(search_space)
    population = generate_population(pop_size, chromosome_length)
    fitness_history = []

    for gen in range(generations):
        # Calculate fitness for each individual
        fitness_scores = [
            calculate_fitness(chromosome, search_space, dress_code, color_palette, comfort_level, budget, weights)
            for chromosome in population
        ]
        
        # Track average fitness
        avg_fitness = sum(fitness_scores) / len(fitness_scores)
        fitness_history.append(avg_fitness)


        # Select parents
        parent1, parent2 = binary_tournament_selection(population, fitness_scores)

        # Crossover to produce offspring
        child1, child2 = crossover(parent1, parent2)

        # Mutate offspring
        child1 = mutate(child1, mutation_rate, search_space)
        child2 = mutate(child2, mutation_rate, search_space)

        # Replace least-fit individuals
        population, fitness_scores = replacement(population, fitness_scores, child1, calculate_fitness(child1, search_space, dress_code, color_palette, comfort_level, budget, weights))
        population, fitness_scores = replacement(population, fitness_scores, child2, calculate_fitness(child2, search_space, dress_code, color_palette, comfort_level, budget, weights))

    # Final fitness calculation
    fitness_scores = [
        calculate_fitness(chromosome, search_space, dress_code, color_palette, comfort_level, budget, weights)
        for chromosome in population
    ]
    best_chromosome = population[fitness_scores.index(max(fitness_scores))]

    # Return best solution and fitness history
    return best_chromosome, fitness_history



# Plots the average fitness per generation across multiple runs of the Genetic Algorithm.
def plot_performance(all_fitness_histories):
        avg_fitness_per_generation = [
            sum(fitness_gen[i] for fitness_gen in all_fitness_histories) / len(all_fitness_histories)
            for i in range(len(all_fitness_histories[0]))
        ]
        
        plt.figure(figsize=(10, 6))
        plt.plot(range(len(avg_fitness_per_generation)), avg_fitness_per_generation, label="Average Fitness", color='blue', linewidth=2)
            
        plt.xlabel("Generation")
        plt.ylabel("Average Fitness")
        plt.title("GA Performance: Average Fitness per Generation (20 Runs)")
        plt.legend(loc='lower right', fontsize='medium')
        plt.grid()
        plt.show()


def main():
    name, dress_code, color_palette, comfort_level, budget = get_user_preferences()
    weights = (0.25, 0.25, 0.25, 0.25)  # Equal weights

   
    all_fitness_histories = [] # Initialize a list to hold fitness history across runs
    overall_best_chromosome = None
    highest_fitness_score = float("-inf")  

    # Run the GA 20 times
    for run in range(20):
        best_chromosome, fitness_history = genetic_algorithm(
        dress_code, color_palette, comfort_level, budget, weights, mutation_rate=0.2
        )
        all_fitness_histories.append(fitness_history)

        # Calculate the fitness of the best chromosome for this run
        best_fitness = calculate_fitness(
            best_chromosome, search_space, dress_code, color_palette, comfort_level, budget, weights
        )

        # Check if this is the best overall
        if best_fitness > highest_fitness_score:
            highest_fitness_score = best_fitness
            overall_best_chromosome = best_chromosome

    # Calculate average fitness per generation
    avg_fitness_per_generation = [
        sum(fitness_gen[i] for fitness_gen in all_fitness_histories) / 20
        for i in range(len(all_fitness_histories[0]))
    ]

    # Display the best outfit
    print("\nYour Best Outfit Selection:")
    for idx, gene in enumerate(overall_best_chromosome):
        category = list(search_space.keys())[idx]
        item = search_space[category][gene]
        print(f"  {category}: {item['Item']}")
    print("\nHope you feel fabulous in your outfit!")


    # Display the overall average fitness
    overall_avg_fitness = sum(avg_fitness_per_generation) / len(avg_fitness_per_generation)
    print(f"\nOverall average fitness across 20 runs: {overall_avg_fitness:.2f}")

    plot_performance(all_fitness_histories)


 

if __name__ == "__main__":
    main()

