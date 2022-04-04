from math import sqrt

def main():
    dic = {i:sqrt(i) for i in range(1,1001)}
    print(dic)
if __name__ == '__main__':
    main()