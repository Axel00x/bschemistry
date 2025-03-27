# bschemistry
#### v0.0.1

Bschemistry (basic chemistry) is a library that contains the basic functions to use chemistry on Python as well!
It has a complete and accurate periodic table with all data updated regularly and frequent updates for new functions and features.

Example of the table structure:

```python
'name': 'Hydrogen',
'symbol': 'H',
'a_num': 1,
'a_mass': 1.00794,           # u
'a_radius': 30,              # pm (picometers)
'electron_config': '1s1', 
'electronegativity': 2.2,    # Pauling's scale
'electron_affinity': 72.8,   # kJ/mol
'ionization_energies': 1312, # kJ/mol
'class': 'nonmetal',
'oxidation_nums': [-1,1],
'melting_temp': 14,          # K
'boiling_temp': 20,          # K
'd': 0.0899,                 # g/L
'yr': 1766                   # year of discovery
```

## Practical examples

To receive a dictionary about an element of the periodic table from the table use:

```python
import bschemistry as ch

print(ch.table[“H”])
```

To get a single datum about an element use:

```python
import bschemistry as ch

print(ch.table[“H”][“a_mass”]) # take the atomic mass of element H (Hydrogen)
```