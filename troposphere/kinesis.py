# Copyright (c) 2014, Guillem Anguera <ganguera@gmail.com>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, Tags
from .validators import integer


class StreamEncryption(AWSProperty):
    props = {
        'EncryptionType': (basestring, True),
        'KeyId': (basestring, True),
    }


class Stream(AWSObject):
    resource_type = "AWS::Kinesis::Stream"

    props = {
        'Name': (basestring, False),
        'RetentionPeriodHours': (integer, False),
        'ShardCount': (integer, True),
        'StreamEncryption': (StreamEncryption, False),
        'Tags': ((Tags, list), False),
    }


class StreamConsumer(AWSObject):
    resource_type = "AWS::Kinesis::StreamConsumer"

    props = {
        'ConsumerName': (basestring, True),
        'StreamARN': (basestring, True),
    }
