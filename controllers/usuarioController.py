from models.usuariosModel import RequestPostUsuario, FirebaseUsuario, RequestPutUsuario
from fastapi import HTTPException

modelo = FirebaseUsuario()

class UsuarioController:

    def ler():
        dados = modelo.ler()
        return {"resultado": dados}
    
    def lerPorId(id):
        dados = modelo.lerPorId(id)
        return {"resultado": dados}
    
    def criar(usuario: RequestPostUsuario):
        
        emBranco = []
        # vai analisar se strings não estão em branco
        for chave, valor in usuario.model_dump().items():
            
            if (isinstance(valor, str) and len(valor) == 0):
                emBranco.append(chave)
        
        # se tiver algum item vazio avisa para o cliente
        if (len(emBranco) > 0):
            mensagemDeErro = "Não foi possível criar, algum(ns) atributo(s) estão vazio(s): "
            
            for chave in emBranco:
                mensagemDeErro += f"{chave} "
            
            raise HTTPException(status_code=400, detail=mensagemDeErro)
            
        # cria o objeto e manda o id para o cliente
        chaveDosDados = modelo.criar(usuario)        
        return {"message": "Deu tudo certo!", "id": chaveDosDados}
    
    def atualizar(id, usuario: RequestPutUsuario):
        objDoUpdate = {}

        if hasattr(usuario, "nome") and usuario.nome != None:
            objDoUpdate['nome'] = usuario.nome

        if hasattr(usuario, "funcao") and usuario.funcao != None:
            objDoUpdate['funcao'] = usuario.funcao

        if hasattr(usuario, "idTribo") and usuario.idTribo != None:
            objDoUpdate['idTribo'] = usuario.idTribo

        if len(objDoUpdate) == 0:
            raise HTTPException(status_code=400, detail="Não foi enviado nenhum dado. Não é possível prosseguir com a atualização.")
        
        modelo.atualizar(id, objDoUpdate)

        return {"message": "Deu tudo certo"}
    
    def deletar(id):
        modelo.deletar(id)
        return {"message": "Deletado com sucesso"}