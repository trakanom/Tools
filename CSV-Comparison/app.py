import sys
import csv

def importCSV(fileName):
    with open(fileName, 'r') as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)
    return data
def exportCSV(fileName, data):
    with open(fileName, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)


def Compare(list1,list2):
    print("Original Size: ",len(list1))
    comparisons, deletions = 0,0
    for item2 in list2:
        for removalindex,item1 in enumerate(list1): #Ouch, a nested for loop. We should improve this efficiency, but that's just a nerd snipe right now.
            comparisons += 1
            if item1[0] == item2[0] and item1[2]==item2[2]:
                deletions += 1
                #remove item2 from list1 and move to next item
                list1.pop(removalindex)
                continue
        
    print(f"Operation Complete. {deletions} items deleted. {comparisons} items compared. {len(list1)} items remaining.")
    return list1




Originals = importCSV(sys.argv[1])
Dupes = importCSV(sys.argv[2])
print("Original Size: ",len(Originals))
print("Dupe Size: ",len(Dupes))
Difference = Compare(Originals,Dupes)
print("Final Size: ",len(Difference))
exportCSV("NewList.csv",Difference)
