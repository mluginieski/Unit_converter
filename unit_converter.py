# Version: 20201019
# Convert units given on input to SI
import sys

def unit(u):
    '''Corrects the string unit and give the convertion factor'''
    
    u = u.replace('\n','')
    
    # Dimensioless
    if u == '.': return 1.0, u

    # Lenght
    if u == 'm': return 1.0, u
    if u == 'cm': u = 'm' ; return 1.0e-02, u
    if u == 'km': u = 'm' ; return 1.0e+03, u
    if u == 'mm': u = 'm' ; return 1.0e-03, u
    if u == 'um': u = 'm' ; return 1.0e-06, u
    if u == 'nm': u = 'm' ; return 1.0e-09, u
    if u == 'Angstron': u = 'm' ; return 1.0e-10, u

    # Temperature
    if u == 'K': return 1.0, u
    if u == 'oC': u = 'K' ; return 273.15, u
    if u == 'oF': u = 'K' ; return 459.67, u

    # Voltage
    if u == 'V': return 1.0, u
    if u == 'mV': u = 'V' ; return 1.0e-3, u
    if u == 'uV': u = 'V' ; return 1.0e-6, u
    if u == 'nV': u = 'V' ; return 1.0e-9, u

    # Charge
    if u == 'C': return 1.0, u

    # Energy
    if u == 'J': return 1.0, u
    if u == 'eV': u = 'J' ; return 1.602176634e-19, u

    # Capacitance per unit area
    if u == 'F/m2': return 1.0, u
    if u == 'F/cm2': u = 'F/m2' ; return 1/1.0e-04, u

    # Field-effect mobility
    if u == 'm2/Vs': return 1.0, u
    if u == 'cm2/Vs': u = 'm2/Vs' ; return 1.0e-04, u

    # Physical constants
    if u == 'J/K': return 1.0, u

    if u == 'F/m': return 1.0, u

    else: error = 'The {} unit is not defined!'.format(u); sys.exit(error)

def converter(parameters):

    # Save the original unit give by user
    u_old = parameters[2].replace('\n','')

    factor, parameters[2] = unit(parameters[2])

    # Calculation block of converted value
    if u_old == 'oC': parameters[1]  += factor
    elif u_old == 'oF': parameters[1] = (parameters[1] + factor)/1.8
    else: parameters[1] *= factor
    
    print('>> ',parameters[1],parameters[2])
    
    return parameters
