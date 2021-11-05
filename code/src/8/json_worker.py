import json

def read_json(file_name): 
    f = open(file_name, "r")
    obj = json.load(f)
    print(obj)

def write_json(file_name, obj): 
    f = open(file_name, "w")
    json.dump(obj, f)

def main():
    write_json(input("push file name here: "), 
        {
            'propInt': 1,
            'propFloat': 3.14,
            'propBool': True,
            'propString': "Hello JSON",
            'propDict': {
                'key1': 1,
                'key1': 2,
            },
            'propList': [1,2,3]
        }
    )
    read_json(input("push file name here: "))

if __name__ == '__main__':
    main()