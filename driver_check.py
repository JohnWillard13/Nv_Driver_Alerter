# Created by Ryan McChesney
# Created on 11/29/2022
# Simple Nvidia driver checker

import requests

#To just get the listed version
def getVersion():
    r = requests.get('https://www.nvidia.com/download/driverResults.aspx/194380/en-us/')
    print(r.text)

def main():
    getVersion()

if __name__ == '__main__':
    main()