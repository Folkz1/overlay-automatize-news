# Changelog - Microserviço Overlay Python

## Versão 1.3 - 14/11/2025

### ✨ Novas Funcionalidades

#### 1. Zoom Inteligente
- ✅ Aplica zoom na imagem mantendo o foco sem cortar partes importantes
- ✅ Configurável via .env ou JSON da requisição
- ✅ Opções de foco: `center`, `top`, `bottom`
- ✅ Fator de zoom ajustável (padrão: 1.2 = 20% de zoom)

#### 2. Logo "NUTRIA" em Negrito
- ✅ Fonte bold aplicada ao logo completo
- ✅ Texto mais grosso e impactante
- ✅ Mantém cores bicolor (branco + laranja)

#### 3. Configurações via .env
- ✅ Arquivo `.env` para configurações padrão
- ✅ Tamanhos de fonte configuráveis
- ✅ Cores configuráveis (logo e categorias)
- ✅ Textos do logo configuráveis
- ✅ Configurações de zoom

#### 4. Configurações via JSON (API)
- ✅ Sobrescrever qualquer configuração por requisição
- ✅ Customizar cores por categoria
- ✅ Customizar textos do logo
- ✅ Customizar tamanhos de fonte
- ✅ Customizar zoom (habilitar/desabilitar, fator, foco)

#### 5. Correção "FOFOCA MAROMBA"
- ✅ Remove underscore automaticamente
- ✅ `FOFOCA_MAROMBA` → `FOFOCA MAROMBA`
- ✅ Funciona tanto no input quanto no display

### 📝 Exemplo de Uso com Zoom

```json
{
  "imageUrl": "https://example.com/image.jpg",
  "title": "Como ganhar massa muscular rapidamente",
  "category": "TREINO",
  "config": {
    "zoom": {
      "enabled": true,
      "factor": 1.3,
      "focus": "center"
    }
  }
}
```

### 📝 Exemplo de Uso com Configurações Customizadas

```json
{
  "imageUrl": "https://example.com/image.jpg",
  "title": "Melhores suplementos para hipertrofia",
  "category": "SUPLEMENTOS",
  "config": {
    "colors": {
      "SUPLEMENTOS": "#FF0000"
    },
    "logoText": {
      "part1": "Fit",
      "part2": "AI"
    },
    "fontSizes": {
      "logo": 60,
      "category": 30,
      "title": 42
    }
  }
}
```

### 📚 Documentação

- ✅ `EXEMPLOS_CONFIG.md` - Guia completo de configuração
- ✅ Exemplos de uso via .env e JSON
- ✅ Todas as opções documentadas

---

## Versão 1.2 - 11/11/2025

### ✨ Novo: Suporte a Base64

#### Aceita 3 formatos de imagem:
- ✅ **URL:** `https://example.com/image.jpg`
- ✅ **Base64 com prefixo:** `data:image/png;base64,iVBORw0KG...`
- ✅ **Base64 puro:** `iVBORw0KG...` (PNG) ou `/9j/...` (JPEG)

#### Arquivos Docker para Deploy
- ✅ `Dockerfile` - Build otimizado
- ✅ `.dockerignore` - Ignora arquivos desnecessários
- ✅ Guias de deploy para Easypanel

#### Testes
- ✅ `test_base64.py` - Testa todos os formatos de imagem
- ✅ Compatibilidade mantida com URLs

### 📝 Exemplo de Uso Base64

```json
{
  "imageUrl": "data:image/jpeg;base64,/9j/4AAQSkZJRg...",
  "title": "TESTE COM BASE64",
  "category": "SUPLEMENTOS"
}
```

---

## Versão 1.1 - 10/11/2025

### ✨ Melhorias

#### 1. Logo NutrIA Bicolor
- ✅ "Nutr" em branco (#FFFFFF)
- ✅ "IA" em laranja (#FF6B00)
- Estilo mais moderno e profissional

#### 2. Categoria "FOFOCA MAROMBA"
- ✅ Removido underscore: `FOFOCA_MAROMBA` → `FOFOCA MAROMBA`
- Mais legível e natural

#### 3. Limite de Palavras no Título
- ✅ Padrão notjournal.ai: 7-15 palavras
- ✅ Truncamento automático se > 15 palavras
- ✅ Adiciona "..." quando truncado
- Títulos mais concisos e impactantes

### 🎨 Cores Mantidas

- SUPLEMENTOS: Verde (#00FF00) ✅
- TREINO: Laranja (#FF6B00) ✅
- NUTRIÇÃO: Azul (#00D4FF) ✅
- FOFOCA MAROMBA: Magenta (#FF00FF) ✅
- FITNESS: Dourado (#FFD700) ✅

### 📝 Exemplo de Uso

```json
{
  "imageUrl": "https://exemplo.com/imagem.jpg",
  "title": "VOCÊ ESTÁ DESPERDIÇANDO SUA CREATINA SEM SABER",
  "category": "SUPLEMENTOS"
}
```

**Resultado:**
- Logo: "Nutr" (branco) + "IA" (laranja)
- Categoria: "SUPLEMENTOS" (verde)
- Título: "VOCÊ ESTÁ DESPERDIÇANDO SUA CREATINA SEM SABER" (8 palavras ✅)

### 🚀 Como Testar

```bash
cd workflows/agentes/instagram/microservico_overlay_python
python app.py
```

Em outro terminal:
```bash
python test.py
```

Verifique os arquivos PNG gerados!

---

## Versão 1.0 - 10/11/2025

### 🎉 Lançamento Inicial

- ✅ API Flask com Pillow
- ✅ Overlay de texto em imagens
- ✅ 5 categorias com cores diferentes
- ✅ Logo NutrIA
- ✅ Gradiente escuro para legibilidade
- ✅ Título em 2 linhas máximo
- ✅ Instalação simples no Windows
