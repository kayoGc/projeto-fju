# Documentação sobre os dados

Nesse arquivo está documentado os dados que guardamos no Firebase Realtime Database.

## Coleção Tribos

### Identificador

O identificador de cada dado é criado pelo proprío Firebase. Ex: **-OdUlsO69X87lD8dM_qA**

### Dados

- **nome**: Nome da tribo.
- **participantes**: lista de identificadores dos usuários participantes. Talvez seja removido por ser redundante.

### Exemplo

```JSON
"tribos": {
    "-OdUlsO69X87lD8dM_qA": {
        "nome": "Tribo A",
        "participantes": [
            "id Usuário A",
            "id Usuário B",
            // ...
        ]
    }
}
```

## Coleção usuários

### Identificador

O identificador de cada dado é criado pelo proprío Firebase. Ex: **-OdUlsO69X87lD8dM_qA**

### Dados

- **nome**: Nome do usuário.
- **funcao**: Qual papel o usuário desempenha em sua tribo (ex: membro, obreiro, lider, ...).
- **id_tribo**: Identificador da tribo que o usuário participa.

### Exemplo

```JSON
"usuarios": {
    "-Of0T20Ovj7BGHI9ms1F": {
        "nome": "Kayo",
        "funcao": "membro",
        // o usuário participa da tribo com o identificador -OdUlsO69X87lD8dM_qA
        "id_tribo": "-OdUlsO69X87lD8dM_qA"
    }
}
```

## Coleção Jovens

### Identificador

O identificador de cada dado é criado pelo proprío Firebase. Ex: **-OdUlsO69X87lD8dM_qA**

### Dados

- **nome**: Nomem do jovem.
- **id_tribo**: Identificador da tribo que trouxe o Jovem.
- **id_usuario**: Identificador do usuário que trouxe o Jovem.
- **e_afastado**: Se o Jovem é afastado ou não.

### Exemplo

```JSON
"jovens": {
    "-OdUlsO69X87lD8dM_kB": {
        "nome": "João",
        // a tribo com o identificador -OdUlsO69X87lD8dM_qA trouxe esse jovem
        "id_tribo": "-OdUlsO69X87lD8dM_qA",
        // o usuário com o identificador -Of0T20Ovj7BGHI9ms1F trouxe esse jovem
        "id_usuario": "-Of0T20Ovj7BGHI9ms1F"
    }
}
```

## Coleção ranking tribos

Essa coleção é um pouco diferente das outras.

Ela vai guardar um ranking semanal dos jovens que cada tribo trouxe.

### identificador

Cada identificador da coleção vai representar uma semana, assim vamos guardar o ranking semanal de cada tribo

Ex: 
```JSON
{
    "semana_1": {
        // ranking semana 1
    },
    "semana_2": {
        // ranking semana 2
    },
    "semana_n": {
        // ranking semana n
    }

}
```

### Dados

- **id aleatorio da tribo**: vai conter o número de jovens que a tribo trouxe. 

### Exemplo

```JSON
"ranking_tribos": {
    "semana_1": {
        // uma tribo levou 4 jovens
        "-OdUlFpNe7GMnfkNSsJm": 4,
        // outra tribo levou 2
        "-OdUlFpNe7GMnfkNSsXm": 2,
        // ...
    },
    "semana_2": {
        // uma tribo levou 12 jovens
        "-OdUlFpNe7GMnfkNSsJm": 12,
        // outra tribo levou 15
        "-OdUlFpNe7GMnfkNSsXm": 15,
        // ...
    },
    "semana_n": {
        // ranking semana n
    }
}
```