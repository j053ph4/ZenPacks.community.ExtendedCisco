from ZenPacks.community.ConstructionKit.BasicDefinition import *
from ZenPacks.community.ConstructionKit.Construct import *

BASE = "ExtendedCisco"
VERSION = Version(1, 0, 0)


ciscoCPUDefinition = type('ciscoCPUDefinition', (BasicDefinition,), {
        'version' : VERSION,
        'zenpackbase': BASE,
        'component' : 'ciscoCPU',
        'componentData' : {
                          'singular': 'Processor',
                          'plural': 'Processors',
                          'displayed': 'id', # component field in Event Console
                          'primaryKey': 'id',
                          'properties': {
                                        'cpmCPUTotalIndex' : addProperty('Total', optional=False),
                                        'cpmCPUTotalPhysicalIndex' : addProperty('Physical', optional=False),
                                        },
                          },
        'componentMethods': [],
        })

ciscoMemoryPoolDefinition = type('ciscoMemoryPoolDefinition', (BasicDefinition,), {
        'version' : VERSION,
        'zenpackbase': BASE,
        'component' : 'ciscoMemoryPool',
        'componentData' : {
                          'singular': 'Memory Pool',
                          'plural': 'Memory Pools',
                          'displayed': 'ciscoMemoryPoolName', # component field in Event Console
                          'primaryKey': 'ciscoMemoryPoolName',
                          'properties': {
                                        'ciscoMemoryPoolType' : addProperty('Type'),
                                        'ciscoMemoryPoolName' : addProperty('Name', optional=False),
                                        'ciscoMemoryPoolAlternate' : addProperty('Alternate'),
                                        'ciscoMemoryPoolValid' : addProperty('Valid'),
                                        },
                          },
        'componentMethods': [],
})

ciscoEnhancedMemoryPoolDefinition = type('ciscoEnhancedMemoryPoolDefinition', (BasicDefinition,), {
        'version' : VERSION,
        'zenpackbase': BASE,
        'component' : 'ciscoEnhancedMemoryPool',
        'componentData' : {
                          'singular': 'Enhanced Memory Pool',
                          'plural': 'Enhanced Memory Pools',
                          'displayed': 'cempMemPoolName', # component field in Event Console
                          'primaryKey': 'cempMemPoolName',
                          'properties': {
                                        'cempMemPoolIndex' : addProperty('Index'),
                                        'cempMemPoolName' : addProperty('Name', optional=False),
                                        'cempMemPoolType' : addProperty('Type', optional=False),
                                        'cempMemPoolValid' : addProperty('Valid'),
                                        },
                          },
        'componentMethods': [],
})

