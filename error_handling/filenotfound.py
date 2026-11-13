try:
    f = open("notreal.py","r")
except FileNotFoundError as e:
    print(f"Error: The file {e.filename} was not found. Please check the filename and path.")

f.close()
