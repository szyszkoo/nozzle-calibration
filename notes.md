Data sets: 
- 1 [x] - eg. line 3707
- 2 [x] - eg. line 28
- 3 [x] - eg. line 264

The special thing about set no. 3 is that the last column (pistol status) is entirely filled with zeros.

### Data format
#### `tankMeasures.log` file: 
1. timestamp
2. locationID (always empty)
3. meterID (always empty)
4. tankID
5. fuelHeight
6. fuelVolume
7. fuelTemperature

#### `nozzleMeasures.log` file:
1. timestamp
2. locationID (always empty)
3. nozzleID
4. tankID
5. literCounter (counter of current transaction)
6. totalCounter (total counter of a nozzle - of all transactions)
7. status (1 - nozzle is not used, 0 - nozzle is being used -> fueling in progress)

#### `refuel.log` file:
1. timestamp
2. tankID
3. fuelHeight (total volume of fuel provided)
4. fuelVolume

In all *timestamp* columns the date and time is given for **beginning** of a transaction.