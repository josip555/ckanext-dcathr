[![Tests](https://github.com/josip555/ckanext-dcathr/workflows/Tests/badge.svg?branch=main)](https://github.com/josip555/ckanext-dcathr/actions)

# ckanext-dcathr

CKAN extension for metadata quality assurance by adding DCAT validation button and enabling custom metadata fields at dataset creation.

## Requirements

This extension requires another CKAN extension to be included, [CKAN + DCAT](https://github.com/ckan/ckanext-dcat) extension. That extension will be included in installation steps of this readme.

Compatibility with core CKAN versions:

| CKAN version    | Compatible?   |
| --------------- | ------------- |
| 2.9             | no            |
| 2.10            | yes           |
| 2.11            | not tested    |

Values meaning:

* "yes"
* "not tested" - I can't think of a reason why it wouldn't work
* "not yet" - there is an intention to get it working
* "no"


## Installation

### Using ckan-docker (tested)

To install ckanext-dcathr using ckan-docker:

1. Clone _ckan-docker_ repository (skip if you already did)

    https://github.com/ckan/ckan-docker

2. Follow the instructions in ckan-docker README file to start CKAN in Development mode. 

    https://github.com/ckan/ckan-docker?tab=readme-ov-file#4--install-build-and-run-ckan-plus-dependencies

3. After successfuly starting CKAN in Docker using those steps and checking its page at localhost adress specified in .env file, shut down all CKAN containers in Docker.

4. In your ckan-docker directory change setup/Dockerfile.dev file. Add following lines (if they're not already in there) below the first line(FROM ckan/ckan-dev:...):

    RUN pip3 install -e 'git+https://github.com/ckan/ckanext-harvest.git@master#egg=ckanext-harvest' && \
        pip3 install -r ${APP_DIR}/src/ckanext-harvest/pip-requirements.txt
    
    RUN  pip3 install setuptools==57.0.0 --force-reinstall
    RUN  pip3 install wheel==0.36.2 --force-reinstall
    RUN  pip3 uninstall comtypes --yes
    RUN  pip3 install --no-cache-dir comtypes

    RUN pip install -e git+https://github.com/ckan/ckanext-dcat.git#egg=ckanext-dcat
    RUN pip install -r /srv/app/src/ckanext-dcat/requirements.txt

    RUN pip install -e git+https://github.com/josip555/ckanext-dcathr#egg=ckanext-dcathr
    RUN pip install -r /srv/app/src/ckanext-dcathr/requirements.txt

    RUN apk add --no-cache bash

    COPY setup/start_ckan_development.sh.override ${APP_DIR}/start_ckan_development.sh
    CMD ["bash", "/srv/app/start_ckan_development.sh"]

5. After that docker compose build ckan again, create a new dataset which you can use to test this extension. After creating new dataset go to the dataset's page and validation button should be visible. 

### Without ckan-docker (not tested)

To install ckanext-dcathr without ckan-docker (make sure CKAN + DCAT extension is already successfully added):

1. Activate your CKAN virtual environment, for example:

     . /usr/lib/ckan/default/bin/activate

2. Clone the source and install it on the virtualenv

    git clone https://github.com/josip555/ckanext-dcathr.git
    cd ckanext-dcathr
    pip install -e .
	pip install -r requirements.txt

3. Add `dcathr` to the `ckan.plugins` setting in your CKAN
   config file (by default the config file is located at
   `/etc/ckan/default/ckan.ini`).

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu:

     sudo service apache2 reload


## Config settings

### When including this extension to ckan-docker

**TODO:** Document any optional config settings here. For example:

	# The minimum number of hours to wait before re-checking a resource
	# (optional, default: 24).
	ckanext.dcathr.some_setting = some_default_value


## Tests

To run the tests, do:

    pytest --ckan-ini=test.ini


## Releasing a new version of ckanext-dcathr

If ckanext-dcathr should be available on PyPI you can follow these steps to publish a new version:

1. Update the version number in the `setup.py` file. See [PEP 440](http://legacy.python.org/dev/peps/pep-0440/#public-version-identifiers) for how to choose version numbers.

2. Make sure you have the latest version of necessary packages:

    pip install --upgrade setuptools wheel twine

3. Create a source and binary distributions of the new version:

       python setup.py sdist bdist_wheel && twine check dist/*

   Fix any errors you get.

4. Upload the source distribution to PyPI:

       twine upload dist/*

5. Commit any outstanding changes:

       git commit -a
       git push

6. Tag the new release of the project on GitHub with the version number from
   the `setup.py` file. For example if the version number in `setup.py` is
   0.0.1 then do:

       git tag 0.0.1
       git push --tags

## License

[AGPL](https://www.gnu.org/licenses/agpl-3.0.en.html)
