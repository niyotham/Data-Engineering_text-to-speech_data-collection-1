from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.s3_file_transform_operator import S3FileTransformOperator

from datetime import datetime, timedelta

default_args = {
    "owner": "g1",
    "depends_on_past": False,
    "start_date": datetime(2022,10, 8),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5)
}
with DAG("S3_reading_data", default_args=default_args, schedule_interval= '@once') as dag:

    t1 = BashOperator(
        task_id='moving_data',
        bash_command='echo "hello, it should work" > s3_conn_test.txt'
    )

moving_unprocessed_data = S3FileTransformOperator(
    ask_id='ETL_amharic_news',
    description='unprocessed data',
    source_s3_key='s3:/home/data/raw_data.csv',
    dest_s3_key='s3:/home/data/raw_data1.csv',
    replace=False,
    #transform_script='transform.py',
    source_aws_conn_id='s3_connection',
    dest_aws_conn_id='s3_connection'
    )
# executing 
t1.set_upstream(moving_unprocessed_data)