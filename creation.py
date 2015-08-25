"""
12/1/2013
Module creates all of the html and css for 
index page.  Also creates all html for daughter pages.
CSS for daughter pages must be manually copied from last iteration.
"""

import os

indexFileCode="<!DOCTYPE html PUBLIC \"-//W3C//DTD HTML 4.01 Transitional//EN\"  \
\"http://www.w3.org/TR/1999/REC-html401-19991224/loose.dtd\">"+"\n"

#indexFileCode+="<html>"+"\n"+"<head><link rel=\"stylesheet\" type=\"text/css\" href=\"indexstyle.css\"></head>""<body>"+"<h1>University of the Pacific</h1><br><h2>Semester: Fall 2015</h2><br><h3>Click any of the following links to see a five-day schedule of courses for a given classroom or professor on Pacific's campus.<br><br>Feel free to contact Stephanie Labasan at s_labasan{at}u.pacific.edu for questions, comments, or suggestions.</h3><br>"+"\n"+"<table>"+"\n"+"<tr>"+"\n"

#NOTE the \ escapes the newline character (ENTER) which allows for a longer string
indexFileCode+="<html><head><link \
href=\'http://fonts.googleapis.com/css?family=Belleza\' rel=\'stylesheet\' \
type=\'text/css\'> <link \
href=\'http://fonts.googleapis.com/css?family=Signika+Negative\' rel=\'stylesheet\' \
type=\'text/css\'> <style> body { background:radial-gradient(#CF7600,#f4EFDD); } \
#toplevelbody { position: relative; height: auto; width: 900px; margin-left: \
auto; margin-right: auto; padding-left: 4px; padding-right: 4px; padding-top: \
4px; padding-bottom: 4px; }  margin-top: 0px; padding-top: 0px; } #header { \
float: right; width: 706px; background-color: \#FFFFFF; } h1 { height: 100%; font-size: 64px; width: 672px; float: right; \
font-family:'Belleza'; padding-top: 13px; }   .col1{ width: 450px; float: \
right; background-color: #FFFFFF;       opacity: .6; font-family: 'Signika \
Negative'; } .col2{ width: 450px; float: right; background-color: #FFFFFF; \
opacity: .6; font-family: 'Signika Negative'; } .text1 { text-align: left; \
padding-right: 1cm; padding-left: .5cm; } .text2 { text-align: left; \
padding-left: 1cm; padding-right: .5cm; } #floated { float: right; opacity: .5; \
margin-bottom: 5px; background-color: #FFFFFF; margin-top: 4px; margin-left: \
34px; } #enablemargin { position: relative; background-color: #FFFFFF; opacity: \
.6; height: 190px; } #instructions { clear: both; background-color: #FFFFFF; \
opacity: .6; margin-top: 0px; margin-bottom: 0px; padding-left: 1cm; \
padding-right: 1cm; position: relative; top: -19px; } h3 { text-align: center; \
font-family: 'Signika Negative'; } #skootup { position: relative; top: -37px; } \
#unique { position: relative; top: -40px; float: right; width: 10px; } </style> \
</head> <body> <div id=\"toplevelbody\"> <div id = \"enablemargin\"> <div \
id=\"header\"> <h1>Fall 2015 Schedule</h1> </div> <div id = \"unique\"> \
<p>&nbsp;</p></div> <img id=\"floated\" src=\"pacific.gif\" \
width=\"180\" height=\"180\"> </div>            <div id=\"instructions\"> \
<h3>Click on the room or professor to see their respective 5-day schedule</h3> </div> <div id=\"skootup\">"






profFileCode="<b>"+"Professors</b>\n"
roomFileCode="<b>Rooms</b>\n"


#creates the index page or Table of Contents with the links to all the other pages created with HTML tables in them
#puts this file in the "htmlfiles" folder
def createIndexPage():
  """
  12/1/2013 
  Function gets called after calling alterIndex() 
  repeatedly to populate lists for professor 
  and room information.  Creates the table 
  of contents (index.html) in a local folder named
  "htmlfiles"
  """  
  global indexFileCode	  						#constant during run-time defined above
  global profFileCode 							#populated by calling alterIndex()
  global roomFileCode 							#populated by calling alterIndex()
  
  if "htmlfiles" not in os.listdir("."):
    os.mkdir("htmlfiles")

  os.chdir("htmlfiles")
  
  f = open("index.html",'w')
  
  
  f.write(indexFileCode)  					
  
  #inserted here::::::
  f.write("<div class=\"col1\">")
  f.write("<ul>")
  f.write(profFileCode) #therefore professors on the right
  f.write("</ul>") 
  f.write("</div>")
  
  f.write("<div class=\"col2\">")
  f.write("<ul>")
  f.write(roomFileCode)
  f.write("</ul>")
  f.write("</div>")
  
  f.write("</div>")								#end div skoot up
  f.write("</div>")								#end div toplevelbody
  f.write("</body>")
  f.write("</html>")
  
  f.close()  
  
  
def addSpaces(num_spaces):
  global roomFileCode
  
  for i in range(num_spaces):
    roomFileCode+="<br>"
  
def alterIndex(PR,queryID):
  """
  Populates global variables (strings) with 
  <li> ... </li> every time it is called. 
  PR is a boolean Professor = '1' 
  and queryID = name to add
  """
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
  """
  Called for every professor and room in the file.  
  Creates the seperate table-like file for that entry
  If there is a space in the name of the professor or room a "_" 
  will be substitued for it instead (portability)
  that name {with _ substituted} become the names of the 
  newly created html files
  """

  #TODO: (1) parse file and save course info for a given ROOM to a dictionary or *other* solution (use cleanedClasses.txt)
  #   	 (2) calculate* duration of the class given the time string units of 5 minutes therefore 12 units = 1 hour
  #      (3) suggest to use a *programming* class to interface with (i,j) in a dictionary in line 49
  #      (3+) i=0 refers to time of day with 0=8am 1=8:05am ...     and j=day of week -> j=1 MONDAY j=2 TUESDAY ...
  
  # time =480
  col_rowspan = [0,0,0,0,0,0,0]
  # dic = {(0,1):0, (0,3):0, (0,5):0}   							#(X,X)=KEY   :# = the value 
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
  fw.write("<table width=\"90%\">")
  fw.write("\n")
  fw.write("<tr><th>&nbsp;</th><th>&nbsp;&nbsp;&nbsp;Monday&nbsp;&nbsp;&nbsp;</th><th>&nbsp;&nbsp;&nbsp;Tuesday&nbsp;&nbsp;&nbsp;</th><th>&nbsp;&nbsp;&nbsp;Wednesday&nbsp;&nbsp;&nbsp;</th><th>&nbsp;&nbsp;&nbsp;Thursday&nbsp;&nbsp;&nbsp;</th><th>&nbsp;&nbsp;&nbsp;Friday&nbsp;&nbsp;&nbsp;</th><th class=\"ghost\">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th></tr>")

  for i in range(168):  											
    fw.write("<tr>")
    fw.write("\n")
    for j in range(7):
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
	      #classes exists at this time so print it and span it
          if (i,j) in dict: 													
            fw.write("<td valign=\"top\" class=\"emphasis\"")
            fw.write("rowspan =\"")
            fw.write(str(dict[(i,j)][0]))										#class duration in 5 minute increments
            col_rowspan[j]=dict[(i,j)][0]										#update our col_rowspan
            fw.write("\">")
            fw.write("<br><br>")
            fw.write("<b>" + str(dict[(i,j)][3][:24])+ "</b>" + "<br><br><br>")	#class name limit to 24 characters long
            fw.write(str(dict[(i,j)][4]) + "<br><br><br>")						#class time
            fw.write(str(dict[(i,j)][5]) + "<br><br><br>")						#class time
            fw.write(str(dict[(i,j)][2]) + "<br><br><br>")						#class professor
            fw.write(str(dict[(i,j)][1]) + "<br><br><br>")           			#class room location 
            fw.write(str(dict[(i,j)][7]))			
            fw.write("</td>")
		  #class does not exist at this time so simply print empty cell and decrement col_rowspan
          else:																	
            fw.write("<td>&nbsp</td>")
      else: 
        col_rowspan[j]=col_rowspan[j]-1	  
    fw.write("</tr>")
  fw.write("</table></body></html>")		  
  fw.close()
  os.chdir("..")
  alterIndex(PR,queryID_)
  
if __name__ == "__main__": 
  createHTML()
  
  
  
  
  
  

