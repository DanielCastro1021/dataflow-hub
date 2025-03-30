from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from pymongo import MongoClient

# MongoDB credentials
USERNAME = "admin"
PASSWORD = "password"
MONGO_URI = f"mongodb://{USERNAME}:{PASSWORD}@host.docker.internal:27017/datahub?authSource=admin"

DB_NAME = "datahub"
COLLECTION_NAME = "users"


# Function to insert data into MongoDB
def insert_into_mongo():
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]

    # Sample data to insert
    data = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 30},
        {"name": "Charlie", "age": 35},
    ]

    # Insert data
    result = collection.insert_many(data)
    print(f"Inserted IDs: {result.inserted_ids}")

    client.close()


# Define Airflow DAG
default_args = {"owner": "airflow", "start_date": datetime(2024, 1, 1), "retries": 1}

dag = DAG(
    "insert_mongo_dag",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False,
)

# Define the task
insert_task = PythonOperator(
    task_id="insert_mongo_task", python_callable=insert_into_mongo, dag=dag
)

# Define task dependencies
insert_task
