import re

from robobrowser import RoboBrowser

br = RoboBrowser()
br.open("https://connect.det.wa.edu.au/group/students/ui/my-settings/assessment-outlines")
form = br.get_form()
form['ssousername'] = 
form['password'] = 
form['acceptterms'] = 'acceptterms'

br.submit_form(form)

print(br.parsed.find('<a'))
