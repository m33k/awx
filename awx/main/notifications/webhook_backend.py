# Copyright (c) 2016 Ansible, Inc.
# All Rights Reserved.

import logging

import requests
import json
from awx.main.notifications.base import TowerBaseEmailBackend

logger = logging.getLogger('awx.main.notifications.webhook_backend')

class WebhookBackend(TowerBaseEmailBackend):

    init_parameters = {"url": {"label": "Target URL", "type": "string"},
                       "headers": {"label": "HTTP Headers", "type": "object"}}
    recipient_parameter = "url"
    sender_parameter = None

    def __init__(self, headers, fail_silently=False, **kwargs):
        self.headers = headers
        super(WebhookBackend, self).__init__(fail_silently=fail_silently)

    def format_body(self, body):
        logger.error("Generating body from {}".format(str(body)))
        return body

    def send_messages(self, messages):
        sent_messages = 0
        for m in messages:
            logger.error("BODY: " + str(m.body))
            r = requests.post("{}".format(m.recipients()[0]),
                              data=json.dumps(m.body),
                              headers=self.headers)
            if r.status_code >= 400:
                logger.error("Error sending notification webhook: {}".format(r.text))
                if not self.fail_silently:
                    raise Exception("Error sending notification webhook: {}".format(r.text))
            sent_messages += 1
        return sent_messages
