import requests
import numpy as np
from multiprocessing import Pool

case1 = "Username is associated with a verified twitter account"
case2 = "Username has already been taken"

def plugrun(i):
    output = open(f"available.txt", "a+", encoding="utf-8")
    resp = requests.get(f"https://weheartit.com/users/validate?user%5Busername%5D={i}")
    boob = str(resp.json())
    if (boob.find(case1) == -1) and (boob.find(case2) == -1):
        print(f"{i} is available")
        output.write(f"{i}\n")
    else:
        print(f"{i} isnt available")

def main(threads, array):
    with Pool(threads) as p:
        p.map(plugrun, array)

if __name__ == "__main__":
    print("o.o")
    threads = int(input("how many threads?: "))
    array = np.array(list(dict.fromkeys(open("users.txt").read().lower().splitlines())))
    main(threads, array)
