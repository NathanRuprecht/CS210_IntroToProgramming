# CS 210 - Introduction to Programming - Fall 2014
#
# Author: C2C Nathan Ruprecht
#
# Section/Instructor: T1 / Dr. Bower
#
# Documentation Statement: I received no outside help on this assignment.
#

""" Random Student Picker
    Authors: Maj David Caswell and Dr. Randy Bower, Fall 2014
    This program reads a data file that includes student names and the number
    of times they have previously been selected and then randomly selects a
    student with preference given to those who have presented fewer times.
    When a student successfully presents, the data file is updated appropriately.
    The result of the program is html that can be rendered in a web browser.
"""

# To run this program in a web browser:
# 0. Create a folder to host the web pages.
# 1. Within the folder from step 0, create a cgi-bin folder.
#    Also within the folder from step 0, create an images folder
#    with all of the image files referenced in Students.txt.
# 2. Place the files picker.py and Students.txt, in the cgi-bin folder.
# 3. Launch a command prompt and change to the folder from step 0 (not the cgi-bin folder).
# 4. Type the following command at the command prompt:
#      python -m http.server --cgi 8000
#    This launches a cgi enabled web server on port 8000.
# 5. In a web browser, open http://localhost:8000/cgi-bin/picker.py

from datetime import datetime
from os.path import dirname
import random
import cgi

# Locates the data file in the same directory as the python source file.
# The full path is necessary when running an application on a web server.
DATA_FILE = dirname( __file__ ) + "\\" + "Students0.txt"

def main():
    # Get the parameters from the URL.  NOTE: If this program is executed from a
    # Python IDE instead of through a web server, the FieldStorage object will be
    # empty and the prev and next variables will be the default value "Nobody".
    fs = cgi.FieldStorage()
    # The second parameter to each of the below calls to the getvalue method
    # is a default value if the given key is not found.
    prev = fs.getvalue( "prev", "Nobody" )
    next = fs.getvalue( "next", "Nobody" )

    # **** Insert Code Below Here ****
    infile = open(DATA_FILE, "r")
    data = infile.readlines()
    infile.close()

    fullname = []
    timespicked = []
    picture = []
    num_students = []

    for i in range(len(data)):
        num_students.append(i)
        num_students[i] = i

    if (prev != "Nobody"):
        
        for word in data:
            values = word.split(";")
            fullname.append(values[0])
            timespicked.append(values[1])
            picture.append(values[2])
            values[2].replace("\n", "")

        for i in range(len(num_students)):
            if prev == fullname[i]:
                timespicked[i] = int(timespicked[i]) + 1

        student = random.choice(num_students)

        outfile = open(DATA_FILE, "w")

        for i in range(len(num_students)):
            outfile.write(str(fullname[i]) + ";" + str(timespicked[i]) + ";" + str(picture[i]))

        outfile.close()


    elif (next != "Nobody"):
        
        for word in data:
            values = word.split(";")
            fullname.append(values[0])
            timespicked.append(values[1])
            picture.append(values[2])

        student = fullname.index(next)

    else:
        for word in data:
            values = word.split(";")
            fullname.append(values[0])
            timespicked.append(values[1])
            picture.append(values[2])

        student = random.choice(num_students)


    # **** Insert Code Above Here ****

    # Create the HTML to show the selected student.
    print( build_html_string( data, student, fullname, num_students, timespicked, picture ) )


def build_html_string( data, student, fullname, num_students, timespicked, picture ):
    """Creates a string with the HTML to be rendered by the browser."""

    html  = '\n'  # For some unknown reason, the string MUST begin with a newline.

    # The first part of the html is standard and always the same; do not change the following seven lines.
    html += '<html>\n'
    html += '<head>\n'
    html += '  <title>Picker</title>\n'
    html += '  <meta http-equiv="Content-Type" content="text/html;charset=utf-8" />\n'
    html += '</head>\n'
    html += '<body>\n'
    html += '  <div style="width: 67%; margin: 0 auto;">\n'

    # This single-column table shows the name and image of the student picked as well as the current date/time.
    # You will need to change second and third lines of code below to display the selected student.
    html += '  <table style="width: 100%; margin: 0 auto;">\n'
    html += '    <tr><td style="text-align: center;"><h1>Next up: {0}</h1></td></tr>\n'.format( fullname[student] )
    html += '    <tr><td style="text-align: center;"><img src="../images/{0}" alt="{1}" height="256" /></td></tr>\n'.format( picture[student], fullname[student] )
    html += '    <tr><td style="text-align: center;">Picked on: {0}</td></tr>\n'.format( str( datetime.now() ) )
    html += '  </table>\n'

    # This two-column table shows the smile and frown faces to be used to indicate a student successfully presented.
    # You will need to change the name passed as the 'prev' parameter in the hyperlink on the smiley face.
    html += '  <br /><br />\n'
    html += '  <table style="width: 80%; margin: 0 auto;">\n'
    html += '    <tr>\n'
    html += '      <td style="width: 10%;"></td>\n'
    html += '      <td style="width: 60%;"><a href="picker.py?prev={0}"><img src="../images/smile.jpg" alt="Success!" height="64" /></a></td>\n'.format( fullname[student] )
    html += '      <td style="text-align: center;"><a href="picker.py"><img src="../images/frown.jpg" alt="Fail..." height="64" /></a></td>\n'
    html += '    </tr>\n'
    html += '  </table>\n'

    # This three-column table shows a thumbnail image, name, and number of times picked for each student.
    # The next seven lines begin the table and create the heading row; these seven lines should not be changed.
    html += '  <br /><br />\n'
    html += '  <table style="width: 80%; margin: 0 auto;">\n'
    html += '    <tr>\n'
    html += '      <td></td>\n'
    html += '      <td style="width: 60%; border-bottom: medium double #000000;">Name</td>\n'
    html += '      <td style="text-align: center; border-bottom: medium double #000000;">Count</td>\n'
    html += '    </tr>\n'

    # The following lines of code create one row in the table for each student. This sample is
    # hard-coded with literal values, but you will need to use a loop and display all students.
    # Notice there are five lines of nearly identical html for each student.
    for i in range(len(num_students)):
        html += '    <tr>\n'
        html += '      <td style="width: 10%; text-align: right;"><img src="../images/{0}" alt="{1}" height="32" /></td>\n'.format( picture[i], fullname[i] )
        html += '      <td><a href="picker.py?next={0}">{0}</a></td>\n'.format( fullname[i] )
        html += '      <td style="text-align: center;">{0}</td>\n'.format( timespicked[i] )
        html += '    </tr>\n'

    # Finish up the closing html tags.
    html += '  </table>\n'
    html += '  </div>\n'
    html += '</body>\n'
    html += '</html>'

    # Finally return the html string where the main program will print it to be rendered by the browser.
    return html


######## Main Program ########
if __name__ == "__main__":
    main()
