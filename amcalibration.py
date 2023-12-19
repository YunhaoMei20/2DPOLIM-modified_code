import math

# Intensity of 0，45，90 and 135 degrees
I0 =167.84307# 
I90 =8.10846E-6# 
I135 =78.83057# 
I45 =71.38417
# calculate S0, S1, S2
S0 = (I0 + I45 + I90 + I135) / 4
S1 = I0 - I90
S2 = I45 - I135

# calculate the degree of polarization p and angle of polarization phi
p = math.sqrt(S1**2 + S2**2) / (2 * S0)
phi = math.atan(S2/S1) / 2

print("The degree of polarization is", p)
print("The polarization angle is", phi * 180 / math.pi, "degrees.")