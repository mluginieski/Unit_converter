# About and Contact
Unit converter for physical simulations. For now, only a few physical units are accepted and are most related to OFET's parameters.
Contact: mluginieski@alunos.utfpr.edu.br
Date: Dec 30, 2021

# Mode of operation
The function is now invoked by a list with three parameters. The first one (parameters[0]) is the name of the variable and is not used on this function. The second (parameters[1]) is the float value that should be converted or not. Finally the third (parameters[2]) is the unit.
When the function converter is invoked, the unit is changed on the unit function and a conversion factor is passed to the main function. After conversion, the float value and the unit are returned to the invoking function.

# Usage
  * Spacing between parameters on input should be given by a simple tab.
  * Some units accept prefixes like milli (m), micro (u), nano (n). The prefix
    should be written before the unit without any spacing, for example:
    micrometer-> 'um'.
  * Dimensionless is written as a dot -> '.'.
  
# Example of use:
```
from unit_converter import converter
my_list = converter(parameters_list)
```

# Units accepted and format
  * Dimensionless:             .
  
  * Length:
    * Centimeter:              cm
    * Meter:                    m
    * Kilometer:               km
    * Millimeter:              mm
    * Micrometer:              um
    * Nanometer:               nm
    * Angstrom:                Angstrom

  * Temperature:
    * Kelvin:                K
    * Degree Celsius:        oC
    * Degree Fahrenheit:     oF

  * Voltage:
    * Volts:                  V
    * Millivolts:            mV
    * Microvolts:            uV
    * Nanovolts:             nV
      
  * Chage:
    * Coulumb:               C

  * Energy:
    * Joule:                 J
    * Electronvolts:         eV
      
  * Capacitance per unit area:
    * F/cm^2:                F/cm2
    * F/m^2:                 F/m2

  * Field-effect mobility
    * m^2/Vs:                m2/Vs
    * cm^2/Vs:               cm2/Vs

  * SI units of constants:
    * Boltzmann constant:    J/K
    * Electric permittivity: F/m
