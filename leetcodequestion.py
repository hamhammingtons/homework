class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        sumof = nums1 + nums2
        sumof.sort()

        if len(sumof) % 2 == 0:
            left = len(sumof) // 2
            right = len(sumof) // 2 - 1

            return (
                sumof[left] + sumof[right]
            ) / 2.0  # why 2.0 -> so it gives us 2.5 a float, like a true num, instead of 2.000 when doing "... / 2"
        else:
            d = len(sumof) // 2
            return sumof[d]
