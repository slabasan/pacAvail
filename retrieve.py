#this function gets rid of all the lines that are column headings and my ID at the top of the orignal .txt file RUN FIRST
#outputs cleanedClasses.txt
def newFile(): 
  f = open('springClasses.txt','r')
  fw = open('cleaned1Classes.txt','w')
  for lines in f: 
    #print lines[:2]
    #print "\n"
    if lines[:3] == "SR\t" or lines[:2] == "C\t" or lines[:3] =="NR\t": 
      fw.write(lines)
      #print ("yes")
  fw.close()
  f.close()  
     
#this function gets rid of the columns that don't matter to us, leaves only the necessary info we will print writes TO necessaryClasses.txt
def readToVariables(): 
  f = open('cleaned1Classes.txt','r')
  fw = open('necessaryClasses.txt','w')
  for lines in f: 
    lInfo=lines.split("\t")
    fw.write(lInfo[7])
    fw.write("\t")
    fw.write(lInfo[8])
    fw.write("\t")
    fw.write(lInfo[9])
    fw.write("\t")
    fw.write(lInfo[19])
    fw.write("\t")
    fw.write(lInfo[21])
    fw.write("\t")
    fw.write(lInfo[22])
  fw.close()
  f.close()
	 
        
if __name__ == "__main__": 
  readToVariables()
  
  
# . any char
# \w word char
# \d digit
# \s whitespace
# \S nonWhitespace
# + 1 or more
# * 0 or more
# re.findall(r'\d\d\d', string)



#this function will not be used, but will remain here for reference of REGEX
def read():
  import re 
  lResults = []
  f = open('springClasses.txt','r')
  fw = open('outputClasses.txt','w')
  i=0
  for lines in f:
    i=i+1
    print i
    mMatch = re.search('.+\t.+\t.+\t.+\t.+\t.+\t.+\t(.+)\t(.+)\t(.+)\t.+\t.+\t.+\t.+\t.+\t.+\t.+\t.+\t.+\t(.+)\t.+\t(.+)\t.+',lines)
    if mMatch:
      lResults.append(mMatch.group)
      print mMatch.group
  fw.write(lResults)
  fw.close()
  f.close() 
   
