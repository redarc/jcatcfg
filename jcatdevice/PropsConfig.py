#########################################################
# File: PropsConfig class definition
# Author: Aaron yao
# Time: 2012/11/23
# Version: 1.0
#########################################################

import jcatdevice.Utils as UT
import os

#parent Propos interface BuildPropos parameter key or childclass
class JunitPropsConfig:
    def __init__(self):
        self.iDict = {'Campaign_enb1':'',\
                      'Campaign_enb2':'',\
                      'Campaign_enb3':'',\
                      'Campaign_ue1':'',\
                      'Campaign_pgw':'cpg nj cpg1',\
                      'Campaign_portbase':'0',\
                      'Campaign_numofues':'1',\
                      'Campaign_isp1':'isp nj njisp210'}
        
    def SetJuitLayout(self,key,value):
        tmpkey = key + '_layoutfile'
        self.SetJuitProps(tmpkey,value)

    def SetJuitCellId(self,key,value):
        tmpkey = key + '_cellid'
        self.SetJuitProps(tmpkey,value)
        
    def SetJuitProps(self,key,value):
        self.iDict[key] = value
        
    def BuildJuitProps(self,juitPropsFile):
        if os.path.exists(juitPropsFile):
            fp = open(juitPropsFile,'r+')
            for line in fp.readlines():
                pos = line.find(' ')
                if pos > -1:
                    key = line[0:pos].strip()
                    value = line[pos+1:len(line)].strip()
                    d_value = self.iDict[key]
                    if not d_value.strip():
                        self.SetJuitProps(key, value)
            fp.close()
            
            fp = open(juitPropsFile,'w+')
            items = self.iDict.items();items.sort()
            for (key,value) in items: 
                #print key, value
                fp.write(key)
                fp.write(' ')
                fp.write(value)
                fp.write('\n')
            fp.close()        


class TestNGPropsConfig:
    def __init__(self):
        self.iDict = {'main_enb1':'',\
                      'main_enb2':'',\
                      'main_ue1':'',\
                      'main_pgw':'cpg ln cpg1',\
                      'main_portbase':'0',\
                      'main_numofues':'1',\
                      'main_isp1':'isp nj njisp210'}

    def SetTestNGLayout(self,key,value):
        tmpkey = key + '_layoutfile'
        self.SetTestNGProps(tmpkey,value)

    def SetTestNGCellId(self,key,value):
        tmpkey = key + '_cellid'
        self.SetTestNGProps(tmpkey,value)
        
    def SetTestNGProps(self,key,value):
        self.iDict[key] = value
        
    def BuildTestNGProps(self,testngPropsFile):
        #Bug the file content will overwrite custom config
        if os.path.exists(testngPropsFile):
            fp = open(testngPropsFile,'r+')
            for line in fp.readlines():
                pos = line.find(' ')
                if pos > -1:
                    key = line[0:pos].strip()
                    value = line[pos+1:len(line)].strip()
                    dict_value = self.iDict[key]
                    if not dict_value.strip():
                        self.SetTestNGProps(key,value)
            #print '-------------------------------------'
            fp.close()
            
            fp = open(testngPropsFile,'w+')
            items = self.iDict.items();items.sort()
            for (key,value) in items: 
                print key, value
                fp.write(key)
                fp.write(' ')
                fp.write(value)
                fp.write('\n')
            fp.close()    
