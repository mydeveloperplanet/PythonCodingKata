# Write some data to a CSV file export.csv
# Write a header
# Use columns ID and Item
# Use references to Monty Python for the items
# Tip: https://docs.python.org/3/library/csv.html
import csv

with open('export.csv', 'w', newline='') as csvfile:
    fieldnames = ['ID', 'Item']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'ID': '0', 'Item': 'Beans'})
    writer.writerow({'ID': '1', 'Item': 'Spam'})
    writer.writerow({'ID': '2', 'Item': 'Eggs'})
    writer.writerow({'ID': '3', 'Item': 'Shrubbery'})
