def main(file_name):
    read_all_data(file_name)
    read_line_by_line(file_name)
    
def read_all_data(file_name):
    f = open(file_name, "r")
    # possible bad idea case it will read all data to memory
    data = f.read()
    print(f"data is {data=}")
    f.close()

def read_line_by_line(file_name):
    f = open(file_name, "r")
    data = []
    for line in f.readlines():
        data.append(line)
    print(f"data is {data=}")
    f.close()

if __name__ == '__main__':
    main(file_name=input("input file name: "))
