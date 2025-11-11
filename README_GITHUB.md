# 🎨 NutrIA Overlay Microservice

Microserviço Python para adicionar overlays de texto em imagens para posts do Instagram.

## 🚀 Deploy Rápido

### Easypanel (Recomendado)

1. **Criar App no Easypanel**
   - Type: App
   - Source: Git Repository
   - Repository: `https://github.com/Folkz1/overlay-automatize-news.git`
   - Branch: `main`
   - Dockerfile: `./Dockerfile`

2. **Configurar**
   - Port: `3000`
   - CPU: `0.5`
   - Memory: `512MB`

3. **Deploy!**

Veja o guia completo: [GUIA_DEPLOY_PASSO_A_PASSO.md](GUIA_DEPLOY_PASSO_A_PASSO.md)

## 📡 API

### Health Check
```bash
GET /health
```

### Add Overlay
```bash
POST /add-overlay
Content-Type: application/json

{
  "imageUrl": "https://example.com/image.jpg",
  "title": "VOCÊ ESTÁ DESPERDIÇANDO SUA CREATINA?",
  "category": "SUPLEMENTOS"
}
```

## 🎨 Categorias

- `SUPLEMENTOS` - Verde
- `TREINO` - Laranja
- `NUTRIÇÃO` - Azul
- `FOFOCA MAROMBA` - Magenta
- `FITNESS` - Dourado

## 🖼️ Especificações

- **Tamanho:** 1080x1080px (Instagram square)
- **Formato:** PNG
- **Logo:** NutrIA (branco + laranja)
- **Título:** 7-15 palavras, máximo 2 linhas

## 🛠️ Tecnologias

- Python 3.11
- Flask
- Pillow (PIL)
- Docker

## 📄 Licença

MIT

---

**Desenvolvido para NutrIA** 🥗💪
