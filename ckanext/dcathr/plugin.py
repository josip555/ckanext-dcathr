# encoding: utf-8
from __future__ import annotations
import logging

from ckan.types import Schema
import ckan.plugins as p
import ckan.plugins.toolkit as tk
from ckanext.dcat.processors import RDFSerializer

logger = logging.getLogger(__name__)

def serialize_dataset(dataset_id):
    serializer = RDFSerializer(profiles=['euro_dcat_ap_2'])
    dataset = tk.get_action('package_show')({}, {'id': dataset_id})
    
    dataset_xml = serializer.serialize_dataset(dataset, _format='xml')

    return dataset_xml

class DatasetFormPlugin(tk.DefaultDatasetForm, p.SingletonPlugin):
    p.implements(p.IConfigurer)
    p.implements(p.ITemplateHelpers)
    p.implements(p.IDatasetForm)

    # ITemplateHelpers
    def get_helpers(self):
        #Register the most_popular_groups() function above as a template
        #helper function.
        
        # Template helper function names should begin with the name of the
        # extension they belong to, to avoid clashing with functions from
        # other extensions.
        return {'dcathr_serialize_dataset': serialize_dataset}

    # IConfigurer
    def update_config(self, config_):
        tk.add_template_directory(config_, "templates")
        tk.add_public_directory(config_, "public")
        tk.add_resource("assets", "dcathr")

    # IDatasetForm
    def create_package_schema(self) -> Schema:
        # let's grab the default schema in our plugin
        schema: Schema = super(
            DatasetFormPlugin, self).create_package_schema()
        # our custom field
        schema.update({
            'custom_text': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')]
        })
        return schema
    
    def update_package_schema(self) -> Schema:
        schema: Schema = super(
            DatasetFormPlugin, self).update_package_schema()
        # our custom field
        schema.update({
            'custom_text': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')]
        })
        return schema
    
    def show_package_schema(self) -> Schema:
        schema: Schema = super(
            DatasetFormPlugin, self).show_package_schema()
        schema.update({
            'custom_text': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')]
        })
        return schema

    def is_fallback(self):
        # Return True to register this plugin as the default handler for
        # package types not handled by any other IDatasetForm plugin.
        return True

    def package_types(self) -> list[str]:
        # This plugin doesn't handle any special package types, it just
        # registers itself as the default (above).
        return []