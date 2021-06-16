# Software Developer Technical Interview Questions
For questions 1 - 6, refer to this table of data:

Suppose we have a database that tracks users’ video playback actions over time

| user_id | device       | action | date_actioned (simplified UNIX timestamp) |
|:-------:|:------------:|:------:|:------:|
|1        | "Windows 10" | "start"| 100
|2        | "OSX 15.4"   | "start"| 200
|1        | "iPhone 8s"  | "start"| 250
|1        | "Windows 10" | "stop" | 370
|1        | "iPhone 8s"  | "stop" | 410
|2        | "OSX 15.4"   | "stop" | 490
|3        | "Android 9.1"| "start"| 700
|...      | ...          |...     | ...
1. Write a function that takes in records (an array of all the database
records), an `action`, a `start_time, end_time` time window and returns all user ids
that performed that action within that time window.
   E.g. `get_users(records, "start", 700, 900)` will return the result `[3]`
2. Write a function that takes in a `user_id` and an array of all the database
records, and reports a user’s total "unique" playback time in seconds.
   E.g. `get_playback_time(1, records)` will return `310` // based on the above example
3. Write inline comments for your functions where appropriate.
4. Write appropriate unit tests for your functions above
5. Identify any possible shortcomings or limitations of both your functions if any.


For questions 6 - 8 use the following example Python dictionary objects/lists

A user has access to a set of applications based on the following list:

```python
[
    {
        "app_id": 1
    },
    {
        "app_id": 2
    },
    {
        "app_id": 3
    },
    ...
]
```

Each application has a series of features available like so:

```python
[
    {
        "app_id": 1,
        "features_available": [1, 2, 3]
    },
    {
        "app_id": 2,
        "features_available": [3, 4, 5, 7]
    },
    {
        "app_id": 3,
        "features_available": [3, 12]
    },
    ...
]
```
And each user has feature specific access like so:
```python
[
    {
        "user_id": 1,
        "features_allowed": [1, 2, 5]
    },
    {
        "user_id": 2,
        "features_allowed": [1, 2, 3, 4, ]
    },
    {
        "user_id": 3,
        "features_allowed": []
    },
    ...
]
```

6. Write a Python 3 function that takes in a user_id, the above three lists and returns a
dictionary object that looks something like this:
```python
{
    "user_id": 1,
    "application_permissions": [
        {
            "app_id": 1,
            "features_allowed": [1, 2]
        },
        {
            "app_id": 2,
            "features_allowed": [5]
        },
        {
            "app_id": 3,
            "features_allowed": []
        },
        ...
    ]
}
```
In other words, return a dictionary object which shows, for all allowed applications, the allowed
features for a user.
7. Write appropriate unit tests for your functions above
8. Identify any possible shortcomings or limitations of both your functions if any.