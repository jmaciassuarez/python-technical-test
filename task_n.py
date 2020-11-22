

""" TERCERA PARTE AIRFLOW """

""" APARTADO 3) """

from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    # ¿Sería necesario empezar desde 1900??
    #'start_date': datetime(1900, 1, 1),
    'start_date': datetime(2020, 11, 21),
    'retries': 1,
    'retry_delay': timedelta(seconds=5)
}

dag = DAG(
    'task_n',
    default_args=default_args,
    description='A task_n DAG',
    #https://crontab.guru/ --> 3:00 UTC,
    schedule_interval='0 3 * * *',
)


task_1 = BashOperator(
    task_id='task_1_print_date',
    bash_command='date',
    dag=dag,
)
task_2 = BashOperator(
    task_id='task_2_sleep',
    depends_on_past=False,
    bash_command='sleep 5',
    retries=3,
    dag=dag,
)
task_3 = BashOperator(
    task_id='task_3_print_date',
    bash_command='date',
    dag=dag,
)
task_4 = BashOperator(
    task_id='task_4_sleep',
    depends_on_past=False,
    bash_command='sleep 5',
    retries=3,
    dag=dag,
)
task_5 = BashOperator(
    task_id='task_5_print_date',
    bash_command='date',
    dag=dag,
)
task_6 = BashOperator(
    task_id='task_6_sleep',
    depends_on_past=False,
    bash_command='sleep 5',
    retries=3,
    dag=dag,
)

task_2.set_downstream([task_1, task_3, task_5])

task_4.set_downstream([task_1, task_3, task_5])

task_6.set_downstream([task_1, task_3, task_5])