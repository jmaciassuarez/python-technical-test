""" TERCERA PARTE AIRFLOW """

from datetime import timedelta, datetime
from airflow import DAG
# Operators
from airflow.operators.dummy_operator import DummyOperator


""" APARTADO 4) """
from time_diff import TimeDiff


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2020, 11, 21),
    'retries': 1,
    'retry_delay': timedelta(seconds=5)
}

dag = DAG(
    dag_id='dag_diff_dates',
    default_args=default_args,
    description='A diff date DAG',
    schedule_interval='0 3 * * *',
)

start = DummyOperator(
    task_id='start',
    dag=dag,
)

task_diff_date = TimeDiff(
    task_id='task_diff_date',
    name='my_task',
    diff_date='2016-11-22',
    format_date='%Y-%m-%d',
    dag=dag,
)

end = DummyOperator(
    task_id='end',
    dag=dag,
)

start >> task_diff_date >> end

