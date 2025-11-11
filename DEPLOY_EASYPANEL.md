# Deploy no Easypanel - Microserviço Overlay

## 🎯 Visão Geral

Guia passo a passo para subir o microserviço de overlay na sua VPS usando Easypanel.

---

## 📋 Pré-requisitos

- [ ] VPS com Easypanel instalado
- [ ] Acesso ao painel do Easypanel
- [ ] Repositório Git (GitHub/GitLab) ou upload manual

---

## 🚀 Método 1: Deploy via Git (RECOMENDADO)

### Passo 1: Preparar Repositório

#### 1.1 Criar Dockerfile

Crie o arquivo `Dockerfile` na pasta `microservico_overlay_python/`:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Instalar dependências do sistema para Pillow
RUN apt-get update && apt-get install -y \
    libjpeg-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements
COPY requirements.txt .

# Instalar dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código
COPY . .

# Expor porta
EXPOSE 3000

# Comando para iniciar
CMD ["python", "app.py"]
```

#### 1.2 Criar .dockerignore

```
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
*.so
*.egg
*.egg-info/
dist/
build/
test_*.png
.env
README.md
CHANGELOG.md
TESTE_RAPIDO.md
TESTAR_AGORA.md
DEPLOY_EASYPANEL.md
```

#### 1.3 Commit e Push

```bash
git add Dockerfile .dockerignore
git commit -m "Add Docker config for Easypanel"
git push
```

### Passo 2: Criar App no Easypanel

#### 2.1 Acessar Easypanel

1. Abrir painel do Easypanel
2. Clicar em **"Create"** ou **"New App"**

#### 2.2 Configurar App

**Aba General:**
- **Name:** `nutria-overlay-service`
- **Type:** App
- **Source:** Git Repository

**Aba Source:**
- **Repository URL:** URL do seu repositório Git
- **Branch:** main (ou master)
- **Build Path:** `/workflows/agentes/instagram/microservico_overlay_python`
- **Dockerfile Path:** `./Dockerfile`

**Aba Domains:**
- **Domain:** `overlay.seudominio.com` (ou usar domínio do Easypanel)
- **Enable HTTPS:** ✅ Sim

**Aba Environment:**
- **PORT:** `3000`

**Aba Resources:**
- **CPU:** 0.5 (suficiente)
- **Memory:** 512MB (suficiente)

#### 2.3 Deploy

1. Clicar em **"Deploy"**
2. Aguardar build (2-3 minutos)
3. Verificar logs

### Passo 3: Testar Deploy

#### 3.1 Health Check

```bash
curl https://overlay.seudominio.com/health
```

Deve retornar:
```json
{"status":"ok","service":"nutria-instagram-overlay-python"}
```

#### 3.2 Testar Overlay

```bash
curl -X POST https://overlay.seudominio.com/add-overlay \
  -H "Content-Type: application/json" \
  -d '{
    "imageUrl": "https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=1024",
    "title": "VOCÊ ESTÁ DESPERDIÇANDO SUA CREATINA",
    "category": "SUPLEMENTOS"
  }'
```

---

## 🚀 Método 2: Deploy Manual (Alternativa)

Se não quiser usar Git, pode fazer upload manual.

### Passo 1: Preparar Arquivos

Criar um arquivo `docker-compose.yml`:

```yaml
version: '3.8'

services:
  overlay-service:
    build: .
    ports:
      - "3000:3000"
    restart: unless-stopped
    environment:
      - PORT=3000
```

### Passo 2: Upload no Easypanel

1. Easypanel → Create App
2. Type: Docker Compose
3. Upload `docker-compose.yml`
4. Deploy

---

## 🔧 Configuração no N8N

Após deploy, atualizar URL no workflow N8N:

### Node: Overlay Service

```json
{
  "method": "POST",
  "url": "https://overlay.seudominio.com/add-overlay",
  "sendBody": true,
  "bodyParameters": {
    "imageUrl": "={{ $json.image_url }}",
    "title": "={{ $json.title }}",
    "category": "={{ $json.category }}"
  }
}
```

---

## 📊 Monitoramento

### Logs no Easypanel

1. Easypanel → Apps → nutria-overlay-service
2. Aba **Logs**
3. Ver logs em tempo real

### Métricas

1. Aba **Metrics**
2. Ver CPU, RAM, Network

### Restart

Se precisar reiniciar:
1. Aba **General**
2. Botão **Restart**

---

## 🔒 Segurança (Opcional)

### Adicionar Autenticação

Editar `app.py`:

```python
from functools import wraps
from flask import request

API_KEY = os.getenv('API_KEY', 'sua-chave-secreta')

def require_api_key(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        key = request.headers.get('X-API-Key')
        if key != API_KEY:
            return jsonify({'error': 'Invalid API key'}), 401
        return f(*args, **kwargs)
    return decorated_function

@app.route('/add-overlay', methods=['POST'])
@require_api_key  # Adicionar decorator
def add_overlay_endpoint():
    # ... resto do código
```

Adicionar variável de ambiente no Easypanel:
- **API_KEY:** `sua-chave-secreta-aqui`

---

## 💰 Custos

### VPS/Easypanel:
- **CPU:** 0.5 core
- **RAM:** 512MB
- **Custo estimado:** ~$2-5/mês (dependendo do plano)

### Tráfego:
- Cada imagem: ~500KB
- 30 posts/mês: ~15MB
- Custo de bandwidth: Desprezível

---

## 🐛 Troubleshooting

### Build falha no Easypanel

**Erro:** "Failed to build"

**Solução:**
1. Verificar se Dockerfile está correto
2. Verificar se requirements.txt está presente
3. Ver logs do build no Easypanel

### Serviço não inicia

**Erro:** "Container keeps restarting"

**Solução:**
1. Ver logs no Easypanel
2. Verificar se porta 3000 está correta
3. Verificar se dependências foram instaladas

### Timeout ao gerar imagem

**Erro:** "Request timeout"

**Solução:**
1. Aumentar timeout no N8N (60 segundos)
2. Verificar se URL da imagem é acessível
3. Verificar recursos da VPS (CPU/RAM)

---

## 🎉 Pronto!

Após deploy, seu microserviço estará disponível em:
```
https://overlay.seudominio.com
```

Use essa URL no workflow N8N! 🚀

---

**Última atualização:** 10/11/2025  
**Versão:** 1.0  
**Status:** ✅ Pronto para deploy
