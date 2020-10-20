# About and Contact
Unit converter for physical simulations. For now, only a few physical units are accepted, and are most related to OFET's parameters.
Contact: mluginieski@alunos.utfpr.edu.br
Date: Out 19, 2020

# Mode of operation
The module operates receiving two string parameters. The first string corresponds to the value to be converted and is called uc_float. The second one is the unit and is called uc_str. In first place, any '\n' is removed from uc_str. Then, the first parameter is converted to a float value and the conversion begins. After conversion the float value and the unit are returned to the involking function.

# Usage
  * Any unit is written between square brackets [].
  * Some units accept prefixes like milli (m), micro (mi), nano (n). The prefix
    should be written before the unit whitout any spacing, for example:
    micrometer-> [mim].
  * Dimensionless is written as [.].
  
# Example of use:
```
from unit_converter import converter
value, unit = converter(float,str)
```

# Units accepted and format
  * Dimensionless:             [.]
  
  * Length:
    * Centimeter:              [cm]
    * Meter:                   [m]
    * Millimeter:              [mm]
    * Micrometer:              [mim]
    * Nanometer:               [nm]

  * Temperature:
    * Kelvin:                [K]
    * Celsius:               [^oC]
    * Fahrenheit:            [^oF]

  * Voltage:
    * Volts:                 [V]
    * Millivolts:            [mV]
    * Microvolts:            [miV]
    * Nanovolts:             [nV]
      
  * Chage:
    * Coulumb:               [C]

  * Energy:
    * Joule:                 [J]
    * Electronvolts:         [eV]
      
  * Capacitance per unit area:
    * F/cm^2:                [F/cm^2]
    * F/m^2:                 [F/m^2]

  * Field-effect mobility
    * m^2/Vs:                [m^2/Vs]
    * cm^2/Vs:               [cm^2/Vs]

  * SI units of constants:
    * Boltzmann constant:    [J/K]
    * Electric permittivity: [F/m]

