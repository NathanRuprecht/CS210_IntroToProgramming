# CS 210 - Introduction to Programming - Fall 2014
#
# Author: Dr. Randy Bower
#
# Documentation Statement: None.
#

""" This program demonstrates use of the cgi.FieldStorage object
    to retrieve parameters passed in the URL.
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
# 5. In a web browser, open http://localhost:8000/cgi-bin/hello.py
#    To see the values of various parameters, try the following URLs:
#      http://localhost:8000/cgi-bin/hello.py?name=Fred
#      http://localhost:8000/cgi-bin/hello.py?name=Fred&size=64
#      http://localhost:8000/cgi-bin/hello.py?name=Fred&size=64&yadda=Elaine

from datetime import datetime
import cgi


def main():
    # Get the parameters from the URL.  NOTE: If this program is executed from a
    # Python IDE instead of through a web server, the FieldStorage object will be
    # empty and the prev and next variables will be the default value "Nobody".
    fs = cgi.FieldStorage()

    # Pass the entire FieldStorage object and use it to create HTML showing its contents.
    print( build_html_string( fs ) )


def build_html_string( fs ):
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
    html += '  <h2 style="text-align: center;">CS 210 - Programming Exercise 2 - Fall 2014</h2>\n'
    html += '  <p style="text-align: center;">Page created on: ' + str( datetime.now() ) + '</p>\n'

    # This two-column table shows each of the keys and associated values.
    # The following six lines begin the table and create the header row.
    html += '  <br /><br />\n'
    html += '  <table style="width: 67%; margin: 0 auto;">\n'
    html += '    <tr>\n'
    html += '      <td style="text-align: center; border-bottom: medium double #000000;">Key</td>\n'
    html += '      <td style="text-align: center; border-bottom: medium double #000000;">Value</td>\n'
    html += '    </tr>\n'

    # Loop through a list of expected keys and create a row in the table for each key/value pair.
    for key in [ "name", "size", "blah", "yadda" ]:
        # Get the value associated with the key; if it's not found, default to "Key not found."
        value = fs.getvalue( key, "Key not found." )
        html += '    <tr>\n'
        html += '      <td style="text-align: center;">' + key + '</td>\n'
        html += '      <td style="text-align: center;">' + value + '</td>\n'
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
