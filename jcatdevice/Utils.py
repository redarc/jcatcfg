#########################################################
# File: Definition the AeroflexConfig class
# Author: Aaron yao
# Time: 2012/11/23
# Version: 1.1
# Log:
# 27/11/2012 Add funtion findelem,getelem,iselem_exist
# to solve duplicate create same node Bug
#########################################################
import os
import fileinput
import xml.etree.ElementTree as ET

# public function
def SetFeatureAttrib(element,name,value,basetype='STRING'):
    element.set('name',name)
    element.set('baseType',basetype)
    element.set('value',value)
    
# this function has discarded
'''
def SetFeatureResource(element,resourceId,interface='SshCommandSession',\
                       featureModel='OperationAndMaintenance',version='1.1',\
                       maxNumberOfAllocations='50',typeOfAllocation='MULTI'):
    element.set('resourceId',resourceId)
    element.set('interface',interface)
    element.set('featureModel',featureModel)
    element.set('version',version)
    element.set('maxNumberOfAllocations',maxNumberOfAllocations)
    element.set('typeOfAllocation',typeOfAllocation)
'''    
        
def findelem(root,tagname, valuename, value):
    searchwords = ".//" + tagname + "/../*[@" + valuename + "='" + value + "']"
    # For Test print "  Attemp to search " + searchwords
    return root.find(searchwords)
    
def getelem(root, tagname, valuename, value, parentNode):
    elem = findelem(root,tagname, valuename, value)
    # For Test print 'elem is None',value
    if elem == None:
        elem = ET.SubElement(parentNode, tagname)
    return elem

def iselem_exist(root,tagname,valuename,value):
    if findelem(root,tagname, valuename, value) != None:
        return True
    else:
        return False
    
# in-place prettyprint formatter    
def FormatXML(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            FormatXML(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i
            
def File_Insert(fname,linenos=[],strings=[]):
    """
    Insert several strings to lines with linenos repectively.
 
    The elements in linenos must be in increasing order and len(strings)
    must be equal to or less than len(linenos).
 
    The extra lines ( if len(linenos)> len(strings)) will be inserted
    with blank line.
    """
    if os.path.exists(fname):
        lineno = 0
        i = 0
        for line in fileinput.input(fname,inplace=1):
            # inplace must be set to 1
            # it will redirect stdout to the input file
            lineno += 1
            line = line.strip()
            if i<len(linenos) and linenos[i]==lineno:
                if i>=len(strings):
                    print "\n",line
                else:
                    print strings[i]
                    print line
                i += 1
            else:
                print line
