import numpy as np
import matplotlib.pyplot as plt

solar_intensity = 1000 
panel_area = 0.01782 
max_output = 3
efficiency = 0.18  

time = np.arange(0, 24, 0.1)


def solar_angle(t):
    declination = 23.45 
    latitude = 0 
    hour_angle = 15 * (t - 12) 

    altitude_angle = np.arcsin(np.sin(np.radians(declination)) * np.sin(np.radians(latitude)) +
                               np.cos(np.radians(declination)) * np.cos(np.radians(latitude)) * np.cos(
        np.radians(hour_angle)))

    altitude_angle_deg = np.degrees(altitude_angle)

    return altitude_angle_deg

fixed_angle = 33.5  

solar_angles = solar_angle(time)
tracking_power = np.where(solar_angles > 0, max_output, 0)

fixed_power = np.where(solar_angles > 0, max_output * np.cos(np.radians(solar_angles - fixed_angle)), 0)

tracking_energy = np.trapz(tracking_power, time)
fixed_energy = np.trapz(fixed_power, time)

plt.figure(figsize=(14, 7))
plt.plot(time, tracking_power, label='Tracking Panel Power (W)')
plt.plot(time, fixed_power, label='Fixed Panel Power (W)', linestyle='--')
plt.xlabel('Time of Day (hours)')
plt.ylabel('Power Output (W)')
plt.title('Power Output of Solar Panels Throughout the Day')
plt.legend()
plt.grid(True)
plt.show()

print(f"Total daily energy output for tracking panel: {tracking_energy:.2f} Wh")
print(f"Total daily energy output for fixed panel: {fixed_energy:.2f} Wh")
print(f"Difference in energy output: {tracking_energy - fixed_energy:.2f} Wh")
