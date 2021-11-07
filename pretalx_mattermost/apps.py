from django.apps import AppConfig
from django.utils.translation import gettext_lazy


class PluginApp(AppConfig):
    name = 'pretalx_mattermost'
    verbose_name = 'MatterMost integration for pretalx'

    class PretalxPluginMeta:
        name = gettext_lazy('MatterMost integration for pretalx')
        author = 'Toshaan Bharvani'
        description = gettext_lazy(
            'Receive notifications whenever a submission changes its state.'
        )
        visible = True
        version = '0.0.0'

    def ready(self):
        from . import signals  # NOQA
