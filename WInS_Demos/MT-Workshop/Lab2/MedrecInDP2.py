connect('weblogic','welcome1','t3://localhost:7001')
edit()
startEdit()

cd('/')
cmo.createVirtualTarget('VT-Medrec-2 ')
cd('/VirtualTargets/VT-Medrec-2')
cmo.setHostNames(array(["localhost"],java.lang.String))
cmo.setUriPrefix('/dp2')
set('Targets',jarray.array([ObjectName('com.bea:Name=app-cluster,Type=Cluster')], ObjectName))
activate()

startEdit()
cd('/')
cmo.createPartition('dp2')
cd('/Partitions/dp2/SystemFileSystem/dp2')
cmo.setRoot('/u01/wins/wls1221/user_projects/domains/base_domain/partitions/dp2/system')
cmo.setCreateOnDemand(true)
cmo.setPreserved(true)
cd('/Partitions/dp2')
set('AvailableTargets',jarray.array([ObjectName('com.bea:Name=VT-Medrec-2,Type=VirtualTarget')], ObjectName))
set('DefaultTargets',jarray.array([ObjectName('com.bea:Name=VT-Medrec-2,Type=VirtualTarget')], ObjectName))
activate()



startEdit()
cd('/Partitions/dp2')
cmo.createResourceGroup('app2RG')
cd('/Partitions/dp2/ResourceGroups/app2RG')
cmo.setUseDefaultTarget(false)
set('Targets',jarray.array([ObjectName('com.bea:Name=VT-Medrec-2,Type=VirtualTarget')], ObjectName))
activate()



startEdit()
cd('/Partitions/dp2/ResourceGroups/app2RG')
cmo.createJDBCSystemResource('MedRec2GlobalDataSourceXA')
cd('/Partitions/dp2/ResourceGroups/app2RG/JDBCSystemResources/MedRec2GlobalDataSourceXA/JDBCResource/MedRec2GlobalDataSourceXA')
cmo.setName('MedRec2GlobalDataSourceXA')
cd('/Partitions/dp2/ResourceGroups/app2RG/JDBCSystemResources/MedRec2GlobalDataSourceXA/JDBCResource/MedRec2GlobalDataSourceXA/JDBCDataSourceParams/MedRec2GlobalDataSourceXA')
set('JNDINames',jarray.array([String('jdbc/MedRecGlobalDataSourceXA')], String))
cd('/Partitions/dp2/ResourceGroups/app2RG/JDBCSystemResources/MedRec2GlobalDataSourceXA/JDBCResource/MedRec2GlobalDataSourceXA')
cmo.setDatasourceType('GENERIC')
cd('/Partitions/dp2/ResourceGroups/app2RG/JDBCSystemResources/MedRec2GlobalDataSourceXA/JDBCResource/MedRec2GlobalDataSourceXA/JDBCDriverParams/MedRec2GlobalDataSourceXA')
cmo.setUrl('jdbc:oracle:thin:@//localhost:1521/pdb2')
cmo.setDriverName('oracle.jdbc.xa.client.OracleXADataSource')
cmo.setPassword('medrec2')
cd('/Partitions/dp2/ResourceGroups/app2RG/JDBCSystemResources/MedRec2GlobalDataSourceXA/JDBCResource/MedRec2GlobalDataSourceXA/JDBCConnectionPoolParams/MedRec2GlobalDataSourceXA')
cmo.setTestTableName('SQL ISVALID\r\n\r\n')
cd('/Partitions/dp2/ResourceGroups/app2RG/JDBCSystemResources/MedRec2GlobalDataSourceXA/JDBCResource/MedRec2GlobalDataSourceXA/JDBCDriverParams/MedRec2GlobalDataSourceXA/Properties/MedRec2GlobalDataSourceXA')
cmo.createProperty('user')
cd('/Partitions/dp2/ResourceGroups/app2RG/JDBCSystemResources/MedRec2GlobalDataSourceXA/JDBCResource/MedRec2GlobalDataSourceXA/JDBCDriverParams/MedRec2GlobalDataSourceXA/Properties/MedRec2GlobalDataSourceXA/Properties/user')
cmo.setValue('medrec2')
cd('/Partitions/dp2/ResourceGroups/app2RG/JDBCSystemResources/MedRec2GlobalDataSourceXA/JDBCResource/MedRec2GlobalDataSourceXA/JDBCDataSourceParams/MedRec2GlobalDataSourceXA')
cmo.setGlobalTransactionsProtocol('TwoPhaseCommit')
activate()

startEdit()
cd('/Partitions/dp2/ResourceGroups/app2RG')
cmo.createMailSession('MedRec2MailSession')
cd('/Partitions/dp2/ResourceGroups/app2RG/MailSessions/MedRec2MailSession')
cmo.setJNDIName('mail/MedRecMailSession')
activate()

startEdit()
cd('/Partitions/dp2/ResourceGroups/app2RG')
cmo.createFileStore('MedRec2-fs')
activate()

startEdit()
cd('/Partitions/dp2/ResourceGroups/app2RG')
cmo.createJMSServer('MedRec2JMSServer')
cd('/Partitions/dp2/ResourceGroups/app2RG/JMSServers/MedRec2JMSServer')
cmo.setPersistentStore(getMBean('/Partitions/dp2/ResourceGroups/app2RG/FileStores/MedRec2-fs'))
activate()


startEdit()
cd('/Partitions/dp2/ResourceGroups/app2RG')
cmo.createJMSSystemResource('MedRecModule')
activate()

startEdit()
cd('/Partitions/dp2/ResourceGroups/app2RG/JMSSystemResources/MedRecModule')
cmo.createSubDeployment('MedRec2JMS ')
cd('/Partitions/dp2/ResourceGroups/app2RG/JMSSystemResources/MedRecModule/SubDeployments/MedRec2JMS')
set('Targets',jarray.array([ObjectName('com.bea:Name=MedRec2JMSServer,Type=JMSServer,Partition=dp2,ResourceGroup=app2RG')], ObjectName))
activate()

startEdit()
cd('/Partitions/dp2/ResourceGroups/app2RG/JMSSystemResources/MedRecModule/JMSResource/MedRecModule')
cmo.createConnectionFactory('MedRec2ConnectionFactory')
cd('/Partitions/dp2/ResourceGroups/app2RG/JMSSystemResources/MedRecModule/JMSResource/MedRecModule/ConnectionFactories/MedRec2ConnectionFactory')
cmo.setJNDIName('com.oracle.medrec.jms.connectionFactory ')
cd('/Partitions/dp2/ResourceGroups/app2RG/JMSSystemResources/MedRecModule/JMSResource/MedRecModule/ConnectionFactories/MedRec2ConnectionFactory/SecurityParams/MedRec2ConnectionFactory')
cmo.setAttachJMSXUserId(false)
cd('/Partitions/dp2/ResourceGroups/app2RG/JMSSystemResources/MedRecModule/JMSResource/MedRecModule/ConnectionFactories/MedRec2ConnectionFactory/ClientParams/MedRec2ConnectionFactory')
cmo.setClientIdPolicy('Restricted')
cmo.setSubscriptionSharingPolicy('Exclusive')
cmo.setMessagesMaximum(10)
cd('/Partitions/dp2/ResourceGroups/app2RG/JMSSystemResources/MedRecModule/JMSResource/MedRecModule/ConnectionFactories/MedRec2ConnectionFactory/TransactionParams/MedRec2ConnectionFactory')
cmo.setXAConnectionFactoryEnabled(true)
cd('/Partitions/dp2/ResourceGroups/app2RG/JMSSystemResources/MedRecModule/SubDeployments/MedRec2JMS')
set('Targets',jarray.array([ObjectName('com.bea:Name=MedRec2JMSServer,Type=JMSServer,Partition=dp2,ResourceGroup=app2RG')], ObjectName))
cd('/Partitions/dp2/ResourceGroups/app2RG/JMSSystemResources/MedRecModule/JMSResource/MedRecModule/ConnectionFactories/MedRec2ConnectionFactory')
activate()

startEdit()
cd('/Partitions/dp2/ResourceGroups/app2RG/JMSSystemResources/MedRecModule/JMSResource/MedRecModule')
cmo.createUniformDistributedQueue('PatientNotificationQueue')
cd('/Partitions/dp2/ResourceGroups/app2RG/JMSSystemResources/MedRecModule/JMSResource/MedRecModule/UniformDistributedQueues/PatientNotificationQueue')
cmo.setJNDIName('com.oracle.medrec.jms.PatientNotificationQueue')
cd('/Partitions/dp2/ResourceGroups/app2RG/JMSSystemResources/MedRecModule/SubDeployments/MedRec2JMS')
set('Targets',jarray.array([ObjectName('com.bea:Name=MedRec2JMSServer,Type=JMSServer,Partition=dp2,ResourceGroup=app2RG')], ObjectName))
cd('/Partitions/dp2/ResourceGroups/app2RG/JMSSystemResources/MedRecModule/JMSResource/MedRecModule/UniformDistributedQueues/PatientNotificationQueue')
cmo.setSubDeploymentName('MedRec2JMS')
activate()

startEdit()
deploy(appName='medrec', partition='dp2', resourceGroup='app2RG', path='/u01/content/weblogic-innovation-seminars/WInS_Demos/MT-Workshop/Lab2/medrec.ear')
deploy(appName='physician', partition='dp2', resourceGroup='app2RG', path='/u01/content/weblogic-innovation-seminars/WInS_Demos/MT-Workshop/Lab2/physician.ear')
deploy(appName='chat', partition='dp2', resourceGroup='app2RG', path='/u01/content/weblogic-innovation-seminars/WInS_Demos/MT-Workshop/Lab2/chat.war')
activate()

startEdit()
cd('/')
partitionBean=cmo.lookupPartition('dp2')
startPartitionWait(partitionBean)
activate()

disconnect()





