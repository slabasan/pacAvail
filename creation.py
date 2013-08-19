# . any char
# \w word char
# \d digit
# \s whitespace
# \S nonWhitespace
# + 1 or more
# * 0 or more
# re.findall(r'\d\d\d', string)

def createHTML(): 

  #TODO: (1) parse file and save course info for a given ROOM to a dictionary or *other* solution (use cleanedClasses.txt)
  #   	 (2) calculate* duration of the class given the time string units of 5 minutes therefore 12 units = 1 hour
  #      (3) suggest to use a *programming* class to interface with (i,j) in a dictionary in line 49
  #      (3+) i=0 refers to time of day with 0=8am 1=8:05am ...     and j=day of week -> j=1 MONDAY j=2 TUESDAY ...
  
  time =480
  col_rowspan = [0,0,0,0,0,0]
  dic = {(0,1):0, (0,3):0, (0,5):0}   								#(X,X)=KEY   :# = the value 
																	#ie) (0,1):0 -> (0,1) is the key *think* apples and 0 is the
																	#index in className, classTime etc to look for that course's info
  className = ["Circuits"]
  classTime = ["8am to 9:50am"]
  classProf = ["Dr. Ross"]
  classRoom = ["CTC 115"]
  classDura = [11]
  
																	
  fw = open("python_html.html",'w')
  fw.write("<!DOCTYPE html PUBLIC \"-//W3C//DTD HTML 4.01 Transitional//EN\" \"http://www.w3.org/TR/1999/REC-html401-19991224/loose.dtd\">")
  fw.write("\n")
  fw.write("<html>")
  fw.write("<head> <link rel=\"stylesheet\" href=\"tableStyle.css\"> </head>")
  fw.write("<body>")
  fw.write("<table>")
  fw.write("\n")
  fw.write("<tr><th>&nbsp;</th><th>&nbsp;&nbsp;&nbsp;Monday&nbsp;&nbsp;&nbsp;</th><th>&nbsp;&nbsp;&nbsp;Tuesday&nbsp;&nbsp;&nbsp;</th><th>&nbsp;&nbsp;&nbsp;Wednesday&nbsp;&nbsp;&nbsp;</th><th>&nbsp;&nbsp;&nbsp;Thursday&nbsp;&nbsp;&nbsp;</th><th>&nbsp;&nbsp;&nbsp;Friday&nbsp;&nbsp;&nbsp;</th></tr>")

  for i in range(24):  												#i holds the values 0-23 through loop
    fw.write("<tr>")
    fw.write("\n")
    for j in range(6):
      if col_rowspan[j] == 0:	  									#if this happens there could be a need to start a class or time
        temp = (480+(i*10))%60
        if j == 0 and temp == 0:									#in the time column and seeing if on a whole hour
          fw.write("<td valign = \"top\" rowspan=\"6\" class=\"emphasis\">")
          fw.write(str((480+(i*10))/60))
          fw.write("</td>")
          fw.write("\n")
          col_rowspan[0]=5
        else:
          if (i,j) in dic: 											#classes exists at this time so print it and span it
            fw.write("<td valign=\"top\" class=\"emphasis\"")
            fw.write("rowspan =\"")
            fw.write(str(classDura[dic[(i,j)]]))
            col_rowspan[j]=classDura[dic[(i,j)]]					#update our col_rowspan
            fw.write("\">")
            fw.write(str(className[dic[(i,j)]]) + "<br>")
            fw.write(str(classTime[dic[(i,j)]]) + "<br>")			
            fw.write(str(classProf[dic[(i,j)]]) + "<br>")
            fw.write(str(classRoom[dic[(i,j)]]) + "<br>")                         
            fw.write("</td>")
          else:														#class does not exist at this time so simply print empty cell and decrement col_rowspan
            fw.write("<td>&nbsp</td>")
      else: 
        col_rowspan[j]=col_rowspan[j]-1	  
    fw.write("</tr>")
  fw.write("</table></body></html>")		  
  fw.close()
  
if __name__ == "__main__": 
  createHTML()
  
  
  
  
  
  
  