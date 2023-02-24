import csv
import Parser
import pandas as pd


theme = "python"
pages = 1
file_name = "data.csv"

with open(file_name, "a", newline='', encoding="utf-8") as file:
    column_name = ["Title", "Specialization", "Salary", "Age", "Employment", "Work schedule",
                   "Experience years", "Experience month", "Citizenship", "Sex", "link to resume"]
    writer = csv.writer(file)
    writer.writerow(column_name)

Parser.go_throw_pages(theme, pages, file_name)

