A_MAX = 500000
B_MAX = 20000
G_MAX = 120000
TOTAL_ANIMALS = 7000

species_order = [
    "golden_snub-nosed_monkey",
    "red_panda",
    "tufted_deer",
    "chinese_alligator",
    "red-crowned_crane",
    "chinese_water_deer",
    "eurasian_otter",
    "gibbon",
    "humboldt_penguin",
    "finless_porpoise"
]

animal_index = dict()

for i in range(10):
    animal_index[species_order[i]] = i

conservation = [1.00, 0.70, 1.00, 1.00, 0.70, 0.70, 0.30, 0.30, 1.00, 1.00]
research = [0.88, 0.78, 0.85, 0.65, 0.60, 0.90, 0.75, 0.80, 0.95, 0.92]
education = [0.92, 0.90, 0.75, 0.80, 0.70, 0.85, 0.88, 0.78, 0.92, 0.90]
recreation = [0.85, 0.88, 0.70, 0.82, 0.65, 0.80, 0.92, 0.83, 0.90, 5] 

weights_EQUAL = [0.25] * 4
weights_CONSERVATION = [0.5, 0.2, 0.2, 0.1]
weights_EDUCATION = [0.1, 0.2, 0.5, 0.2]

a_i = [150, 80, 100, 120, 60, 130, 50, 400, 500, 300]
b_i = [30, 20, 20, 25, 15, 35, 30, 50, 80, 100]
f_i = [0.5, 0.4, 0.2, 0.3, 0.2, 0.7, 0.3, 0.3, 0.4, 0.4]
C_i_cap = [5.0, 3.0, 2.0, 4.0, 1.5, 4.5, 6.0, 8.0, 20.0, 15.0]
C_i_build = [40, 25, 15, 30, 10, 45, 60, 80, 200, 200]
n_i_min = [4, 2, 3, 2, 3, 2, 5, 2, 2, 1]
n_i_max = [10, 6, 8, 5, 8, 4, 15, 4, 4, 2]
n_i_min = [v * 100 for v in n_i_min]
n_i_max = [v * 100 for v in n_i_max]
n_i_min[9] = n_i_max[9] = 1
