# ICE (internal combustion engine) Diesel to EV equivalent

How to convert the instantaneous fuel consumption of a diesel vehicle (in liters/100km) to the equivalent energy consumption of an electric vehicle (in kWh/100km).

## Conversion Steps

1. **Find the instantaneous fuel consumption** in liters/100km of your diesel vehicle. For example, let's say the instantaneous consumption is 5 liters/100km.

2. **Convert the diesel consumption to energy**. Diesel has an energy density of approximately 35.8 MJ/liter (megajoules per liter). To do this, multiply the consumption in liters by the energy density:

   5 liters/100km * 35.8 MJ/liter = 179 MJ/100km

3. **Convert the megajoules to kilowatt-hours (kWh)**. There are 0.27778 kWh in a megajoule (1 MJ = 0.27778 kWh):

   179 MJ/100km * 0.27778 kWh/MJ = 49.72 kWh/100km

4. **Account for energy efficiency**. Diesel engines are generally less efficient than electric motors. Diesel engines have an efficiency of around 30% to 40%, while electric motors have an efficiency of 85% to 95%. To estimate the equivalent kWh/100km for an electric vehicle, divide the diesel vehicle's energy consumption by the ratio of engine efficiencies. Assume the diesel engine efficiency is 35% and the electric motor efficiency is 90%:

   Efficiency ratio: (35% / 90%) = 0.389
   49.72 kWh/100km * 0.389 = 19.34 kWh/100km (approximately)

The equivalent energy consumption for an electric vehicle with the same instantaneous consumption as our diesel vehicle example would be approximately 19.34 kWh/100km. Keep in mind that this method is an approximation, and actual values may vary depending on the specifics of the vehicles and their driving conditions.
