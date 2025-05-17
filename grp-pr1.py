dic = [
    {"code": "AK", "rate": "100", "amount": "1000"},
    {"code": "AC", "rate": "200", "amount": "1000"},
    {"code": "AD", "rate": "300", "amount": "1000"},
    {"code": "AK", "rate": "100", "amount": "1000"}
]

grouped = {}

for item in dic:
    code = item["code"]
    rate = int(item["rate"])
    amount = int(item["amount"])

    key = (code, rate)

    if key not in grouped:
        grouped[key] = {
            "total_amount": 0,
            "count": 0,

        }

    grouped[key]["total_amount"] += amount
    grouped["count"] += 1


# Convert to list of dicts
result = []
for (code, rate), data in grouped.items():
    result.append({
        "code": code,
        "rate": str(rate),
        "total_amount": str(data["total_amount"]),
        "count": data["count"],

    })

print(result)
