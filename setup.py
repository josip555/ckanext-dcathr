# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    entry_points='''
    [ckan.plugins]
    dcat_dataset_form=ckanext.dcathr.plugin:DatasetFormPlugin

    [ckan.rdf.profiles]
    euro_dcat_ap=ckanext.dcat.profiles:EuropeanDCATAPProfile
    euro_dcat_ap_2=ckanext.dcat.profiles:EuropeanDCATAP2Profile
    ''',
    # If you are changing from the default layout of your extension, you may
    # have to change the message extractors, you can read more about babel
    # message extraction at
    # http://babel.pocoo.org/docs/messages/#extraction-method-mapping-and-configuration
    message_extractors={
        'ckanext': [
            ('**.py', 'python', None),
            ('**.js', 'javascript', None),
            ('**/templates/**.html', 'ckan', None),
        ],
    }
)
