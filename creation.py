#this file is used to generate the HTML/PHP necessary to complete the task

indexFileCode="<!DOCTYPE html PUBLIC \"-//W3C//DTD HTML 4.01 Transitional//EN\" \"http://www.w3.org/TR/1999/REC-html401-19991224/loose.dtd\">"+"\n"
indexFileCode+="<html>"+"\n"+"<head><link rel=\"stylesheet\" type=\"text/css\" href=\"indexstyle.css\"></head>""<body>"+"\n"+"<table>"+"\n"+"<tr>"+"\n"

profFileCode="<th>"+"Professors</th>\n<th>Rooms</th>\n<tr><td>"+"<ul>"
roomFileCode="<td>"+"<ul>"


#creates the index page or Table of Contents with the links to all the other pages created with HTML tables in them
def createIndexPage():
  global indexFileCode
  global profFileCode
  global roomFileCode
  f = open("index.html",'w')
  profFileCode+="\n"+"</ul>"
  roomFileCode+="\n"+"</ul>"
  f.write(indexFileCode)  
  f.write(profFileCode)
  f.write(roomFileCode)
  f.write("</tr>"+"\n"+"</table>"+"\n"+"</body>"+"\n"+"</html>")
  f.close()  
  
  
def alterIndex(PR,queryID):
  global profFileCode
  global roomFileCode
  if PR: 
    profFileCode+="<li>"
    profFileCode+="<a href=\""+queryID+".html\">"+queryID+"</a>"
    profFileCode+="</li>"
  elif not PR:
    roomFileCode+="<li>"  
    roomFileCode+="<a href=\""+queryID+".html\">"+queryID+"</a>"
    roomFileCode+="</li>"
  
  
def createHTML(dict,PR,queryID): 

  #TODO: (1) parse file and save course info for a given ROOM to a dictionary or *other* solution (use cleanedClasses.txt)
  #   	 (2) calculate* duration of the class given the time string units of 5 minutes therefore 12 units = 1 hour
  #      (3) suggest to use a *programming* class to interface with (i,j) in a dictionary in line 49
  #      (3+) i=0 refers to time of day with 0=8am 1=8:05am ...     and j=day of week -> j=1 MONDAY j=2 TUESDAY ...
  
  import os
  
  # time =480
  col_rowspan = [0,0,0,0,0,0]
  # dic = {(0,1):0, (0,3):0, (0,5):0}   								#(X,X)=KEY   :# = the value 
																	#ie) (0,1):0 -> (0,1) is the key *think* apples and 0 is the
																	#index in className, classTime etc to look for that course's info
  queryID_=""
  for letter in queryID:
    if letter==" ":
      queryID_+="_"
    else: 
      queryID_+=letter

  if "htmlfiles" not in os.listdir("."):
    os.mkdir("htmlfiles")

  os.chdir("htmlfiles")
  
																	
  fw = open(queryID_+".html",'w')
  fw.write("<!DOCTYPE html PUBLIC \"-//W3C//DTD HTML 4.01 Transitional//EN\" \"http://www.w3.org/TR/1999/REC-html401-19991224/loose.dtd\">")
  fw.write("\n")
  fw.write("<html>")
  fw.write("<head> <link rel=\"stylesheet\" href=\"tableStyle.css\"> </head>")
  fw.write("<body>")
  fw.write("<table width=\"80%\">")
  fw.write("\n")
  fw.write("<tr><th>&nbsp;</th><th>&nbsp;&nbsp;&nbsp;Monday&nbsp;&nbsp;&nbsp;</th><th>&nbsp;&nbsp;&nbsp;Tuesday&nbsp;&nbsp;&nbsp;</th><th>&nbsp;&nbsp;&nbsp;Wednesday&nbsp;&nbsp;&nbsp;</th><th>&nbsp;&nbsp;&nbsp;Thursday&nbsp;&nbsp;&nbsp;</th><th>&nbsp;&nbsp;&nbsp;Friday&nbsp;&nbsp;&nbsp;</th></tr>")

  for i in range(168):  											
    fw.write("<tr>")
    fw.write("\n")
    for j in range(6):
      if col_rowspan[j] == 0:	  									#if this happens there could be a need to start a class or time
        temp = (480+(i*5))%60
        if j == 0 and temp == 0:									#in the time column and seeing if on a whole hour
          fw.write("<td valign = \"top\" rowspan=\"12\" class=\"emphasis\">")
          if (((480+(i*5))/60)<12):
            fw.write("<br><br>")
            fw.write(str((480+(i*5))/60))
            fw.write("am")
          elif (((480+(i*5))/60)>12):
            fw.write("<br><br>")
            fw.write(str(((480+(i*5))/60)-12))
            fw.write("pm")
          else:
            fw.write("<br><br>")		  
            fw.write(str((480+(i*5))/60))
            fw.write("pm")
          fw.write("</td>")
          fw.write("\n")
          col_rowspan[0]=11
        else:
          if (i,j) in dict: 													#classes exists at this time so print it and span it
            fw.write("<td valign=\"top\" class=\"emphasis\"")
            fw.write("rowspan =\"")
            fw.write(str(dict[(i,j)][0]))										#class duration in 5 minute increments
            col_rowspan[j]=dict[(i,j)][0]										#update our col_rowspan
            fw.write("\">")
            fw.write("<br><br>")
            fw.write("<b>" + str(dict[(i,j)][3][:25])+ "</b>" + "<br><br><br>")						#class name limit to 24 characters long
            fw.write(str(dict[(i,j)][5]) + "<br><br><br>")						#class time
            fw.write(str(dict[(i,j)][2]) + "<br><br><br>")						#class professor
            fw.write(str(dict[(i,j)][1]) + "<br><br><br>")           			#class room location 
            fw.write(str(dict[(i,j)][7]))			
            fw.write("</td>")
          else:																	#class does not exist at this time so simply print empty cell and decrement col_rowspan
            fw.write("<td>&nbsp</td>")
      else: 
        col_rowspan[j]=col_rowspan[j]-1	  
    fw.write("</tr>")
  fw.write("</table></body></html>")		  
  fw.close()
  os.chdir("..")
  
if __name__ == "__main__": 
  createHTML()
  
  
  
  
  
  
  