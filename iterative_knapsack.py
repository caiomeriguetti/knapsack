import sys

from knapsack import get_solution_recursive, get_solution_iter

problem_name = sys.argv[1]

print get_solution_iter(problem_name)