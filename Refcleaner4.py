#!/usr/bin/python

import re

file = open('/Users/phae_girl/Documents/Development/Ruby/reflinks.md', 'r')
content = file.read()
file.close()

newLinks = []
newRefs = []

#Define the regex functions
def findAllLinks(allText):
	return (re.compile('\[.*?\]\[.*?\]')).findall(allText)
	
def findAllRefs(allText):
	return (re.compile('\[.*\]:.*')).findall(allText)
	
def oneLink(allLinks):
	return (re.compile('(?<=\[).*?(?=\])')).findall(allLinks)
	
def oneRef(allRefs):
	return (re.compile('(?<=\[).*(?=\])')).findall(allRefs) + (re.compile('(?<=:).*')).findall(allRefs)

#Collect the links and references in the text
allLinks = findAllLinks(content)
allRefs = findAllRefs(content)

#Build nested lists of links and references
for item in allLinks:
	newLinks.append(oneLink(item))
	
for item in allRefs:
	newRefs.append(oneRef(item))

#Associate the links with the references
for index, linkItem in enumerate(newLinks, 1):
	for jdex, refItem in enumerate(newRefs, 0): 
		if linkItem[1] == refItem[0]:
			linkItem.append(refItem[1])
			newRefs.pop(jdex)
	linkItem[1] = str(index)
	linkItem[0] = linkItem[0]
	if len(linkItem) == 2:
		linkItem.append('***A Missing Link***')
	linkItem.append(False)
	
#Testing stuff	
print 'First Break'
print '***********'
for item in newLinks:
	print item
print '\n'
print '************'
print '\n'
for item in newRefs:
	print item


#Fix the surplus references
for item in newRefs:
	item[0] = '???'
	item.append(False)

#Nuke the references, flag duplicate links, rebuild reference list
#newRefs =[]
for item in newLinks:
	for jtem in newLinks:
		if item[0] != jtem [0] and item[2] == jtem[2] and item[0] > jtem [0]:
			jtem[1] = item[1]
			jtem[3] = True
		#else:
	newRefs.append([item[1], item[2], item[3]])

#Remove the duplicate references	
for index, item in enumerate(newRefs):
	if item[2]:
		newRefs.pop(index)


			



##Renumber the reference list
#for index, item in enumerate(newRefs, 1):
#	item[0] = str(index)
#	
##Clean up the links list
#for item in newRefs:
#	for jtem in newLinks:
#		if item[1] == jtem[2]:
#			jtem[1] = item[0]
#		
##Put the new links into the content
#for item in newLinks:
#	pattern = re.compile('\[' + item[0]+ '\]\[.*?\]')
#	sub = '[' + item[0]+ '][' + item[1]+ ']'
#	content = re.sub(pattern, sub, content)
#
##Nuke the old references	
#for item in newRefs:
#	pattern = re.compile('\[.*?\]:.*')
#	sub = ''
#	content = re.sub(pattern, sub, content)
#	
##Strip the whitespace off the end and add three newlines to
##make things look pretty
#content = content.rstrip()
#content += '\n\n\n'
#	
##Add the new links back in
#for item in newRefs:
#	content += '[' + item[0] + ']: ' + item[1] + '\n' 
#	
#
#####################################################
#print '\n'
#print '************'
#print '\n'
#
#print content
#
#print '\n'
#print '************'
#print '\n'
#
#print allRefs
			
