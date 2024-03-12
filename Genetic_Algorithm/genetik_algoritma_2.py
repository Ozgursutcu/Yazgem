import random
import string

def generate_individual(length):
    """Rastgele bir string oluştur."""
    return ''.join(random.choices(string.ascii_letters, k=length))

def compute_fitness(individual, target):
    """Bireyin uygunluk skorunu hesapla."""
    return sum(ind1 == ind2 for ind1, ind2 in zip(individual, target))

def crossover(parent1, parent2):
    """İki ebeveyn arasında çaprazlama yap."""
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def mutate(individual, mutation_rate=0.01):
    """Bireyi mutasyona uğrat."""
    individual = list(individual)
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = random.choice(string.ascii_letters)
    return ''.join(individual)

def genetic_algorithm(target, population_size=100, generations=1000, mutation_rate=0.01):
    # Başlangıç popülasyonunu oluştur
    population = [generate_individual(len(target)) for _ in range(population_size)]
    
    for generation in range(generations):
        # Uygunluk skorlarını hesapla
        fitness_scores = [compute_fitness(individual, target) for individual in population]
        
        # En iyi çözümü kontrol et
        best_individual = population[fitness_scores.index(max(fitness_scores))]
        if compute_fitness(best_individual, target) == len(target):
            return best_individual, generation
        
        # Yeni popülasyonu seçme ve oluşturma
        new_population = []
        sorted_population = [x for _, x in sorted(zip(fitness_scores, population), reverse=True)]
        
        # En iyi bireyleri doğrudan sonraki nesle taşı
        new_population.extend(sorted_population[:2])
        
        while len(new_population) < population_size:
            parent1, parent2 = random.sample(sorted_population[:50], 2)  # En iyi 50 bireyden ebeveyn seç
            child1, child2 = crossover(parent1, parent2)
            new_population.append(mutate(child1, mutation_rate))
            if len(new_population) < population_size:
                new_population.append(mutate(child2, mutation_rate))
                
        population = new_population
        
    # En iyi çözümü döndür
    return best_individual, generations

# Hedef string ve algoritma parametreleri
target_string = "HelloWorld"
population_size = 200
generations = 100
mutation_rate = 0.03

# Genetik algoritmayı çalıştır
best_solution, generation = genetic_algorithm(target_string, population_size, generations, mutation_rate)
print(best_solution, generation)
