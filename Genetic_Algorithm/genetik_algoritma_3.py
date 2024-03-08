import numpy as np
import random

# Şehirler arası mesafeleri temsil eden matris
distance_matrix = np.array([
    [0, 2, 9, 10],
    [1, 0, 6, 4],
    [15, 7, 0, 8],
    [6, 3, 12, 0]
])

def calculate_total_distance(tour):
    """Belirli bir turun toplam mesafesini hesaplar."""
    total_distance = 0
    for i in range(len(tour)):
        total_distance += distance_matrix[tour[i-1]][tour[i]]
    return total_distance

def create_initial_population(size, num_cities):
    """Rastgele turlardan oluşan başlangıç popülasyonunu oluşturur."""
    return [random.sample(range(num_cities), num_cities) for _ in range(size)]

def crossover(parent1, parent2):
    """Çaprazlama yoluyla iki ebeveynden yeni bir tur oluşturur."""
    cut = random.randint(0, len(parent1)-1)
    child = parent1[:cut] + [city for city in parent2 if city not in parent1[:cut]]
    return child

def mutate(tour, mutation_rate=0.01):
    """Rastgele mutasyon ile turu değiştirir."""
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(tour)), 2)
        tour[i], tour[j] = tour[j], tour[i]
    return tour

def genetic_algorithm_tsp(distance_matrix, population_size=100, generations=1000, mutation_rate=0.01):
    num_cities = distance_matrix.shape[0]
    population = create_initial_population(population_size, num_cities)
    
    for _ in range(generations):
        # Uygunluk skorlarına göre popülasyonu sırala
        population.sort(key=calculate_total_distance)
        # En iyi bireyleri seç
        selected = population[:20]
        # Yeni popülasyon oluştur
        population = selected
        while len(population) < population_size:
            parents = random.sample(selected, 2)
            child = crossover(parents[0], parents[1])
            child = mutate(child, mutation_rate)
            population.append(child)
    
    # En iyi turu döndür
    best_tour = population[0]
    best_distance = calculate_total_distance(best_tour)
    return best_tour, best_distance

# Algoritmayı çalıştır
best_tour, best_distance = genetic_algorithm_tsp(distance_matrix)
print(f"En iyi tur: {best_tour}, Mesafe: {best_distance}")
