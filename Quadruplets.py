# Store the pair of indices
class Pair:
    def __init__(self, x, y):
        self.index1 = x
        self.index2 = y


# Function to find the all the unique quadruplets
# with the elements at different indices
def GetQuadruplets(nums, target):
    # Store the sum mapped to a list of pair indices
    map = {}

    # Generate all possible pairs for the map
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            # Find the sum of pairs of elements
            sum = nums[i] + nums[j]

            # If the sum doesn't exist then update with the new pairs
            if sum not in map:
                map[sum] = [Pair(i, j)]
            # Otherwise, add the new pair of indices to the current sum
            else:
                map[sum].append(Pair(i, j))

    # Store all the Quadruplets
    ans = set()

    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            lookUp = target - (nums[i] + nums[j])

            # If the sum with value (K - sum) exists
            if lookUp in map:
                # Get the pair of indices of sum
                temp = map[lookUp]

                for pair in temp:
                    # Check if i, j, k and l are distinct or not
                    if pair.index1 != i and pair.index1 != j and pair.index2 != i and pair.index2 != j:
                        l1 = [nums[pair.index1], nums[pair.index2], nums[i], nums[j]]

                        # Sort the list to avoid duplicacy
                        l1.sort()

                        # Update the set
                        ans.add(tuple(l1))

    print(*reversed(list(ans)), sep='\n')


arr = [1, 0, -1, 0, -2, 2]
K = 0
GetQuadruplets(arr, K)

