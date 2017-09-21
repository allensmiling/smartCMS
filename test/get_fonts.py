#!/usr/bin/env python3.6

from fontTools.ttLib import TTFont
import xml.etree.cElementTree as ET


#f = TTFont('fontawesome-webfont.woff2')
#f.saveXML('fonts.xml')
#f.close()

t = ET.parse('fonts.xml')
d = {}

for i in t.findall('map'):
    d[i.get('code')] = i.get('name')

for a,b in d.items():
    a = a[2:]
    print(".uk-icon-%s:before {content:'\%s';}"%(a,a))
