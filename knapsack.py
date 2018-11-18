# coding=utf-8
import json

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

    print "Carregando dados"

    problem_data = load_data(problem_name)

    max_weight = problem_data['max_weight']

    w, h = max_weight + 1, len(problem_data['element_values']) + 1

    table = [[0 for x in range(w)] for y in range(h)]
    solution_track = [[0 for x in range(w)] for y in range(h)]

    def get_result(el_num, weight):

        return table[el_num][weight]

    print "Calculando tabela"

    for weight in range(0, max_weight + 1):

        for element_num in range(0, len(problem_data['element_values']) + 1):

            if element_num == 0 or weight == 0:
                table[element_num][weight] = 0
                continue

            element_weight = problem_data['element_weights'][element_num - 1]
            element_value = problem_data['element_values'][element_num - 1]

            if element_weight > weight:

                # nao cabe na mochila

                table[element_num][weight] = get_result(element_num - 1, weight)
                solution_track[element_num][weight] = (element_num - 1, weight)
            else:

                # cabe na mochila

                v1 = get_result(element_num - 1, weight - element_weight) + element_value
                v2 = get_result(element_num - 1, weight)

                if v1 >= v2:
                    w_track = weight - element_weight
                else:
                    w_track = weight

                table[element_num][weight] = max(v1, v2)

                solution_track[element_num][weight] = (element_num - 1, w_track)

    # find elements

    print "Calculando composicao da solucao"

    current_key = (len(problem_data['element_values']), problem_data['max_weight'])

    solution_elements = []

    while 1:

        current_weight = current_key[1]
        current_element = current_key[0]

        try:
            current_key = solution_track[current_element][current_weight]

            if current_key[1] < current_weight:
                solution_elements.append(current_element)

        except:
            break

    return solution_elements, get_result(len(problem_data['element_values']), problem_data['max_weight'])

