import glob
import os
import re
from os.path import basename

#SUPER DIRTY RESULT PRINTER FROM SCRAPING, RAN OUT OF TIME

files = glob.glob(os.getcwd() + '/scraped/*.html')



#shitty regex for:
#<a href="/food/calories/304002151">Zwiebel</a>

pattern = re.compile("calories\/\d+?.+?\<\/a")

broken_links = []

for fname in files:
    try:
        
        print basename(fname).replace(".html",""), " - ",
        
        first_result = re.findall(pattern, open(fname).read())[0]
        #print first_result
        first_result = re.findall("\>.+\<", first_result)[0].replace("<","").replace(">","")
        print first_result
        
        
    except Exception as g:
        print "BROKEN: ", fname
        broken_links.append(fname)
        #os.remove(fname)

print ""
print "NO MATCHES / BROKEN LINKS"
print "-----"

for i in broken_links:
    print i

