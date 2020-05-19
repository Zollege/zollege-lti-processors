"""
Common LTI processors for Zollege.
"""
from helpers import get_user


def personal_user_info(xblock):
    """
    Provide additional standard LTI user personal information.
    """
    user = get_user(xblock)
    if not user:
        return

    user_full_name = user.profile.name
    names_list = user_full_name.split(' ', 1)

    params = {
        'lis_person_name_given': names_list[0],
    }

    if len(names_list) > 1:
        params['lis_person_name_family'] = names_list[1]

    return params


personal_user_info.lti_xblock_default_params = {
    'lis_person_name_given': '',
    'lis_person_name_family': '',
}
