"""http://rosalind.info/problems/fibd/"""

from fibonacci import fib

l_month, y = map(int, input().strip().split())

rabbit_cache = {}

def rabbits(month, repr_rate):
    """matured * (repr_rate + 1) coz matured 's also part of the population"""
    if rabbit_cache.setdefault(month, 0): return rabbit_cache[month]
    elif month <=2: 
        rabbit_cache[month] = 1
        return 1
    else:
        matured = rabbits(month - 2, repr_rate)
        newborns = rabbits(month - 1, repr_rate) - matured 
        result = matured * (repr_rate + 1) + newborns 
        print(month, ": ", matured, newborns, result)
        rabbit_cache[month] = result
        return result

mort_rabbit_cache = {}

def rabbits_die(month, death_period):
    difference =  (month - death_period) if month > death_period else 0
    if difference:
        old_rabbits = mortal_rabbits(difference, death_period)
        to_die_family = old_rabbits * (difference)
    return 0

def mortal_rabbits(m, life):
    def reproduce(rbc):
        new_rbc = [0] * life
        matured = 0
        for age in reversed(range(life)):
            if age:
                new_rbc[age] += rbc[age-1]
                if age-1: matured += rbc[age-1]
            else:
                new_rbc[0] = matured + rbc[life-1]
        #    print("age:", age, new_rbc, "old:", rbc, "kids?:", matured)
        return new_rbc

    def get_population(months, rabbits_colony):
        if months<2: return rabbits_colony
        else:
            print(months, ":", rabbits_colony, "s:", sum(rabbits_colony))
            rabbits_colony = reproduce(rabbits_colony)
            return get_population(months-1, rabbits_colony)
    
    rabbits_col = [0] * life
    rabbits_col[0] = 1
    res = get_population(m, rabbits_col)
    print("rse", res)
    return sum(res)
    
    
# print(rabbits(l_month, y))
print(mortal_rabbits(l_month, y))
