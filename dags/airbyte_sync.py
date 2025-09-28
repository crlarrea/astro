from airflow.sdk import Asset, dag, task
from cosmos import DbtTaskGroup, ProjectConfig, ProfileConfig, ExecutionConfig


from cosmos.profiles import PostgresUserPasswordProfileMapping
from pendulum import datetime, duration
from airflow import DAG

import os

# Replace with your actual Airbyte connection ID
AIRBYTE_CONNECTION_ID = "c7daabed-46d8-4a3a-81e9-0b1f6395157d"

# Replace with your Airflow connection to Airbyte
AIRBYTE_CONN_ID = "airby_conn"


YOUR_NAME = "testing airbyte + airflow"

default_args = {
    "owner": "airflow",
    "retries": 5,
    "retry_delay": duration(minutes=5),
}

@dag(
    start_date=datetime(2023, 8, 1),
    schedule='0 1 * * *',
    catchup=False,
    # params={"my_name": YOUR_NAME},
)

def airbyte_sync():
    trigger_airbyte_sync = AirbyteTriggerSyncOperator(
        task_id="trigger_airbyte_sync",
        airbyte_conn_id=AIRBYTE_CONN_ID,
        connection_id=AIRBYTE_CONNECTION_ID,
        asynchronous=False,  # set True if you want to wait using a sensor
        timeout=3600,
        wait_seconds=3,
    )

    trigger_airbyte_sync
