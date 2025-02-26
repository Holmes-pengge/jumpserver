from django.utils.translation import gettext_lazy as _

from .base import BaseType


class DeviceTypes(BaseType):
    GENERAL = 'general', _("General")
    SWITCH = 'switch', _("Switch")
    ROUTER = 'router', _("Router")
    FIREWALL = 'firewall', _("Firewall")

    @classmethod
    def _get_base_constrains(cls) -> dict:
        return {
            '*': {
                'charset_enabled': False,
                'domain_enabled': True,
                'su_enabled': False,
            }
        }

    @classmethod
    def _get_protocol_constrains(cls) -> dict:
        return {
            '*': {
                'choices': ['ssh', 'telnet']
            }
        }

    @classmethod
    def _get_automation_constrains(cls) -> dict:
        return {
            '*': {
                'ansible_enabled': False,
                'ansible_config': {
                    'ansible_connection': 'local',
                },
                'ping_enabled': False,
                'gather_facts_enabled': False,
                'gather_accounts_enabled': False,
                'verify_account_enabled': False,
                'change_secret_enabled': False,
                'push_account_enabled': False
            }
        }

    @classmethod
    def internal_platforms(cls):
        return {
            cls.GENERAL: [{'name': 'General'}, {'name': 'Cisco'}, {'name': 'Huawei'}, {'name': 'H3C'}],
            cls.SWITCH: [],
            cls.ROUTER: [],
            cls.FIREWALL: []
        }

    @classmethod
    def get_community_types(cls):
        return [
            cls.GENERAL, cls.SWITCH, cls.ROUTER, cls.FIREWALL
        ]
