#!/usr/bin/python3

"""Prime number module"""


def isWinner(x, nums):
    """Prime number winner"""
    if x <= 0 or not nums:
        return None

    max_num = max(nums)

    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(max_num ** 0.5) + 1):
        if is_prime[i]:
            for multiple in range(i * i, max_num + 1, i):
                is_prime[multiple] = False

    def simulate_game(n):
        remaining_numbers = [i for i in range(1, n + 1)]
        maria_turn = True

        while True:
            current_prime = None
            for num in remaining_numbers:
                if is_prime[num]:
                    current_prime = num
                    break

            if current_prime is None:
                return "Ben" if maria_turn else "Maria"

            remaining_numbers = [
                num for num in remaining_numbers if num % current_prime != 0]
            maria_turn = not maria_turn

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = simulate_game(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
