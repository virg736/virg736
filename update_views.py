import json
import matplotlib.pyplot as plt
from datetime import datetime

json_file = "profile-views.json"
chart_file = "profile-views-chart.png"
badge_file = "profile-views-badge.svg"

with open(json_file, "r") as f:
    data = json.load(f)

today = datetime.now().strftime("%Y-%m-%d")
views_today = data["views"][-1]["count"] + 1 if data["views"] else 1

data["views"].append({"date": today, "count": views_today})

with open(json_file, "w") as f:
    json.dump(data, f, indent=4)

dates = [v["date"] for v in data["views"]]
counts = [v["count"] for v in data["views"]]

plt.figure(figsize=(10,5))
plt.plot(dates, counts)
plt.xlabel("Date")
plt.ylabel("Profile Views")
plt.title("GitHub Profile Views Evolution")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(chart_file)

badge_svg = f"""
<svg xmlns="http://www.w3.org/2000/svg" width="150" height="30">
  <rect width="150" height="30" fill="#555"/>
  <rect x="80" width="70" height="30" fill="#007BFF"/>
  <text x="10" y="20" fill="white" font-size="14">Profile views</text>
  <text x="95" y="20" fill="white" font-size="14">{views_today}</text>
</svg>
"""

with open(badge_file, "w") as f:
    f.write(badge_svg)
