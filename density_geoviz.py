#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 16:54:41 2021

@author: luca
This is to recreate the original 3 density visualisations (active businesses, overdue accounts)
"""

"""
Open Connection - cnx.reconnect()
Close Connection - cnx.close()
Check Connection - cnx.is_connected()
"""

import numpy as np
import pandas as pd
import mysql.connector

import geopandas as gpd
import geoplot as gplt
import geoplot.crs as gcrs
import matplotlib.pyplot as plt
import contextily as cx

# ----SQL----

postcodes = pd.read_csv(r'/home/luca/Documents/ukpostcodes.csv')

cnx = mysql.connector.connect(user='', password='', host='34.123.17.39', database='ust')

cursor = cnx.cursor()

table = pd.read_sql("""SELECT * FROM ust.companies_house ORDER BY RAND() LIMIT 1500;""", cnx)

table = pd.merge(table, postcodes, how='inner', left_on='registered_office_address.postal_code', right_on='postcode')
table = table.drop('registered_office_address.postal_code', axis=1)

overdue_accs = table.loc[lambda table: table['accounts.overdue'] == 1]
non_overdue_accs = table.loc[lambda table: table['accounts.overdue'] == 0]

# ----Geovisualisation----

uk_gdf = gpd.read_file(r"/home/luca/Downloads/Countries_(December_2020)_UK_BFC/Countries_(December_2020)_UK_BFC.shp")

ust_gdf = gpd.GeoDataFrame(overdue_accs, geometry=gpd.points_from_xy(overdue_accs.longitude, overdue_accs.latitude))
ust_gdf_2 = gpd.GeoDataFrame(non_overdue_accs, geometry=gpd.points_from_xy(non_overdue_accs.longitude, non_overdue_accs.latitude))

ust_gdf = ust_gdf.set_crs(epsg=4326)
ust_gdf_2 = ust_gdf_2.set_crs(epsg=4326)

uk_gdf = uk_gdf.to_crs(epsg=4326)

fig, ax = plt.subplots(figsize = (20, 16))

plt.title('Overdue Accounts Density', fontsize=20)

gplt.kdeplot(ust_gdf, cmap='coolwarm', shade=True, ax=ax, alpha=0.6)
#gplt.kdeplot(ust_gdf_2, cmap='coolwarm', shade=True, ax=ax)

uk_gdf.plot(facecolor="none", edgecolor="black", ax=ax)

# cx.add_basemap(ax)
