import random

# Popülasyon sınıfı
class Population:
    def __init__(self, size):
        self.size = size
        self.population = []
        self.fitness_scores = []

    def initialize(self):
        # Rastgele popülasyon oluşturma
        for _ in range(self.size):
            individual = [random.randint(0, 1) for _ in range(10)]  # 10 genlik bireyler
            self.population.append(individual)

    def calculate_fitness(self):
        # Fitness skorlarını hesaplama
        self.fitness_scores = []
        for individual in self.population:
            fitness_score = sum(individual)
            self.fitness_scores.append(fitness_score)

    def selection(self):
        # Seçim işlemi
        selected_population = []
        total_fitness = sum(self.fitness_scores)
        probabilities = [score / total_fitness for score in self.fitness_scores]

        for _ in range(self.size):
            selected_individual = random.choices(self.population, probabilities)[0]
            selected_population.append(selected_individual)

        self.population = selected_population

    def crossover(self):
        # Çaprazlama işlemi
        new_population = []
        for i in range(0, self.size, 2):
            parent1 = self.population[i]
            parent2 = self.population[i + 1]
            crossover_point = random.randint(1, len(parent1) - 1)
            child1 = parent1[:crossover_point] + parent2[crossover_point:]
            child2 = parent2[:crossover_point] + parent1[crossover_point:]
            new_population.extend([child1, child2])

        self.population = new_population

    def mutation(self, mutation_rate):
        # Mutasyon işlemi
        for individual in self.population:
            for i in range(len(individual)):
                if random.random() < mutation_rate:
                    individual[i] = 1 - individual[i]

    def evolve(self, generations, mutation_rate):
        # Evrim işlemi
        self.initialize()
        for _ in range(generations):
            self.calculate_fitness()
            self.selection()
            self.crossover()
            self.mutation(mutation_rate)

        best_individual = max(self.population, key=lambda x: sum(x))
        return best_individual


# Kullanım örneği
population_size = 100
generations = 60
mutation_rate = 0.01

population = Population(population_size)
best_individual = population.evolve(generations, mutation_rate)

print("En iyi birey:", best_individual)