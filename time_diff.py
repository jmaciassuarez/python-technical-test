from airflow.models.baseoperator import BaseOperator
from airflow.utils.decorators import apply_defaults
from datetime import datetime, date

"""
APARTADO 5)
    Los Hooks actúan como interfaces para establecer conexiones con recursos externos compartidos en un DAG. 
    Por ejemplo, varias tareas en un DAG pueden requerir acceso a una base de datos MySQL. 
    En lugar de crear una conexión por tarea, se puede recuperar una conexión del hook y utilizarla en las distintas tareas
    y también ayuda a evitar el almacenamiento de parámetros de autenticación de conexión en un DAG.
"""

class TimeDiff(BaseOperator):
    @apply_defaults
    def __init__(
            self,
            name: str,
            diff_date: str,
            format_date: str,
            *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.name = name
        self.diff_date = diff_date
        self.format_date = format_date

    def execute(self, context):
        diff_date = datetime.strptime(self.diff_date, self.format_date)
        today_str = date.today().strftime(self.format_date)
        today = datetime.strptime(today_str, self.format_date)
        diff = abs((today - diff_date).days)
        print(diff, "en días")
        #return diff
        pass

