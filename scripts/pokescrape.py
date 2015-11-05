#!/usr/bin/env python

import urllib
import urllib2
from lxml import etree
import StringIO
import re, sys, os

sys.path.append('..')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

from django.core.files import File
from django.core.files.temp import NamedTemporaryFile

result = urllib.urlopen('http://www.pokemon.com/us/pokedex/')

html = result.read()

parser = etree.HTMLParser()

tree = etree.parse(StringIO.StringIO(html), parser)

href_xpath = "/html/body/div/section/ul/li/a/@href"

filtered_html = tree.xpath(href_xpath)

print filtered_html

links = [link for link in filtered_html]

for link in links:

    print link

# for link in links:
#     state_name_pattern = "(?<=\W).*(?=.htm)"
#     state_name_search = re.search(state_name_pattern, link)
#     state_name = "%s" % state_name_search.group()
#     #use the xpath to the abbreviation to get the abbreviation
#     #use a get instead of a filter to find the state object
#     state_object = State.objects.filter(name__icontains=state_name.strip('new').strip('nc').strip('wv')).first()

#     state_page = urllib.urlopen("http://www.50states.com/%s" % link)

#     state_page_html = state_page.read()

#     tree = etree.parse(StringIO.StringIO(state_page_html), parser)

#     state_population_xpath = "//*[@id='collapseQuick-Facts']/div/ul/li[6]/div/text()"

#     state_population_string = tree.xpath(state_population_xpath)

#     #how can I clean up this string so the regex is more simple?
#     #['735,132; Rank: 47 of 50 | ', '\r\n\r\n']
#     #look at strip and replace to clean up this string
#     # print state_population_string
#     state_population_pattern = "\d+,\d+,\d+"
#     cleaned_pop_string = re.search(state_population_pattern, '%s' % state_population_string)

#     try:
#         # print cleaned_pop_string.group()
#         state_object.pop = cleaned_pop_string.group()
#         state_object.save()

#     except AttributeError, e:
#         pass

#     state_map_link_xpath = '//*[@id="collapseGovernment"]/div/ul/li[2]/div/a/@href'
#     # my_list = [1,2,3]
#     # my_list[0]

#     try:
#         state_map_link = tree.xpath(state_map_link_xpath)[0]
#     except Exception, e:
#         print e

#     state_map_page = urllib.urlopen(state_map_link)

#     state_map_page_html = state_map_page.read()

#     tree = etree.parse(StringIO.StringIO(state_map_page_html), parser)

#     image_link_xpath = '//*[@id="innerPage"]/img/@src'

#     state_map_image = tree.xpath(image_link_xpath)[0]

#     url = 'http://quickfacts.census.gov/%s' % state_map_image

#     image_response = urllib2.urlopen(url).read()

#     img_temp = NamedTemporaryFile(delete=True)

#     img_temp.write(image_response)

#     try:
#         state_object.state_map.save('map_img.gif', File(img_temp))
#     except Exception, e:
#         print e