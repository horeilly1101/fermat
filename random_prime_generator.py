from primality_testing import is_prime
import random


# def create_sieve(limit):
#     nums: list = [i for i in range(2, limit)]
#     for num in nums:
#         if num is None:
#             continue
#
#         for i in range(2, limit // num):
#             nums[num * i - 2] = None
#     return [i for i in nums if i is not None]


class RandomPrimeGenerator:
    def __init__(self, max_value=pow(2, 500)):
        self._max_value = max_value

    def generate(self):
        prime_candidate = random.randint(0, self._max_value)
        while not is_prime(prime_candidate):
            prime_candidate += 1
        return prime_candidate


if __name__ == "__main__":
    gen = RandomPrimeGenerator()
    print(gen.generate())
