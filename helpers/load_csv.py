import csv

def load_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    return data

def load_test_data(file_path):
    with open(file_path, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            yield(
                row['city'],
                row['lat'],
                row['lon'],
                row['temp'],
                row['humidity'],
                row['weather']
            )   