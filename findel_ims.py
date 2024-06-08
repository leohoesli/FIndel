import pandas as pd
import matplotlib.pyplot as plt
# import seaborn as sns
import numpy as np


##### Given values #####

discharge = 0.1  # estimate [meters^3 second^-1]
discharge_max = 0.22  # from measurement [meters^3 second^-1]
main_discharge = 5.5 # estimate for Findelbach [meters^3 second^-1]
delta_T_main = 0.7
specific_heat_capacity = 4184  # JkgK (specific heat capacity of water)
latent_heat_of_fusion_ice = 334000  # Latent heat of fusion for ice (J/kg)
rho_ice = 917 #density of ice [kg meter^-]
rho_water = 1000 #density of water [kg meter^-3]
area_findel = 13870000 #Area of Findelgletscher (GLAMOS) [m^2]
geotherm_findel = 0.070 #Geothermal Heat Flux [W/m^2]


##### Filepaths and Dataframes #####

df = pd.read_csv('C:/Users/leoho/OneDrive/Documents/1_Ausbildung/ETH/MA/1_Data/2_Field23/230929_Findel/1_Temperature/1_IMS.csv') # Water temperature data series, define path, replace \ with / when copying from explorer
df['Datum'] = pd.to_datetime(df['Datum'], format='%d.%m.%Y %H:%M:%S')

df2 = pd.read_csv('C:/Users/leoho/OneDrive/Documents/1_Ausbildung/ETH/MA/1_Data/6_Meteo/Gornergrat/Temperature/Gorner/gorner_temp.csv') # Air temperature Gornergrat station
df2['time'] = pd.to_datetime(df2['time'], format='%Y%m%d%H%M%S')

df3 = pd.read_csv('C:/Users/leoho/OneDrive/Documents/1_Ausbildung/ETH/MA/1_Data/6_Meteo/Findel/Precipitation/Findel_1day/findel_precip_1day.csv') #Precipitation Findelen station
df3['time']= pd.to_datetime(df3['time'], format='%Y%m%d')


##### Plots #####

### Timeline ###

# def timeline_simple():
# start_timestamp = pd.Timestamp('07.07.2023 10:46:28')
# end_timestamp = pd.Timestamp('29.09.2023 13:32:28')

# plt.figure(figsize=(20, 8))  # Adjust the figure size as needed

# plt.plot(df['Datum'], df['external'], label='water', color='blue')
# # plt.plot(df['Datum'], df['internal'], label='air', color='green')
# plt.title('Stream Temperature Findelen', fontsize=40)
# # plt.xlabel('Date', fontsize=20)
# plt.ylabel('Temperature [°C]', fontsize=26)
# plt.grid(True)

# plt.xticks(rotation=45, fontsize=22)  # Rotate x-axis labels for better readability
# plt.yticks(fontsize=26)
# plt.xlim(start_timestamp, end_timestamp)  # Set x-axis limits

# date_range = pd.date_range(start=start_timestamp, end=end_timestamp, freq='W') # Set the x-axis ticks to display a date every week

# plt.xticks(date_range)

# plt.tight_layout() # Ensure the plot layout is tight
# plt.show()

# correlation_ex_in = df['external'].corr(df['internal'])

# print(f"-Corelation coeff. Water (Findel)/ Air (Findel) Temp: {correlation_ex_in:.2f}")


### Timeline Water/Air ###

# def timeline_w_a():
start_timestamp = pd.Timestamp('07.07.2023 10:46:28')
end_timestamp = pd.Timestamp('29.09.2023 13:32:28') #This is used later on to set the width of the plot to the timeseries

plt.figure(figsize=(14, 8)) # Create subplots for the combined plot

plt.subplot(211) # Subplot for df
plt.plot(df['Datum'], df['external'], label='Stream temperature Findel IMS', color='blue')
plt.ylabel('Temperature [°C]', fontsize=18)
plt.legend(loc='upper right', fontsize=22)
plt.xlim(start_timestamp, end_timestamp)
plt.grid(axis='x')

date_range = pd.date_range(start=start_timestamp, end=end_timestamp, freq='2W') # Set the x-axis ticks to display a date every week
plt.xticks(date_range, fontsize=18)
plt.yticks(fontsize=18)

plt.subplot(212) # Subplot for df2
plt.plot(df2['time'], df2['tre200s0'], label='Air temperature Gornergrat (3090m)', color='red')
# plt.xlabel('Time', fontsize=16)
plt.ylabel('Temperature [°C]', fontsize=18)
plt.legend(loc='upper right', fontsize=22)
# plt.suptitle('Water and Air Temperatures at Findel Glacier', fontsize=28)
plt.xlim(start_timestamp, end_timestamp)
plt.grid(axis='x')
plt.xticks(date_range, fontsize=18)
plt.yticks(fontsize=18)

# plt.subplot(212) #subplot for df3
# plt.bar(range(len(df3['rka150d0'])), df3['rka150d0'], color='lightblue')
# plt.xlabel('Time')
# plt.ylabel('Daily Precipitation [mm]')

plt.tight_layout() # Adjust the layout and spacing


### Scatterplot Findel water/ Gorner air ###

# def scatter_w_a_1():
# df.set_index('Datum', inplace=True) # Set the 'timestamp' column as the index
# df2.set_index('time', inplace=True)

# df_resampled = df['external'].resample('10T').mean() # Resample the data to create 10-minute averages for the first file
# df2_resampled = df2['tre200s0'].resample('10T').mean() # Resample the data to create 10-minute averages for the second file

# df_resampled = df_resampled[df_resampled.index.isin(df2_resampled.index)] # Ensure that the resampled data frames have the same size
# df2_resampled = df2_resampled[df2_resampled.index.isin(df_resampled.index)]

# plt.figure(figsize=(8, 8)) # Create a scatterplot of the two datasets
# plt.scatter(df_resampled, df2_resampled, alpha=0.5, color='blue')
# plt.title('Correlation Between Water (Findel) and Air (Gorner) Temperature')
# plt.xlabel('Water Temperature [°C]', fontsize=16)
# plt.ylabel('Air Temperature [°C]', fontsize=16)
# plt.tight_layout()
# plt.show()

# correlation_fin_gor = df_resampled.corr(df2_resampled)
# print('-Corelation coeff. Water (Findel)/ Air (Gorner) Temp: ', correlation_fin_gor)


### Scatterplot Findel water/ Findel air ###

# def scatter_w_a_2():
# plt.figure(figsize=(8, 8))
# plt.scatter(df['external'], df['internal'], alpha=0.3, color='blue')
    
# coefficients = np.polyfit(df['external'], df['internal'], 1) # Perform linear regression to get the trendline
# trendline = np.poly1d(coefficients)

# plt.plot(df['external'], trendline(df['external']), color='red', label=f'Trendline: y = {coefficients[0]:.2f}x + {coefficients[1]:.2f}') # Plot the trendline

# plt.title('Correlation Between Water (Findel) and Air (Findel) Temperature')
# plt.xlabel('Water Temperature')
# plt.ylabel('Air Temperature')
# plt.legend()

# plt.tight_layout()
# plt.show()


### 1-hour average ###
#broken?

# def timeline_1h():
# df.set_index('Datum', inplace=True) #Resample the data to calculate hourly averages
# hourly_avg = df['external'].resample('1H').mean()

# plt.figure(figsize=(12, 6))

# plt.plot(hourly_avg.index, hourly_avg.values, marker='o', linestyle='-')
# plt.title('1-hour Averages Timeline')
# plt.xlabel('Date')
# plt.ylabel('1-hour Average Temperature')
# plt.grid(True)

# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()


### Diurnal Cycle ###

# def diurnal():
# df['time_of_day'] = df['Datum'].dt.strftime('%H:%M')  # Extract the time of day from the timestamp, Format as hh:mm

# diurnal_avg = df.groupby('time_of_day')['external'].mean() # Calculate the average measurement for each time of day
    
# time_range = pd.date_range(start='10.07.2023 00:00:00', end='10.07.2023 23:59:00', freq='T') # Create a time range from 00:00 to 23:59
# time_labels = [str(time.time()) for time in time_range] # Create a corresponding list of time labels

# plt.figure(figsize=(12, 6)) # Plot the average diurnal cycle
# plt.plot(time_labels, diurnal_avg, marker='o', linestyle='-')
# plt.title('Average Diurnal Cycle of Water Temperatures', fontsize=28)
# plt.xlabel('Time of Day', fontsize=16)
# plt.ylabel('Temperature [°C]', fontsize=16)
# # Set x-axis ticks every 3 hours
# plt.xticks(time_labels[::180], rotation=45, fontsize=14)

# plt.tight_layout()
# plt.show()


### Diurnal Cycle Variability ###

# def diurnal_var():
# df['time_of_day'] = df['Datum'].dt.strftime('%H:%M') # Extract the time of day from the timestamp


# diurnal_min = df.groupby('time_of_day')['external'].min() # Group by time of day and calculate the minimum and maximum measurements
# diurnal_max = df.groupby('time_of_day')['external'].max()
# diurnal_avg = df.groupby('time_of_day')['external'].mean()

# time_range = pd.date_range(start='10.07.2023 00:00:00', end='10.07.2023 23:59:00', freq='T') # Create a time range from 00:00 to 23:59
# time_labels = [str(time.time()) for time in time_range] # Create a corresponding list of time labels

# plt.figure(figsize=(12, 6)) # Plot the diurnal cycle with lines for average, min, and max measurements
# plt.plot(time_range, diurnal_avg, color='black', label='Average Measurement')
# plt.plot(time_range, diurnal_min, color='blue', alpha=0.5, label='Min Measurement')
# plt.plot(time_range, diurnal_max, color='red', alpha=0.5, label='Max Measurement')
# plt.fill_between(time_range, diurnal_min, diurnal_max, color='lightgray', alpha=0.5, label='Range')
# plt.title('Diurnal Cycle with Average and Range of Measurements', fontsize=28)
# plt.xlabel('Time of Day', fontsize=16)
# plt.ylabel('Measurement', )

# plt.xticks(time_labels[::180], rotation=45, fontsize=14) # Set x-axis ticks every 3 hours

# plt.legend()

# plt.tight_layout()
# plt.show()


### Boxplot diurnal cycle ###

# def diurnal_bp():
# df['Datum'] = pd.to_datetime(df['Datum']) # Convert the 'timestamp' column to a datetime format if not already done

# df['hour_of_day'] = df['Datum'].dt.hour # Extract the hour of the day from the timestamp

# hourly_avg = df.groupby('hour_of_day')['external'].mean() # Calculate the average measurement for each hour of the day

# plt.figure(figsize=(12, 6)) # Create a box plot to visualize the variability
# sns.boxplot(x='hour_of_day', y='external', data=df, showfliers=False, color='#007acc')
# plt.title('Hourly Variability of Measurements')
# plt.xlabel('Hour of the Day')
# plt.ylabel('Average Measurement')

# plt.tight_layout()
# plt.show()


### Energy ###

# def timeline_energy():
# df['energy'] = discharge * 1000 * 60 * specific_heat_capacity * df['external'] / 1000000 # Calculate the energy change for each time step, convert discharge from m^3 to kg, over 60 seconds, in MJ

# plt.figure(figsize=(12, 6)) # Plot the energy change over time
# plt.plot(df['Datum'], df['energy'], marker='', linestyle='-')
# plt.title('Energy Change Over Time')
# plt.xlabel('Datum')
# plt.ylabel('Available Energy [MJ]')
# plt.grid(True)
# plt.xticks(rotation=45)

# plt.tight_layout()
# plt.show()


##### Energy Calculations #####

timespan_sec = df['external'].count() * 60 # timespan of measurements in seconds
# timespan_sec = 90*24*60*60 #90 days

# def energy_cal():
temperature_avg = df['external'].mean()
energy_ims = discharge * rho_water * timespan_sec * specific_heat_capacity * temperature_avg #convert discharge into kg, energy in J
energy_ims_GJ = f"{energy_ims /1000000000:.2f}" #Energy in GJ, 2 decimal places

print(f"-IMS: energy {energy_ims_GJ} GJ")

melted_mass = energy_ims / latent_heat_of_fusion_ice
melted_mass_r = f"{melted_mass:.2f}" #rounded
melted_volume = melted_mass / rho_ice
melted_volume_r = f"{melted_volume:.2f}" #rounded

print(f"-IMS: ice melt {melted_mass_r} kg or {melted_volume_r} m^3")

ablation_ims = melted_mass / rho_water / area_findel * 1000 #ablation in mm w.e.
ablation_ims_r = f"{ablation_ims:.2f}" #rounded

print(f"-IMS: ablation {ablation_ims_r} mm w.e.")

delta_T_pot = energy_ims / (main_discharge * rho_water * specific_heat_capacity * timespan_sec) # potential dT of main stream
delta_T_pot_r = f"{delta_T_pot:.2f}"
print(f"-IMS: main meltwater stream heatup by {delta_T_pot_r} K.")

energy_heatup = main_discharge * rho_water * specific_heat_capacity * delta_T_main * 60 # energy required to heat up Findelbach by 0.5°C over 60s
energy_heatup_r = f"{energy_heatup:.2f}" #rounded
energy_heatup_total = main_discharge * rho_water * specific_heat_capacity * delta_T_main * timespan_sec # energy required to heat up Findelbach by 0.5°C over entire timeperiod
energy_heatup_total_r = f"{energy_heatup_total:.2f}" #rounded
heatup_percent = energy_heatup_total / energy_ims * 100
heatup_percent_r = f"{heatup_percent:.2f}" #rounded

print(f"-Total energy required to heat up Findelbach by 0.5°C for 1 minute is {energy_heatup_r} J. For the entire time period: {energy_heatup_total_r} J. This is {heatup_percent_r}% of the total available energy")


### Geothermal Heat Flux (rough) ###

energy_ghf = geotherm_findel * area_findel * timespan_sec #Energy [J]
energy_ghf_GJ_r = f"{energy_ghf / 1000000000:.2f}" #rounded and J to GJ
ratio_ghf_ims = energy_ghf / energy_ims *100
ratio_ghf_ims_r = f"{ratio_ghf_ims:.2f}" #rounded

ablation_ghf = energy_ghf / (latent_heat_of_fusion_ice * rho_water * area_findel) * 1000 #ablation in mm w.e.
ablation_ghf_r = f"{ablation_ghf:.2f}"  #rounded

print(f"-GHF: energy {energy_ghf_GJ_r} GJ.")
print(f"-Ratio GHF/IMS {ratio_ghf_ims_r}%.")
print(f"-GHF: ablation {ablation_ghf_r} mm w.e.")


##### Perform Functions #####

# timeline_w_a()
# scatter_w_a_1()
# timeline_simple()
# scatter_w_a_2()
# timeline_1h()
# diurnal()
# diurnal_var()
# diurnal_bp()
# timeline_energy()
# energy_cal()




# -*- coding: utf-8 -*-