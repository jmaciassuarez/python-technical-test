from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator



""" TERCERA PARTE AIRFLOW """

""" APARTADO 1) """
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
    'test',
    default_args=default_args,
    description='A simple test DAG',
    #https://crontab.guru/ --> 3:00 UTC,
    schedule_interval='0 3 * * *',
)


""" APARTADO 2) """
start = DummyOperator(
    task_id='start',
    dag=dag,
)

end = DummyOperator(
    task_id='end',
    dag=dag,
)

start >> end

