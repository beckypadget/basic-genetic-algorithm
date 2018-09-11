#setwd("~/Documents/1.Uni/Python/Genetic_algorithms")
#Import libraries
import random
import operator
import numpy as np
import matplotlib.pyplot as plt

#Begin
TARGET_SEQUENCE = "AGTCAGCAT"
SURVIVAL_RATE = 10 #the number of sequences taken (sorted from best-worst)
POPULATION_SIZE = 1000
NUM_GENERATIONS = 100
MUTATION_RATE = 0.05

#Calculate fitness of each test_word
def fitness(sequence):
  fitscore = 0
  for i in range(len(sequence)):
    if sequence[i] == TARGET_SEQUENCE[i]:
      fitscore += 1
  return fitscore

def generate_sequence(length):
  sequence = ""
  for i in range(length):
      sequence += random.choice("ACTG")
  return sequence

#Generate the initial population
def generate_population(population_size, TARGET_SEQUENCE):
  population = []
  for i in range(population_size):
    population.append(generate_sequence(len(TARGET_SEQUENCE)))
  return population

#Crossover
def crossover(mother, father):
  offspring = []
  split_point = len(mother)//2
  allele1, allele2 = mother[:split_point], mother[split_point:]
  allele3, allele4 = father[:split_point], father[split_point:]
  offspring = [allele1 + allele4, allele2 + allele3]
  return offspring

#Crossover everything
def crossover_population(population):
  offspring = []
  for i in range(-1, len(population)-1):
    offspring += crossover(population[i], population[i+1])
  return population + offspring

#Mutate
def mutate(sequence, mutation_rate):
  if random.random() < mutation_rate:
    mutation_point = random.randrange(0, len(sequence))
    substitution = random.choice("ACGT")
    sequence = list(sequence)
    sequence[mutation_point] = substitution
    sequence = "".join(sequence)
  return sequence

population_means = []
population = generate_population(POPULATION_SIZE, TARGET_SEQUENCE)

for i in range(NUM_GENERATIONS):
  population = sorted(population, key = fitness)
  population = population[POPULATION_SIZE-SURVIVAL_RATE:]
  population_means.append(np.mean([fitness(x) for x in population]))
  population = crossover_population(population)
  population = [mutate(x, MUTATION_RATE) for x in population]
  population += generate_population((POPULATION_SIZE-len(population)), TARGET_SEQUENCE)

print(population_means)
exit()

#Put 'fitness' into an array
mean_fitness = np.asarray([population_means])
np.savetxt("mean_fitness.csv", a, delimiter="\n")

generations = np.arange(0, 100, 1)

#Plot
s = [20*1 for n in range(len(generations))]
plt.scatter(generations, mean_fitness, s=s)
plt.show()

exit()
