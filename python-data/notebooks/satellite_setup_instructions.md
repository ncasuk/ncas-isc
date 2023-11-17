# Setup Instructions for the Satellite Exercise (2023)

A few things will need to be done before we're ready to have a crack at the satellite exercise:

1. Run `git pull` in the ncas-isc repo (again)
2. Copy the updated notebooks to your isc-work repo `cp ncas-isc/python-data/notebooks/ex04b_satellite*.ipynb my-isc-work/python-data/notebooks/.`
    1. Similarly, but optionally, copy over the solutions if you like

We also need to install some additional python packages which unfortunately aren't (yet) on Jaspy. To do this, we run:

`pip install --user pystac_client rioxarray shapely pyproj`

Which will install these python packages into your local python path, so we can use them with your account alongside all the packages in Jaspy. __NOTE: this command may take some time__ 

[Link to the software carpentry course](https://carpentries-incubator.github.io/geospatial-python)