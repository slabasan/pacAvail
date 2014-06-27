import csv
import creation
import mkDict
import moveCSS
import retrieve
import sys

def main(rawClassesFile):
	# -- creates cleanedClasses.txt from plain text of InsidePacific for a given
	# -- semester
	retrieve.newFile(rawClassesFile)

	#--- make list of unique professors & rooms
	my_profs=[]
	my_rooms=[]
	with open('cleanedClasses.txt','rb') as csv_file:
		csv_reader=csv.reader(csv_file, delimiter='\t')
		my_profs=[row[19] for row in csv_reader]
	with open('cleanedClasses.txt','rb') as csv_file:
		csv_reader=csv.reader(csv_file, delimiter='\t')
		my_rooms=[row[21] for row in csv_reader]
	csv_file.close()

	newProfs=sorted(list(set(my_profs)))
	newRooms=sorted(list(set(my_rooms)))

	#--- generate individual HTML files for each professor & room w/info from dict
	#--- in htmlfiles dir 
	#--- list all HTML files in index file
	#--- move CSS files into htmlfiles dir
	a=len(newProfs)
	b=len(newRooms)

	c=a-b			#how many spaces I need to make to make the two lists equal in vertical size (HTML)
	c=c-1

	for profs in newProfs:
		if profs != "TBA":
		  tup=mkDict.createDict(1,profs)
		  creation.createHTML(tup[0],tup[1],tup[2])
		  
	for rooms in newRooms:
	  tup=mkDict.createDict(0,rooms)
	  creation.createHTML(tup[0],tup[1],tup[2])

	creation.addSpaces(c) 
	creation.createIndexPage()
	moveCSS.move()

#execute program with "python main.py"
if __name__=="__main__":
	if len(sys.argv) != 2:
		print "Usage: python main.py <Fall14Classes.txt>"
	else:
		main(sys.argv[1])
