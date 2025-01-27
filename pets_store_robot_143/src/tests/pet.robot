*** Settings ***
### Bibliotecas
Library    RequestsLibrary
 
*** Variables ***
### Dados e Variaveis
${url}    https://petstore.swagger.io/v2/pet
 
${id}    298304288                    # $ = variavel simples
&{category}    id=1    name=Dog       # & = lista com campos fixos
${name}    Bolinha
@{photoUrls}                          # @ = lista não limitada
&{tag}    id=9    name=vaccined
@{tags}    ${tag}                     # Faz uma lista de outra lista
${status}   available
 
*** Test Cases ***
### Sequencia de execução dos passos/keywords
 
Post pet
    # montar a mensagem / request / body
    ${body}    Create Dictionary    id=${id}    category=${category}
                             ...    name=${name}  photoUrls=${photoUrls}
                             ...    tags=${tags}  status=${status}  
    # executar / enviar a request
    ${response}    POST    url=${url}    json=${body}
 
    # validar a response
    ${response_body}    Set Variable    ${response.json()}
    Log To Console    ${response_body}
 
    Status Should Be    200    #Status da Comunicação
    Should Be Equal    ${response_body}[id]                ${{int($id)}}
    Should Be Equal    ${response_body}[category][id]      ${{int($category['id'])}}
    Should Be Equal    ${response_body}[category][name]    ${category['name']}
    Should Be Equal    ${response_body}[name]              ${name}
    Should Be Empty    ${response_body}[photoUrls]        
    Should Be Equal    ${response_body}[tags][0][id]       ${{int($tag['id'])}}
    Should Be Equal    ${response_body}[tags][0][name]     ${tag['name']}
    Should Be Equal    ${response_body}[status]            ${status}
 
 
*** Keywords ***
### Ações associadas com frases reaproveitáveis

