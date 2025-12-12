import random

def analyze_data(data_list):
    """
    Analyzes a list of numbers to find the average and max.
    """
    if not data_list:
        return None
    
    total = 0
    max_val = -1
    
    # Loop through data to calculate sum
    for num in data_list:
        total += num
        if num > max_val:
            max_val = num
            
    average = total / len(data_list)
    return {"average": average, "max": max_val}

# Main execution
if __name__ == "__main__":
    # Simulate sensor data
    sensor_data = [random.randint(1, 100) for _ in range(50)]
    
    result = analyze_data(sensor_data)
    print(f"Analysis Complete: {result}")
