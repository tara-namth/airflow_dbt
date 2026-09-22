FROM apache/airflow:3.3.2-python3.12

# Cài provider/package khai báo trong requirements.txt.
# Constraints bảo đảm chúng tương thích với Airflow 3.3.2 và Python 3.12.
COPY airflow/requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt \
    --constraint https://raw.githubusercontent.com/apache/airflow/constraints-3.3.2/constraints-3.12.txt
