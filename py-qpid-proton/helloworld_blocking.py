# qpid.apache.org/releases/qpid-proton-0.20.0/proton/python/examples/helloworld_blocking.py.html
from __future__ import print_function

import os
import time

import proton
from proton import Message
from proton.utils import BlockingConnection
from proton.handlers import IncomingMessageHandler

while time.sleep(1) is None:
    try:
        conn = BlockingConnection(os.environ["AMQP_HOST"],
                                  user=os.environ["AMQP_USER"],
                                  password=os.environ["AMQP_PASS"])
        receiver = conn.create_receiver("examples")
        sender = conn.create_sender("examples")
        sender.send(Message(body="Hello World!"));
        msg = receiver.receive(timeout=30)
        print(msg.body)
        receiver.accept()
        conn.close()
    except proton.ConnectionException as e:
        print(e)

