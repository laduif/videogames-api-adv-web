import os
import csv
import django

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "videogames_api.settings"
)

django.setup()

from games.models import Game

Game.objects.all().delete()

records_count = 0

with open("vgsales.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        
        if records_count >= 10000:
            break
        
        if row["Year"] == "N/A":
            continue

        game = Game(
            name=row["Name"],
            platform=row["Platform"],
            genre=row["Genre"],
            publisher=row["Publisher"],
            release_year=int(row["Year"]),
            na_sales=float(row["NA_Sales"]),
            eu_sales=float(row["EU_Sales"]),
            jp_sales=float(row["JP_Sales"]),
            other_sales=float(row["Other_Sales"]),
            global_sales=float(row["Global_Sales"])
        )

        game.save()

        records_count += 1

print("Imports successful.")
print(f"Games imported: {records_count}")