import pulp
import tabulate

from test_data import *

weights_chosen = weights_EQUAL


def Sol(weights_chosen, n_i_max, n_i_min, C_i_build, C_i_cap, f_i, a_i, b_i):

    prob = pulp.LpProblem("Animal", sense=pulp.LpMaximize)
    x_i = []
    n_i = []
    for i in range(10):
        x_i.append(pulp.LpVariable(f'x_{i}', lowBound=0, upBound=1, cat="Binary"))
        n_i.append(pulp.LpVariable(f'n_{i}', lowBound=0, upBound=n_i_max[i], cat="Integer"))
        prob += (n_i_min[i] * x_i[i] <= n_i[i])
        prob += (n_i[i] <= n_i_max[i] * x_i[i])

    prob += (x_i[9] == 1)


    prob += pulp.lpSum(xi for xi in x_i) <= TOTAL_ANIMALS
    Q = [0] * 10

    for i in range(10):
        Q[i] = weights_chosen[0] * conservation[i] + weights_chosen[1] * research[i] + weights_chosen[2] * education[i] + weights_chosen[3] * recreation[i];

    Z = Q[0] * n_i[0]
    for i in range(1, 10):
        Z += Q[i] * n_i[i]
    prob += Z

    A_MAX_f = (a_i[0] * (1 + f_i[0]) + b_i[0]) * n_i[0]
    for i in range(1, 10):
        A_MAX_f += (a_i[i] * (1 + f_i[i]) + b_i[i]) * n_i[i]
    prob += (A_MAX_f <= A_MAX)

    B_MAX_f = (C_i_cap[0] * n_i[0])
    for i in range(1, 10):
        B_MAX_f += (C_i_cap[i] * n_i[i])
    prob += (B_MAX_f <= B_MAX)

    C_MAX_f = (C_i_build[0] * n_i[0])
    for i in range(1, 10):
        C_MAX_f += (C_i_build[i] * n_i[i]);
    prob += (C_MAX_f <= G_MAX)

    prob.solve()

    x_ans = []
    n_ans = []

    for i in range(len(prob.variables())):
        if i <= 9:
            n_ans.append(prob.variables()[i].varValue)
        else:
            x_ans.append(prob.variables()[i].varValue)

    data = []
    for i in range(10):
        data.append([species_order[i], x_ans[i], n_ans[i], a_i[i] * n_ans[i] * (1 + f_i[i]), b_i[i] * n_ans[i], C_i_build[i] * n_ans[i], C_i_cap[i] * n_ans[i]])
    return data, pulp.value(prob.objective)

def print_sol(data, objective):
    print("max Z =", objective)
    headers = ["Animal Name", "Selected", "Quantity", "Exhibit Area", "Backstage Area", "Construction Cost", "Operating Cost"]

    print(tabulate.tabulate(data, headers=headers, tablefmt="simple"))
    for i in range(3, len(headers)):
        sumtmp = 0
        for j in range(10):
            sumtmp += data[j][i]
        print(f"Sum of {headers[i]}: ", sumtmp)

if __name__ == "__main__":
    print_sol(*Sol(weights_chosen, n_i_max, n_i_min, C_i_build, C_i_cap, f_i, a_i, b_i))