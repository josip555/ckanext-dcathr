[![Tests](https://github.com/josip555/ckanext-dcathr/workflows/Tests/badge.svg?branch=main)](https://github.com/josip555/ckanext-dcathr/actions)

# ckanext-dcathr

CKAN extension for metadata quality assurance by adding DCAT validation button and enabling custom metadata fields at dataset creation.

## Requirements

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

### Without ckan-docker (not tested)

To install ckanext-dcathr using ckan-docker:

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
