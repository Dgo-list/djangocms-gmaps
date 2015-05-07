# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from aldryn_client import forms


class Form(forms.BaseForm):
    plugin_module = forms.CharField("Plugin module name", initial='Generic')
    plugin_name = forms.CharField("Plugin name", initial='Map')
    location_plugin_name = forms.CharField("Location plugin name",
        initial='Location')
    page_only = forms.CheckboxField("Page placeholders only?", initial=False,
        help_text="Check this box to limit use of these plugins to CMSPage "
                    "placholders only.")
    parent_classes = forms.CharField("Parent plugin classes", max_length=255)
    require_parent = forms.CheckboxField("Child only?", initial=False,
        help_text="Chcck this box to only allow these plugins to be used "
                    "only as children of other plugins.")
    text_enabled = forms.CheckboxField("Text enabled?", initial=False,
        help_text="Check this box to allow these plugins to be used as "
                    "children of TextPlugin instances.")
    template = forms.CharField("Render template",
        initial="djangocms_gmaps/default.html")
    infowindow_template = forms.CharField("InfoWindow render template",
        initial="djangocms_gmaps/infowindow.html")
    # fieldsets:          Not really sure it is feasible to allow this to be
    #                     entered in CharField input widget. The plugins use
    #                     sensible defaults already, so, not really required.
    # location_fieldsets: - ditto -
    advanced_options_enabled = forms.CheckboxField("Show advanced options",
        initial=True,
        help_text="Enable Advanced Options to allow the users to fully "
                    "customise map controls e.g. streetViewControl")
    styled_maps_enabled = forms.CheckboxField("Enable styled maps?",
        initial=True, help_text="Check this box to allow the user to "
                                  "customize tha appearance of maps.")
    infowindow_enabled = forms.CheckboxField("Enable InfoWindow?",
        initial=True, help_text="Check this box to enable the InfoWindow")
    infowindow_maxwidth = forms.NumberField("Max width", initial=220,
        help_text="Set this to the desired maximum InfoWindow width.")
    custom_markers_enabled = forms.CheckboxField("Custom markers?",
        initial=True,
        help_text="Check this box to allow the use of custom markers.")

    def to_settings(self, data, settings):
        settings['DJANGOCMS_GMAPS_PLUGIN_MODULE'] = data['plugin_module']
        settings['DJANGOCMS_GMAPS_PLUGIN_NAME'] = data['plugin_name']
        settings['DJANGOCMS_GMAPS_LOCATION_PLUGIN_NAME'] = data[
            'location_plugin_name']
        settings['DJANGOCMS_GMAPS_PAGE_ONLY'] = data['page_only']
        settings['DJANGOCMS_GMAPS_PARENT_CLASSES'] = data['parent_classes']
        settings['DJANGOCMS_GMAPS_REQUIRE_PARENT'] = data['require_parent']
        settings['DJANGOCMS_GMAPS_TEXT_ENABLED'] = data['text_enabled']
        settings['DJANGOCMS_GMAPS_TEMPLATE'] = data['template']
        settings['DJANGOCMS_GMAPS_INFOWINDOW_TEMPLATE'] = data[
            'infowindow_template']
        # See comments above...
        # settings['DJANGOCMS_GMAPS_FIELDSETS']
        # settings['DJANGOCMS_GMAPS_LOCATION_FIELDSETS']
        settings['DJANGOCMS_GMAPS_ADVANCED_OPTIONS_ENABLED'] = data[
            'advanced_options_enabled']
        settings['DJANGOCMS_GMAPS_STYLED_MAPS_ENABLED'] = data[
            'styled_maps_enabled']
        settings['DJANGOCMS_GMAPS_INFOWINDOW_ENABLED'] = data[
            'infowindow_enabled']
        settings['DJANGOCMS_GMAPS_INFOWINDOW_MAXWIDTH'] = data[
            'infowindow_maxwidth']
        settings['DJANGOCMS_GMAPS_CUSTOM_MARKERS_ENABLED'] = data[
            'custom_markers_enabled']
        return settings
