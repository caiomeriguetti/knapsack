import math
import random

import yaml

data = {
    'max_weight': 1000,
    'element_weights': [],
    'element_values': []
}

for i in range(0, 1000):

    data['element_weights'].append(random.randint(1, data['max_weight']))
    data['element_values'].append(random.randint(1, 1000))


with open('random_dataset.yml', 'w') as random_dataset_file:
    yaml.dump(data, random_dataset_file)
