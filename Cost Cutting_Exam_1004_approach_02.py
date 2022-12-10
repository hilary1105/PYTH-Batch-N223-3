test_list1 = [1500, 1200, 1800]
# printing list
print("The original list : " + str(test_list1))
# Median of list
# Using loop + "~" operator
test_list1.sort()
mid = len(test_list1) // 2
res = (test_list1[mid] + test_list1[~mid]) / 2
# Printing result
print("Case 3: " + str (res))

