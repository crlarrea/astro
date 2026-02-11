"""
### Run a dbt Core project as a task group with Cosmos

Simple DAG showing how to run a dbt project as a task group, using
an Airflow connection and injecting a variable into the dbt project.
"""

from airflow.sdk import dag, chain
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from cosmos import DbtTaskGroup, ProjectConfig, ProfileConfig, ExecutionConfig
from pendulum import datetime

# adjust for other database types
from cosmos.profiles.postgres import PostgresUserPasswordProfileMapping
import os

YOUR_NAME = "Christian Larrea"
CONNECTION_ID = "db_conn"
DB_NAME = "postgres"


SOURCE_SCHEMA_NAME= "public"
API_SCHEMA_NAME = "api"
# The path to the dbt project
DBT_PROJECT_PATH = f"{os.environ['AIRFLOW_HOME']}/include/dbt/larrea"

# OPTIONAL: The path where Cosmos will find the dbt executable
# in the virtual environment created in the Dockerfile if you cannot 
# install your dbt adapter in requirements.txt due to package conflicts.
# DBT_EXECUTABLE_PATH = f"{os.environ['AIRFLOW_HOME']}/dbt_venv/bin/dbt"

profile_config = ProfileConfig(
    profile_name="default",
    target_name="dev",
    profile_mapping=PostgresUserPasswordProfileMapping(
        conn_id=CONNECTION_ID,
        profile_args={"schema": SOURCE_SCHEMA_NAME},
    ),
)

# OPTIONAL: The path where Cosmos will find the dbt executable
# execution_config = ExecutionConfig(
#     dbt_executable_path=DBT_EXECUTABLE_PATH,
# )


@dag(
    params={"my_name": YOUR_NAME},
    start_date=datetime(2026, 1, 10),
    schedule="@daily",
    doc_md=__doc__,
    default_args={"owner": "Astro", "retries": 3},
    tags=["content"],
)

def featured_content():
    transform_data = DbtTaskGroup(
        group_id="featured_content",
        project_config=ProjectConfig(DBT_PROJECT_PATH),
        profile_config=profile_config,
        # OPTIONAL: your execution config if you are using a virtual environment
        # execution_config=execution_config,
        operator_args={
            "vars": '{"my_name": {{ params.my_name }} }',
        },
        default_args={"retries": 2},
    )

    featured_book_api = SQLExecuteQueryOperator(
        task_id="featured_book_api",
        conn_id=CONNECTION_ID,
        sql=f"TRUNCATE {API_SCHEMA_NAME}.feautred_book; INSERT INTO {DB_NAME}.{API_SCHEMA_NAME}.featured_book (SELECT * FROM {DB_NAME}.{SOURCE_SCHEMA_NAME}.featured_book)",
    )
    featured_article_api = SQLExecuteQueryOperator(
        task_id="featured_article_api",
        conn_id=CONNECTION_ID,
        sql=f"TRUNCATE {API_SCHEMA_NAME}.featured_article; INSERT INTO {DB_NAME}.{API_SCHEMA_NAME}.featured_article (SELECT * FROM {DB_NAME}.{SOURCE_SCHEMA_NAME}.featured_article)",
    )

    chain(transform_data, [featured_book_api, featured_article_api])


featured_content()
