import random

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

def selection_sort(numbers):
    nums = numbers.copy()
    delka = len(nums)
    # serazeny = []
    for i in range(delka):
        m = i
        for j in range(i,delka):
            if nums[j] < nums[m]:
                m = j
                # serazeny.append(j)
        nums[i], nums[m] = nums[m], nums[i]
    return nums

# def selection_sort(numbers):
#     nums = numbers.copy()
#     delka = len(nums)
#     i = 1
#     for j in range(i,delka):
#         if nums[j] < nums[i]:
#             i= j
#     nums[j], nums[i] = nums[i], nums[j]
#     return nums

def bubble_sort(numbers):
    nums = numbers.copy()
    n = len(nums)
    for i in range(n-1):
        for j in range(n-1):
            if nums[j]>nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

if __name__ == "__main__":
    values = random_numbers(10)  # 10 čísel v rozsahu 0–100
    print(values)  # např. [42, 7, 91, 15, 63, 8, 57, 73, 2, 100]
    small = random_numbers(5, low=0, high=20)  # 5 čísel v rozsahu 0–20
    print(small)
    sort = selection_sort([5, 1, 4, 2, 8, 10, 20,18, 15])
    print(sort)
    sorting = selection_sort(random_numbers(10))
    print(sorting)
    numb = sorted(sorting)
    print(numb)
    bubble = bubble_sort([5, 1, 4, 2, 8])
    print(bubble)
    bubbles = bubble_sort(random_numbers(10))
    print(bubbles)