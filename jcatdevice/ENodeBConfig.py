#########################################################
# File: Definition the ENodeBConfig class
# Author: Aaron yao
# Time: 2012/11/23
# Version: 1.2
# Log:
# 25/11/2012 Refactory for xml generate logic,use dictory
# instead
# 27/11/2012 Fix duplicate create same Nodes add
# __iselem_exist, __findelem, __getelem
#    Refactory SetENGValue mothod to adapt BAS_CELLID input
#########################################################

import xml.etree.ElementTree as ET
import jcatdevice.Utils as UT

class ENodeBConfig:
    def __init__(self):
        self.iDict = {'resourceId':'',\
                      'interface':'SshCommandSession',\
                      'featureModel':'OperationAndMaintenance',\
                      'version':'1.1',\
                      'maxNumberOfAllocations':'50',\
                      'typeOfAllocation':'MULTI',\
                      'rbsIp':'',\
                      'rbsPassword':'rbs',\
                      'rbsName':'rbs',\
                      'enbCpIp':'x.x.x.x',\
                      'rs232Ip':'10.186.135.51',\
                      'rs232Port':'4032',\
                      'defaultRouter':'x.x.x.x',\
                      'enbUpIp':'',\
                      'unixHost':'10.186.135.171',\
                      'unixPort':'22',\
                      'unixUser':'jcat',\
                      'unixPassword':'jcat123',\
                      'unixPrompt':'jcat@linux-w6kl:~> ',\
                      'defaultWorkStation':'workStation nj moshellSvr171',\
                      'relatedResource0':'',\
                      'relatedResource1':'',\
                      'HOST':'$(targethost)',\
                      'PORT':'$(targetport)',\
                      'USER':'$(targetuser)',\
                      'setPrompt':'*assword*',\
                      'sendCmd':'$(targetpassword)',\
                      'setRegExPrompt':'$(targetprompt)'}

    def SetENGValue(self, key, value = ''):
        #for handle BAS_CELLID input !!Excellent!!
        if isinstance(key,dict):
            items = key.items();items.sort()
            for (k,v) in items:
                self.SetENGValue('relatedResource'+ str(key.keys().index(k)),v)
        else:
            self.iDict[key] = value
    
    def BuildENGTag(self,remoteFile):
        print " Build New ENBTag"

        tree = ET.parse(remoteFile)
        root = tree.getroot()
        factoryIdentity = root.find('FactoryIdentity')
        eNodeB = UT.getelem(root,\
                            'FeatureResource',
                            'resourceId',\
                            self.iDict['resourceId'],\
                            factoryIdentity)
        host = UT.getelem(root,\
                          'ConfigurationAttribute',\
                          'name',\
                          'HOST',\
                          eNodeB)
        port = UT.getelem(root,\
                          'ConfigurationAttribute',\
                          'name',\
                          'PORT',\
                          host)
        user = UT.getelem(root,\
                          'ConfigurationAttribute',\
                          'name',\
                          'USER',\
                          port)
        setPrompt = UT.getelem(root,\
                               'ConfigurationAttribute',\
                               'name',\
                               'setPrompt',\
                                user)
        sendCmd = UT.getelem(root,\
                             'ConfigurationAttribute',\
                             'name',\
                             'sendCmd',\
                             setPrompt)
        setRegExPrompt = UT.getelem(root,\
                                    'ConfigurationAttribute',\
                                    'name',\
                                    'setRegExPrompt',\
                                    sendCmd)

        items = self.iDict.items();items.sort()
        for (key,value) in items:            
            if 'interface' == key or\
               'featureModel' == key or\
               'version' == key or\
               'maxNumberOfAllocations' == key or\
               'typeOfAllocation' == key or\
               'resourceId' == key:
                eNodeB.set(key,value)
            elif 'HOST' == key:
                UT.SetFeatureAttrib(host,key,value)
            elif 'PORT' == key:
                UT.SetFeatureAttrib(port,key,value,'INTEGER')
            elif 'USER' == key:
                UT.SetFeatureAttrib(user,key,value)
            elif 'setPrompt' == key:
                UT.SetFeatureAttrib(setPrompt,key,value)
            elif 'sendCmd' == key:
                UT.SetFeatureAttrib(sendCmd,key,value)
            elif 'setRegExPrompt' == key:
                UT.SetFeatureAttrib(setRegExPrompt,key,value)
            elif -1 != key.find('relatedResource') and\
                 value.strip():
                print 'Set relatedResource'
                tmpNode = UT.getelem(root,'FeatureAttribute','name',key,eNodeB)
                UT.SetFeatureAttrib(tmpNode,key,value)
            else:
                tmpNode = UT.getelem(root,'FeatureAttribute','name',key,eNodeB)
                UT.SetFeatureAttrib(tmpNode,key,value)

        UT.FormatXML(root)
        tree.write(remoteFile, encoding='UTF-8', xml_declaration = True)
