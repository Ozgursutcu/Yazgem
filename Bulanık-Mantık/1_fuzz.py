#Write your fuzzy logic code here
# Importing the necessary libraries
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Creating the input variables
temperature = ctrl.Antecedent(np.arange(0, 101, 1), 'temperature')
humidity = ctrl.Antecedent(np.arange(0, 101, 1), 'humidity')

# Creating the output variable
fan_speed = ctrl.Consequent(np.arange(0, 101, 1), 'fan_speed')

# Defining the membership functions for the input variables
temperature['low'] = fuzz.trimf(temperature.universe, [0, 0, 50])
temperature['medium'] = fuzz.trimf(temperature.universe, [0, 50, 100])
temperature['high'] = fuzz.trimf(temperature.universe, [50, 100, 100])

humidity['low'] = fuzz.trimf(humidity.universe, [0, 0, 50])
humidity['medium'] = fuzz.trimf(humidity.universe, [0, 50, 100])
humidity['high'] = fuzz.trimf(humidity.universe, [50, 100, 100])

# Defining the membership functions for the output variable
fan_speed['low'] = fuzz.trimf(fan_speed.universe, [0, 0, 50])
fan_speed['medium'] = fuzz.trimf(fan_speed.universe, [0, 50, 100])
fan_speed['high'] = fuzz.trimf(fan_speed.universe, [50, 100, 100])

# Defining the fuzzy rules
rule1 = ctrl.Rule(temperature['low'] & humidity['low'], fan_speed['low'])
rule2 = ctrl.Rule(temperature['medium'] & humidity['medium'], fan_speed['medium'])
rule3 = ctrl.Rule(temperature['high'] & humidity['high'], fan_speed['high'])

# Creating the control system
fan_speed_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
fan_speed_simulation = ctrl.ControlSystemSimulation(fan_speed_ctrl)

# Setting the input values
fan_speed_simulation.input['temperature'] = 75
fan_speed_simulation.input['humidity'] = 80

# Running the simulation
fan_speed_simulation.compute()

# Getting the output value
output_speed = fan_speed_simulation.output['fan_speed']
print("Fan Speed:", output_speed)

