import random

import yaml

max_weight = 300
data = {
    'max_weight': max_weight,
    'element_weights': [],
    'element_values': []
}

n = 1000

for i in range(0, n):

    data['element_weights'].append(random.randint(1, data['max_weight']))
    data['element_values'].append(random.randint(1, 1000))


with open('w%s_n%s.yml' % (max_weight, n), 'w') as random_dataset_file:
    yaml.dump(data, random_dataset_file)
