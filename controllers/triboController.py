from models.triboModel import RequestPostTribo, FirebaseTribo, RequestPutTribo
from fastapi import HTTPException

modelo = FirebaseTribo()
    
class TriboController:
    '''
    Controla o que acontece nas requisições
    '''
    
    def ler():
        dados = modelo.ler()
        
        return { "resultado": dados }
    
    def lerPorId(id):
        dados = modelo.lerPorId(id)
        
        return { "resultado": dados }
        
    
    def criar(tribo: RequestPostTribo):
        emBranco = []
        
        # vai analisar se strings não estão em branco
        for chave, valor in tribo.model_dump().items():
            
            if (isinstance(valor, str) and len(valor) == 0):
                emBranco.append(chave)
        
        # se tiver algum item vazio avisa para o cliente
        if (len(emBranco) > 0):
            mensagemDeErro = "Não foi possível criar, algum(ns) atributo(s) estão vazio(s): "
            
            for chave in emBranco:
                mensagemDeErro += f"{chave} "
            
            raise HTTPException(status_code=400, detail=mensagemDeErro)
            
        # cria o objeto e manda o id para o cliente
        chaveDosDados = modelo.criar(tribo)

        return { "message": "Deu tudo certo", "id": chaveDosDados }
    
    def atualizar(id, tribo: RequestPutTribo): 
        objDoUpdate = {}        
        
        # vai filtrar os dados no objDoUpdate
        if hasattr(tribo, "nome") and tribo.nome != None: 
            objDoUpdate['nome'] = tribo.nome
        
        if hasattr(tribo, "participantes") and tribo.participantes != None:
            objDoUpdate['participantes'] = tribo.participantes
        
        # retorna erro para o usuário se não tiver nada
        # len -> length -> tamanho
        if len(objDoUpdate) == 0:
            raise HTTPException(status_code=400, detail="Não foi enviado nenhum dado. Não da para proceder a atualização.")
        
        # se chegar aqui signfica da para atualizar sem erros
        modelo.atualizar(id, objDoUpdate)        
        
        return { "message": "Deu tudo certo" }
    
    def deletar(id):
        modelo.deletar(id)
        
        return { "message": "Deletado com sucesso" }