# ✅ Código no GitHub - Agora Configure no Easypanel!

## 🎉 Status: Código Enviado com Sucesso!

Seu repositório está pronto:
**https://github.com/Folkz1/overlay-automatize-news.git**

---

## 🚀 Próximo Passo: Configurar no Easypanel

### 1️⃣ Acessar Easypanel

Abra seu painel do Easypanel no navegador.

### 2️⃣ Criar Novo App

Clique em **"Create"** ou **"New App"**

### 3️⃣ Configurações Exatas

Copie e cole estas configurações:

#### 📦 Aba: General
```
Name: nutria-overlay-service
Type: App
```

#### 🔗 Aba: Source
```
Type: Git Repository
Repository URL: https://github.com/Folkz1/overlay-automatize-news.git
Branch: master
Build Path: (deixar vazio)
Dockerfile Path: ./Dockerfile
```

#### 🌐 Aba: Domains
```
Adicionar domínio:
- Use o domínio automático do Easypanel, OU
- Configure seu próprio subdomínio (ex: overlay.seudominio.com)

✅ Marcar: Enable HTTPS
```

#### ⚙️ Aba: Environment Variables
```
PORT = 3000
```

#### 💻 Aba: Resources
```
CPU: 0.5
Memory: 512 (MB)
```

### 4️⃣ Deploy!

1. Clique em **"Deploy"** ou **"Create & Deploy"**
2. Aguarde 2-5 minutos (acompanhe os logs)
3. Quando aparecer "Running", está pronto!

---

## 🧪 Testar Após Deploy

### Health Check

Substitua `SEU-DOMINIO` pelo domínio que o Easypanel forneceu:

```bash
curl https://SEU-DOMINIO/health
```

Deve retornar:
```json
{"status":"ok","service":"nutria-instagram-overlay-python"}
```

### Testar Overlay

```bash
curl -X POST https://SEU-DOMINIO/add-overlay ^
  -H "Content-Type: application/json" ^
  -d "{\"imageUrl\":\"https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=1024\",\"title\":\"VOCÊ ESTÁ DESPERDIÇANDO SUA CREATINA\",\"category\":\"SUPLEMENTOS\"}"
```

---

## 🔧 Configurar no N8N

Após o deploy funcionar, atualizar o workflow N8N:

1. Abrir workflow do Instagram no N8N
2. Encontrar node **"Overlay Service"** ou **"HTTP Request"**
3. Atualizar URL para: `https://SEU-DOMINIO/add-overlay`
4. Salvar e testar!

---

## 📊 Monitorar no Easypanel

### Ver Logs
- Easypanel → Apps → nutria-overlay-service
- Aba **"Logs"**

### Ver Métricas
- Aba **"Metrics"**
- Monitorar CPU, RAM, Network

### Reiniciar
- Aba **"General"**
- Botão **"Restart"**

---

## 🐛 Problemas Comuns

### Build Falha

**Erro:** "Build failed"

**Solução:**
1. Verificar logs do build
2. Confirmar que Branch é `master` (não `main`)
3. Confirmar que Dockerfile Path é `./Dockerfile`

### Container Reinicia

**Erro:** "Container keeps restarting"

**Solução:**
1. Ver logs no Easypanel
2. Verificar se porta 3000 está configurada
3. Verificar se há erros no código

### Não Consegue Acessar

**Erro:** "Cannot reach service"

**Solução:**
1. Verificar se HTTPS está habilitado
2. Aguardar alguns minutos (DNS pode demorar)
3. Verificar se domínio está correto

---

## ✅ Checklist Final

- [ ] Código no GitHub ✅ (FEITO!)
- [ ] App criado no Easypanel
- [ ] Configurações corretas
- [ ] Deploy completado
- [ ] Health check funcionando
- [ ] Teste de overlay funcionando
- [ ] URL atualizada no N8N
- [ ] Workflow testado

---

## 🎯 Resumo das URLs

**Repositório GitHub:**
```
https://github.com/Folkz1/overlay-automatize-news.git
```

**Branch:**
```
master
```

**Dockerfile:**
```
./Dockerfile
```

**Porta:**
```
3000
```

---

## 💡 Dica

Salve o domínio que o Easypanel fornecer! Você vai precisar dele para configurar no N8N.

Exemplo: `https://nutria-overlay-service-abc123.easypanel.host`

---

**Última atualização:** 11/11/2025  
**Status:** ✅ Pronto para configurar no Easypanel!
