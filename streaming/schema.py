from pyspark.sql.functions import *
from pyspark.sql.types import *

c_schema = StructType() \
    .add("utc_timestamp", TimestampType()) \
    .add("cet_cest_timestamp", TimestampType()) \
    .add("DE_KN_industrial1_grid_import", FloatType()) \
    .add("DE_KN_industrial1_pv_1", FloatType()) \
    .add("DE_KN_industrial1_pv_2", FloatType()) \
    .add("DE_KN_industrial2_grid_import", FloatType()) \
    .add("DE_KN_industrial2_pv", FloatType()) \
    .add("DE_KN_industrial2_storage_charge", FloatType()) \
    .add("DE_KN_industrial2_storage_decharge", FloatType()) \
    .add("DE_KN_industrial3_area_offices", FloatType()) \
    .add("DE_KN_industrial3_area_room_1", FloatType()) \
    .add("DE_KN_industrial3_area_room_2", FloatType()) \
    .add("DE_KN_industrial3_area_room_3", FloatType()) \
    .add("DE_KN_industrial3_area_room_4", FloatType()) \
    .add("DE_KN_industrial3_compressor", FloatType()) \
    .add("DE_KN_industrial3_cooling_aggregate", FloatType()) \
    .add("DE_KN_industrial3_cooling_pumps", FloatType()) \
    .add("DE_KN_industrial3_dishwasher", FloatType()) \
    .add("DE_KN_industrial3_ev", FloatType()) \
    .add("DE_KN_industrial3_grid_import", FloatType()) \
    .add("DE_KN_industrial3_machine_1", FloatType()) \
    .add("DE_KN_industrial3_machine_2", FloatType()) \
    .add("DE_KN_industrial3_machine_3", FloatType()) \
    .add("DE_KN_industrial3_machine_4", FloatType()) \
    .add("DE_KN_industrial3_machine_5", FloatType()) \
    .add("DE_KN_industrial3_pv_facade", FloatType()) \
    .add("DE_KN_industrial3_pv_roof", FloatType()) \
    .add("DE_KN_industrial3_refrigerator", FloatType()) \
    .add("DE_KN_industrial3_ventilation", FloatType()) \
    .add("DE_KN_public1_grid_import", FloatType()) \
    .add("DE_KN_public2_grid_import", FloatType()) \
    .add("DE_KN_residential1_dishwasher", FloatType()) \
    .add("DE_KN_residential1_freezer", FloatType()) \
    .add("DE_KN_residential1_grid_import", FloatType()) \
    .add("DE_KN_residential1_heat_pump", FloatType()) \
    .add("DE_KN_residential1_pv", FloatType()) \
    .add("DE_KN_residential1_washing_machine", FloatType()) \
    .add("DE_KN_residential2_circulation_pump", FloatType()) \
    .add("DE_KN_residential2_dishwasher", FloatType()) \
    .add("DE_KN_residential2_freezer", FloatType()) \
    .add("DE_KN_residential2_grid_import", FloatType()) \
    .add("DE_KN_residential2_washing_machine", FloatType()) \
    .add("DE_KN_residential3_circulation_pump", FloatType()) \
    .add("DE_KN_residential3_dishwasher", FloatType()) \
    .add("DE_KN_residential3_freezer", FloatType()) \
    .add("DE_KN_residential3_grid_export", FloatType()) \
    .add("DE_KN_residential3_grid_import", FloatType()) \
    .add("DE_KN_residential3_pv", FloatType()) \
    .add("DE_KN_residential3_refrigerator", FloatType()) \
    .add("DE_KN_residential3_washing_machine", FloatType()) \
    .add("DE_KN_residential4_dishwasher", FloatType()) \
    .add("DE_KN_residential4_ev", FloatType()) \
    .add("DE_KN_residential4_freezer", FloatType()) \
    .add("DE_KN_residential4_grid_export", FloatType()) \
    .add("DE_KN_residential4_grid_import", FloatType()) \
    .add("DE_KN_residential4_heat_pump", FloatType()) \
    .add("DE_KN_residential4_pv", FloatType()) \
    .add("DE_KN_residential4_refrigerator", FloatType()) \
    .add("DE_KN_residential4_washing_machine", FloatType()) \
    .add("DE_KN_residential5_dishwasher", FloatType()) \
    .add("DE_KN_residential5_grid_import", FloatType()) \
    .add("DE_KN_residential5_refrigerator", FloatType()) \
    .add("DE_KN_residential5_washing_machine", FloatType()) \
    .add("DE_KN_residential6_circulation_pump", FloatType()) \
    .add("DE_KN_residential6_dishwasher", FloatType()) \
    .add("DE_KN_residential6_freezer", FloatType()) \
    .add("DE_KN_residential6_grid_export", FloatType()) \
    .add("DE_KN_residential6_grid_import", FloatType()) \
    .add("DE_KN_residential6_pv", FloatType()) \
    .add("DE_KN_residential6_washing_machine", FloatType()) \
    .add("interpolated", FloatType()) \



