import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("./adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df["race"].value_counts()

    # What is the average age of men?
    male_data = df[df["sex"]== "Male"]
    average_age_men = round(male_data["age"].mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    bachelorCount= df["education"].value_counts().get("Bachelors",0)
    percentage_of_bachelors= (bachelorCount/df["education"].count())*100
    percentage_bachelors = round(percentage_of_bachelors,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    advanced_education = df[df["education"].isin(["Bachelors","Masters","Doctorate"])]
    advanced_education_salary_50k = advanced_education[advanced_education["salary"] == ">50K"]
    percentage_of_rich = (advanced_education_salary_50k.shape[0]/advanced_education.shape[0])*100
    # What percentage of people without advanced education make more than 50K?
    regular_education = pd.concat([df, advanced_education]).drop_duplicates(keep=False)
    regular_50 = regular_education[regular_education["salary"]==">50K"]
    regular_percent = (len(regular_50)/len(regular_education))*100
    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = advanced_education
    lower_education = regular_50

    # percentage with salary >50K
    higher_education_rich = round(percentage_of_rich,1)
    lower_education_rich = round(regular_percent,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?

    min_work_hours = df["hours-per-week"].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_hours_workers = df[df["hours-per-week"] == 1]
    percentage_min_50k = (min_hours_workers[min_hours_workers["salary"] ==">50K"].shape[0]/min_hours_workers["salary"].shape[0])*100
    num_min_workers = min_hours_workers.shape[0]

    rich_percentage = round(percentage_min_50k,1)

    # What country has the highest percentage of people that earn >50K?
    countries = df["native-country"].unique()
    #initializing the dictionary to store percentages
    countries_percentage ={}
    for country in countries:
        country_data = df[df["native-country"] == country]
        country_count = country_data.shape[0]
        country_rich_count = country_data[country_data["salary"] == ">50K"].shape[0]
        country_salary_percentage = (country_rich_count/country_count)*100
        countries_percentage[country] = round(country_salary_percentage,1)
    max_country=max(countries_percentage, key=countries_percentage.get)
    highest_earning_country = max_country
    highest_earning_country_percentage = countries_percentage[max_country]

    # Identify the most popular occupation for those who earn >50K in India.
    rich_india = df[(df["native-country"]=="India") & (df["salary"] == ">50K")]
    top_IN_occupation = rich_india["occupation"].value_counts().idxmax()
    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
