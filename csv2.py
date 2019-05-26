import os
import csv

def scrape():
    newlist=[]
    iterator = 1
    testlist = [1, 2, 3, "a", "b", "c", "z", "y", "x"]
    with open('test00.csv', 'w', newline='') as csvfile:
        newwriter = csv.writer(csvfile, delimiter=',')
        for index in range(len(testlist)):
            if iterator % 3 != 0:
                newlist.append(testlist[index])
                iterator += 1
            else:
                newlist.append(testlist[index])
                iterator += 1
                print(newlist)
                newwriter.writerow(newlist)
                newlist=[]
            
    from subprocess import Popen
    p = Popen('test00.csv', shell=True)
scrape()

