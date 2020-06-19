import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ('january', 'february', 'march', 'april', 'may', 'june','all')
weekdays = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all')
cities = ['chicago','washington','new_york_city']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
<<<<<<< HEAD
    # get user input for city (chicago, new york city, washington). 
||||||| merged common ancestors
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
=======
    # get user input for city (chicago, new york city, washington).
>>>>>>> refactoring

    city = input('Which city would you like to analyze? Available cities are Chicago, New York City, and Washington.\n').lower()
    while city not in cities:
        print('Invalid city input. Please enter "Chicago", "New York City", or "Washington".')
        city = input('Which city would you like to analyze?\n').lower()
            
    # filter options:
    filt_option = input('Would you like to filter the data or not. Enter yes or no.\n')
    
    while filt_option.lower() != 'yes' and filt_option.lower != 'no':
        print('Invalid choice.')
        filt_option = input('Would you like to filter the data or not. Enter yes or no.\n')
        
    if filt_option.lower() == 'no':
        month = 'all'
        day = 'all'
        
    # get user input for month (all, january, february, ... , june)
    else:
        month = input('Which month would you like to analyze? Available months are from January to June. If you would like to see data in all months, enter "all".\n').lower()
        while month not in months: 
            print('\n Invalid month input. Please input a month from January to June, spelled in full or enter "all" for all the records.\n')
            month = input('Which month would you like to analyze? ').lower()
    # get user input for day of week (all, monday, tuesday, ... sunday)
        day = input('Which day of the week would you like to analyze? Please enter the full weekday name. If you would like to see dat in all weekdays, enter "all".\n').lower()
        while day not in weekdays:
            print('\n Invalid weekday input. Please enter the full weekday name or enter "all" for all the records.\n')
            day = input('Which day of the week would you like to analyze?\n').lower()

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
    df = pd.read_csv(CITY_DATA[city.lower()])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday #Monday=0,Sunday=6
    
    # filter by month if applicable
    
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        filt1 = (df['month'] == month)
        df = df[filt1]

    # filter by day of week if applicable
    
    if day != 'all':
        # filter by day of week to create the new dataframe
        weekday = weekdays.index(day)
        filt2 = (df['day_of_week'] == weekday) 
        df = df[filt2]
        
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month_index = int(df.mode()['month'][0])
    popular_month = months[popular_month_index-1].title()
    print('The most popular month is {}'.format(popular_month))

    # display the most common day of week
    popular_weekday_index = int(df.mode()['day_of_week'][0])
    popular_weekday = weekdays[popular_weekday_index].title()
    print('The most popular weekday is {}'.format(popular_weekday))

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df.mode()['hour'][0]
    print('The most popular hour is {}'.format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start = df.mode()['Start Station'][0]
    print('The most commonly used start station is {}'.format(popular_start))

    # display most commonly used end station
    popular_end = df.mode()['End Station'][0]
    print('The most commonly used end station is {}'.format(popular_end))

    # display most frequent combination of start station and end station trip
    df['start_end'] = 'From ' + df['Start Station'] + ' To ' + df['End Station'] 
    popular_combo = df.mode()['start_end'][0]
    print('The most frequent trip is {}'.format(popular_combo))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time = df['Trip Duration'].sum()
    print("Total travel time is {}".format(total_time))
    # display mean travel time
    avg_time = df['Trip Duration'].mean()
    print("Average travel time is {}".format(avg_time))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # Display counts of gender
    if city == 'washington':
        print('User gender information is not avaialbe for {}'.format(city.title()))
    else:
        user_gender = df['Gender'].value_counts()
        print(user_gender)
    
    # Display earliest, most recent, and most common year of birth
    if city == 'washington':
        print('User birth year information is not avaialbe for {}'.format(city.title()))
    else:
        user_birth_min = df['Birth Year'].min()
        user_birth_max = df['Birth Year'].max()
        user_birth_mode = df['Birth Year'].mode()[0] 
        print('The earliest year of birth is {}. The most recent year of birth is {}. The msot common year of birth is {}.'.format(user_birth_min, user_birth_max, user_birth_mode))
    
def load_raw(df): 
    """Load 5 raw records a time per user request."""
    raw_date = input("Would you like to see some raw data? Enter yes or no. \n")
    i = 0
    while raw_date.lower() == 'yes':
        print('\nLoading 5 records...\n')
        print(df.iloc[i:i+5])
        i +=5
        raw_date = input("Would you like to see some raw data? Enter yes or no. \n")

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        load_raw(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
