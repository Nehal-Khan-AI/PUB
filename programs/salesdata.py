def analyze_sales(data):
    total_sales = sum(data)
    average_sales = total_sales / len(data) if data else 0
    highest_sale = max(data) if data else 0
    return total_sales, average_sales, highest_sale

# Get sales input from user
sales_input = input("Enter daily sales amounts separated by commas (e.g., 200, 300, 150): ")

# Convert input string to list of numbers
sales_list = [float(x.strip()) for x in sales_input.split(",") if x.strip().isdigit() or x.strip().replace('.', '', 1).isdigit()]

# Analyze sales
total, average, highest = analyze_sales(sales_list)

# Display results
print("\n--- Sales Summary ---")
print("Total Sales:", total)
print("Average Sale:", average)
print("Highest Sale:", highest)
print("Hello")
print("Hell2o")