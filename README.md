# Apache Airflow 3.3.2

Stack chạy Apache Airflow 3.3.2 với `LocalExecutor` và PostgreSQL bên ngoài Docker.

Khởi động:

```powershell
Copy-Item .env.example .env
docker compose up -d --build
```

Lần đầu chạy sẽ build image cục bộ có FAB Auth Manager, sau đó `airflow-init` migrate metadata database và tạo tài khoản admin.

Các service Airflow chạy thường trực là `airflow-api-server`, `airflow-scheduler` và `airflow-dag-processor`. Service `airflow-init` chỉ chạy một lần để migrate các bảng metadata.

Các Python provider/package bổ sung được khai báo trong `airflow/requirements.txt`. Sau khi thay đổi file này, build lại image:

```powershell
docker compose up -d --build
```

## Đường dẫn và kết nối

| Thành phần | Giá trị |
| --- | --- |
| Airflow UI | http://localhost:8080 |
| DAGs trên máy | `./airflow/dags/` |
| DAGs trong container | `/opt/airflow/dags` |
| Airflow logs | Docker volume `airflow-logs` (`/opt/airflow/logs`) |
| Metadata PostgreSQL | `10.47.4.74:5432/airflow` |
| Biến kết nối | `AIRFLOW_DB_URL` trong `.env` |

`AIRFLOW_DB_URL` phải có dạng SQLAlchemy PostgreSQL:

```env
AIRFLOW_DB_URL=postgresql+psycopg2://<username>:<password>@10.47.4.74:5432/airflow
```

PostgreSQL phải cho phép Docker host kết nối đến cổng `5432`, và user cần quyền tạo/cập nhật các bảng metadata của Airflow trong database `airflow`.

## Tài khoản và mật khẩu

Đặt username và password quản trị trong `.env`:

```env
AIRFLOW_ADMIN_USER=admin
AIRFLOW_ADMIN_PASSWORD=doi-mat-khau-manh-o-day
```

Airflow dùng FAB Auth Manager; user và mật khẩu được lưu trong metadata PostgreSQL, không ghi plaintext vào Docker volume. Đăng nhập tại http://localhost:8080 bằng hai giá trị trên.
