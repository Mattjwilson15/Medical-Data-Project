import csv as csv


# usefull stats pulled from csv to use for calculations later "no = non smoker as no is the data in smoker columb is stored as yes or no"
stats = {
    'avg_cost_male': 0,
    'total_male_no': 0,
    'avg_cost_female': 0,
    'total_female_no': 0,
    'avg_cost_male_smoker' : 0,
    'total_male_yes' : 0,
    'avg_cost_female_smoker' : 0,
    'total_female_yes' : 0
    
}


# open csv file and saving data needed line by line
with open('insurance.csv') as insurance_data:
    data = csv.DictReader(insurance_data)
    total_cost_male_no = 0
    total_cost_male_yes = 0
    total_cost_female_no = 0
    total_cost_female_yes = 0
    for line in data:        
        if line['sex'] == 'male' and line['smoker'] == 'no':
            total_cost_male_no += float(line['charges'])
            stats['total_male_no'] += 1
        elif line['sex'] == 'female' and line['smoker'] == 'no':
            total_cost_female_no += float(line['charges'])
            stats['total_female_no'] += 1
        elif line['sex'] == 'male' and line['smoker'] == 'yes':
            total_cost_male_yes += float(line['charges'])
            stats['total_male_yes'] += 1
        elif line['sex'] == 'female' and line['smoker'] == 'yes':
            total_cost_female_yes += float(line['charges'])
            stats['total_female_yes'] += 1

# calculating avgs for all
stats['avg_cost_female'] = round(total_cost_female_no / stats['total_female_no'],3)
stats['avg_cost_female_smoker'] = round(total_cost_female_yes / stats['total_female_yes'],3)
stats['avg_cost_male'] = round(total_cost_male_no / stats['total_male_no'],3)
stats['avg_cost_male_smoker'] = round(total_cost_male_yes / stats['total_male_yes'],3)
dif_in_gen_smoker = round(stats['avg_cost_male_smoker'] - stats['avg_cost_female_smoker'],3)
dif_in_gen_nonsmoker = round(stats['avg_cost_female'] - stats['avg_cost_male'], 3)

print('-------------Results-------------')
print(f'The Avg difference in cost between a male smoker and male non-smoker is: {stats["avg_cost_male_smoker"]-stats["avg_cost_male"]}')
print(f'The Avg difference in cost between a female smoker and female non-smoker is: {stats["avg_cost_female_smoker"]-stats["avg_cost_female"]}')


print(f'This means a male smoker will pay {dif_in_gen_smoker} more than a female smoker while a male non-smoker will pay {dif_in_gen_nonsmoker} less than a female non-smoker')




