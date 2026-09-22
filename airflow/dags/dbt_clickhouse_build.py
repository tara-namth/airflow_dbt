from datetime import datetime

from airflow.providers.standard.operators.bash import BashOperator
from airflow.sdk import DAG


with DAG(
    dag_id="dbt_clickhouse_build",
    description="Run dbt models in ClickHouse using the isolated dbt virtualenv.",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    tags=["dbt", "clickhouse"],
) as dag:
    BashOperator(
        task_id="dbt_build",
        bash_command=(
            "/opt/dbt-venv/bin/dbt build "
            "--project-dir /opt/airflow/dbt "
            "--profiles-dir /opt/airflow/dbt"
        ),
    )
