import fire
from boiler import getIpAddr

if __name__ == '__main__':
    url = fire.Fire(getIpAddr)
    print(url)
