# Microserviço de Overlay - Python (Pillow)

## 🎯 Por Que Python?

- ✅ **Fácil instalação no Windows** (sem Visual Studio Build Tools)
- ✅ **Pillow é leve e rápido**
- ✅ **Funciona em qualquer OS**
- ✅ **Código mais simples**

## 🚀 Instalação e Uso

### 1. Instalar Python

Se não tiver Python instalado:
- Download: https://www.python.org/downloads/
- Marque "Add Python to PATH" durante instalação

### 2. Instalar Dependências

```bash
cd workflows/agentes/instagram/microservico_overlay_python
pip install -r requirements.txt
```

### 3. Iniciar Serviço

```bash
python app.py
```

Deve aparecer:
```
🚀 Overlay Microservice (Python) running on port 3000
📍 Health check: http://localhost:3000/health
📍 Add overlay: POST http://localhost:3000/add-overlay
```

### 4. Testar (Outro Terminal)

**Teste básico:**
```bash
python test.py
```

**Teste com base64:**
```bash
python test_base64.py
```

Isso vai gerar várias imagens PNG de exemplo!

## 📡 API

### Health Check

```bash
GET http://localhost:3000/health
```

### Adicionar Overlay

```bash
POST http://localhost:3000/add-overlay
Content-Type: application/json

{
  "imageUrl": "https://exemplo.com/imagem.jpg",
  "title": "VOCÊ ESTÁ DESPERDIÇANDO SUA CREATINA?",
  "category": "SUPLEMENTOS"
}
```

**imageUrl aceita:**
- ✅ URL: `https://example.com/image.jpg`
- ✅ Base64 com prefixo: `data:image/png;base64,iVBORw0KG...`
- ✅ Base64 puro: `iVBORw0KG...` (PNG) ou `/9j/...` (JPEG)

## 🎨 Categorias e Cores

- `SUPLEMENTOS` - Verde (#00FF00)
- `TREINO` - Laranja (#FF6B00)
- `NUTRIÇÃO` - Azul (#00D4FF)
- `FOFOCA MAROMBA` - Magenta (#FF00FF)
- `FITNESS` - Dourado (#FFD700)

## 🎨 Logo NutrIA

- "Nutr" - Branco (#FFFFFF)
- "IA" - Laranja (#FF6B00)

## 🖼️ Layout e Especificações

### Tamanho da Imagem
- **Largura:** 1080px
- **Altura:** 1080px
- **Formato:** PNG
- **Qualidade:** Alta (sem compressão)
- **Aspect Ratio:** 1:1 (Instagram square)

### Layout Visual

```
┌─────────────────────────────────────┐ 0px
│ NutrIA                              │ ← Logo (52px, posição Y: 80px)
│                                     │   "Nutr" branco + "IA" laranja
│                                     │
│         [IMAGEM DE FUNDO]           │
│                                     │
│                                     │ 700px ← Gradiente começa aqui
│ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ │
│ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ │
│ SUPLEMENTOS                         │ ← Categoria (26px, Y: 880px)
│ VOCÊ ESTÁ DESPERDIÇANDO             │ ← Título linha 1 (38px, Y: 930px)
│ SUA CREATINA?                       │ ← Título linha 2 (38px, Y: 980px)
└─────────────────────────────────────┘ 1080px

Posições Exatas:
- Logo: X: 40px, Y: 80px
- Categoria: X: 40px, Y: 880px
- Título (linha 1): X: 40px, Y: 930px
- Título (linha 2): X: 40px, Y: 980px
- Gradiente: Y: 700px até 1080px (380px de altura)
```

## 📏 Regras de Título

- **Mínimo:** 7 palavras
- **Máximo:** 15 palavras (padrão notjournal.ai)
- **Linhas:** Máximo 2 linhas
- **Truncamento:** Se > 15 palavras, adiciona "..."

## 🔧 Troubleshooting

### Erro: "No module named 'PIL'"

```bash
pip install Pillow
```

### Erro: "Address already in use"

Outro processo está usando a porta 3000. Mude a porta em `app.py`:

```python
PORT = 3001  # ou outra porta
```

### Fonte não encontrada

O código usa fonte padrão se Arial não estiver disponível. Funciona normalmente!

## 💰 Custos

- **Grátis** (self-hosted)
- Sem APIs externas
- Apenas CPU/RAM local

## 🚀 Produção

Para produção, use Gunicorn:

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:3000 app:app
```

---

**Vantagens sobre Node.js + Canvas:**
- ✅ Instalação mais simples no Windows
- ✅ Sem dependências nativas complexas
- ✅ Código mais limpo e legível
- ✅ Pillow é muito estável e maduro

**Última atualização:** 10/11/2025  
**Versão:** 1.0  
**Status:** ✅ Pronto para uso
