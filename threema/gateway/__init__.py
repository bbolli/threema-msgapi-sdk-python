"""
This API can be used to send text messages to any Threema user, and to
receive incoming messages and delivery receipts.

There are two main modes of operation:

* Basic mode (server-based encryption)
    - The server handles all encryption for you.
    - The server needs to know the private key associated with your
      Threema API identity.
    - Incoming messages and delivery receipts are not supported.

* End-to-end encrypted mode
    - The server doesn't know your private key.
    - Incoming messages and delivery receipts are supported.
    - You need to run software on your side to encrypt each message
      before it can be sent, and to decrypt any incoming messages or
      delivery receipts.

The mode that you can use depends on the way your account was set up.

.. moduleauthor:: Lennart Grahl <lennart.grahl@threema.ch>
"""
import itertools

# noinspection PyUnresolvedReferences
from ._gateway import *  # noqa
# noinspection PyUnresolvedReferences
from .exception import *  # noqa
# noinspection PyUnresolvedReferences
from . import bin, simple, e2e, key, util  # noqa

__author__ = 'Lennart Grahl <lennart.grahl@threema.ch>'
__status__ = 'Production'
__version__ = '3.0.0'
feature_level = 3

__all__ = tuple(itertools.chain(
    ('feature_level',),
    _gateway.__all__,  # noqa
    exception.__all__,  # noqa
    ('bin', 'simple', 'e2e', 'key', 'util')
))
