import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')
    df.isnull().sum()

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count =  df["race"].value_counts()

    # What is the average age of men?
    men = df[df["sex"] == "Male"]
    average_age_men = men["age"].mean()
    average_age_men = round(average_age_men,1)

    # What is the percentage of people who have a Bachelor's degree?
    total_people = len(df)
    bach = (df["education-num"] == 13).sum()
    print(bach)
    percentage_bachelors = (bach/total_people)*100
    percentage_bachelors = round(percentage_bachelors,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    #degree_count =  df["education-num"].value_counts()
    #print(degree_count)
    # with and without `Bachelors`, `Masters`, or `Doctorate`
    bach1 = len(df[(df["education-num"] == 13) & (df["salary"] == ">50K")])
    
    bach11 = len(df[(df["education-num"] == 14) & (df["salary"] == ">50K")])
    
    bach12 = len(df[(df["education-num"] == 16) & (df["salary"] == ">50K")])
    
    Num_of_people_higher_education = (df["education-num"] ==13).sum()+(df["education-num"] ==16).sum()+(df["education-num"] ==14).sum()   
    bach2 = (df["salary"] == ">50K").sum()
    bach2 = bach2 - (bach1 + bach11 + bach12)
    print(bach2)
    People_with_lower_education = total_people - (Num_of_people_higher_education)

    # percentage with salary >50K
    higher_education_rich = round(((bach1+bach11+bach12)/Num_of_people_higher_education)*100,1)
    lower_education_rich = round((bach2/People_with_lower_education)*100,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = (df["hours-per-week"] == min_work_hours).sum()
    people_with_min_high_wage = len(df[(df["hours-per-week"] == min_work_hours) & (df["salary"] == ">50K")])

    rich_percentage = round((people_with_min_high_wage/num_min_workers)*100,1)

    # What country has the highest percentage of people that earn >50K?
    filtered_df = df[df['salary'] == ">50K"]
    country_count =  filtered_df["native-country"].value_counts()
    total_count = df["native-country"].value_counts()
    
    percentage = (country_count / total_count) * 100

    # Find the country with the highest percentage
    highest_earning_country = percentage.idxmax()
    highest_earning_country_percentage = round(percentage[highest_earning_country],1)


    # Identify the most popular occupation for those who earn >50K in India.
    filtered1_df = filtered_df[filtered_df['native-country'] == "India"]
    occupation_count =  filtered1_df["occupation"].value_counts()
    top_IN_occupation = occupation_count.idxmax()
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
