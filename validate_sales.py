"""Independent Power BI source reconciliation without requiring Power BI Desktop."""
import csv,json,sys
from collections import defaultdict
from decimal import Decimal
from pathlib import Path

def summary(path):
    data=list(csv.DictReader(Path(path).open(newline='',encoding='utf-8')))
    seen=set();by_region=defaultdict(lambda:Decimal('0'));total=Decimal('0');units=0
    for row in data:
        if row['order_id'] in seen: raise ValueError('Duplicate order')
        seen.add(row['order_id'])
        q=int(row['quantity']);price=Decimal(row['unit_price'])
        if q<=0 or price<0:raise ValueError('Invalid amount')
        revenue=price*q;total+=revenue;by_region[row['region']]+=revenue;units+=q
    return {'orders':len(seen),'units':units,'revenue_usd':str(total),
            'aov_usd':str((total/len(seen)).quantize(Decimal('0.01'))) if seen else None,
            'revenue_by_region':{k:str(v) for k,v in sorted(by_region.items())}}

if __name__=='__main__':
    print(json.dumps(summary(sys.argv[1] if len(sys.argv)>1 else 'data/sales_orders.csv'),indent=2))
