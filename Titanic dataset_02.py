import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    "Name": ["Alice Smith", "Bob Johnson", "Charlie Brown", "Diana Lee", "Ethan Williams",
             "Fiona Green", "George Harris", "Hannah Clark", "Ivy Baker", "Jack Taylor"],
    "Email": ["alice.123@email.com", "bob10@emai.com", "charlie25@funmail.org", "diana.05@home.com", "ethan.w34@example.com",
              "fiona234.g@mail.com", "george21@company.co.in", "hannah09@personal.net", "ivy56.b@domain.com", "jack45.t@anymail.com"],
    "Order Date": ["2025-05-01", "2025-05-01", "2025-05-02", "2025-05-03", "2025-05-03",
                   "2025-05-04", "2025-05-04", "2025-05-05", "2025-05-05", "2025-05-06"],
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Webcam",
                "Laptop", "Headphones", "Mouse Pad", "External Hard Drive", "Laptop Stand"],
    "Quantity": [1, 1, 1, 1, 1, 1, 1, 3, 1, 1],
    "Price": [1200, 25, 75, 300, 50, 1250, 150, 10, 120, 35],
    "Status": ["Shipped", "Delivered", "Processing", "Shipped", "Delivered",
               "Processing", "Shipped", "Delivered", "Processing", "Pending"]
}

# Create DataFrame
df = pd.DataFrame(data)

# Count the number of orders per status
status_counts = df["Status"].value_counts()

# Pie chart
plt.figure(figsize=(8, 6))
plt.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Pastel2.colors)
plt.title("Order Status Distribution")
plt.axis('equal')  # Ensures pie chart is a circle
plt.show()
