class MyIter:
    def __init__(self, end, start=0, step=1):
        self.__start = start
        self.__end = end
        self.__step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.__start + self.__step >= self.__end:
            raise StopIteration("stop interation under my iter")
        self.__start += self.__step
        return self.__start

if __name__ == '__main__':
    for i in MyIter(5):
        print(i)