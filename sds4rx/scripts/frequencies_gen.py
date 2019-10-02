DAYS_OF_WEEK = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

HOURS_SPELLED = [
    "one", "two", "three", "four", "five", "six",
    "seven", "eight", "nine", "ten", "eleven", "twelve"
]

HOURS = [str(x) + ' pm' for x in range(1,13)] + [str(x) + ' am' for x in range(1,13)]

'''
select N and L as needed
'''
N = 2
l = HOURS

def _combo_n(choices, n):
    if choices == [] or n == 0:
        return []

    if n == 1:
        return [[c] for c in choices]

    combos = []
    for i in range(len(choices)):
        c = choices[i]
        remaining = choices[:i] + choices[i+1:]
        tail = _combo_n(remaining, n-1)
        combos += [t + [c] for t in tail]

    return combos

if __name__ == "__main__":
    combos = _combo_n(L, N)

    combos = [' and '.join(c) for c in combos]
    combos = ['"{}",'.format(c) for c in combos]

    print("\n".join(combos))