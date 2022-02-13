def fizz_buzz(n: int, m: int):
    result = list(map(lambda x: "FizzBuzz" if x % 15 == 0
                                else "Fizz" if x % 3 == 0
                                else "Buzz" if x % 5 == 0
                                else x,
                                range(n, m + 1)))
    print(*result, sep='\n')


n, m = input(), input()
fizz_buzz(int(n), int(m))
