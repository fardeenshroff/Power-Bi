# Sales performance dashboard — implementation specification

## Dataset

Import `data/sales_orders.csv` as a single fact table using the query under `powerquery/SalesOrders.pq`. **Change the file path** in the Power Query `Source` step to the local file before running. The dataset is entirely synthetic. This repository contains DAX/Power Query source, **not a packaged PBIX**; it has not been opened in Power BI Desktop within the automated checks.

## Page 1: Commercial overview

| Visual | Configuration |
|---|---|
| KPI cards | Total Revenue, Order Count, Total Units, Average Order Value |
| Monthly line chart | Axis: order_date month; Value: Total Revenue |
| Region bar chart | Axis: region; Value: Total Revenue |
| Category split | Category and Total Revenue |
| Order-detail table | order_id, order_date, product, customer, quantity, unit_price |
| Slicers | region, category, month |

## Quality / transparency

Reconcile the report totals with `python validate_sales.py`. The local validator calculates the same metrics using decimal arithmetic, independently of Power BI. For future data, define a Date dimension and star schema, decide whether order IDs represent orders or line items, and add security and incremental refresh.
