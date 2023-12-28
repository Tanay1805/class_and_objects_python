class DivisibleBySevenGenerator:
    def __init__(self, n):
        self.n = n

    def generate_divisible_by_seven(self):
        for i in range(self.n + 1):
            if i % 7 == 0:
                yield i


n = int(input('Enter the number:'))
divisible_by_seven_generator = DivisibleBySevenGenerator(n)

for num in divisible_by_seven_generator.generate_divisible_by_seven():
    print(num)
