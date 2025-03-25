# test file

# template:
'''
    '': {
        'name': '',
        'symbol': '',
        'a_num': 0,
        'a_mass': 0,
        'a_radius': 0,
        'electron_config': '', 
        'electronegativity': 0,
        'electron_affinity': 0,
        'ionization_energies': 0,
        'class': '',
        'oxidation_nums': [],
        'melting_temp': 0, 
        'boiling_temp': 0,
        'd': 0,
        'yr': 0 
    },
'''

table = {
    'H': {
        'name': 'Hydrogen',
        'symbol': 'H',
        'a_num': 1,
        'a_mass': 1.00794, # u
        'a_radius': 30, # pm (picometers)
        'electron_config': '1s1', 
        'electronegativity': 2.2,
        'electron_affinity': 72.8, # kJ/mol
        'ionization_energies': 1312, # kJ/mol
        'class': 'nonmetal',
        'oxidation_nums': [-1,1],
        'melting_temp': 14, # K
        'boiling_temp': 20, # K
        'd': 0.0899, # g/L
        'yr': 1766 # year of discovery
    },
    'He': {
        'name': 'Helium',
        'symbol': 'He',
        'a_num': 2,
        'a_mass': 4.003, # u
        'a_radius': 93, # pm (picometers)
        'electron_config': '1s2', 
        'electronegativity': 0,
        'electron_affinity': 0, # kJ/mol
        'ionization_energies': 2372, # kJ/mol
        'class': 'noble gas',
        'oxidation_nums': [],
        'melting_temp': 1, # K
        'boiling_temp': 4, # K
        'd': 0.18, # g/L
        'yr': 1895 # year of discovery
    },
    'Li': {
        'name': 'Lithium',
        'symbol': 'Li',
        'a_num': 3,
        'a_mass': 6.941, # u
        'a_radius': 155, # pm (picometers)
        'electron_config': '[He]2s1', 
        'electronegativity': 0.98,
        'electron_affinity': 59.6, # kJ/mol
        'ionization_energies': 513, # kJ/mol
        'class': 'alkali metal',
        'oxidation_nums': [1],
        'melting_temp': 454, # K
        'boiling_temp': 1615, # K
        'd': 530, # g/L
        'yr': 1817 # year of discovery
    },
    'Be': {
        'name': 'Beryllium',
        'symbol': 'Be',
        'a_num': 4,
        'a_mass': 9.012,
        'a_radius': 112,
        'electron_config': '[He]2s2', 
        'electronegativity': 1.57,
        'electron_affinity': 0,
        'ionization_energies': 0,
        'class': 'earthy alkali metal',
        'oxidation_nums': [2],
        'melting_temp': 1561, 
        'boiling_temp': 2744,
        'd': 1850,
        'yr': 1798 
    },
    'B': {
        'name': 'Boron',
        'symbol': 'B',
        'a_num': 5,
        'a_mass': 10.81,
        'a_radius': 98,
        'electron_config': '[He]2s22p1', 
        'electronegativity': 2.04,
        'electron_affinity': 26.7,
        'ionization_energies': 801,
        'class': 'semimetals',
        'oxidation_nums': [3],
        'melting_temp': 2573.15, 
        'boiling_temp': 3923.15,
        'd': 2470,
        'yr': 1808
    },
    'C': {
        'name': 'Carbon',
        'symbol': 'C',
        'a_num': 6,
        'a_mass': 12.01,
        'a_radius': 91,
        'electron_config': '[He]2s22p2', 
        'electronegativity': 2.55,
        'electron_affinity': 153.9,
        'ionization_energies': 1086,
        'class': 'nonmetal',
        'oxidation_nums': [-4, 2, 4],
        'melting_temp': 0, 
        'boiling_temp': 3823.15,
        'd': 2260,
        'yr': 0 
    },
    'N': {
        'name': 'Nitrogen',
        'symbol': 'N',
        'a_num': 7,
        'a_mass': 14.01,
        'a_radius': 92,
        'electron_config': '[He]2s22p3', 
        'electronegativity': 3.04,
        'electron_affinity': 7,
        'ionization_energies': 1402,
        'class': 'nonmetal',
        'oxidation_nums': [-3, 2, 3, 4, 5],
        'melting_temp': 63, 
        'boiling_temp': 77,
        'd': 1.25,
        'yr': 1772
    },
    'O': {
        'name': 'Oxygen',
        'symbol': 'O',
        'a_num': 8,
        'a_mass': 16,
        'a_radius': 66,
        'electron_config': '[He]2s22p4', 
        'electronegativity': 3.44,
        'electron_affinity': 141,
        'ionization_energies': 1314,
        'class': 'nonmetal',
        'oxidation_nums': [-2],
        'melting_temp': 54, 
        'boiling_temp': 90,
        'd': 1.43,
        'yr': 1774
    },
    'F': {
        'name': 'Fluorine',
        'symbol': 'F',
        'a_num': 9,
        'a_mass': 19,
        'a_radius': 64,
        'electron_config': '[He]2s22p5', 
        'electronegativity': 3.98,
        'electron_affinity': 328,
        'ionization_energies': 1681,
        'class': 'halogens',
        'oxidation_nums': [-1],
        'melting_temp': 53, 
        'boiling_temp': 85,
        'd': 1.7,
        'yr': 1771
    },
    'Ne': {
        'name': 'Neon',
        'symbol': 'Ne',
        'a_num': 10,
        'a_mass': 20.18,
        'a_radius': 160,
        'electron_config': '[He]2s22p6', 
        'electronegativity': 0,
        'electron_affinity': 0,
        'ionization_energies': 2081,
        'class': 'noble gas',
        'oxidation_nums': [],
        'melting_temp': 24, 
        'boiling_temp': 27,
        'd': 0.9,
        'yr': 1898 
    },
    'Na': {
        'name': 'Sodium',
        'symbol': 'Na',
        'a_num': 11,
        'a_mass': 22.99,
        'a_radius': 190,
        'electron_config': '[Ne]3s1', 
        'electronegativity': 0.93,
        'electron_affinity': 52.8,
        'ionization_energies': 496,
        'class': 'alkali metals',
        'oxidation_nums': [1],
        'melting_temp': 371, 
        'boiling_temp': 1156,
        'd': 970,
        'yr': 1807
    },
    'Mg': {
        'name': 'Magnesium',
        'symbol': 'Mg',
        'a_num': 12,
        'a_mass': 24.31,
        'a_radius': 160,
        'electron_config': '[Ne]3s2', 
        'electronegativity': 1.31,
        'electron_affinity': 0,
        'ionization_energies': 738,
        'class': 'eartjy alkali metal',
        'oxidation_nums': [2],
        'melting_temp': 923, 
        'boiling_temp': 1363,
        'd': 1740,
        'yr': 1755
    },
    'Al': {
        'name': 'Aluminum',
        'symbol': 'Al',
        'a_num': 13,
        'a_mass': 26.98,
        'a_radius': 143,
        'electron_config': '[Ne]3s23p1', 
        'electronegativity': 1.61,
        'electron_affinity': 42.5,
        'ionization_energies': 578,
        'class': 'block p metals',
        'oxidation_nums': [3],
        'melting_temp': 933, 
        'boiling_temp': 2792,
        'd': 2700,
        'yr': 1827
    },
    'Si': {
        'name': 'Silicon',
        'symbol': 'Si',
        'a_num': 14,
        'a_mass': 28.09,
        'a_radius': 132,
        'electron_config': '[Ne]3s23p2', 
        'electronegativity': 1.9,
        'electron_affinity': 133.6,
        'ionization_energies': 786,
        'class': 'semimetal',
        'oxidation_nums': [-4, 2, 4],
        'melting_temp': 1687, 
        'boiling_temp': 3553,
        'd': 2330,
        'yr': 1823 
    },
    'P': {
        'name': 'Phosphorus',
        'symbol': 'P',
        'a_num': 15,
        'a_mass': 30.97,
        'a_radius': 128,
        'electron_config': '[Ne]3s23p3', 
        'electronegativity': 2.19,
        'electron_affinity': 72,
        'ionization_energies': 1012,
        'class': 'nonmetal',
        'oxidation_nums': [-3, 3, 5],
        'melting_temp': 317, 
        'boiling_temp': 553,
        'd': 1820,
        'yr': 0
    },
}       