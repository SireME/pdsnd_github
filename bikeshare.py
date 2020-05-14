import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        city=input('What city do you intend to explore from? Chicago?,New York City? or Washington?\n')
        city=city.lower()
        if city not in ('chicago','new york city','washington'):
            print('That does not seem correct')
        else:
            break


    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
        month=input('Your month please...\nyou can Choose to explore from all months indicate with "all" or choose from "january" to "june".\n')
        month=month.lower()
        if month not in ('all','january','february','march','april','may','june'):
            print("Oh oh Please check what you typed again and enter the correct value")
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day=input('please choose day("monday" to "sunday") or "all" if you want to explore from every day of the week.\n')
        day=day.lower()
        if day not in ('all','monday','tuesday','wednesday','thursday','friday','saturday','sunday'):
          print("Oh oh Please check what you typed again and enter the correct value")
        else:
            break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # using the index of the days list to get the corresponding int
        days=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
        day = days.index(day) + 1
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    print('Most common month is :\n Month number {} '.format(df['month'].mode()[0]))

    # TO DO: display the most common day of week
    df['week_day'] = df['Start Time'].dt.day
    print('Most common week day  is :\n Day number {}'.format(df['week_day'].mode()[0]))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print('Most common hour is :\n Hour number {}'.format(df['hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station= df['Start Station'].mode()[0]
    print('The most commonly used start station is : {}'.format(popular_start_station))
    # TO DO: display most commonly used end station
    popular_end_station= df['End Station'].mode()[0]
    print('The most commonly used end station is : {}'.format(popular_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['combination']=df['Start Station'] +" "+ df['End Station']
    print('Most popular combination for start and End stations are : {}'.format(df['combination'].mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print('The total travel time is {} hours'.format(str(total_travel_time/3600)))

    # TO DO: display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print('The average travel time is {} minutes'.format((mean_travel_time/60)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types=df['User Type'].value_counts()
    print('User types in categories are :\n {}'.format(user_types))

    #handling erros that can arise for Washington
    try:
        # TO DO: Display counts of gender
        gender_count=df['Gender'].value_counts()
        print('Total males and females are :\n {}'.format(gender_count))
    except Exception as e:
        print('Total males and females are :\n Not applicable for Washington')

    #handling erros that can arise for Washington
    try:
        # TO DO: Display earliest, most recent, and most common year of birth
        print('year of Birth\n','Earliest: {}'.format(df['Birth Year'].min()))
        print('Mosr Recent: {}'.format(df['Birth Year'].max()))
        print('Most common: {}'.format(df['Birth Year'].mode()[0]))
    except Exception as e:
        print('Earliest, Most Recent, and Most Common year of birth\n not applicable for washington')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
     """Prompts the user if they want to see the raw data"""
     data =''
     counter=0
     boolean_ans=('yes','no')
     while data not in boolean_ans:
         data=input('Do you want to see the raw data? type yes or no :\n')
         data=data.lower()
         if data =='yes':
              print(df.head())
         elif data not in boolean_ans:
              print('Wrong Input please choose YES or NO')

     while data =='yes':

          counter +=5
          data=input('Do you want to see more  raw data? type yes or no:\n')
          data=data.lower()
          if data =='yes':
             print(df[counter:counter+5])
             # counter1 +=5
             #counter2 +=6
          elif data=="no":
             break




def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
