# temperature_check.py

# Accept temperature from the user
temperature = float(input("Enter temperature in °C: "))

# Determine status
if temperature <= 30:
    status = "Normal"
else:
    status = "Hot"

# Display result
print(f"Temperature: {temperature}°C")
print(f"Status: {status}")
# temperature_check.py

# Accept temperature from the user
temperature = float(input("Enter temperature in °C: "))

# Determine status
if temperature <= 30:
    status = "Normal"
else:
    status = "Hot"

# Convert to Fahrenheit
fahrenheit = (temperature * 9/5) + 32

# Display result
print(f"Temperature: {temperature}°C")
print(f"Status: {status}")
print(f"Temperature in Fahrenheit: {fahrenheit}°F")