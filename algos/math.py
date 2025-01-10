from typing import Sequence, Tuple


def two_sum(num1: float, num2: float) -> Tuple[float, float]:
    # 2Sum
    rounded_sum = num1 + num2
    rounded_num1 = rounded_sum - num2
    rounded_num2 = rounded_sum - num1
    err1 = num1 - rounded_num1
    err2 = num2 - rounded_num2
    err = err1 + err2
    return (rounded_sum, err)


def fast_two_sum(num1: float, num2: float) -> Tuple[float, float]:
    # Fast2Sum
    rounded_sum = num1 + num2
    diff = rounded_sum - num1
    err = num2 - diff
    return (rounded_sum, err)


def compensated_sum(nums: Sequence[float]) -> float:
    # Kahan summation algorithm
    res = 0.0
    diff = 0.0
    for num in nums:
        summand = num - diff
        new_res = res + summand
        diff = (new_res - res) - summand
        res = new_res
    return res
