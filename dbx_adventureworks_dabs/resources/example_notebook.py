# Databricks notebook source
from pyspark.sql.functions import col, lit

table = "samples.nyctaxi.trips"

df = spark.read.table(table)

df. select("tpep_pickup_datetime", "tpep_dropoff_datetime",
           "trip_distance", "fare_amount", "pickup_zip", "dropoff_zip").limit(100).show()

# COMMAND ----------

df.createOrReplaceTempView("trips_vw")

# COMMAND ----------

# MAGIC %sql
# MAGIC select tpep_pickup_datetime, trip_distance from trips_vw limit 5
