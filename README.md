# Backstage Catalog Components

This is largely just a simple repo to mock an organization that will have several catalog entities within backstage. Used mainly for testing purposes.

Included is a script `catalog-script.py` that can be used to quickly create a large number of catalog entities within backstage.

Currently, these entities are very basic and are primarily used to fill in the catalog.

## Python Script

To execute the python script, at the root level of the directory and in the terminal run `python ./catalog-script.py`

You can also pass in additional command line arguments to specify the number of resources that you wish to create.

ex. `python catalog-script.py --groups 2 --users 3 --apis 3 --components 3 --resources 3 --systems 3`

In this example there will be 2 groups created that will each have 3 users, 3 apis, 3 components, 3 resources, and 3 systems
