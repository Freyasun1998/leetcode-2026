class RandomizedSet:

    def __init__(self):

        self.nums = []
        self.val_to_index = {}

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False
        self.nums.append(val)
        self.val_to_index[val] = len(self.nums) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False
        index = self.val_to_index[val]
        last_num = self.nums[-1]
        self.nums[index] = last_num
        self.val_to_index[last_num] = index
        self.nums.pop()
        del self.val_to_index[val]
        return True
        
    def getRandom(self) -> int:
        import random
        return random.choice(self.nums)
        

def test_randomized_set() -> None:
    randomized_set = RandomizedSet()
    assert randomized_set.insert(1) == True
    assert randomized_set.insert(2) == True
    assert randomized_set.insert(2) == False
    assert randomized_set.remove(2) == True
    assert randomized_set.remove(3) == False
    assert randomized_set.getRandom() in [1, 2]