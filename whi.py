import requests
import numpy as np
from multiprocessing import Pool

def plugrun(i):
    output = open(f"available.txt", "a+", encoding="utf-8")
    resp = requests.get(f"https://weheartit.com/users/validate?user%5Busername%5D={i}")
    try:
        resp.json()["errors"]["username"]
        print(f"{i} not available")
    except:
        output.write(f"{i}\n")
        print(f"{i} available")

    
def main(threads, array):
    with Pool(threads) as p:
        p.map(plugrun, array)

if __name__ == "__main__":
    print("o.o")
    threads = int(input("how many threads?: "))
    array = np.array(list(dict.fromkeys(open("users.txt").read().lower().splitlines())))
    main(threads, array)
