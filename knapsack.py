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


def get_solution_iter(problem_name):

    problem_data = load_data(problem_name)

    max_weight = problem_data['max_weight']

    table = {}

    def get_result(element_num, weight):

        table_key = '%s-%s' % (element_num, weight)

        return table[table_key]

    for weight in range(0, max_weight+1):
        for element_num in range(0, len(problem_data['element_values']) + 1):

            table_key = '%s-%s' % (element_num, weight)

            if element_num == 0 or weight == 0:
                table[table_key] = 0
                continue

            element_weight = problem_data['element_weights'][element_num - 1]
            element_value = problem_data['element_values'][element_num - 1]

            if element_weight > weight:
                # nao cabe na mochila

                table[table_key] = get_result(element_num - 1, weight)
            else:
                # cabe na mochila

                table[table_key] = max(
                    get_result(element_num - 1, weight - element_weight) + element_value,
                    get_result(element_num - 1, weight),
                )

    return get_result(len(problem_data['element_values']), problem_data['max_weight'])



# print get_solution_recursive('basic.yml')
# print get_solution_recursive('random_dataset.yml')

print get_solution_iter('basic.yml')