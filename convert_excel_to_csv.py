import pandas as pd

excel_file = "StyleKart_Capstone_Dataset.xlsx"

sheets = [
    "Customers",
    "Products",
    "Orders",
    "Payments",
    "Returns",
    "Inventory"
]

for sheet in sheets:

    df = pd.read_excel(
        excel_file,
        sheet_name=sheet
    )

    csv_file = f"{sheet}.csv"

    df.to_csv(
        csv_file,
        index=False
    )



    import pandas as pd

orders = pd.read_excel(
    "StyleKart_Capstone_Dataset.xlsx",
    sheet_name="Orders"
)

products = pd.read_excel(
    "StyleKart_Capstone_Dataset.xlsx",
    sheet_name="Products"
)

print("Orders:", orders.shape)
print("Products:", products.shape)

merged = orders.merge(
    products,
    on="Product_ID"
)
print(merged.head())
print(merged.shape)


category_revenue = (
    merged
    .groupby("Category")["Order_Amount"]
    .sum()
    .sort_values(ascending=False)
)

print(category_revenue)
orders["Order_Date"] = pd.to_datetime(
    orders["Order_Date"]
)

orders["Month"] = orders[
    "Order_Date"
].dt.to_period("M")

monthly = (
    orders
    .groupby("Month")["Order_Amount"]
    .sum()
)

print(monthly)



import matplotlib.pyplot as plt
monthly.plot(
    kind="line",
    title="Monthly Revenue — StyleKart",
    xlabel="Month",
    ylabel="Revenue",
    figsize=(10, 4)
)

plt.tight_layout()
plt.show()



customer_summary = (
    orders
    .groupby("Customer_ID")
    .agg(
        Order_Count=("Order_ID", "count"),
        Total_Spend=("Order_Amount", "sum"),
        Avg_Order_Val=("Order_Amount", "mean")
    )
    .reset_index()
)
print(customer_summary.head())

print(
    "Customer summary shape:",
    customer_summary.shape
)


# Load Returns sheet
returns = pd.read_excel(
    "StyleKart_Capstone_Dataset.xlsx",
    sheet_name="Returns"
)

print("Returns shape:", returns.shape)
print(returns.head())

return_summary = (
    returns
    .groupby("Return_Reason")
    .agg(
        Count=("Return_Reason", "count"),
        Units=("Return_Quantity", "sum"),
        Refund=("Refund_Amount", "sum")
    )
    .sort_values(
        "Refund",
        ascending=False
    )
)

print(return_summary)








from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
features = customer_summary[
    [
        "Total_Spend",
        "Order_Count",
        "Avg_Order_Val"
    ]
]
print(features.head())
scaler = StandardScaler()
features_scaled = scaler.fit_transform(
    features
)
kmeans = KMeans(
    n_clusters=3,
    random_state=42
)
kmeans.fit(features_scaled)
customer_summary["Segment"] = (
    kmeans.labels_
)
print(
    customer_summary.head()
)
segment_summary = (
    customer_summary
    .groupby("Segment")
    [
        [
            "Total_Spend",
            "Order_Count",
            "Avg_Order_Val"
        ]
    ]
    .mean()
)

print(segment_summary)
inertias = []

k_range = range(2, 10)

for k in k_range:
    km = KMeans(
        n_clusters=k,
        random_state=42
    )

    km.fit(features_scaled)

    inertias.append(
        km.inertia_
    )
plt.plot(
    k_range,
    inertias,
    marker="o"
)

plt.xlabel(
    "Number of Clusters (k)"
)

plt.ylabel(
    "Inertia"
)

plt.title(
    "Elbow Method — StyleKart"
)

plt.show()
print(segment_summary)
customer_summary.to_excel(
    "StyleKart_Customer_Segments.xlsx",
    index=False
)
