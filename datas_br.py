from datetime import datetime, timedelta

class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.format_data()

    def mes_cadastro(self):
        meses_do_ano = ["janeiro","fevereiro","março","abril","maio","junho","julho","agisto","setembro","outubro","novembro","dezembro"]
        mes_cadastro = self.momento_cadastro.month-1
        return meses_do_ano[mes_cadastro]

    def dia_semana(self):
        dia_semana = ["segunda","terça","quarta","quinta","sexta","sabado","domingo"]
        dia_cadastro = self.momento_cadastro.weekday()
        return dia_semana[dia_cadastro]

    def format_data(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
        return (data_formatada)