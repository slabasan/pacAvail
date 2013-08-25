import csv
#import creation
import mkDict

#--- make list of unique professors & rooms
my_profs=[]
my_rooms=[]
with open('cleanedClasses.txt','rb') as csv_file:
	csv_reader=csv.reader(csv_file, delimiter='\t')
	my_profs=[row[19][:-4] for row in csv_reader]
with open('cleanedClasses.txt','rb') as csv_file:
	csv_reader=csv.reader(csv_file, delimiter='\t')
	my_rooms=[row[21] for row in csv_reader]
csv_file.close()
newProfs=list(set(my_profs))
newRooms=list(set(my_rooms))
for prof in newProfs:
	mkDict.createDict(1,"prof")
#print newRooms
#print len(newProfs)
#print len(newRooms)

#creation.createIndexPage()
