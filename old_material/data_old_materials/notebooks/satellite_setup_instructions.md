# Setup Instructions for the Satellite Exercise (2023)

A few things will need to be done before we're ready to have a crack at the satellite exercise:

1. Run `git pull` in the ncas-isc repo (again)
2. Copy the updated notebooks to your isc-work repo `cp ncas-isc/python-data/notebooks/ex04b_satellite*.ipynb my-isc-work/python-data/notebooks/.`
    1. Similarly, but optionally, copy over the solutions if you like

We also need to install some additional python packages which unfortunately aren't (yet) on Jaspy. To do this, we run:

`pip install --user pystac_client rioxarray shapely pyproj`

Which will install these python packages into your local python path, so we can use them with your account alongside all the packages in Jaspy. __NOTE: this command may take some time__ 

## Stuff to do once you're finished with the notebook

There's no more taught material after this, but if you want to carry on you have a few options available:

1. You can carry on with the [software carpentry course](https://carpentries-incubator.github.io/geospatial-python), you just finished lesson 6 so you can go to 7+ if you fancy
2. You can have a go at figuring out how to combine several `xarray.DataArray`s for different bands into a single `xarray.Dataset`. Would probably be wise to consult the [xarray documentation](https://docs.xarray.dev/en/stable/).
3. [Project pythia](https://projectpythia.org/landsat-ml-cookbook/notebooks/1.0_Data_Ingestion-Planetary_Computer.html) has another good tutorial going through the same stuff with a slightly different approach on another STAC endpoint which might be useful/interesting
4. Do some of your own work, feeling free to ask us questions about any of it (we'll do our best here).  