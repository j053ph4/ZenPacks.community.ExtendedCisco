from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetMap, GetTableMap
from Products.DataCollector.plugins.DataMaps import ObjectMap
from ZenPacks.community.ExtendedCisco.Definition import *

__doc__ = """ciscoCPUMap

ciscoCPUMap detects Cisco CPUs

"""

class ciscoCPUMap(SnmpPlugin):
    """
    """
    compname = "os"
    constr = Construct(ciscoCPUDefinition)
    relname = constr.relname
    modname = constr.zenpackComponentModule
    baseid = constr.baseid

    snmpTableName = 'cpmCPUTotalEntry'
    snmpTableOID = '.1.3.6.1.4.1.9.9.109.1.1.1.1'
    snmpIndexName = 'cpmCPUTotalIndex'
    snmpTitleName = 'cpmCPUTotalPhysicalIndex'

    
    snmpGetTableMaps = (
        GetTableMap(snmpTableName, snmpTableOID, {
            '.1': snmpIndexName,
            '.2': snmpTitleName,
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
            name = 'cpu-%s' % snmpindex
            om.id = self.prepId(name)
            om.title = name
            om.snmpindex = snmpindex
            rm.append(om)
        maps.append(rm)
        return maps

