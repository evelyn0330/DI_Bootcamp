import random
from typing import List


class Gene:
    def __init__(self, value:int):
        self.value = value

    def flip(self):
        self.value = random.randint(0, 1)


class Chromosome:
    def __init__(self, genes: List[Gene]):
        if len(genes) != 10:
            raise Exception('The number of genes must be 10')

        self.genes = genes  

    def flip(self):
         for i in range(len(self.genes)):
           self.genes[i].flip()

    def is_ones(self):
        for gene in self.genes:
            if gene.value == 0:
                return False

        return True
    
    def show(self):
        for gene in self.genes:
            print(gene.value, end ="")



class DNA:
    def __init__(self, chromosomes: List[Chromosome]):
        if not len(chromosomes) == 10:
            raise Exception('The number of chromosomes must be 10')

        self.chromosomes = chromosomes

    def flip(self):
        for i in range(len(self.chromosomes)):
            self.chromosomes[i].flip()

    def is_ones(self):
        for chromosomes in self.chromosomes:
           if not chromosomes.is_ones():
               return False

        return True

    def show(self):
        for chromosome in self.chromosomes:
            chromosome.show()

        print("")


class Organism:
    def __init__(self, dna: DNA):
        self.dna = dna
       
    def flip_and_show(self):
        while not self.dna.is_ones():
            self.dna.show()
            self.dna.flip()

        self.dna.show()
     
genes1 = [Gene(0),Gene(0),Gene(0),Gene(0),Gene(0),Gene(0),Gene(0),Gene(0),Gene(0),Gene(0)]
genes2 = [Gene(0),Gene(0),Gene(1),Gene(0),Gene(0),Gene(1),Gene(0),Gene(0),Gene(0),Gene(0)]

chromosome1 = Chromosome(genes1)
chromosome2 = Chromosome(genes2)

chromosomes = [chromosome1, chromosome2, chromosome2 ,chromosome2,chromosome1,chromosome1,chromosome1,chromosome1,chromosome1,chromosome2]

dna = DNA(chromosomes)

organism = Organism(dna)
organism.flip_and_show()