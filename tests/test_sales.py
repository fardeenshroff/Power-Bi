from pathlib import Path
from decimal import Decimal
from validate_sales import summary

def test_sales_measure_reconciliation():
    p=Path(__file__).resolve().parents[1]/'data/sales_orders.csv'
    s=summary(p)
    assert s['orders']==10 and s['units']==31
    assert Decimal(s['revenue_usd'])==sum(map(Decimal,s['revenue_by_region'].values()))
