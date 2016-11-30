from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cmsplugin_forms_builder.models import PluginForm
from django.utils.translation import ugettext_lazy as _


class FormBuilderPlugin(CMSPluginBase):
    """
        Plugin class for form-builder forms.
    """

    model = PluginForm
    name = _("Form")
    render_template = "forms/form_plugin_detail.html"
    cache = False

    def render(self, context, instance, placeholder):
        context['form'] = instance.form
        return context

plugin_pool.register_plugin(FormBuilderPlugin)
