
def scratch(random):
    one, two = 0, 1
    total_cost = 0

    step = min(random[one], random[two])
    skipped = max(random[one], random[two])

    while random.index(step) or random.index(skipped) <= (len(random)-1):
        total_cost += random[step]
        random.index(step) += 2




