from models.jovensModel import RequestPostJovem, FirebaseJovem, RequestPutJovem
from models.rankingModel import FirebaseRanking
from fastapi import HTTPException

modelo = FirebaseJovem()
modeloRanking = FirebaseRanking()
    
class JovemController:
    '''
    Controla o que acontece nas requisições
    '''
    
    def ler():
        dados = modelo.ler()
        
        return { "resultado": dados }
    
    def lerPorId(id):
        dados = modelo.lerPorId(id)
        
        return { "resultado": dados }
        
    
    def criar(jovem: RequestPostJovem):
        
        emBranco = []
        # vai analisar se strings não estão em branco
        for chave, valor in jovem.model_dump().items():
            
            if (isinstance(valor, str) and len(valor) == 0):
                emBranco.append(chave)
        
        # se tiver algum item vazio avisa para o cliente
        if (len(emBranco) > 0):
            mensagemDeErro = "Não foi possível criar, algum(ns) atributo(s) estão vazio(s): "
            
            for chave in emBranco:
                mensagemDeErro += f"{chave} "
            
            raise HTTPException(status_code=400, detail=mensagemDeErro)
            
        # cria o objeto e manda o id para o cliente
        chaveDosDados = modelo.criar(jovem)
        
        modeloRanking.atualizar(jovem.idTribo, True)

        return { "message": "Deu tudo certo", "id": chaveDosDados }
    
    def atualizar(id, jovem: RequestPutJovem): 
        objDoUpdate = {}        
        
        # vai filtrar os dados no objDoUpdate
        if hasattr(jovem, "nome") and jovem.nome != None: 
            objDoUpdate['nome'] = jovem.nome
        
        if hasattr(jovem, "idTribo") and jovem.idTribo != None:
            objDoUpdate['id_tribo'] = jovem.idTribo
        
        if hasattr(jovem, "idUsuario") and jovem.idUsuario != None:
            objDoUpdate['id_usuario'] = jovem.idUsuario
        
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