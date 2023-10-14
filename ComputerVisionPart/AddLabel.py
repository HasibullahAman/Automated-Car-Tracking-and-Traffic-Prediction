# -------------------------------- Import Libraries
import pandas as pd

# -------------------------------- Read CSV
data = pd.read_csv('CountingCar.csv')


# Function to calculate the Total, BusCount, TruckCount, and update the Traffic_Situation column in the CSV file
class Addlabel:
    def AddLabel(self, data):
        # Calculate the maxBus, maxTruck, and maxTotal using the FindMax class
        maxTotal = FindMax().FindMaxTotal(data)
        maxBus = FindMax().FindMaxBus(data)
        maxTruck = FindMax().FindMaxTruck(data)

        # print(int((75 / 100) * maxTotal))

        # Update the "Traffic_Situation" column based on the "Total", 'BusCount', 'Truck_Count' columns
        for index, row in data.iterrows():
            total = row['Total']
            bus_count = row['BusCount']
            truck_count = row['TruckCount']

            if total > int((80 / 100) * maxTotal):
                data.at[index, 'Traffic Situation'] = 'heavy'
            elif int((60 / 100) * maxTotal) < total < int((80 / 100) * maxTotal):
                if bus_count > int((75 // 100) * maxBus) or truck_count > int((75 // 100) * maxTruck):
                    data.at[index, 'Traffic Situation'] = 'heavy'
                else:
                    data.at[index, 'Traffic Situation'] = 'high'
            elif int((40 / 100) * maxTotal) < total < int((60 / 100) * maxTotal):
                if bus_count > int((50 / 100) * maxBus) or truck_count > int((50 / 100) * maxTruck):
                    data.at[index, 'Traffic Situation'] = 'high'
                else:
                    data.at[index, 'Traffic Situation'] = 'normal'
            else:
                if bus_count > int((30 / 100) * maxBus) or truck_count > int((30 / 100) * maxTruck):
                    data.at[index, 'Traffic Situation'] = 'normal'
                else:
                    data.at[index, 'Traffic Situation'] = 'low'
        #
        # # Save the updated data back to the CSV file
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


# Create an instance of the Addlabel class
add_label = Addlabel()

# Call the AddLabel method and pass the 'data' argument
add_label.AddLabel(data)
