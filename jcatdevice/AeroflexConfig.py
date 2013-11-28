#########################################################
# File: Definition the AeroflexConfig class
# Author: Aaron yao
# Time: 2012/11/23
# Version: 1.1
# 2012/11/27 Fix duplicate add same node Bug
#########################################################
import xml.etree.ElementTree as ET
import jcatdevice.Utils as UT

class AeroflexConfig:
    def __init__(self):
        '''
        self.iReourceId = tm500Name
        self.iAeroflexPcHost = aeroflexPcHost
        self.iAeroflexIP = aeroflexIP
        self.iAeroflexLinuxHost = aeroflexLinuxHost
        self.iFeatureModel = 'OperationAndMaintenance'
        self.iInterface = 'TelnetCommandSession'
        self.iMaxNumberOfAllocations = '50'
        self.iTypeOfAllocation = 'MULTI'
        self.iVersion = '1.1'
        
        self.iUeName = 'Ue' + tm500Name
        self.iUeDriver = 'AeroflexTm500'
        self.iPowerSwitchDriver = 'PowerSwitchUtronix800'
        self.iPowerSwitchNr = '8'
        self.iPowerSwitchUser = 'clever'
        self.iPowerSwitchPassword = 'clever'
        self.iPowerSwitchIp = '10.186.135.151'
        
        self.iAeroflexPcPort = '5003'
        self.iAeroflexPcUserName = 'admin'
        self.iAeroflexPcPassword = 'admin'
        self.iAeroflexPcPrompt = 'C:\Users\\admin'#need double \\,otherwise it will cause \a escape character
        self.iAeroflexPcRestart = 'restart-vista.bat'
        self.iAeroflexPcTmaStartScript = 'C:\\Users\\lteran\\TmaStart.vbs'
        self.iAeroflexPcTmaProcessName = 'TmaApplication.exe'

        self.iAeroflexCmdPort = '5001'
        self.iAeroflexLogPort = '5002'
        self.iAeroflexLinuxUser = 'jcat'
        self.iAeroflexLinuxPassword = 'jcat123'
        self.iAeroflexLinuxHost = 'JCATPPPoE01' #same as Hosts definition
        self.iAeroflexLinuxPort = '22'
        self.iAeroflexLinuxPrompt = 'jcat@lte-OptiPlex-990:~\-> '

        self.iIsPort = '53401-53529'
        self.iCpg1Imsi = '460990025000000,460990025000199'
        '''
        self.iDict = {'resourceId':'',\
                      'interface':'TelnetCommandSession',\
                      'featureModel':'OperationAndMaintenance',\
                      'version':'1.1',\
                      'maxNumberOfAllocations':'50',\
                      'typeOfAllocation':'MULTI',\
                      'ueName':'',\
                      'ueDriver':'AeroflexTm500',\
                      'powerSwitchDriver':'PowerSwitchUtronix800',\
                      'powerSwitchNr':'',\
                      'powerSwitchUser':'clever',\
                      'powerSwitchPassword':'clever',\
                      'powerSwitchIp':'10.186.135.151',\
                      'aeroflexPcHost':'',\
                      'aeroflexPcPort':'5003',\
                      'aeroflexPcUsername':'admin',\
                      'aeroflexPcPassword':'admin',\
                      'aeroflexPcPrompt':"C:\Users\\admin>",\
                      'aeroflexPcRestart':'restart-vista.bat',\
                      "aeroflexPcTmaStartScript":"C:\\Users\\lteran\\TmaStart.vbs",\
                      'aeroflexPcTmaProcessName':'TmaApplication.exe',\
                      'aeroflexIP':'',\
                      'aeroflexCmdPort':'5001',\
                      'aeroflexLogPort':'5002',\
                      'aeroflexLinuxUser':'jcat',\
                      'aeroflexLinuxPassword':'jcat123',\
                      'aeroflexLinuxHost':'JCATPPPoE01',\
                      'aeroflexLinuxPort':'22',\
                      'aeroflexLinuxPrompt':"jcat@lte-OptiPlex-990.*",\
                      'ispPort':'53401-53529',\
                      'cpg1Imsi':''}
        
    def SetAeroflex(self,key,value):
        self.iDict[key] = value
        
    def BuildAeroflexTag(self,remoteFile):
        print " Build Aeroflex Tag"
        #!Fix: once file not exist
        tree = ET.parse(remoteFile)
        root = tree.getroot()
        factoryIdentity = root.find('FactoryIdentity')
        aeroflex = UT.getelem(root,\
                              'FeatureResource',
                              'resourceId',
                              self.iDict['resourceId'],
                              factoryIdentity)
        
        items = self.iDict.items();items.sort()
        for (key,value) in items:
            if 'interface' == key or\
               'featureModel' == key or\
               'version' == key or\
               'maxNumberOfAllocations' == key or\
               'typeOfAllocation' == key or\
               'resourceId' == key:
                aeroflex.set(key,value)
            else:
                tmpNode = UT.getelem(root,'FeatureAttribute','name',key,aeroflex)
                UT.SetFeatureAttrib(tmpNode,key,value)
        UT.FormatXML(root)
        tree.write(remoteFile, encoding='UTF-8', xml_declaration = True)
