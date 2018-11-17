# coding=utf-8

import yaml


def load_data(problem_name):
    with open('problems/%s' % problem_name) as f:
        return yaml.load(f)


def get_sub_solution_recursive(data, start_point, max_weight, recorded_solutions):

    solution_key = '%s-%s' % (start_point, max_weight)

    try:
        already_calculated_solution = recorded_solutions[solution_key]

        print 'Reusing calculation', solution_key

        return already_calculated_solution
    except KeyError:
        pass

    if max_weight == 0:
        result = 0

        recorded_solutions[solution_key] = result

        return result

    if start_point == len(data['element_values']):
        result = 0
        recorded_solutions[solution_key] = result
        return result

    element_weight = data['element_weights'][start_point]
    element_value = data['element_values'][start_point]

    if element_weight > max_weight:

        # não cabe na mochila

        result = get_sub_solution_recursive(data, start_point + 1, max_weight, recorded_solutions)

        recorded_solutions[solution_key] = result

        return result

    else:

        # cabe na mochila

        result = max(
            get_sub_solution_recursive(data, start_point + 1, max_weight - element_weight, recorded_solutions) + element_value,
            get_sub_solution_recursive(data, start_point + 1, max_weight, recorded_solutions),
        )

        recorded_solutions[solution_key] = result

        return result


def get_solution_recursive(problem_name):

    problem_data = load_data(problem_name)

    return get_sub_solution_recursive(problem_data, 0, problem_data['max_weight'], recorded_solutions={})


print get_solution_recursive('basic.yml')
print get_solution_recursive('bit_complex.yml')