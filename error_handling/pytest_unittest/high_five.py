def high_five(num):
    if int(num) != num:
        raise TypeError

    if num % 5 == 0:
        return True
    return False

def main():
    pass

if __name__ == "__main__":
    main()
