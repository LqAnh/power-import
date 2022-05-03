from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from schema import c_schema

if __name__ == "__main__":
    spark = SparkSession \
        .builder \
        .appName("PySpark Kafka ") \
        .master("local[*]") \
        .config("spark.cassandra.connection.host", "localhost") \
        .getOrCreate()

    spark.sparkContext.setLogLevel("ERROR")

    df = spark \
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "localhost:9092") \
        .option("subscribe", "test") \
        .option("startingOffsets", "latest") \
        .load()
    
    df.printSchema()
    
    df1 = df.selectExpr("CAST(value AS STRING)", "timestamp")

    
    df2 = df1\
        .select(from_json(col("value"), c_schema)\
        .alias("order"), "timestamp")

    df3 = df2.select("timestamp","order.*")

    col = ["utc_timestamp", "cet_cest_timestamp","DE_KN_industrial1_pv_1", "DE_KN_industrial1_pv_2","DE_KN_industrial2_pv","DE_KN_industrial2_storage_charge","DE_KN_industrial2_storage_decharge","DE_KN_industrial3_area_offices","DE_KN_industrial3_area_room_1","DE_KN_industrial3_area_room_2","DE_KN_industrial3_area_room_3","DE_KN_industrial3_area_room_4","DE_KN_industrial3_compressor","DE_KN_industrial3_cooling_aggregate","DE_KN_industrial3_cooling_pumps","DE_KN_industrial3_dishwasher","DE_KN_industrial3_ev","DE_KN_industrial3_machine_1","DE_KN_industrial3_machine_2","DE_KN_industrial3_machine_3", "DE_KN_industrial3_machine_4","DE_KN_industrial3_machine_5","DE_KN_industrial3_pv_facade","DE_KN_industrial3_pv_roof","DE_KN_industrial3_refrigerator","DE_KN_industrial3_ventilation","DE_KN_residential1_dishwasher","DE_KN_residential1_freezer","DE_KN_residential1_heat_pump","DE_KN_residential1_pv","DE_KN_residential1_washing_machine","DE_KN_residential2_circulation_pump","DE_KN_residential2_dishwasher","DE_KN_residential2_freezer","DE_KN_residential2_washing_machine","DE_KN_residential3_circulation_pump","DE_KN_residential3_dishwasher","DE_KN_residential3_freezer","DE_KN_residential3_grid_export","DE_KN_residential3_pv","DE_KN_residential3_refrigerator","DE_KN_residential3_washing_machine","DE_KN_residential4_dishwasher","DE_KN_residential4_ev","DE_KN_residential4_freezer","DE_KN_residential4_grid_export","DE_KN_residential4_heat_pump","DE_KN_residential4_pv","DE_KN_residential4_refrigerator","DE_KN_residential4_washing_machine","DE_KN_residential5_dishwasher","DE_KN_residential5_refrigerator","DE_KN_residential5_washing_machine","DE_KN_public1_grid_import","DE_KN_public2_grid_import","DE_KN_residential6_circulation_pump","DE_KN_residential6_dishwasher","DE_KN_residential6_freezer","DE_KN_residential6_grid_export","DE_KN_residential6_pv","DE_KN_residential6_washing_machine","interpolated"]
    for item in col:
        df3 = df3.drop(item)
    

    df3 = df3.withColumnRenamed("timestamp", "time") \
                .withColumnRenamed("DE_KN_industrial1_grid_import", "indus1") \
                .withColumnRenamed("DE_KN_industrial2_grid_import", "indus2") \
                .withColumnRenamed("DE_KN_industrial3_grid_import", "indus3") \
                .withColumnRenamed("DE_KN_residential1_grid_import", "res1") \
                .withColumnRenamed("DE_KN_residential2_grid_import", "res2") \
                .withColumnRenamed("DE_KN_residential3_grid_import", "res3") \
                .withColumnRenamed("DE_KN_residential4_grid_import", "res4") \
                .withColumnRenamed("DE_KN_residential5_grid_import", "res5") \
                .withColumnRenamed("DE_KN_residential6_grid_import", "res6") \
            
    
    write_stream = df3 \
        .writeStream \
        .outputMode("append") \
        .format("org.apache.spark.sql.cassandra") \
        .options(table="import", keyspace="power_import") \
        .option("checkpointLocation", "./__checkpoint__") \
        .start()

    write_stream.awaitTermination()