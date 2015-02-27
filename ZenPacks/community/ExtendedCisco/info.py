from ZenPacks.community.ConstructionKit.ClassHelper import *

def ciscoMemoryPoolgetEventClassesVocabulary(context):
    return SimpleVocabulary.fromValues(context.listgetEventClasses())

class ciscoMemoryPoolInfo(ClassHelper.ciscoMemoryPoolInfo):
    ''''''

def ciscoCPUgetEventClassesVocabulary(context):
    return SimpleVocabulary.fromValues(context.listgetEventClasses())

class ciscoCPUInfo(ClassHelper.ciscoCPUInfo):
    ''''''

def ciscoEnhancedMemoryPoolgetEventClassesVocabulary(context):
    return SimpleVocabulary.fromValues(context.listgetEventClasses())

class ciscoEnhancedMemoryPoolInfo(ClassHelper.ciscoEnhancedMemoryPoolInfo):
    ''''''


