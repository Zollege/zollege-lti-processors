"""
Common LTI processors for Zollege.
"""
from __future__ import absolute_import
from .helpers import get_user
from six import text_type

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
        'lis_person_contact_email_primary': user.email,
        'lis_person_name_given': names_list[0],
        'user_id': text_type(user.id),
        'ExternalUserID': user.username,
    }

    if len(names_list) > 1:
        params['lis_person_name_family'] = names_list[1]

    return params


personal_user_info.lti_xblock_default_params = {
    'lis_person_contact_email_primary': '',
    'lis_person_name_given': '',
    'lis_person_name_family': '',
    'user_id': '',
    'ExternalUserID': '',
}

def course_info(xblock):
    """
    Provide additional course information.
    """
    params = {
        'course_id': text_type(xblock.parent.course_key),
        'location': xblock.parent.course_key.org,
    }
    return params

course_info.lti_xblock_default_params = {
    'course_id': '',
    'location': '',
}
