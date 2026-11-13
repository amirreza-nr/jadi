def read_file(filename):
    file = None
    try:
        file = open(filename,"r")
        data = file.read()
    except FileNotFoundError as e:
        print(f"{filename} is not found.")
    else:
        print(f"request was done succesfully! for {file.name} ")
        print(data,end='\n')
    finally:
        if file:
            file.close()

read_file("index_error.py")
read_file("notreal.py")
