from datetime import datetime, timedelta
from collections import defaultdict
from calendar import monthrange


def generate_monthly_bill(item_list: list, target_month: str) -> dict:
    year, month = map(int, target_month.split("-"))
    month_start = datetime(year, month, 1)
    last_day = monthrange(year, month)[1]
    month_end = datetime(year, month, last_day)

    grouped_items = defaultdict(lambda: {"qty": 0, "amount": 0.0})
    total_revenue = 0.0

    for item in item_list:
        item_start = datetime.strptime(item["start_date"], "%Y-%m-%d")
        item_stop = datetime.strptime(item["stop_date"], "%Y-%m-%d")

        active_start = max(item_start, month_start)
        active_end = min(item_stop, month_end)

        if active_start > active_end:
            continue

        days_active = (active_end - active_start).days + 1
        total_days = (month_end - month_start).days + 1
        qty = int(item["qty"])
        rate = float(item["rate"])
        prorated_amount = round((rate * qty) * (days_active / total_days), 2)
        billing_period = f"{active_start.strftime('%Y-%m-%d')} to {active_end.strftime('%Y-%m-%d')}"
        key = (item["item_code"], rate, billing_period)
        grouped_items[key]["qty"] += qty
        grouped_items[key]["amount"] += prorated_amount

    print(grouped_items)
    line_items = []
    for (item_code, rate, billing_period), values in grouped_items.items():
        amount = round(values["amount"], 2)
        line_items.append({
            "item_code": item_code,
            "rate": rate,
            "qty": values["qty"],
            "amount": amount,
            "billing_period": billing_period
        })
        total_revenue += amount

    return {
        "line_items": line_items,
        "total_revenue": round(total_revenue, 2)
    }


item_list = [
    {
        "idx": 1,
        "item_code": "Executive Desk (4*2)",
        "sales_description": "Dedicated Executive Desk",
        "qty": 10,
        "rate": "1000",
        "amount": "10000",
        "start_date": "2023-11-01",
        "stop_date": "2024-10-17",

    },
    {
        "idx": 2,
        "item_code": "Executive Desk (4*2)",
        "qty": "10",
        "rate": "1080",
        "amount": "10800",
        "start_date": "2024-10-18",
        "stop_date": "2025-10-31",

    },
    {
        "idx": 3,
        "item_code": "Executive Desk (4*2)",
        "qty": 15,
        "rate": "1080",
        "amount": "16200",
        "start_date": "2024-11-01",
        "stop_date": "2025-10-31",

    },
    {
        "idx": 4,
        "item_code": "Executive Desk (4*2)",
        "qty": 5,
        "rate": "1000",
        "amount": "5000",
        "start_date": "2024-11-01",
        "stop_date": "2025-10-31",

    },
    {
        "idx": 6,
        "item_code": "Manager Cabin",
        "qty": 7,
        "rate": "5000",
        "amount": 35000,
        "start_date": "2024-12-15",
        "stop_date": "2025-10-31",

    },
    {
        "idx": 7,
        "item_code": "Manager Cabin",
        "qty": 10,
        "rate": 4600,
        "amount": 46000,
        "start_date": "2023-11-01",
        "stop_date": "2024-10-17",

    },
    {
        "idx": 8,
        "item_code": "Parking (2S)",
        "qty": 10,
        "rate": 1000,
        "amount": 10000,
        "start_date": "2024-11-01",
        "stop_date": "2025-10-31",

    },
    {
        "idx": 9,
        "item_code": "Parking (2S)",
        "qty": 10,
        "rate": 0,
        "amount": 0,
        "start_date": "2024-11-01",
        "stop_date": "2025-10-31",

    },
    {
        "idx": 10,
        "item_code": "Executive Desk (4*2)",
        "qty": "8",
        "rate": "1100",
        "amount": "8800",
        "start_date": "2024-11-15",
        "stop_date": "2025-01-31",

    },
    {
        "idx": 11,
        "item_code": "Manager Cabin",
        "qty": "3",
        "rate": "5200",
        "amount": "15600",
        "start_date": "2024-10-10",
        "stop_date": "2024-11-10",

    },
    {
        "idx": 12,
        "item_code": "Conference Table",
        "qty": 1,
        "rate": "20000",
        "amount": "20000",
        "start_date": "2024-11-05",
        "stop_date": "2024-11-20",

    },
    {
        "idx": 13,
        "item_code": "Parking (2S)",
        "qty": 5,
        "rate": "1000",
        "amount": "5000",
        "start_date": "2024-11-15",
        "stop_date": "2025-02-28",

    },
    {
        "idx": 14,
        "item_code": "Reception Desk",
        "qty": 2,
        "rate": "7000",
        "amount": "14000",
        "start_date": "2024-11-01",
        "stop_date": "2025-03-31",

    },
    {
        "idx": 15,
        "item_code": "Reception Desk",
        "qty": 1,
        "rate": "7000",
        "amount": "7000",
        "start_date": "2024-11-10",
        "stop_date": "2024-11-25",

    },
    {
        "idx": 16,
        "item_code": "Breakout Area",
        "qty": 3,
        "rate": "3000",
        "amount": "9000",
        "start_date": "2024-01-01",
        "stop_date": "2024-01-31",

    }
]
result = generate_monthly_bill(item_list, "2024-11")
print(result)
