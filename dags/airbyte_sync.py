from airflow.sdk import Asset, dag, task
from pendulum import datetime


# Define the basic parameters of the DAG, like schedule and start_date
@dag(
    start_date=datetime(2025, 4, 22),
    schedule="@daily",
    doc_md=__doc__,
    default_args={"owner": "Airbyte", "retries": 3},
    tags=["airbyte"],
)
def airbyte():
    # Define tasks

    @task
    def get_meta():
        print("This should sync meta data through airbyte")    
    get_meta()
    @task
    def get_gads():
        print("This should sync gads data through airbyte")    
    get_gads()

# Instantiate the DAG
airbyte()
