from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetMap, GetTableMap
from Products.DataCollector.plugins.DataMaps import ObjectMap
from ZenPacks.community.ExtendedCisco.Definition import *

__doc__ = """ciscoMemoryPoolMap

ciscoMemoryPoolMap detects Cisco Memory Pools

"""

class ciscoMemoryPoolMap(SnmpPlugin):
    """
    """
    compname = "os"
    constr = Construct(ciscoMemoryPoolDefinition)
    relname = constr.relname
    modname = constr.zenpackComponentModule
    baseid = constr.baseid

    snmpTableName = 'ciscoMemoryPoolEntry'
    snmpTableOID = '.1.3.6.1.4.1.9.9.48.1.1.1'
    snmpIndexName = 'ciscoMemoryPoolType'
    snmpTitleName = 'ciscoMemoryPoolName'
    snmpMonitorName = 'ciscoMemoryPoolValid'
    snmpMonitorFlagExists = True
    
    snmpGetTableMaps = (
        GetTableMap(snmpTableName, snmpTableOID, {
            '.1': snmpIndexName,
            '.2': snmpTitleName,
            '.3': 'ciscoMemoryPoolAlternate',
            '.4': snmpMonitorName,
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

