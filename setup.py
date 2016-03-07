#!/usr/bin/env python
from setuptools import setup

setup(
    name='keepkey',
    version='0.7.1',
    author='Bitcoin TREZOR and KeepKey',
    author_email='support@keepkey.com',
    description='Python library for communicating with KeepKey Hardware Wallet',
    url='https://github.com/keepkey/python-keepkey',
    py_modules=[
        'keepkeylib.ckd_public',
        'keepkeylib.client',
        'keepkeylib.debuglink',
        'keepkeylib.mapping',
        'keepkeylib.messages_pb2',
        'keepkeylib.protobuf_json',
        'keepkeylib.qt.pinmatrix',
        'keepkeylib.tools',
        'keepkeylib.transport',
        'keepkeylib.transport_fake',
        'keepkeylib.transport_hid',
        'keepkeylib.transport_pipe',
        'keepkeylib.transport_serial',
        'keepkeylib.transport_socket',
        'keepkeylib.tx_api',
        'keepkeylib.types_pb2',
    ],
    scripts = ['keepkeyctl'],
    test_suite='tests',
    install_requires=['ecdsa>=0.9', 'protobuf==2.6.1', 'mnemonic>=0.8', 'hidapi>=0.7.99'],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',
    ],
)
