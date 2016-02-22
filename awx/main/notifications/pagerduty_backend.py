# Copyright (c) 2016 Ansible, Inc.
# All Rights Reserved.

import logging
import pygerduty

from awx.main.notifications.base import TowerBaseEmailBackend

logger = logging.getLogger('awx.main.notifications.pagerduty_backend')

class PagerDutyBackend(TowerBaseEmailBackend):

    init_parameters = {"subdomain": {"label": "Pagerduty subdomain", "type": "string"},
                       "token": {"label": "API Token", "type": "password"},
                       "service_key": {"label": "API Service/Integration Key", "type": "string"},
                       "client_name": {"label": "Client Identifier", "type": "string"}}
    recipient_parameter = "service_key"
    sender_parameter = "client_name"

    def __init__(self, subdomain, token, fail_silently=False, **kwargs):
        super(PagerDutyBackend, self).__init__(fail_silently=fail_silently)
        self.subdomain = subdomain
        self.token = token

    def format_body(self, body):
        return body

    def send_messages(self, messages):
        sent_messages = 0

        try:
            pager = pygerduty.PagerDuty(self.subdomain, self.token)
        except Exception as e:
            if not self.fail_silently:
                raise
            logger.error("Exception connecting to PagerDuty: {}".format(e))
        for m in messages:
            try:
                pager.trigger_incident(m.recipients()[0],
                                       description=m.subject,
                                       details=m.body,
                                       client=m.from_email)
            except Exception as e:
                logger.error("Exception sending messages: {}".format(e))
                if not self.fail_silently:
                    raise
        return sent_messages
