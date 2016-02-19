# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 22:36:55 2016

@author: chris
"""

from ramanTools.RamanSpectrum import *

try:
    FTPRef =  RamanSpectrum('Utilities/150430_08.txt')
except:
    pass
try:
    BrTPRef = RamanSpectrum('Utilities/150430_14.txt')
except:
    pass
try:
    ClTPRef = RamanSpectrum('Utilities/150424_06.txt')
except:
    pass
try:
    MeOTPRef = RamanSpectrum('Utilities/4_methoxythiophenol.spe')
except:
    pass
try:
    MethylTPRef = RamanSpectrum('Utilities/1_methylbenzenethiol.spe')
except:
    pass
try:
    CdMethylTPRef = RamanSpectrum('Utilities/150707_02.txt')
except:
    pass
try:
    CdMeOTPRef = RamanSpectrum('Utilities/150707_03.txt')
except:
    pass
try:
    CdODPARef =  RamanSpectrum('Utilities/1_reference CdODPA.spe') 
except:
    pass
try:
    tolueneRef =  RamanSpectrum('Utilities/Liquid sample corrected-spectrum of toluene.txt') 
except:
    pass
try:
    ODPARef =  RamanSpectrum('Utilities/OPDA 100s collection time on glass_bendregion_50xObj.spe')
except:
    pass
try:
    CdOPARef = RamanSpectrum('Utilities/150612_04.txt')
except:
    pass
try:
    OPARef = RamanSpectrum('Utilities/octylphosphonic acid.txt')
    #
except:
    pass
try:
    Table_SPIDcorrect785 = RamanSpectrum(pandas.Series.from_csv('/home/chris/Dropbox/DataWeiss/Utilities/Table_SPIDcorrect785.csv'))
except:
    pass
try:
    Table_SPIDcorrect633 = RamanSpectrum(pandas.Series.from_csv('/home/chris/Dropbox/DataWeiss/Utilities/Table_SPIDcorrect633.csv'))
except:
    pass
try:
    Table_SPIDcorrect473 = RamanSpectrum(pandas.Series.from_csv('/home/chris/Dropbox/DataWeiss/Utilities/Table_SPIDcorrect473.csv'))
except:
    pass 
    