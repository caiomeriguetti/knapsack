# coding=utf-8

import yaml


def load_data(problem_name):
    with open('problems/%s' % problem_name) as f:
        return yaml.load(f)


def get_sub_solution(data, start_point, max_weight):

    if max_weight == 0:
        return 0

    if start_point == len(data['element_values']):
        return 0

    element_weight = data['element_weights'][start_point]
    element_value = data['element_values'][start_point]

    if element_weight > max_weight:
        # não cabe na mochila
        return get_sub_solution(data, start_point + 1, max_weight)
    else:
        # cabe na mochila
        return max(
            get_sub_solution(data, start_point + 1, max_weight - element_weight) + element_value,
            get_sub_solution(data, start_point + 1, max_weight),
        )


def get_solution(problem_name):

    problem_data = load_data(problem_name)

    return get_sub_solution(problem_data, 0, problem_data['max_weight'])


print get_solution('basic.yml')