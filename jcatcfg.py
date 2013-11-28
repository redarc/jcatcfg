#########################################################
# File: jatcat_config main function
# Author: Aaron yao
# Time: 2012/11/23
# Version: 1.2
# Description: This script can auto set remotemcd.rd
#      CCN8001.xml,CCN8001.rd,Helloworld.props,testng.props
#      according to the parameter you set
# Log: 26/11/2012 Refactory all jactdevice classes,
#      use dictionary instead
#########################################################

import xml.etree.ElementTree as ET
import jcatdevice.AeroflexConfig as AC
import jcatdevice.CCNRDConfig as CC
import jcatdevice.ENodeBConfig as EC
import jcatdevice.PropsConfig as PC
import jcatdevice.Utils as UT

print "Welcome to JCAT world!\n"

# Paths
ARGS_PATH = 'C:/Users/EGANYAO/Desktop/args_tmplate/new_lab/'

# !!Key Parameters we MUST set parameter here
ENB_1 = 'enb_nj_njenb108'
UE_1 = 'ue_aeroflex_nj_08'
UE_NAME = 'UeAeroflexNj08'
#CCN_IDENTIFIER = 'LTESVCCN_1b_3x3'
#BAS_CELLID = {'bas_4':'3'}
#LAYOUT_CASE = {'casename':'layoutpath'}
ENODEB_IP = '10.186.137.134'
ENODEB_USER_PLAIN_IP = '10.186.135.210'
TM500_IP = '192.168.1.208'
TM500_IMSI = '460990025000600,460990025000799'
TM500_HOSTPC_IP = '192.168.1.108'
TM500_PPPoEIP = '10.186.135.182'

# Constant
JUNITPROPS_PATH = ARGS_PATH + 'helloworld.props'
TESTNGPROPS_PATH = ARGS_PATH + 'testng.props'
CCNRD_PATH = ARGS_PATH + 'msms/CCN8001.rd'
CCNXML_PATH = ARGS_PATH + 'msms/CCN8001.xml'
REMOTECMD_PATH = ARGS_PATH + 'remotecmd/thc/remotecmd.rd'

#######################################################
print "1.Step Process Helloworld.props file"
'''
default keywords for you set
we can use
'Campaign_enb1':''
'Campaign_enb2':''
'Campaign_enb3':''
'Campaign_ue1':''
'Campaign_pgw':'cpg nj cpg1'
'Campaign_portbase':'0'
'Campaign_numofues':'1'
'Campaign_isp1':'isp nj njisp210'}
'''

junitProps = PC.JunitPropsConfig()
junitProps.SetJuitProps('Campaign_enb1',ENB_1)
junitProps.SetJuitProps('Campaign_ue1',UE_1)
junitProps.BuildJuitProps(JUNITPROPS_PATH)

#######################################################
print "2.Step Process testng.props file"
'''
default keywords for you set
'main_enb1':'',\
'main_enb2':'',\
'main_ue1':'',\
'main_pgw':'cpg ln cpg7',\
'main_portbase':'0',\
'main_numofues':'1',\
'main_isp1':'isp nj njisp250'
'''
testngProps = PC.TestNGPropsConfig()
testngProps.SetTestNGProps('main_enb1',ENB_1)
testngProps.SetTestNGProps('main_ue1',UE_1)
testngProps.BuildTestNGProps(TESTNGPROPS_PATH)

#######################################################
print "3.Step Process remotecmd.rd file"
'''
default keywords for you set
'resourceId':'',\
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
'rs232Port':'4028',\
'defaultRouter':'x.x.x.x',\
'enbUpIp':'',\
'unixHost':'22',\
'unixUser':'jcat',\
'unixPassword':'jcat123',\
'unixPrompt':'',\
'defaultWorkStation':'workStation nj moshellSvr171',\
'relatedResource0':'',\
'relatedResource1':'',\
'HOST':'$(targethost)',\
'PORT':'$(targetport)',\
'USER':'$(targetuser)',\
'setPrompt':'*assword*',\
'sendCmd':'$(targetpassword)',\
'setRegExPrompt':'$(targetprompt)'
'''
# need to config resourceID condition


eNBCfg = EC.ENodeBConfig()
eNBCfg.SetENGValue('resourceId',ENB_1)
eNBCfg.SetENGValue('rbsIp',ENODEB_IP)
eNBCfg.SetENGValue('enbUpIp',ENODEB_USER_PLAIN_IP)
eNBCfg.BuildENGTag(REMOTECMD_PATH)

'''
Default keywords for you set
'resourceId':'',\
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
'aeroflexPcPrompt':'C:\Users\\admin>',\
'aeroflexPcRestart':'restart-vista.bat',\
'aeroflexPcTmaStartScript':'C:\\Users\\lteran\\TmaStart.vbs',\
'aeroflexPcTmaProcessName':'TmaApplication.exe',\
'aeroflexIP':'',\
'aeroflexCmdPort':'5001',\
'aeroflexLogPort':'5002',\
'aeroflexLinuxUser':'jcat',\
'aeroflexLinuxPassword':'jcat123',\
'aeroflexLinuxHost':'JCATPPPoE01',\
'aeroflexLinuxPort':'22',\
'aeroflexLinuxPrompt':'jcat@lte-OptiPlex-990:~\-> ',\
'ispPort':'53401-53529',\
'cpg1Imsi':''}
'''

#need to config resourceId condition
aeroflexCfg = AC.AeroflexConfig()
aeroflexCfg.SetAeroflex('resourceId',UE_1)
aeroflexCfg.SetAeroflex('ueName',UE_NAME)
aeroflexCfg.SetAeroflex('aeroflexPcHost',TM500_HOSTPC_IP)
aeroflexCfg.SetAeroflex('aeroflexIP',TM500_IP)
aeroflexCfg.SetAeroflex('cpg1Imsi',TM500_IMSI)
aeroflexCfg.SetAeroflex('aeroflexLinuxHost',TM500_PPPoEIP)
aeroflexCfg.BuildAeroflexTag(REMOTECMD_PATH)

#######################################################
print "4.Step Process CNN8001.xml file"
'''
'toolInstance':'',\
'TMS_GUI_NameService':'lteccn2:13579',\
'MSMS_ToolIdentifier':''
'''

'''
ccnxmlCfg = CC.CCNXMLConfig()
ccnxmlCfg.SetCCN_XML('toolInstance',CCN_IDENTIFIER)
ccnxmlCfg.SetCCN_XML('MSMS_ToolIdentifier',CCN_IDENTIFIER)
ccnxmlCfg.BuildCCNXML(CCNXML_PATH)
'''
#######################################################
print "5.Step Process CNN8001.rd file"
'''
defalut keywords for you set
'toolInstance':'',\
'bas_1':'',\
'bas_2':'',\
'bas_3':'',\
'bas_4':'',\
'bas_5':'',\
'bas_6':'',\
'bas_7':'',\
'bas_8':''
'''
'''
ccnrdConfig = CC.CCNRDConfig()
ccnrdConfig.SetCCN_RD('toolInstance',CCN_IDENTIFIER)
for (key,value) in BAS_CELLID.items():
    ccnrdConfig.SetCCN_RD(key,value)
ccnrdConfig.BuildCCNRDTag(CCNRD_PATH)
'''
print "6.All finished"
