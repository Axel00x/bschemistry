import main

class Element():
    def __init__(self, name, symbol, a_num, a_mass, a_radius, electron_config, electronegativity, electron_affinity, ionization_energies, e_class, oxidation_nums, melting_temp, boiling_temp, d, yr):
        self.name = name
        self.symbol = symbol
        self.a_num = a_num
        self.a_mass = a_mass
        self.a_radius = a_radius
        self.electron_config = electron_config
        self.electronegativity = electronegativity
        self.electron_affinity = electron_affinity
        self.ionization_energies = ionization_energies
        self.e_class = e_class
        self.oxidation_nums = oxidation_nums
        self.melting_temp = melting_temp
        self.boiling_temp = boiling_temp
        self.d = d
        self.yr = yr   
     
class Table():
    def __init__(self):
        self.table = {}
        
    def add_elem(self, ind, elem):
        self.table[ind] = elem
    
    def elem(self, ind):
        return self.table[ind]
    
t = Table()

for i in main.table:
    t.add_elem(i, Element(main.table[i]["name"],
                       main.table[i]["symbol"],
                       main.table[i]["a_num"],
                       main.table[i]["a_mass"],
                       main.table[i]["a_radius"],
                       main.table[i]["electron_config"],
                       main.table[i]["electronegativity"],
                       main.table[i]["electron_affinity"],
                       main.table[i]["ionization_energies"],
                       main.table[i]["class"],
                       main.table[i]["oxidation_nums"],
                       main.table[i]["melting_temp"],
                       main.table[i]["boiling_temp"],
                       main.table[i]["d"],
                       main.table[i]["yr"]))

print(t.elem(input()).name)

