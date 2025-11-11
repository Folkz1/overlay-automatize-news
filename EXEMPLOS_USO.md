# 📚 Exemplos de Uso - Microserviço Overlay

## 🌐 Exemplo 1: Com URL (Tradicional)

```json
POST /add-overlay
Content-Type: application/json

{
  "imageUrl": "https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=1024",
  "title": "VOCÊ ESTÁ DESPERDIÇANDO SUA CREATINA",
  "category": "SUPLEMENTOS"
}
```

## 🖼️ Exemplo 2: Com Base64 + Prefixo Data URI

```json
POST /add-overlay
Content-Type: application/json

{
  "imageUrl": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEAYABgAAD...",
  "title": "TREINO DE PERNAS COMPLETO",
  "category": "TREINO"
}
```

## 📦 Exemplo 3: Com Base64 Puro

```json
POST /add-overlay
Content-Type: application/json

{
  "imageUrl": "iVBORw0KGgoAAAANSUhEUgAAAAUA...",
  "title": "DIETA PARA GANHO DE MASSA",
  "category": "NUTRIÇÃO"
}
```


## 🔧 Exemplo 4: No N8N com URL

```json
{
  "method": "POST",
  "url": "https://seu-dominio.com/add-overlay",
  "sendBody": true,
  "bodyParameters": {
    "imageUrl": "={{ $json.image_url }}",
    "title": "={{ $json.title }}",
    "category": "={{ $json.category }}"
  }
}
```

## 🎨 Exemplo 5: No N8N com Base64 do DALL-E

Se o DALL-E retornar base64:

```json
{
  "method": "POST",
  "url": "https://seu-dominio.com/add-overlay",
  "sendBody": true,
  "bodyParameters": {
    "imageUrl": "={{ $json.dalle_image_base64 }}",
    "title": "={{ $json.title }}",
    "category": "={{ $json.category }}"
  }
}
```

## ✅ Resposta de Sucesso

```json
{
  "success": true,
  "image": "iVBORw0KGgoAAAANSUhEUgAAAAUA...",
  "contentType": "image/png",
  "size": 245678
}
```

## ❌ Resposta de Erro

```json
{
  "error": "Failed to add overlay",
  "message": "Invalid image format"
}
```

---

**Dica:** Use base64 quando a imagem já estiver em memória (ex: gerada por IA). Use URL quando a imagem estiver hospedada.
