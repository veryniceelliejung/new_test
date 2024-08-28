# def new_id(name, number):
#     return f"{name}{number+1}"
#
# assert new_id("Ellie", 22) == "Ellie22", "ERROR!"

# Return a dict of each unique number in nums and its frequency in the list.

def value_counts(nums):
    counts = {}

    if nums is not None:
        for num in nums:
            # if num in counts:
            #     counts[num] += 1
            # else:
            #     counts[num] = 1
            counts[num] = 1 if num not in counts else counts[num] + 1

    return counts

nums = [6, 7, 0, 8, 0, 0, 8]
print(value_counts(nums))

assert value_counts(nums) == {0: 3, 6: 1, 7: 1, 8: 2}