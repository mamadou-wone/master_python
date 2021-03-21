from pprint import pprint

import pandas

data = pandas.read_csv('salaries_by_college_major.csv')

# Affiche les ligne ayant pour valeur NAN
data.tail()