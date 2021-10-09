#!/usr/bin/env python3

# @author Augustin Mortier
# @email augustinm@met.no
# @desc A-Profiles - Time Series plot

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import seaborn as sns
sns.set_theme()


def plot(da, var='aod', **kwargs):
    """Plot time series of selected variable from :class: :ref:`ProfilesData` object.

    Args:
        da ([type]): [description]
        var (str, optional): [description]. Defaults to 'aod'.
    """

    def __init__(self):
        pass

    #get kwargs
    ymin = kwargs.get('ymin',None)
    ymax = kwargs.get('ymax',None)

    #time
    time = da.time.data

    fig, axs = plt.subplots(1, 1, figsize=(12, 4))

    #plot time series
    plt.plot(time, da[var].data)

    #limit to altitude range
    if ymin!=None or ymax!=None:
        plt.ylim([ymin, ymax])

    #set title and axis labels
    yyyy = pd.to_datetime(da.time.values[0]).year
    mm = pd.to_datetime(da.time.values[0]).month
    dd = pd.to_datetime(da.time.values[0]).day
    latitude = da.station_latitude.data
    longitude = da.station_longitude.data
    altitude = da.station_altitude.data
    station_id = da.attrs['site_location']
    #title
    plt.title('{} ({:.2f};{:.2f};{:.1f}m) - {}/{:02}/{:02}'.format(station_id, latitude, longitude, altitude, yyyy, mm, dd), weight='bold')
    #labels
    plt.xlabel('Time')

    if 'units' in list(da[var].attrs) and da[var].units!=None:
        ylabel = '{} ({})'.format(da[var].long_name, da[var].units)
    else:
        ylabel = '{}'.format(da[var].long_name)
    plt.ylabel(ylabel)