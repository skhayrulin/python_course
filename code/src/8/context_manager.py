def main(file_name):
    with open(file_name, 'r') as f:
        print(f.read())

if __name__ == '__main__':
    main(input("Put name of file: "))