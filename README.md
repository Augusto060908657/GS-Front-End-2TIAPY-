# 🔥 FireGuard AI

## Global Solution 2026/1 – Front-End e Mobile Development em Sistemas de IA

### Integrantes

* Octavio Augusto Ramalho Brandão Pires RM:555696
* Guilherme Santos de Almeida RM:563972

---

# 📖 Sobre o Projeto

O FireGuard AI é uma plataforma inteligente de monitoramento climático e predição de risco de incêndios agrícolas desenvolvida para auxiliar produtores rurais, órgãos ambientais e gestores públicos na tomada de decisão preventiva.

A solução utiliza dados meteorológicos e ambientais para identificar condições favoráveis ao surgimento de queimadas, classificar o nível de risco e detectar possíveis anomalias climáticas.

O sistema foi desenvolvido utilizando Streamlit e segue uma arquitetura modular baseada em boas práticas de engenharia de software.

---

# 🎯 Problema

Eventos climáticos extremos vêm aumentando significativamente nos últimos anos, impactando diretamente a agricultura, a preservação ambiental e a segurança da população.

A identificação precoce de condições críticas pode reduzir prejuízos econômicos, minimizar impactos ambientais e aumentar a eficiência de ações preventivas.

O FireGuard AI foi criado para transformar dados climáticos em informações visuais e acionáveis para usuários não técnicos.

---

# 🚀 Funcionalidades

### Monitoramento Climático

* Temperatura
* Umidade
* Velocidade do vento
* Índice de precipitação

### Predição de Risco de Incêndio

Classificação automática em:

* 🟢 Baixo
* 🟡 Médio
* 🟠 Alto
* 🔴 Crítico

### Detecção de Anomalias Climáticas

Identificação automática de padrões climáticos fora da normalidade.

### Dashboard Interativo

* Filtros por região
* Filtros por período
* Filtros por nível mínimo de risco

### Human in the Loop

O sistema sugere alertas para regiões críticas e permite que o usuário aprove ou rejeite o envio.

---

# 🏗 Arquitetura do Projeto

```text
fireguard-ai/

├── app.py
│
├── providers/
│   ├── weather_provider.py
│   └── mock_provider.py
│
├── pipelines/
│   ├── risk_pipeline.py
│   └── anomaly_pipeline.py
│
├── features/
│   ├── dashboard.py
│   └── alerts.py
│
├── state/
│   └── app_state.py
│
├── UI/
│   ├── sidebar.py
│   ├── cards.py
│   └── charts.py
│
├── requirements.txt
└── README.md
```

---

# 🧠 Tecnologias Utilizadas

* Python 3.11+
* Streamlit
* Pandas
* NumPy
* Plotly
* Matplotlib
* Requests

---

# 📊 Fluxo de Funcionamento

```text
Dados Climáticos
        ↓
Providers
        ↓
Pipelines
        ↓
Classificação de Risco
        ↓
Detecção de Anomalias
        ↓
Dashboard Interativo
        ↓
Tomada de Decisão
```

---

# 🔍 Cálculo de Risco

O índice de risco é calculado considerando:

* Temperatura
* Velocidade do vento
* Umidade relativa do ar
* Volume de chuva

Fórmula utilizada:

Risco =
(Temperatura × 0.4)

* (Vento × 0.3)
* ((100 - Umidade) × 0.2)
* ((30 - Chuva) × 0.1)

---

# ⚙️ Instalação

Clone o repositório:

```bash
git clone 
```

Acesse a pasta:

```bash
cd fireguard-ai
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

# ▶️ Execução

Execute:

```bash
streamlit run app.py
```

A aplicação ficará disponível em:

```text
http://localhost:8501
```

---

# 📄 Licença

Projeto acadêmico desenvolvido para a disciplina Front-End e Mobile Development em Sistemas de IA – Global Solution 2026/1.
