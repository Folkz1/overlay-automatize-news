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

## ⚙️ Configuração

### Via .env (Configurações Padrão)

Copie `.env.example` para `.env` e ajuste:

```env
# Tamanhos de fonte
FONT_SIZE_LOGO=52
FONT_SIZE_CATEGORY=26
FONT_SIZE_TITLE=38

# Cores do logo (RGB)
LOGO_COLOR_NUTR=255,255,255
LOGO_COLOR_IA=255,107,0

# Cores por categoria (HEX)
COLOR_SUPLEMENTOS=#00FF00
COLOR_TREINO=#FF6B00
COLOR_NUTRICAO=#00D4FF
COLOR_FOFOCA_MAROMBA=#FF00FF
COLOR_FITNESS=#FFD700

# Textos do logo
TEXT_LOGO_PART1=Nutr
TEXT_LOGO_PART2=IA

# Zoom inteligente
ZOOM_ENABLED=true
ZOOM_FACTOR=1.2
ZOOM_FOCUS=center
```

### Via JSON (Por Requisição)

Você pode sobrescrever qualquer configuração por requisição! Veja `EXEMPLOS_CONFIG.md` para mais detalhes.

## 📡 API

### Health Check

```bash
GET http://localhost:3000/health
```

### Adicionar Overlay (Básico)

```bash
POST http://localhost:3000/add-overlay
Content-Type: application/json

{
  "imageUrl": "https://exemplo.com/imagem.jpg",
  "title": "VOCÊ ESTÁ DESPERDIÇANDO SUA CREATINA?",
  "category": "SUPLEMENTOS"
}
```

### Adicionar Overlay (Com Configurações)

```bash
POST http://localhost:3000/add-overlay
Content-Type: application/json

{
  "imageUrl": "https://exemplo.com/imagem.jpg",
  "title": "VOCÊ ESTÁ DESPERDIÇANDO SUA CREATINA?",
  "category": "SUPLEMENTOS",
  "config": {
    "zoom": {
      "enabled": true,
      "factor": 1.3,
      "focus": "center"
    },
    "colors": {
      "SUPLEMENTOS": "#FF0000"
    },
    "fontSizes": {
      "title": 42
    }
  }
}
```

**imageUrl aceita:**
- ✅ URL: `https://example.com/image.jpg`
- ✅ Base64 com prefixo: `data:image/png;base64,iVBORw0KG...`
- ✅ Base64 puro: `iVBORw0KG...` (PNG) ou `/9j/...` (JPEG)

**config (opcional):**
- `zoom`: Configurações de zoom inteligente
- `colors`: Cores customizadas por categoria
- `logoText`: Textos customizados do logo
- `logoColorNutr` / `logoColorIA`: Cores do logo
- `fontSizes`: Tamanhos de fonte customizados

## 🎨 Categorias e Cores

- `SUPLEMENTOS` - Verde (#00FF00)
- `TREINO` - Laranja (#FF6B00)
- `NUTRIÇÃO` - Azul (#00D4FF)
- `FOFOCA MAROMBA` - Magenta (#FF00FF)
- `FITNESS` - Dourado (#FFD700)

## 🎨 Logo NutrIA

- "Nutr" - Branco (#FFFFFF) - **NEGRITO**
- "IA" - Laranja (#FF6B00) - **NEGRITO**

## ✨ Zoom Inteligente

O microserviço aplica zoom inteligente nas imagens para melhor composição:

- **Habilitado por padrão** (configurável via .env ou JSON)
- **Fator de zoom:** 1.2 (20% de zoom) - ajustável
- **Foco:** center, top ou bottom
- **Mantém o foco** sem cortar partes importantes

Exemplo de uso:
```json
{
  "imageUrl": "...",
  "title": "...",
  "category": "...",
  "config": {
    "zoom": {
      "enabled": true,
      "factor": 1.3,
      "focus": "center"
    }
  }
}
```

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

## 📚 Documentação Adicional

- `EXEMPLOS_CONFIG.md` - Guia completo de configuração
- `CHANGELOG.md` - Histórico de versões
- `.env.example` - Exemplo de configuração

---

**Última atualização:** 14/11/2025  
**Versão:** 1.3  
**Status:** ✅ Pronto para uso

**Novidades v1.3:**
- ✅ Zoom inteligente configurável
- ✅ Logo em negrito
- ✅ Configurações via .env e JSON
- ✅ Correção automática "FOFOCA MAROMBA"
