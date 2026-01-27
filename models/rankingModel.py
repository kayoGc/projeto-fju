from firebase_admin import db
from datetime import datetime
# from pydantic import BaseModel
# from typing import Optional

referencia = db.reference('/ranking_tribos')

class FirebaseRanking:
    
    def atualizar(self, idTribo, seSubiu):
        # pega o timestamp no banco de dados
        # -> referencia para o timestamp
        refTempoQueComecou = referencia.child("data_comeco") 
        # -> pega o timestamp
        timestamp = refTempoQueComecou.get() 
        
        # converte o timestamp para data que o python entende
        dataQueComecou = datetime.fromtimestamp(timestamp)
        # pega a data de hoje
        dataDeHoje = datetime.now()
                
        # calcula a diferença entre as datas
        diferenca = dataDeHoje - dataQueComecou
        
        # pega o número da semana
        semana = (diferenca.days // 7) + 1
        
        # pega a quantidade de jovens no banco
        refSemanaTribo = referencia.child(f"semana_{semana}/{idTribo}")
        quantidadeDeJovens = refSemanaTribo.get() or 0
        
        # adiciona ou diminui a quantidade
        if seSubiu:
            quantidadeDeJovens += 1
        else:
            quantidadeDeJovens -= 1
            
        # atualiza o valor no banco
        refSemanaTribo.set(quantidadeDeJovens)