import math
import random
# calculate possible combinations


def pos_uniq_combi(num_of_items: int, pair: int) -> int:  # takes in the number of items and required pair
    # combination = factorial of num_of_items
    #               -------------------------
    #              factorial of (num_of_items-pair)*factorial of pair
    try:
        numerator = math.factorial(num_of_items)
        denominator = math.factorial(num_of_items - pair) * math.factorial(pair)
        possible_combination = numerator / denominator
        return int(possible_combination)
    except TypeError:
        raise TypeError


def set_combinations(user_set: list, pair: int):
    try:
        pos_combi = pos_uniq_combi(len(user_set), pair)
        print(pos_combi)
        list_of_combinations = []
        while len(list_of_combinations) != pos_combi:
            a_pair = random.choices(user_set, k=pair)
            # make sure no doubles in a_pair
            no_double_in_pair = True
            for i in a_pair:
                if a_pair.count(i) > 1:
                    no_double_in_pair *= False
            if no_double_in_pair:
                if len(list_of_combinations) == 0:
                    list_of_combinations.append(a_pair)
                else:
                    if a_pair not in list_of_combinations:
                        not_in = True
                        for i in list_of_combinations:
                            count = 0
                            for x in a_pair:
                                if x in i:
                                    count += 1
                            if count == len(i):
                                not_in *= False
                        if not_in:
                            list_of_combinations.append(a_pair)
        return list_of_combinations
    except TypeError:
        raise TypeError
