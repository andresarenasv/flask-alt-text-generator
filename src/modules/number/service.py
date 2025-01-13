import random

class NumberService:
    def generate_random_number(self) -> int:
        """Generate a random number between 1 and 100"""
        return random.randint(1, 100) 