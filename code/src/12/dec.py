import datetime

def prof(func):
    def foo(*argc, **kwargs):
        start_time = datetime.datetime.now()
        result = func(*argc, **kwargs)
        print(f"working time is {datetime.datetime.now() - start_time}")
        return result
    return foo

@prof
def is_prime(num):
    for i in range(2, int(num ** 0.5)):
        if num % i == 0:
            return False
        
    return True

if __name__ == '__main__':
    while True:
        num = input("input number: ")
        if num == 'exit':
            break
        else:
            try:
                num = int(num)
                print(f"{num} is prime {is_prime(num)}")
            except ValueError as err:
                print("Bad value")
            