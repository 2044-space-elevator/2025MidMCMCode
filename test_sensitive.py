from program_main import Sol
from test_data import *
from random import randint, uniform

result_str = ""

data, Z = Sol(weights_EQUAL, n_i_max, n_i_min, C_i_build, C_i_cap, f_i, a_i, b_i)
all_n = [v[2] for v in data]
all_n = map(str, all_n)
result_str += f"Standard n_i: {', '.join(all_n)}\n"
result_str += f"Standard Z: {Z}\n\n"

# test for weight

TEST_TIMES_WEIGHT = 5

result_str += "TESTING THE SENSITIVE OF WEIGHT.\n\n "

for i in range(TEST_TIMES_WEIGHT):
    weights_chosen = list(weights_EQUAL)
    delta = uniform(-0.25, 0.25)
    change_obj_a = randint(0, 3)
    change_obj_b = randint(0, 3)
    weights_chosen[change_obj_a] += delta
    weights_chosen[change_obj_b] -= delta
    data, Z = Sol(weights_chosen, n_i_max, n_i_min, C_i_build, C_i_cap, f_i, a_i, b_i)
    all_n = [v[2] for v in data]
    all_n = map(str, all_n)
    result_str += f"Delta: {delta}\n"
    result_str += f"(result of n) {i}: {', '.join(all_n)}\n"
    result_str += f"(result of Z) {i}: {Z}\n\n"

# test for other paraments

TEST_TIMES_PARA = 5

# (1): Parament a_i

result_str += "TESTING THE SENSITE OF a_i.\n\n"

for i in range(TEST_TIMES_PARA):
    a_i_fortest = list(a_i)
    chosen_change_par_1 = uniform(0.05, 0.1)
    chosen_change_par_2 = uniform(0.05, 0.1)
    chosen_change_1 = randint(0, 9)
    chosen_change_2 = randint(0, 9)
    a_i_fortest[chosen_change_1] *=  chosen_change_par_1
    a_i_fortest[chosen_change_2] *= chosen_change_par_2
    result_str += f"Delta1: {chosen_change_par_1}\n"
    result_str += f"Delta2: {chosen_change_par_2}\n"
    data, Z = Sol(weights_EQUAL, n_i_max, n_i_min, C_i_build, C_i_cap, f_i, a_i_fortest, b_i)
    all_n = [v[2] for v in data]
    all_n = map(str, all_n)
    result_str += f"(result of n) {i}: {', '.join(all_n)}\n"
    result_str += f"(result of Z) {i}: {Z}\n\n"

result_str += "TESTING THE SENSITIVE OF b_i.\n\n"

for i in range(TEST_TIMES_PARA):
    b_i_fortest = list(b_i)
    chosen_change_par_1 = uniform(0.05, 0.1)
    chosen_change_par_2 = uniform(0.05, 0.1)
    chosen_change_1 = randint(0, 9)
    chosen_change_2 = randint(0, 9)
    b_i_fortest[chosen_change_1] *= chosen_change_par_1
    b_i_fortest[chosen_change_2] *= chosen_change_par_2
    result_str += f"Delta1: {chosen_change_par_1}\n"
    result_str += f"Delta2: {chosen_change_par_2}\n"
    data, Z = Sol(weights_EQUAL, n_i_max, n_i_min, C_i_build, C_i_cap, f_i, a_i, b_i_fortest)
    all_n = [v[2] for v in data]
    all_n = map(str, all_n)
    result_str += f"(result of n) {i}: {', '.join(all_n)}\n"
    result_str += f"(result of Z) {i}: {Z}\n\n"


print(result_str)