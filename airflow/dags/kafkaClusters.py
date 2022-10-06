# importing the required libraries
import os
import sys
import defaults as defs
from airflow import DAG
from datetime import timedelta, datetime
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
#from airflow.providers.postgres.operators.postgres import PostgresOperator
from sqlalchemy import create_engine
import pandas as pd

# ENV_ID = os.environ.get("SYSTEM_TESTS_ENV_ID")
connection_string = defs.conn_string

default_args = {
    'owner': 'foxtrot',
    'depends_on_past': False,
    # 'start_date': days_ago(5),
    'email': ['fisseha.137@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(seconds=30),
    'tags': ['week7', 'Kafka clusters']
}

# define the DAG
etl_dag = DAG(
    'KAFKA_CLUSTERS_data_pipeline',
    default_args=default_args,
    start_date=datetime(2022, 10, 1),
    description='A data Extraction and loading pipeline for week 6 of 10 '
    + 'academy project',
    schedule=timedelta(days=1),     # run every day
    catchup=False                   # dont perform a backfill of missing runs
)


# region trigger task

def receive_trigger():
    print('trigger received . . .')


trigger_pipeline = PythonOperator(
    task_id='trigger_pipeline',
    python_callable=receive_trigger,
    dag=etl_dag
)

# endregion


# region read raw data

def read_raw_data():
    print('reading raw data . . .')
    raw_data = pd.read_csv('../data/raw_data.csv')
    print(raw_data.shape)
    print('reading raw data completed . . .')


raw_data_read = PythonOperator(
    task_id='raw_data_read',
    python_callable=read_raw_data,
    dag=etl_dag
)

# endregion


# region produce message

def produce_the_message():
    print('message procured')


produce_message = PythonOperator(
    task_id='produce_message',
    python_callable=produce_the_message,
    dag=etl_dag
)

# endregion


# region consume message

def consume_the_message():
    print('message consumed')


consume_message = PythonOperator(
    task_id='consume_message',
    python_callable=receive_trigger,
    dag=etl_dag
)

# endregion


# region transform and clean

def transform_and_prepare_the_message():
    print('message transformed and prepared')


transform_message = PythonOperator(
    task_id='transform_message',
    python_callable=transform_and_prepare_the_message,
    dag=etl_dag
)

# endregion


# region add meta data

def add_base_metadata():
    print('meta data added')


add_metadata = PythonOperator(
    task_id='add_metadata',
    python_callable=add_base_metadata,
    dag=etl_dag
)

# endregion


# region load to DWH

def load_to_DWH():
    print('data loaded to DWH')


load_message_to_DWH = PythonOperator(
    task_id='load_message_to_DWH',
    python_callable=load_to_DWH,
    dag=etl_dag
)

# endregion

trigger_pipeline >> raw_data_read >> produce_message >> consume_message >> transform_message >> add_metadata >> load_message_to_DWH
