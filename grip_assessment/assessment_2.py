def get_user_features_allowed(user_features: dict, user_id: int) -> list:
    """A function that extracts the features allowed for the given user_id

    :param user_features: The list of user specific features
    :param user_id: The user id to search for

    :returns: A list of features for the user, empty list if user not found
    """

    user_features_allowed = []
    for user in user_features:
        if user['user_id'] == user_id:
            user_features_allowed = user['features_allowed']
            break
    return user_features_allowed


def get_features(app_features: list) -> dict:
    """Converts the list of app feature dictionaries into a dictionary keyed by app_id

    :param app_features: The list of app specific features

    :returns: app id keyed dictionary
    """

    feature_dict = {}
    for app in app_features:
        feature_dict[app['app_id']] = app['features_available']
    return feature_dict


def get_users_application_permissions(user_id: int, user_access: list, app_features: list, user_features: list) -> dict:
    """Converts the list of app feature dictionaries into a dictionary keyed by app_id

    :param user_id: The user id to format the result for
    :param user_access: The list of apps this user has
    :param app_features: The list of app specific features
    :param user_features: The list of user specific features

    :returns: app id keyed dictionary
    """

    feature_dict = get_features(app_features)

    user_features_allowed = get_user_features_allowed(user_features, user_id)

    user_permission_dict = {
        "user_id": user_id,
        "application_permissions": []
    }

    for app in user_access:
        features_allowed = []
        # if the current app is in feature_dict features_allowed is a list containing elements that are in both
        # the features for the app and that the user is allowed
        if app['app_id'] in feature_dict.keys():
            features_allowed = list(set(feature_dict[app['app_id']]).intersection(user_features_allowed))
        feat = {
            "app_id": app['app_id'],
            "features_allowed": features_allowed
        }
        user_permission_dict['application_permissions'].append(feat)
    return user_permission_dict
