# Input: arr1[] = {1, 3, 4, 5, 7}
#         arr2[] = {2, 3, 5, 6}
# Output: Union : {1, 2, 3, 4, 5, 6, 7}
#          Intersection : {3, 5}
#
# Input: arr1[] = {2, 5, 6}
#         arr2[] = {4, 6, 8, 10}
# Output: Union : {2, 4, 5, 6, 8, 10}
#          Intersection : {6}


def union(nums1, nums2):
    final_num1 = list(set(nums1 + nums2))
    return final_num1

def intersection(nums1, nums2):
    final_num2 = []
    for i in nums1:
        if i in nums2:
            final_num2.append(i)
    return final_num2


nums1 = [1, 3, 4, 5, 7, 10]
nums2 = [2, 3, 5, 6]
print(union(nums1, nums2))
print(intersection(nums1, nums2))
