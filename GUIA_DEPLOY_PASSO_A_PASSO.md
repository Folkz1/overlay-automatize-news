# 🚀 Guia de Deploy - Passo a Passo

## ✅ Arquivos Criados

Os seguintes arquivos foram criados para o deploy:

- ✅ `Dockerfile` - Configuração do container Docker
- ✅ `.dockerignore` - Arquivos a ignorar no build
- ✅ `.gitignore` - Arquivos a ignorar no Git

## 📦 Passo 1: Preparar Repositório Git

### 1.1 Navegar até a pasta do microserviço

```bash
cd workflows/agentes/instagram/microservico_overlay_python
```

### 1.2 Inicializar Git (se ainda não foi feito)

```bash
git init
```

### 1.3 Adicionar remote do seu repositório

```bash
git remote add origin https://github.com/Folkz1/overlay-automatize-news.git
```

### 1.4 Adicionar todos os arquivos

```bash
git add .
```

### 1.5 Fazer commit

```bash
git commit -m "Add overlay microservice with Docker config"
```

### 1.6 Push para GitHub

```bash
git push -u origin main
```

**Nota:** Se o branch for `master` ao invés de `main`, use:
```bash
git push -u origin master
```

---

## 🌐 Passo 2: Configurar no Easypanel

### 2.1 Acessar Easypanel

1. Abrir o painel do Easypanel no navegador
2. Fazer login

### 2.2 Criar Novo App

1. Clicar em **"Create"** ou **"New App"**
2. Escolher **"App"** (não Service)

### 2.3 Configurar Source

**Aba: Source**
- **Type:** Git Repository
- **Repository URL:** `https://github.com/Folkz1/overlay-automatize-news.git`
- **Branch:** `main` (ou `master`)
- **Build Path:** `/` (deixar vazio ou raiz)
- **Dockerfile Path:** `./Dockerfile`

### 2.4 Configurar General

**Aba: General**
- **Name:** `nutria-overlay-service`
- **Description:** Microserviço de overlay para Instagram

### 2.5 Configurar Domains

**Aba: Domains**
- Clicar em **"Add Domain"**
- Escolher um subdomínio (ex: `overlay.seudominio.com`)
- Ou usar o domínio automático do Easypanel
- **Enable HTTPS:** ✅ Marcar

### 2.6 Configurar Environment

**Aba: Environment Variables**
- **PORT:** `3000`

(Não precisa adicionar mais nada por enquanto)

### 2.7 Configurar Resources

**Aba: Resources**
- **CPU:** `0.5` (meio core é suficiente)
- **Memory:** `512` MB (suficiente para o serviço)

### 2.8 Deploy!

1. Clicar em **"Deploy"** ou **"Create & Deploy"**
2. Aguardar o build (2-5 minutos)
3. Acompanhar os logs

---

## 🧪 Passo 3: Testar o Deploy

### 3.1 Verificar Health Check

Após o deploy, testar:

```bash
curl https://SEU-DOMINIO.com/health
```

Deve retornar:
```json
{"status":"ok","service":"nutria-instagram-overlay-python"}
```

### 3.2 Testar Overlay

```bash
curl -X POST https://SEU-DOMINIO.com/add-overlay \
  -H "Content-Type: application/json" \
  -d "{\"imageUrl\":\"https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=1024\",\"title\":\"VOCÊ ESTÁ DESPERDIÇANDO SUA CREATINA\",\"category\":\"SUPLEMENTOS\"}"
```

Deve retornar JSON com `success: true` e a imagem em base64.

---

## 🔧 Passo 4: Configurar no N8N

### 4.1 Atualizar URL no Workflow

No seu workflow N8N, encontrar o node **"Overlay Service"** e atualizar:

**URL:** `https://SEU-DOMINIO.com/add-overlay`

### 4.2 Testar Integração

Executar o workflow e verificar se a imagem é gerada corretamente.

---

## 📊 Monitoramento

### Ver Logs

1. Easypanel → Apps → nutria-overlay-service
2. Aba **"Logs"**
3. Ver logs em tempo real

### Ver Métricas

1. Aba **"Metrics"**
2. Monitorar CPU, RAM, Network

### Reiniciar Serviço

Se necessário:
1. Aba **"General"**
2. Botão **"Restart"**

---

## 🐛 Troubleshooting

### Build Falha

**Problema:** Build não completa

**Solução:**
1. Verificar logs do build no Easypanel
2. Verificar se `requirements.txt` está presente
3. Verificar se Dockerfile está correto

### Container Reinicia Constantemente

**Problema:** Container keeps restarting

**Solução:**
1. Ver logs no Easypanel
2. Verificar se porta 3000 está correta
3. Verificar se app.py está sem erros

### Timeout ao Gerar Imagem

**Problema:** Request timeout

**Solução:**
1. Aumentar timeout no N8N (60 segundos)
2. Verificar se URL da imagem é acessível
3. Aumentar recursos (CPU/RAM) no Easypanel

---

## 🎉 Pronto!

Seu microserviço está no ar! 🚀

**URL do serviço:** `https://SEU-DOMINIO.com`

Use essa URL no N8N para gerar overlays automaticamente!

---

## 📝 Checklist Final

- [ ] Repositório Git configurado
- [ ] Push feito para GitHub
- [ ] App criado no Easypanel
- [ ] Build completado com sucesso
- [ ] Health check funcionando
- [ ] Teste de overlay funcionando
- [ ] URL atualizada no N8N
- [ ] Workflow testado end-to-end

---

**Última atualização:** 11/11/2025  
**Versão:** 1.0  
**Status:** ✅ Pronto para deploy
