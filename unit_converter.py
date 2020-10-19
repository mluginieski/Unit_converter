# Version: 20201019

def converter(uc_float, uc_str):
    '''Convert units from imput to SI'''
    uc_str = uc_str.replace('\n','')
    uc_float = float(uc_float)
    
    # Dimensionless
    if uc_str == '[.]':
        pass
    
    # Length
    if uc_str == '[m]':
        pass
    
    if uc_str == '[cm]':
        uc_float *= 0.01
        uc_str = '[m]'

    if uc_str == '[mm]':
        uc_float *= 1e-3
        uc_str = '[m]'
        
    if uc_str == '[mim]':
        uc_float *= 1e-6
        uc_str = '[m]'
        
    if uc_str == '[nm]':
        uc_float *= 1e-9
        uc_str = '[m]'
        
    # Temperature
    if uc_str == '[K]':
        pass
    
    if uc_str == '[^oC]':
        uc_float += 273.15
        uc_str = '[K]'
    
    if uc_str == '[^oF]':
        uc_float = (uc_float + 459.67)*(5/9)
        uc_str = '[K]'
        
    # Voltage
    if uc_str == '[V]':
        pass
    
    if uc_str == '[mV]':
        uc_float *= 1e-3
        uc_str = '[V]'
        
    if uc_str == '[miV]':
        uc_float *= 1e-6
        uc_str = '[V]'
        
    if uc_str == '[nV]':
        uc_float *= 1e-9
        uc_str = '[V]'
        
    # Charge
    if uc_str == '[C]':
        pass
    
    # Energy
    if uc_str == '[J]':
        pass
    
    if uc_str == '[eV]':
        uc_float *=  1.602176634e-19
        uc_str = '[J]'

    # Capacitance per unit area
    if uc_str == '[F/m^2]':
        pass
    
    if uc_str == '[F/cm^2]':
        uc_float *= 1/0.0001
        uc_str = '[F/m^2]'
        
    # Field-effect mobility
    if uc_str == '[m^2/Vs]':
        pass
    
    if uc_str == '[cm^2/Vs]':
        uc_float *= 0.0001
        uc_str = '[m^2/Vs]'
        
    # Physical constants
    if uc_str == '[J/K]':
        uc_str = '[J/K]'
        
    if uc_str == '[F/m]':
        uc_str = '[F/m]'

    return uc_float, uc_str
