import random
# from answer import alphabet
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

answer = "gmiR4JGijr23UH1Euhl0mijmi78ojg"

# Creating a random individual
def get_letter():
    return random.choice(alphabet)

def create_chromosome(size):
    return ''.join(get_letter() for _ in range(size))

# Scoring an individual
# from answer import get_answer
def get_score(chrom):
    key = answer
    # TODO: implement the scoring function
    #  * compare the chromosome with the solution (how many character are in the correct position?)
    return sum(1 for c,d in zip(chrom, key) if c == d)/len(chrom)
        
# def score(chrom):
#     # floating number between 0 and 1. The better the chromosome, the closer to 1
#     # We coded the get_score(chrom) in the previous exercise
#     return get_score(chrom)
    
def selection(chromosomes_list):
    GRADED_RETAIN_PERCENT = 0.3     # percentage of retained best fitting individuals
    NONGRADED_RETAIN_PERCENT = 0.2  # percentage of retained remaining individuals (randomly selected)
    # TODO: implement the selection function
    #  * Sort individuals by their fitting score
    #  * Select the best individuals
    #  * Randomly select other individuals

    scores = {}
    for c in chromosomes_list:
        scores[c] = get_score(c)

    scores = dict(sorted(scores.items(), key = lambda x:x[1]))

    ans = []
    i = 0
    keys = list(scores.keys())

    while i < int(GRADED_RETAIN_PERCENT*len(chromosomes_list)):
        ans.append(keys[-1-i])
        i += 1

    count = 0
    i = 0
    while count < int(NONGRADED_RETAIN_PERCENT*len(chromosomes_list)):
        if keys[i] not in ans:
            ans.append(keys[i])
            count += 1
        i += 1

    return ans


def crossover(parent1, parent2):
    # TODO: implement the crossover function
    #  * Select half of the parent genetic material
    #  * child = half_parent1 + half_parent2
    #  * Return the new chromosome
    #  * Genes should not be moved
    crossover_location = len(parent1)//2

    return parent1[:crossover_location] + parent2[crossover_location:]


def mutation(chrom):
    # TODO: implement the mutation function
    #  * Random gene mutation : a character is replaced
    ind_mutation = random.randint(0, len(chrom)-1)
    
    return chrom[:ind_mutation] + get_letter() + chrom[ind_mutation+1:]


def create_population(pop_size, chrom_size):
    # use the previously defined create_chromosome(size) function
    # TODO: create the base population
    ans = []
    for i in range(pop_size):
        ans.append(create_chromosome(chrom_size))

    return ans
    
def generation(population):
    
    # selection
    # use the selection(population) function created on exercise 2
    select = selection(population)
    
    # reproduction
    # As long as we need individuals in the new population, fill it with children
    children = []
    # TODO: implement the reproduction
    while len(children) < len(population)//2:
        ## crossover
        parent1 = random.choice(population) # randomly selected
        parent2 = random.choice(population) # randomly selected
        # use the crossover(parent1, parent2) function created on exercise 2
        child = crossover(parent1, parent2)
        
        ## mutation
        # use the mutation(child) function created on exercise 2
        child = mutation(child)
        children.append(child)
    
    # return the new generation
    return select + children

def get_mean_score(population):
    
    return sum(get_score(chromosome) for chromosome in population)/len(population)


def algorithm():
    chrom_size = len(answer)
    population_size = 2000
    
    # create the base population
    population = create_population(population_size, chrom_size)
    
    best_answers = [""]
    curr_max_score = -1
    
    itr = 0
    
    # while a solution has not been found :
    while best_answers[-1] != answer and itr < 1000:
        ## create the next generation
        # TODO: create the next generation using the generation(population) function
        population = generation(population)
        
        ## display the average score of the population (watch it improve)
        print(get_mean_score(population), end = ' ')
    
        ## check if a solution has been found
        for chrom in population:
            if get_score(chrom) > curr_max_score:
                best_answers.append(chrom)
                curr_max_score = get_score(chrom)
        
        print(best_answers[-1])
        itr += 1
        
    print(best_answers)
    
algorithm()


