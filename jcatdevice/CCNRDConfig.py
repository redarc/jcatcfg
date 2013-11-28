#########################################################
# File: Definition the CCNRDConfig class
# Author: Aaron yao
# Time: 2012/11/23
# Version: 1.0
# Bug duplicate add CCN_DOCTYPE_RD tag
#########################################################
import xml.etree.ElementTree as ET
import jcatdevice.Utils as UT

CCN_DOCTYPE_RD = "<!DOCTYPE ResourceData SYSTEM \"ResourceData.dtd\">"
CCN_DOCTYPE_XML = "<!DOCTYPE ResourceFactoryData SYSTEM \"ResourceFactoryData.dtd\">"

class CCNXMLConfig:
    def __init__(self):
        self.iDict = {'toolInstance':'',\
                      'TMS_GUI_NameService':'lteccn2:13579',\
                      'MSMS_ToolIdentifier':''}
        
    def SetCCN_XML(self, key, value = ''):
        #for handle BAS_CELLID input !!Excellent!!
        if isinstance(key,dict):
            items = key.items();items.sort()
            for (k,v) in items:
                print k,v
                #self.SetENGValue('relatedResource'+ str(key.keys().index(k)),v)
        else:
            self.iDict[key] = value
            
    def BuildCCNXML(self,ccnxmlFile):
        print " BuildCCNXML"
        tree = ET.parse(ccnxmlFile)
        root = tree.getroot()

        factoryIdentity = root.find("FactoryIdentity")
        factoryIdentity.set('toolInstance',self.iDict['toolInstance'])

        mSMS_ToolIdentifier = root.find(".//ConfigurationAttribute/../*[@name='MSMS_ToolIdentifier']")
        mSMS_ToolIdentifier.set('value',self.iDict['MSMS_ToolIdentifier']+':wrn.tcg')

        tms_GUI_NameService = root.find(".//ConfigurationAttribute/../*[@name='TMS_GUI_NameService']")
        tms_GUI_NameService.set('value',self.iDict['TMS_GUI_NameService'])
        
        UT.FormatXML(root)
        tree.write(ccnxmlFile, encoding='UTF-8', xml_declaration = True)
        
        fp = open(ccnxmlFile, 'r')
        for line in fp.readlines():
            if -1 == line.find(CCN_DOCTYPE_XML):
                fp.close()
                UT.File_Insert(ccnxmlFile, [2], [CCN_DOCTYPE_XML])
                break
        fp.close()
        
        #! Add function to set/get hosts file
        #fp = open('C:/Windows/System32/drivers/etc/hosts','r')
        #for line in fp.readlines():
        #    print line

class CCNRDConfig:
    def __init__(self):
        self.iDict = {'toolInstance':'',\
                      'bas_1':'',\
                      'bas_2':'',\
                      'bas_3':'',\
                      'bas_4':'',\
                      'bas_5':'',\
                      'bas_6':'',\
                      'bas_7':'',\
                      'bas_8':''}
        
    def __SetCellId(self,elem,cellId_value):
        elem.set('name','cellId')
        elem.set('baseType','STRING')
        elem.set('value',cellId_value)
        
    def SetCCN_RD(self,key,value):
        self.iDict[key] = value
        
    def BuildCCNRDTag(self,ccnrdFile):
        print "  BuildCCNRDTag"

        tree = ET.parse(ccnrdFile)
        root = tree.getroot()
        #find FactoryIdentity
        msms = root.find(".//FactoryIdentity/../*[@tool='Msms']")
        msms.set('toolInstance',self.iDict['toolInstance'])
        '''
        for i in range(1,8,1):
            index = str(i)
            bas_name = 'bas_' + index
            bas_tag_name = ".//FeatureResource/../*[@resourceId='" + bas_name +"']"
            bas_node_cellid = bas_name + '_cellid'

            bas_node = root.find(bas_tag_name)
            if self.iBasDict[bas_name].strip():
                bas_node_cellid = ET.SubElement(bas_node,'FeatureAttribute')
                self.__SetCellId(bas_node_cellid, self.iDict[bas_name])
            elif bas_node.find('FeatureAttribute') != None:
                child = bas_node.find('FeatureAttribute')
                bas_node.remove(child)
        '''        
        for (key,value) in self.iDict.items():
            if  key != 'toolInstance':
                basNode = root.find(".//FeatureResource/../*[@resourceId='" + key +"']")
                if basNode != None:
                    if self.iDict[key].strip():
                        tmpnode = ET.SubElement(basNode,'FeatureAttribute')
                        self.__SetCellId(tmpnode,self.iDict[key])
                    elif basNode.find('FeatureAttribute') != None:
                        child = basNode.find('FeatureAttribute')
                        basNode.remove(child)
                        
        UT.FormatXML(root)
        tree.write(ccnrdFile, encoding='UTF-8', xml_declaration = True)
        fp = open(ccnrdFile,'r')
        for line in fp.readlines():
            if -1 == line.find(CCN_DOCTYPE_RD):
                fp.close()
                UT.File_Insert(ccnrdFile, [2], [CCN_DOCTYPE_RD])
                break
        fp.close()
        
