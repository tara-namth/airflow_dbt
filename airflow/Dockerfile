FROM apache/airflow:3.3.2-python3.12

# FAB Auth Manager cung cấp xác thực username/password lưu trong metadata database.
# Constraints bảo đảm provider tương thích với Airflow 3.3.2 và Python 3.12.
RUN pip install --no-cache-dir apache-airflow-providers-fab \
    --constraint https://raw.githubusercontent.com/apache/airflow/constraints-3.3.2/constraints-3.12.txt
