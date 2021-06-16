from grip_assessment.assessment_2 import get_users_application_permissions

app_features = [
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
    }
]

user_features = [
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
    }
]


def test_get_users_application_permissions_example():
    user_access = [
        {
            "app_id": 1
        },
        {
            "app_id": 2
        },
        {
            "app_id": 3
        }
    ]

    test_user = 1
    expected_result = {
        "user_id": test_user,
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
            }
        ]
    }

    assert get_users_application_permissions(
        user_id=test_user,
        user_access=user_access,
        app_features=app_features,
        user_features=user_features
    ) == expected_result


def test_get_users_application_permissions_unknown_user():
    user_access = []
    test_user = 99
    expected_result = {
        "user_id": test_user,
        "application_permissions": [
        ]
    }

    assert get_users_application_permissions(
        user_id=test_user,
        user_access=user_access,
        app_features=app_features,
        user_features=user_features
    ) == expected_result


def test_get_users_application_permissions_unknown_app():
    user_access = [
        {
            "app_id": 1
        },
        {
            "app_id": 2
        },
        {
            "app_id": 99
        }
    ]

    test_user = 1
    expected_result = {
        "user_id": test_user,
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
                "app_id": 99,
                "features_allowed": []
            }
        ]
    }

    assert get_users_application_permissions(
        user_id=test_user,
        user_access=user_access,
        app_features=app_features,
        user_features=user_features
    ) == expected_result
