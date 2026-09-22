FROM apache/airflow:3.3.2-python3.12

# dbt có virtualenv riêng, tránh xung đột dependency (như protobuf) với Airflow.
USER root
COPY dbt/requirements.txt /tmp/dbt-requirements.txt
RUN python -m venv /opt/dbt-venv \
    && /opt/dbt-venv/bin/pip install --no-cache-dir -r /tmp/dbt-requirements.txt \
    && chown -R 50000:0 /opt/dbt-venv

# Cài provider/package Airflow trong environment Airflow theo constraints chính thức.
USER airflow
COPY airflow/requirements.txt /requirements/airflow.txt
RUN pip install --no-cache-dir \
    -r /requirements/airflow.txt \
    --constraint https://raw.githubusercontent.com/apache/airflow/constraints-3.3.2/constraints-3.12.txt
