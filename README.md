# Power BI — Sales Analytics and Semantic Measure Design

I assembled this analytics project around a practical requirement: a dashboard is only useful if its underlying calculations are consistent and independently verifiable. The repository provides the **data, Power Query import pipeline, DAX measure definitions, dashboard specification, and a Python reconciliation utility**.

## Deliverables

- Synthetic sales-orders dataset (`data/sales_orders.csv`)
- Power Query M transformation with typing, revenue calculation and basic filtering
- DAX measures for revenue, units, order count and average order value
- A dashboard blueprint with cards, trends, category and regional segmentation
- Independent Python data reconciliation and GitHub CI

## Run and build

```bash
python validate_sales.py
python -m pip install pytest
python -m pytest -q
```

In Power BI Desktop, choose **Transform Data → Advanced Editor**, paste `powerquery/SalesOrders.pq` and point its local path to the CSV; create measures from `dax/Measures.dax` one at a time. See [the dashboard specification](docs/DASHBOARD_SPEC.md).

**Honest scope:** This repository does not contain a `.pbix` file and no native Power BI report execution is claimed. It is a working, testable source-and-specification project awaiting the final desktop dashboard artifact.
