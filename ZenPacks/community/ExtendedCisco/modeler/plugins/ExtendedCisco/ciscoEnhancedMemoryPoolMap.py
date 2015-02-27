from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetMap, GetTableMap
from Products.DataCollector.plugins.DataMaps import ObjectMap
from ZenPacks.community.ExtendedCisco.Definition import *
from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetMap, GetTableMap
from Products.DataCollector.plugins.DataMaps import ObjectMap
from ZenPacks.community.ExtendedCisco.Definition import *

__doc__ = """ciscoEnhancedMemoryPoolMap

ciscoEnhancedMemoryPoolMap detects Cisco Enhanced Memory Pools

"""

class ciscoEnhancedMemoryPoolMap(SnmpPlugin):
    """
    """
    compname = "os"
    constr = Construct(ciscoEnhancedMemoryPoolDefinition)
    relname = constr.relname
    modname = constr.zenpackComponentModule
    baseid = constr.baseid

    snmpTableName = 'cempMemPoolEntry'
    snmpTableOID = '.1.3.6.1.4.1.9.9.221.1.1.1.1'
    snmpIndexName = 'cempMemPoolIndex'
    snmpTitleName = 'cempMemPoolName'
    snmpMonitorName = 'cempMemPoolValid'
    snmpMonitorFlagExists = False
    
    snmpGetTableMaps = (
        GetTableMap(snmpTableName, snmpTableOID, {
            '.1': snmpIndexName,
            '.2': 'cempMemPoolType',
            '.3': snmpTitleName,
            '.5': snmpMonitorName,
            }),
        )


    def process(self, device, results, log):
        log.info("Modeler %s processing data for device %s",
            self.name(), device.id)
        getdata, tabledata = results
        maps = []
        rm = self.relMap()
        trunktable = tabledata.get(self.snmpTableName)
        for snmpindex, trunk in trunktable.items():
            log.debug("idx: %s, trunk: %s" % (snmpindex, trunk))
            om = self.objectMap(trunk)
            name = 'memorypool-%s' % snmpindex
            om.id = self.prepId(name)
            om.title = name
            om.snmpindex = snmpindex
            if self.snmpMonitorFlagExists == True:
                if getattr(om, self.snmpMonitorName) == 0:
                    om.monitor = False
            rm.append(om)
        maps.append(rm)
        return maps
    
