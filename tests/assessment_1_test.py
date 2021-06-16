import pytest

from grip_assessment.assessment_1 import get_users, get_playback_time


def test_get_users_example():
    expected_result = [3]
    records = [
        [1, "Windows 10", "start", 100],
        [2, "OSX 15.4", "start", 200],
        [1, "iPhone 8s", "start", 250],
        [1, "Windows 10", "stop", 370],
        [1, "iPhone 8s", "stop", 410],
        [2, "OSX 15.4", "stop", 490],
        [3, "Android 9.1", "start", 700]
    ]

    assert get_users(records=records, action='start', start_time=700, end_time=900) == expected_result


def test_get_users_all_results():
    expected_result = [1, 2, 3]
    records = [
        [1, "Windows 10", "start", 100],
        [2, "OSX 15.4", "start", 200],
        [1, "iPhone 8s", "start", 250],
        [1, "Windows 10", "stop", 370],
        [1, "iPhone 8s", "stop", 410],
        [2, "OSX 15.4", "stop", 490],
        [3, "Android 9.1", "start", 700]
    ]

    assert get_users(records=records, action='start', start_time=100, end_time=900) == expected_result


def test_get_users_no_results():
    expected_result = []
    records = [
        [1, "Windows 10", "start", 100],
        [2, "OSX 15.4", "start", 200],
        [1, "iPhone 8s", "start", 250],
        [1, "Windows 10", "stop", 370],
        [1, "iPhone 8s", "stop", 410],
        [2, "OSX 15.4", "stop", 490],
        [3, "Android 9.1", "start", 700]
    ]

    assert get_users(records=records, action='start', start_time=900, end_time=900) == expected_result


def test_get_users_transposed_time():
    records = []
    with pytest.raises(ValueError, match='end_time must be greater than start_time'):
        get_users(records=records, action='start', start_time=900, end_time=700)


def test_get_users_no_input():
    expected_result = []
    records = []

    assert get_users(records=records, action='start', start_time=700, end_time=900) == expected_result


def test_get_playback_time_example():
    expected_result = 310
    records = [
        [1, "Windows 10", "start", 100],
        [2, "OSX 15.4", "start", 200],
        [1, "iPhone 8s", "start", 250],
        [1, "Windows 10", "stop", 370],
        [1, "iPhone 8s", "stop", 410],
        [2, "OSX 15.4", "stop", 490],
        [3, "Android 9.1", "start", 700]
    ]

    assert get_playback_time(user_id=1, records=records) == expected_result


def test_get_playback_time_unknown_user():
    expected_result = None
    records = [
        [1, "Windows 10", "start", 100],
        [2, "OSX 15.4", "start", 200],
        [1, "iPhone 8s", "start", 250],
        [1, "Windows 10", "stop", 370],
        [1, "iPhone 8s", "stop", 410],
        [2, "OSX 15.4", "stop", 490],
        [3, "Android 9.1", "start", 700]
    ]

    assert get_playback_time(user_id=99, records=records) == expected_result


def test_get_playback_time_start_only():
    expected_result = 0
    records = [
        [1, "Windows 10", "start", 100],
        [2, "OSX 15.4", "start", 200],
        [1, "iPhone 8s", "start", 250],
        [1, "Windows 10", "stop", 370],
        [1, "iPhone 8s", "stop", 410],
        [2, "OSX 15.4", "stop", 490],
        [3, "Android 9.1", "start", 700]
    ]

    assert get_playback_time(user_id=3, records=records) == expected_result


def test_get_playback_time_stop_only():
    expected_result = 0
    records = [
        [1, "Windows 10", "start", 100],
        [2, "OSX 15.4", "start", 200],
        [1, "iPhone 8s", "start", 250],
        [1, "Windows 10", "stop", 370],
        [1, "iPhone 8s", "stop", 410],
        [2, "OSX 15.4", "stop", 490],
        [3, "Android 9.1", "stop", 700]
    ]

    assert get_playback_time(user_id=3, records=records) == expected_result
