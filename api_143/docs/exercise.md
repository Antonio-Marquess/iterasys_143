# Exercício de Teste de API com Postman: Entidade Store

## **Descrição do Exercício**

Na API da Pet Store, Vamos testar o Post da entidade Store, utilizando o Postman.

### **Objetivo**

O objetivo deste teste é garantir que o endpoint de criação de pedidos da entidade `Store` (método `POST`) funcione corretamente, retornando os dados esperados com base nos valores fornecidos.

---

### **Etapas:**

* [x] 1 - Ver a documentação (o que é transmitido na ida e na volta)
* [x] 2 - Criar um arquivo csv com os dados
* [x] 3 - Duplicar o método padrão (Post Store DDT)
* [x] 4 - Parametrizar o body com as variáveis
* [x] 5 - Criar os testes em Post Scripts (validar os 6 campos)
* [x] 6 - Usar o Runner para rodar o teste

---

## **Etapas do Exercício**

### **1. Ver a documentação da API**

Antes de começar, acesse a [documentação oficial da Pet Store API](https://petstore.swagger.io/) para entender os dados necessários na requisição e os campos esperados na resposta. O endpoint que vamos usar é:

* **URL:** `/v2/store/order`
* **Método:** POST

#### **Campos Requeridos na Requisição:**

* `id` (number): ID do pedido.
* `petId` (number): ID do animal de estimação.
* `quantity` (number): Quantidade do pedido.
* `shipDate` (string): Data de envio no formato ISO 8601.
* `status` (string): Status do pedido. Valores possíveis: `placed`, `approved`, `delivered`, `canceled`.
* `complete` (boolean): Indica se o pedido foi concluído.

#### **Resposta Esperada:**

A resposta deve retornar um JSON com os mesmos campos enviados na requisição, além de um status HTTP 200 para sucesso.

---

### **2. Criar um arquivo CSV com os dados de teste**

Criou um arquivo chamado `store_data.csv` contendo os dados de entrada para o teste. Cada linha representa uma iteração no teste automatizado.

#### **Conteúdo do Arquivo CSV:**

```csv
id,petId,quantity,shipDate,status,complete
1,101,5,2024-01-25T10:00:00Z,placed,true
2,102,2,2024-01-26T12:30:00Z,approved,false
3,103,1,2024-01-27T15:45:00Z,delivered,true
4,104,10,2024-01-28T09:15:00Z,canceled,false
5,105,3,2024-01-29T18:20:00Z,placed,true
```

| **id** | **petId** | **quantity** | **shipDate**            | **status** | **complete** |
|--------|-----------|--------------|-------------------------|------------|--------------|
| 1      | 101       | 5            | 2024-01-25T10:00:00Z    | placed     | true         |
| 2      | 102       | 2            | 2024-01-26T12:30:00Z    | approved   | false        |
| 3      | 103       | 1            | 2024-01-27T15:45:00Z    | delivered  | true         |
| 4      | 104       | 10           | 2024-01-28T09:15:00Z    | canceled   | false        |
| 5      | 105       | 3            | 2024-01-29T18:20:00Z    | placed     | true         |

Cada coluna corresponde a uma variável que será usada para preencher o body da requisição e validar a resposta da API.

---

### **3 - Duplicar o método padrão (Post Store DDT)**

* **Passo 1: Localizar a Requisição POST na Coleção**
  * 1 -> Abra o **Postman**.
  * 2 -> Vá até a **coleção** onde você já tem a requisição **POST** configurada.
  * 3 -> Clique na coleção para expandi-la e encontrar a requisição **POST** que você deseja duplicar (por exemplo, `/v2/store/order`).

* **Passo 2: Duplicar a Requisição POST**
  * 1 -> Com a requisição **POST** aberta, no topo da requisição, clique no ícone de **três pontos verticais** (opções) no canto superior direito da requisição.
  * 2 -> No menu que aparece, selecione a opção **"Duplicate"** (Duplicar). Isso criará uma **cópia exata** da requisição.

* **Passo 3: Renomear a Nova Requisição**

  * 1 -> Após duplicar a requisição, o **Postman** criará uma nova requisição com o nome padrão **"Copy of [Nome da Requisição]"**.
  * 2 -> Clique no nome da nova requisição para editar e renomeá-la para algo mais específico, como **"Post Store DDT"** ou algo que ajude a identificar que é para **Data-Driven Testing**.

* **Passo 4: Parametrizar o Body da Requisição**

  * Agora, você vai substituir os **valores fixos** no corpo da requisição por **variáveis** para permitir que o Postman alimente os dados de maneira dinâmica durante o teste.

---

### **4. Configuração do Postman**

#### **Requisição: POST Store DDT**

Configuração básica da requisição na coleção:

* **URL:** `https://petstore.swagger.io/v2/store`
* **Método:** POST
* **Headers:**
  * Content-Type: application/json
* **Body (parametrizado):**

```json
{
  "id": {{id}},
  "petId": {{petId}},
  "quantity": {{quantity}},
  "shipDate": "{{shipDate}}",
  "status": "{{status}}",
  "complete": {{complete}}
}
```

Os campos entre `{{}}` são placeholders que serão substituídos pelos valores do arquivo CSV durante a execução.

---

### **5. Scripts de Testes (Post-Scripts)**

Os testes são implementados na aba **Tests** da requisição, verificando os campos da resposta e o status code.

#### **Script Completo:**

```javascript
// Carregar as variáveis da iteração (csv)
let id = pm.iterationData.get('id');
let petId = pm.iterationData.get('petId');
let quantity = pm.iterationData.get('quantity');
let shipDate = pm.iterationData.get('shipDate');
let status = pm.iterationData.get('status');
let complete = pm.iterationData.get('complete');

// Verificar o status code da comunicação
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});

// Converter a resposta para JSON
let jsonData = pm.response.json();

// Teste para validar o campo "id"
pm.test('Verifica o id', function(){
    pm.expect(jsonData.id).to.eql(id);
});

// Teste para validar o campo "petId"
pm.test('Verifica o petId', function(){
    pm.expect(jsonData.petId).to.equal(petId);
});

// Teste para validar o campo "quantity"
pm.test('Verifica a quantidade', function(){
    pm.expect(jsonData.quantity).to.eql(quantity);
});

// Teste para validar o campo "shipDate"
pm.test('Verifica o shipDate', function(){
    pm.expect(jsonData.shipDate).to.equal(shipDate);
});

// Teste para validar o campo "status"
pm.test('Verifica o status', function(){
    pm.expect(jsonData.status).to.eql(status);
});

// Teste para validar o campo "complete"
pm.test('Verifica o termino', function(){
    pm.expect(jsonData.complete).to.equal(complete);
});
```

---

### **6. Executando o Teste no Runner**

1. Abra o **Collection Runner** no Postman.
2. Selecione a coleção que contém a requisição `POST Store DDT`.
3. Configure:
   * **Arquivo de Dados:** `store_data.csv`
   * **Número de iterações:** Automático (baseado no número de linhas do CSV).
4. Clique em **Run**.

#### **Resultados Esperados:**

* Cada iteração valida os campos `id`, `petId`, `quantity`, `shipDate`, `status` e `complete` retornados pela API.
* Todos os testes devem passar para confirmar o funcionamento correto do endpoint.

---

#### **Link da collections:**

[text](https://www.postman.com/maintenance-saganist-87549155/iterasys-143/collection/ka1uv9i/swagger-petstore)
