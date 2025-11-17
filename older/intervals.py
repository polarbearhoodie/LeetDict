# insert interval into schedule
def insert_merge(schedule: list[list[int]], interval: list[int]) -> list[list[int]]:
    keep = []

    # pass through and set the bounds of the interval and new schedule
    for itr, entry in enumerate(schedule):
        set_pass = False

        if entry[0] <= interval[0] <= entry[1]:
            interval[0] = entry[0]
            set_pass = True

        if entry[0] <= interval[1] <= entry[1]:
            interval[1] = entry[1]
            set_pass = True

        if interval[0] < entry[0] and entry[1] < interval[1]:
            set_pass = True

        if not set_pass:
            keep.append(itr)

    new_schedule = []

    # append the interval to the new schedule
    set_insert = False
    for i in keep:
        entry = schedule[i]

        if entry[0] > interval[1] and not set_insert:
            new_schedule.append(interval)
            set_insert = True

            new_schedule.append(entry)
            continue

        new_schedule.append(entry)

    if not set_insert:
        new_schedule.append(interval)
        set_insert = True

    return new_schedule


# number of intervals that overlap another interval
def overlap(intervals: list[list[int]]) -> int:
    max_total = 0
    for e in intervals:
        total = [0, 0]
        for e2 in intervals:
            if e is not e2:
                if e2[0] <= e[0] < e2[1]:
                    total[0] += 1
                if e2[0] < e[1] <= e2[1]:
                    total[1] += 1
        if max(total) > max_total:
            max_total = max(total)

    return max_total


# a more succinct idea
def min_employees(intervals: list[list[int]]) -> int:
    return overlap(intervals) + 1


# testing procedure
def histo_overlap(intervals: list[list[int]]) -> int:
    histo = {}

    for e in intervals:
        for i in range(e[0], e[1]):
            count = histo.get(i, 0)
            histo[i] = count + 1

    return max(list(histo.values()))

