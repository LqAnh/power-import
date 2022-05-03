from kafka import KafkaProducer
import time
import pandas as pd
import json

if __name__ == '__main__':
    kafka_producer_obj = KafkaProducer(bootstrap_servers="localhost:9092",
                                       value_serializer=lambda x: json.dumps(x).encode('utf-8'))

    df = pd.read_csv("power.csv")
    for row in df.iterrows():
        msg = row[1].to_dict()
        time.sleep(5)
        print("sent", msg)
        kafka_producer_obj.send("test", msg)
