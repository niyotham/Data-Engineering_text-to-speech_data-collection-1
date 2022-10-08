from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

# print("this is a check for airflow")
with DAG(
    dag_id ='FirstDag',
    description = "First Dag",
    start_date = datetime(2022,10,4,10),
    schedule_interval = '@daily'
) as dag:
    # A task bash operator = runs bash command, python operator = runs python
    # code
    task1 = BashOperator(
        task_id='task_bash_operator_1',
        bash_command="echo 'Hello World!'"
    )
    task1
