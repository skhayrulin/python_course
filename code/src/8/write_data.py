def main(file_name):
    #write_all_data(file_name)
    write_line_by_line(file_name)

def write_all_data(file_name):
    f = open(file_name, "w")
    data = ['Some data', 'Some other data']
    f.write(str(data))
    f.close()

def write_line_by_line(file_name):
    f = open(file_name, "w")
    data = ['Some data', 'Some other data']
    
    f.writelines(data)
    f.close()

if __name__ == '__main__':
    main(file_name=input("input file name: "))
