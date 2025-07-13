n = int(input("Enter the required numbers: "))
nums = []
i = 0
while i < n:
    nums.append(int(input("Enter the number: ")))
    i += 1
max_num = nums[0]
min_num = nums[0]
i = 1
while i < len(nums):
    if nums[i] > max_num:
        max_num = nums[i]
    if nums[i] < min_num:
        min_num = nums[i]
    i += 1
print("\nWithout using built-in functions")
print("Max:", max_num)
print("Min:", min_num)
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] > nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
print("Sorted:", nums)
unique = []
for num in nums:
    if num not in unique:
        unique.append(num)
print("No Duplicates:", unique)
print("\nBy using the built-in functions")
a = set(nums)
m = max(nums)
mi = min(nums)
s = sorted(nums)
print("Max:", m)
print("Min:", mi)
print("Sorted numbers:", s)
print("Without Duplicates:", list(a))
