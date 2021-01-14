import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTHS = { 'january': 1,
           'february': 2,
           'march': 3,
           'april': 4,
           'may': 5,
           'june': 6,
           'july': 7,
           'august': 8,
           'september': 9,
           'october': 10,
           'november': 11,
           'december': 12 }

DAYS = { 'monday': 0,
         'tuesday': 1,
         'wednesday': 2,
         'thursday': 3,
         'friday': 4,
         'saturday': 5,
         'sunday': 6 }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington).
    # HINT: Use a while loop to handle invalid inputs
    print()
    print('   [C]hicago     [N]ew York City     [W]ashington')
    print()

    while True:
        city = str(input('Please choose a city: ')).lower().strip()

        if city[0] == 'c':
            city = 'chicago'
            break
        if city[0] == 'n':
            city = 'new york city'
            break
        if city[0] == 'w':
            city = 'washington'
            break

    # get user input for month (all, january, february, ... , june)
    print()
    print('   [All]        [Jan]uary    [Feb]ruary   [Mar]ch' )
    print('                [Apr]il      [May]        [Jun]e')
    print()

    while True:
        month = str(input('Please choose a month: ')).lower().strip()

        if month.startswith('all'):
            month = 'all'
            break
        if month == '1' or month.startswith('jan'):
            month = 'january'
            break
        if month == '2' or month.startswith('feb'):
            month = 'february'
            break
        if month == '3' or month.startswith('mar'):
            month = 'march'
            break
        if month == '4' or month.startswith('apr'):
            month = 'april'
            break
        if month == '5' or month.startswith('may'):
            month = 'may'
            break
        if month == '6' or month.startswith('jun'):
            month = 'june'
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    print()
    print('   [All]        [Sun]day     [Mon]day     [Tue]sday')
    print('   [Wed]nesday  [Thu]rsday   [Fri]day     [Sat]urday')
    print()

    while True:
        day = str(input('Please choose a weekday: ')).lower().strip()

        if day.startswith('all'):
            day = 'all'
            break
        if day.startswith('sun'):
            day = 'sunday'
            break
        if day.startswith('mon'):
            day = 'monday'
            break
        if day.startswith('tue'):
            day = 'tuesday'
            break
        if day.startswith('wed'):
            day = 'wednesday'
            break
        if day.startswith('thu'):
            day = 'thursday'
            break
        if day.startswith('fri'):
            day = 'friday'
            break
        if day.startswith('sat'):
            day = 'saturday'
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

    print('Analyzing',city.title(),'in',month.title(),'on',day.title())
    # filter by city
    df = pd.read_csv(CITY_DATA[city])

    # change type to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # filter by month
    if not month == 'all':
        df = df[df['Start Time'].dt.month==MONTHS[month]]

    # filter by weekday
    if not day == 'all':
        df = df[df['Start Time'].dt.weekday==DAYS[day]]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    mode_month = df['Start Time'].dt.month_name().mode().values[0]
    print('The most common month is:', mode_month)

    # display the most common day of week
    mode_weekday = df['Start Time'].dt.day_name().mode().values[0]
    print('The most common day of the week is:', mode_weekday)

    # display the most common start hour
    mode_starthour = df['Start Time'].dt.hour.mode().values[0]
    print('The most common start hour is:', mode_starthour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    mode_start = df['Start Station'].mode().values[0]
    print('The most common start station is:',mode_start)

    # display most commonly used end station
    mode_end = df['End Station'].mode().values[0]
    print('The most common end station is:',mode_end)

    # display most frequent combination of start station and end station trip
    trips = df['Start Station'] + ' -> ' + df['End Station']
    mode_trip = trips.mode().values[0]
    print('The most common trip is:',mode_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    delta_t = df['End Time'] - df['Start Time']

    # display total travel time
    print('Total Travel Time:', delta_t.sum())

    # display mean travel time
    print('Mean Travel Time:', delta_t.mean().round('S'))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    if 'User Type' in df.columns:
        print('Counts of User Types:')
        print(df['User Type'].value_counts())
        print()

    # Display counts of gender
    if 'Gender' in df.columns:
        print('Counts of Gender:')
        print(df['Gender'].value_counts())
        print()

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('Earliest Birth Year:',int(df['Birth Year'].min()))
        print('Most Recent Birth Year:',int(df['Birth Year'].max()))
        print('Most Common Birth Year:',int(df['Birth Year'].mode().values[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
