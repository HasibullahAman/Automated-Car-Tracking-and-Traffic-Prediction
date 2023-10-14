import pandas as pd

# Read CSV
data = pd.read_csv('CountingCar.csv')

# Function to calculate the Total, BusCount, TruckCount, and update the Traffic_Situation column in the CSV file
def AddLabel():
    # Calculate the maxBus, maxTruck, and maxTotal using the FindMax class
    maxTotal = FindMax().FindMaxTotal(data)
    maxBus = FindMax().FindMaxBus(data)
    maxTruck = FindMax().FindMaxTruck(data)

    # Update the "Traffic_Situation" column based on the "Total", 'BusCount', 'Truck_Count' columns
    for index, row in data.iterrows():
        total = row['Total']
        bus_count = row['BusCount']
        truck_count = row['TruckCount']

        if total > int((75 // 100) * maxTotal):
            data.at[index, 'Traffic_Situation'] = 'heavy'
        elif int((50 // 100) * maxTotal) < total < int((75 // 100) * maxTotal):
            if bus_count > int((75 // 100) * maxBus) or truck_count > int((75 // 100) * maxTruck):
                data.at[index, 'Traffic_Situation'] = 'heavy'
            else:
                data.at[index, 'Traffic_Situation'] = 'high'
        elif int((30 // 100) * maxTotal) < total < int((50 // 100) * maxTotal):
            if bus_count > int((50 // 100) * maxBus) or truck_count > int((50 // 100) * maxTruck):
                data.at[index, 'Traffic_Situation'] = 'high'
            else:
                data.at[index, 'Traffic_Situation'] = 'normal'
        else:
            if bus_count > int((30 // 100) * maxBus) or truck_count > int((30 // 100) * maxTruck):
                data.at[index, 'Traffic_Situation'] = 'normal'
            else:
                data.at[index, 'Traffic_Situation'] = 'low'

    # Save the updated data back to the CSV file
    data.to_csv('CountingCar.csv', index=False)

# Class used for finding the max values
class FindMax:
    def FindMaxTotal(self, data):
        maxTotal = data['Total'].max()
        return maxTotal

    def FindMaxBus(self, data):
        maxBus = data['BusCount'].max()
        return maxBus

    def FindMaxTruck(self, data):
        maxTruck = data['TruckCount'].max()
        return maxTruck

# Call the function to add labels
AddLabel()