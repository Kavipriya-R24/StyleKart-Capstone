#CREATE DATABASE stylekart_capstone;
USE stylekart_capstone;

#SHOW TABLES;
#SELECT *
#FROM Customers
#LIMIT 5;
#SELECT
 #   Order_Status,
  #  COUNT(Order_ID) AS Order_Count
#FROM Orders
#GROUP BY Order_Status
#ORDER BY Order_Count DESC;
#SELECT
  #  p.Category,
 #   SUM(o.Order_Amount) AS Total_Revenue
#FROM Orders o
#JOIN Products p
 #   ON o.Product_ID = p.Product_ID
#GROUP BY p.Category
#ORDER BY Total_Revenue DESC;
#SELECT
 #   p.Product_Name,
  #  SUM(o.Quantity) AS Total_Units,
   # SUM(o.Order_Amount) AS Total_Revenue
#FROM Orders o
#JOIN Products p
 #   ON o.Product_ID = p.Product_ID
#GROUP BY p.Product_Name
#ORDER BY Total_Revenue DESC
#LIMIT 10;
#SELECT
 #   c.Region,
  #  COUNT(o.Order_ID) AS Order_Count,
   # SUM(o.Order_Amount) AS Total_Revenue
#FROM Orders o
#JOIN Customers c
#    ON o.Customer_ID = c.Customer_ID
#GROUP BY c.Region
#ORDER BY Total_Revenue DESC;
#SELECT
 #   Payment_Method,
  #  Payment_Status,
   # COUNT(*) AS Transaction_Count,
    #SUM(Amount) AS Total_Amount
#FROM Payments
#GROUP BY Payment_Method, Payment_Status
#ORDER BY Total_Amount DESC;
#SELECT
 #   Return_Reason,
  #  COUNT(*) AS Return_Count,
   # SUM(Return_Quantity) AS Total_Units,
    #SUM(Refund_Amount) AS Total_Refund
#FROM Returns
#GROUP BY Return_Reason
#ORDER BY Total_Refund DESC;
SELECT
    i.Product_ID,
    p.Product_Name,
    i.Stock_Quantity,
    i.Reorder_Level,
    CASE
        WHEN i.Stock_Quantity <= i.Reorder_Level
        THEN 'Reorder Required'
        ELSE 'Sufficient'
    END AS Stock_Status
FROM Inventory i
JOIN Products p
    ON i.Product_ID = p.Product_ID
ORDER BY i.Stock_Quantity ASC;
