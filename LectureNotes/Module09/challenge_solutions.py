def word_frequencies(file):
    frequencies = {}
    with open(file, "r") as file:
        content = file.read()
        for word in content.split():
            if word in frequencies:
                frequencies[word] += 1
            else:
                frequencies[word] = 1
        return frequencies
    
def print_selected_municipalities():
  with open("data/dutch_municipalities.csv", "r") as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter='\t')
    for row in csvreader:
        income = row["avg_household_income_2012"]
        if income != "" and int(row["avg_household_income_2012"]) > 40000:
            print(f'{row["municipality"]}: {row["province"]}')

def safe_print_selected_municipalities():
    with open("data/dutch_municipalities.csv", "r") as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter='\t')
    for row in csvreader:
        try: 
            if int(row["avg_household_income_2012"]) > 40000:
                print(f'{row["municipality"]}: {row["province"]}')
        except ValueError:
            print(f'No INCOME for --> {row["municipality"]}: {row["province"]}')
