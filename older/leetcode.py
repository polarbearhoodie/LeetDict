import math


def two_sum(nums, target):
    max_len = len(nums)

    for i in range(max_len):
        for j in range(i, max_len):
            if nums[i] + nums[j] == target:
                return [i, j]

    return [0, 0]


# best implementation
def two_sum_2(nums, target):
    maps = {}
    index = 0
    for entry in nums:
        maps[entry] = index
        pair = target - entry

        if maps.get(pair) is not None:
            return [index, maps[pair]]

        index += 1

    return [-1, -1]


# access practice:
def nums_nums(nums):
    ret = []
    for entry in nums:
        ret.append(nums[entry])

    return ret


def false_coins(nums, target):
    remain = target
    count = 0
    for x in nums:
        remain = remain % x
        count += math.floor(remain / x)

    if remain == 0:
        return count
    else:
        return -1


def water_volume(height: list[int]) -> int:
    # two pointer
    n = len(height)
    p1 = 0
    p2 = n - 1

    max_volume = 0
    for i in range(n):
        if p1 >= p2:
            break

        if height[p1] != height[p2]:
            if height[p1] > height[p2]:
                p2 -= 1
            else:
                p1 += 1
        else:
            p1 += 1
            p2 -= 1

        distance = p2 - p1
        volume = distance * min(height[p1], height[p2])

        if volume > max_volume:
            max_volume = volume

    return max_volume


def insert_merge(intervals: list[list[int]], section: list[int]) -> list[list[int]]:
    a = section[0]
    b = section[1]
    last_itr = 0

    # remove overlaps
    for itr, entry in enumerate(intervals):
        if b < entry[0]:
            last_itr = itr

        if entry[0] > a and entry[1] < b:
            intervals[itr] = -1
            last_itr = itr

    intervals = [x for x in intervals if x != -1]

    # merge intervals
    for itr, entry in enumerate(intervals):

        # merge right
        if entry[0] <= a <= entry[1]:
            a = entry[0]
            last_itr = itr
            intervals.remove(entry)

        # merge left
        if entry[0] <= b <= entry[1]:
            b = entry[1]
            last_itr = itr
            intervals.remove(entry)
            break

    # insert
    intervals.insert(last_itr, [a, b])

    return intervals


def merge(intervals: list[list[int]], section: list[int]) -> list[list[int]]:
    a = section[0]
    b = section[1]

    for itr in range(len(intervals)):
        entry = intervals[itr]

        # merge left
        if entry[0] <= a <= entry[1]:
            a = entry[0]
            intervals[itr] = [-1, -1]

        # remove overlaps
        if a < entry[0] and entry[1] < b:
            intervals[itr] = [-1, -1]

        # merge right
        if entry[0] <= b <= entry[1]:
            b = entry[1]
            intervals[itr] = [-1, -1]

        if entry[1] > b:
            break

    intervals.insert(itr, [a, b])

    return [x for x in intervals if x != [-1, -1]]