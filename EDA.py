import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = "StyleKart_Capstone_Dataset.xlsx"
customers = pd.read_excel(
    file_path,
    sheet_name="Customers"
)

products = pd.read_excel(
    file_path,
    sheet_name="Products"
)

orders = pd.read_excel(
    file_path,
    sheet_name="Orders"
)

payments = pd.read_excel(
    file_path,
    sheet_name="Payments"
)

returns = pd.read_excel(
    file_path,
    sheet_name="Returns"
)

inventory = pd.read_excel(
    file_path,
    sheet_name="Inventory"
)
print("Customers:", customers.shape)
print("Products:", products.shape)
print("Orders:", orders.shape)
print("Payments:", payments.shape)
print("Returns:", returns.shape)
print("Inventory:", inventory.shape)


print("\n--- CUSTOMERS ---")
print(customers.head())
print(customers.info())
print("\n--- PRODUCTS ---")
print(products.head())
print(products.info())
print("\n--- ORDERS ---")
print(orders.head())
print(orders.info())
print("\n--- PAYMENTS ---")
print(payments.head())
print(payments.info())
print("\n--- RETURNS ---")
print(returns.head())
print(returns.info())
print("\n--- INVENTORY ---")
print(inventory.head())
print(inventory.info())



print("\nCustomers columns:")
print(customers.columns.tolist())

print("\nProducts columns:")
print(products.columns.tolist())

print("\nOrders columns:")
print(orders.columns.tolist())

print("\nPayments columns:")
print(payments.columns.tolist())

print("\nReturns columns:")
print(returns.columns.tolist())

print("\nInventory columns:")
print(inventory.columns.tolist())



print("\n--- CUSTOMERS MISSING VALUES ---")
print(customers.isnull().sum())

print("\n--- PRODUCTS MISSING VALUES ---")
print(products.isnull().sum())

print("\n--- ORDERS MISSING VALUES ---")
print(orders.isnull().sum())

print("\n--- PAYMENTS MISSING VALUES ---")
print(payments.isnull().sum())

print("\n--- RETURNS MISSING VALUES ---")
print(returns.isnull().sum())

print("\n--- INVENTORY MISSING VALUES ---")
print(inventory.isnull().sum())



print("Customer duplicates:", customers.duplicated().sum())
print("Product duplicates:", products.duplicated().sum())
print("Order duplicates:", orders.duplicated().sum())
print("Payment duplicates:", payments.duplicated().sum())
print("Return duplicates:", returns.duplicated().sum())
print("Inventory duplicates:", inventory.duplicated().sum())



print("\n--- ORDERS SUMMARY ---")
print(orders.describe())

print("\n--- PRODUCTS SUMMARY ---")
print(products.describe())

print("\n--- PAYMENTS SUMMARY ---")
print(payments.describe())

print("\n--- INVENTORY SUMMARY ---")
print(inventory.describe())


print("\n--- ORDER STATUS ---")
print(orders["Order_Status"].value_counts())


print(orders.columns.tolist())



inventory["Low_Stock"] = (
    inventory["Stock_Quantity"]
    < inventory["Reorder_Level"]
)
print(
    inventory["Low_Stock"].value_counts()
)
print(
    inventory[
        inventory["Low_Stock"] == True
    ][[
        "Product_ID",
        "Warehouse",
        "Stock_Quantity",
        "Reorder_Level"
    ]]
)


orders["Order_Status"].value_counts().plot(
    kind="bar"
)

plt.title("Order Status Distribution")
plt.xlabel("Order Status")
plt.ylabel("Number of Orders")
plt.tight_layout()
plt.show()


inventory["Stock_Quantity"].plot(
    kind="hist",
    bins=20
)

plt.title("Inventory Stock Distribution")
plt.xlabel("Stock Quantity")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# Join inventory details with product names and categories
inventory_with_products = inventory.merge(
    products[
        ["Product_ID", "Product_Name", "Brand", "Category"]
    ],
    on="Product_ID",
    how="left"
)

# A product is at stockout risk when stock is at or below its reorder level
inventory_with_products["Stockout_Risk"] = (
    inventory_with_products["Stock_Quantity"]
    <= inventory_with_products["Reorder_Level"]
)

# Product and warehouse combinations at risk
stockout_risk = (
    inventory_with_products[
        inventory_with_products["Stockout_Risk"]
    ]
    .assign(
        Stock_Gap=lambda data:
        data["Reorder_Level"] - data["Stock_Quantity"]
    )
    .sort_values(
        ["Warehouse", "Stock_Gap"],
        ascending=[True, False]
    )
)

print(stockout_risk[
    [
        "Product_ID",
        "Product_Name",
        "Brand",
        "Category",
        "Warehouse",
        "Stock_Quantity",
        "Reorder_Level",
        "Stock_Gap"
    ]
])

# Summary of stockout risk by warehouse
warehouse_risk = (
    stockout_risk
    .groupby("Warehouse", as_index=False)
    .agg(
        At_Risk_Product_Count=("Product_ID", "nunique"),
        Total_Stock_Gap=("Stock_Gap", "sum")
    )
    .sort_values(
        "At_Risk_Product_Count",
        ascending=False
    )
)

print(warehouse_risk)