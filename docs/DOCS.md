# bschemistry
### v0.1.1

Welcome to bschemistry! (Full name: basic chemistry)

## How to install bschemistry?
To install bschemistry simply use the command `pip install bschemistry` or `pip3 install bschemistry`.
#### Requirements:
- None

## How to install an update for the library?
To update it simply run the command `pip install bschemistry --upgrade` on the cmd.

## Quick start
To start using bschemistry it must first be imported.
```python
import bschemistry as ch
``
Once this is done you can create a periodic table with the following code:
``python
import bschemistry as ch

t = ch.Table()
``
Once the table has been initialized you can access its elements with the `elem()` function. 
For example:
``python
import bschrmistry as ch

t = ch.Table()

print(t.elem("O").a_mass) # print the atomic mass of O (Oxygen)
``

## Data available
``python
'name': 'Hydrogen',
'symbol': 'H',
'a_num': 1,
'a_mass': 1. 00794, # u
'a_radius': 30, # pm (picometers)
'electron_config': '1s1', 
'electronegativity': 2.2, # Pauling's scale
'electron_affinity': 72.8, # kJ/mol
'ionization_energies': 1312, # kJ/mol
'class': 'nonmetal',
'oxidation_nums': [-1,1],
'melting_temp': 14, # K
'boiling_temp': 20, # K
'd': 0.0899, # g/L
'yr': 1766 # year of discovery
``

## Functions
#### format(elem)
To receive a dictionary of a formatted molecule:
```python
import bschemistry as ch

print(ch.format("{1}H2O")

# output:
# {'1':{ 'H': 2, 'O': 1}}
```