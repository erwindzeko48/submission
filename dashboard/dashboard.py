import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style='dark')
day_df = pd.read_csv("dashboard/day_transformed.csv")
day_df['dteday'] = pd.to_datetime(day_df['dteday'])
min_date = day_df["dteday"].min()
max_date = day_df["dteday"].max()

with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://cdn.pixabay.com/photo/2013/07/27/09/54/bike-168159_1280.jpg")
    
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

    main_df = day_df[(day_df["dteday"] >= str(start_date)) & 
                (day_df["dteday"] <= str(end_date))]
    
st.header('Bike Rental Dashboard :sparkles:')
st.subheader('Daily Rental')

col1, col2 = st.columns(2)
 
with col1:
    total_rental1 = main_df[main_df["variable"] == "registered"].value.mean()
    st.metric("Rata-Rata Rental Registered", value=total_rental1.round())
 
with col2:
    total_rental2 = main_df[main_df["variable"] =="casual"].value.mean()
    st.metric("Rata-rata Rental Casual", value=total_rental2.round())

fig, ax = plt.subplots(figsize=(16, 8))
myplot = sns.lineplot(main_df, x="dteday", y="value", hue="variable", estimator="mean")
myplot.set(xlabel="Tanggal",
           ylabel="Penyewa",
           title="Jumlah Penyewa Perhari")
myplot.xaxis.label.set_size(14)
myplot.yaxis.label.set_size(14)
myplot.tick_params(axis='both', labelsize=15)
myplot.legend(title="Jenis Penyewa")
st.pyplot(myplot.get_figure())

st.subheader("Monthly Rental")
fig, ax = plt.subplots(figsize=(16, 8))
myplot2 = sns.lineplot(main_df, x="month", y="value", hue="variable", estimator="mean")
myplot2.set(xlabel="Bulan",
           ylabel="Penyewa",
           title="Rata-Rata Jumlah Penyewa Perbulan")
myplot2.xaxis.label.set_size(14)
myplot2.yaxis.label.set_size(14)
myplot2.tick_params(axis='both', labelsize=15)
myplot2.legend(title="Jenis Penyewa")
st.pyplot(myplot2.get_figure())

st.subheader("Hubungan Jumlah Penyewa, Rata-Rata Suhu, dan Rata-Rata Kecepatan Angin")
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(35, 15))
myplot3 = sns.lineplot(data=main_df,x="month", y="value", estimator="sum",ax=ax[0], color = "red", ci=None, linewidth=4)
ax2 = ax[0].twinx()
myplot3 = sns.lineplot(data=main_df,x="month", y="temp", estimator="mean",ax=ax2, color="blue",ci=None,linewidth=4)
myplot3.xaxis.label.set_size(20)
myplot3.yaxis.label.set_size(20)
myplot3.tick_params(axis='both', labelsize=20)
myplot3 = sns.lineplot(data=main_df,x="month", y="value", estimator="sum",ax=ax[1], color = "red",ci=None, linewidth=4)
ax3 = ax[1].twinx()
myplot3 = sns.lineplot(data=main_df,x="month", y="windspeed", estimator="mean",ax=ax3, color="yellow", ci=None, linewidth=4)
myplot3.xaxis.label.set_size(20)
myplot3.yaxis.label.set_size(20)
myplot3.tick_params(axis='both', labelsize=20)
st.pyplot(myplot3.get_figure())

st.subheader("Rata-Rata Penyewaan Sepeda Menurut Musim dan Cuaca")
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(35, 15))
myplot4 = sns.barplot(data=main_df,x="season", y="value", estimator="mean", ax=ax[0])
myplot4.xaxis.label.set_size(20)
myplot4.yaxis.label.set_size(20)
myplot4.tick_params(axis='both', labelsize=20)
myplot4 = sns.barplot(data=main_df,x="weathersit", y="value", estimator="mean",ax=ax[1])
myplot4.xaxis.label.set_size(20)
myplot4.yaxis.label.set_size(20)
myplot4.tick_params(axis='both', labelsize=20)
st.pyplot(myplot4.get_figure())

st.caption('Copyright (c) Dicoding 2024')
