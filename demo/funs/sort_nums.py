data = ["10", "1", "100", "2", "45"]

nums = map(int, data)  # convert each element to int

for v in sorted(nums):
    print(v)
