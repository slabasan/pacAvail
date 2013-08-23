import csv

#--- make list of unique classrooms
#mylist=[]
#with open('ecpe.txt','rb') as csv_file:
#	csv_reader=csv.reader(csv_file, delimiter='\t')
#	my_list=[row[21] for row in csv_reader]
#csv_file.close()
#newList=list(set(my_list))
#print newList
#print len(newList)

#--- make variables in loop
#d={}
#for x in newList:
#   d["{0}".format(x)]="Hello"
#print d

#--- convert time to 5 min increment
def timeConvert(s):
	startH=s[0:2]
	startM=s[3:6]
	endH=s[9:11]
	endM=s[12:15]
	x=s[6:8]
	y=s[15:17]
	if s == "TBA":
		resultH=0
		resultM=0
	elif x == "am" and y == "pm" and endH != 12:
		newEndH=int(float(endH))+12
		resultH=int(float(newEndH))-int(float(startH))
		resultM=int(float(endM))-int(float(startM))
	elif x == "pm" and y == "pm" and endH < startH:
		newEndH=int(float(endH))+12
		resultH=int(float(newEndH))-int(float(startH))
		resultM=int(float(endM))-int(float(startM))
	else:
		resultH=int(float(endH))-int(float(startH))
		resultM=int(float(endM))-int(float(startM))
	if resultM < 0:
		resultM+=60
		resultH-=1
	result_hourtomin=resultH*60
	totaltime=result_hourtomin+resultM
	unitconversion=totaltime/5
	return unitconversion

def convertDay(x):
	days=list("MWF")
	for i in range(len(x)):
		if x[i] == "M":
			x[i] = 0
		elif x[i] == "T":
			x[i] = 1
		elif x[i] == "W":
			x[i] = 2
		elif x[i] == "R":
			x[i] = 3
		elif x[i] == "F":
			x[i] = 4
	return x

#--- create dictionary (...or list of dictionaries?)
# {('day(8)','time(9)'): ['course(2,3)','name(7)','prof(19)','room(21)']}
dict={}
with open('ecpe.txt','rb') as csv_file:
	csv_reader=csv.reader(csv_file, delimiter='\t')
	for row in csv_reader:
		time=timeConvert(row[9])	
		if row[8]=="MWF":
			days=list(row[8])
			newDays=convertDay(days)
			dict[newDays[0],time,row[21],row[19][:-4],row[7]]=[row[21],row[19][:-4],row[7],row[2]+" "+row[3],row[9]]
			dict[newDays[1],time,row[21],row[19][:-4],row[7]]=[row[21],row[19][:-4],row[7],row[2]+" "+row[3],row[9]]
			dict[newDays[2],time,row[21],row[19][:-4],row[7]]=[row[21],row[19][:-4],row[7],row[2]+" "+row[3],row[9]]
		#elif row[8]=="TR":
			#days=list(row[8])
			#newDays=convertDay(days)
			#dict[newDays[0],time,row[21],row[19][:-4],row[7]]=[row[21],row[19][:-4],row[7],row[2]+" "+row[3],row[9]]
			#dict[newDays[1],time,row[21],row[19][:-4],row[7]]=[row[21],row[19][:-4],row[7],row[2]+" "+row[3],row[9]]
		#elif row[8]=="MW":
			#days=list(row[8])
			#newDays=convertDay(days)
			#dict[newDays[0],time,row[21],row[19][:-4],row[7]]=[row[21],row[19][:-4],row[7],row[2]+" "+row[3],row[9]]
			#dict[newDays[1],time,row[21],row[19][:-4],row[7]]=[row[21],row[19][:-4],row[7],row[2]+" "+row[3],row[9]]
		#elif row[8]=="WF":
			#days=list(row[8])
			#newDays=convertDay(days)
			#dict[newDays[0],time,row[21],row[19][:-4],row[7]]=[row[21],row[19][:-4],row[7],row[2]+" "+row[3],row[9]]
			#dict[newDays[1],time,row[21],row[19][:-4],row[7]]=[row[21],row[19][:-4],row[7],row[2]+" "+row[3],row[9]]
		#else:
			#days=list(row[8])
			#newDays=convertDay(days)
			#dict[newDays[0],time,row[21],row[19][:-4],row[7]]=[row[21],row[19][:-4],row[7],row[2]+" "+row[3],row[9]]
print dict
print len(dict)
