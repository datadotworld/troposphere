# Copyright (c) 2012-2020, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***
# Resource specification version: 18.6.0


from . import AWSObject
from troposphere import Tags


class Assignment(AWSObject):
    resource_type = "AWS::SSO::Assignment"

    props = {
        'InstanceArn': (basestring, True),
        'PermissionSetArn': (basestring, True),
        'PrincipalId': (basestring, True),
        'PrincipalType': (basestring, True),
        'TargetId': (basestring, True),
        'TargetType': (basestring, True),
    }


class PermissionSet(AWSObject):
    resource_type = "AWS::SSO::PermissionSet"

    props = {
        'Description': (basestring, False),
        'InlinePolicy': (basestring, False),
        'InstanceArn': (basestring, True),
        'ManagedPolicies': ([basestring], False),
        'Name': (basestring, True),
        'RelayStateType': (basestring, False),
        'SessionDuration': (basestring, False),
        'Tags': (Tags, False),
    }
