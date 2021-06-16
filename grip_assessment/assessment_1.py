import pandas as pd


def create_dataframe(records: list) -> pd.DataFrame:
    """For the list of records builds a pandas DataFrame

    :param records: The database extract

    :returns: DataFrame
    """

    # Create a DataFrame from records
    df = pd.DataFrame(records, columns=['user_id', 'device', 'action', 'date_actioned'])
    return df


def get_users(records: list, action: str, start_time: int, end_time: int):
    """A function that takes in records (an array of all the database
    records), an `action`, a `start_time, end_time` time window and returns all user ids
    that performed that action within that time window.

    end_time must be greater than start_time if not a ValueError is raised

    :param records: The database extract
    :param action: The action to search the records for
    :param start_time: The start of the time window, timestamp format
    :param end_time: The end of the time window, timestamp format

    :returns: List of users, empty if no users found
    """

    if end_time < start_time:
        raise ValueError('end_time must be greater than start_time')

    df = create_dataframe(records)

    # Take the first view of the dataframe for all the matching actions
    action_df = df[df['action'] == action]

    # from the actions dataframe find all the records where date actioned is between start and end times
    result_df = action_df[(action_df['date_actioned'] >= start_time) & (action_df['date_actioned'] <= end_time)]

    # finally get user_id as a Series return all the unique values as a list
    users = list(result_df['user_id'].unique())
    return users


def get_playback_time(user_id: int, records: list) -> int:
    """A function that takes in a `user_id` and an array of all the database
    records, and reports a user’s total "unique" playback time in seconds.

    :param user_id: The action to search the records for
    :param records: The database extract

    :returns: The number of seconds if user is found. None if user not present in the data
    """

    df = create_dataframe(records)

    # Get all the records for the user_id
    user_df = df[df['user_id'] == user_id]

    # If no records found for the user return None
    if len(user_df.index) == 0:
        return None

    # Get all the start rows return the date_actioned series and compute the min value
    min_start = user_df[user_df['action'] == 'start']['date_actioned'].min()

    # Get all the stop rows return the date_actioned series and compute the max value
    max_stop = user_df[user_df['action'] == 'stop']['date_actioned'].max()

    # Just check if max greater than min, this also filters out missing values
    if max_stop >= min_start:
        return max_stop - min_start
    return 0
