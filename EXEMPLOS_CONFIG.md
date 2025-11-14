# Exemplos de Configuração - Microserviço Overlay

## Configuração via .env

Todas as configurações padrão podem ser definidas no arquivo `.env`:

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

## Uso Básico (sem configurações customizadas)

```json
{
  "imageUrl": "https://example.com/image.jpg",
  "title": "Como ganhar massa muscular rapidamente",
  "category": "TREINO"
}
```

## Uso com Configurações Customizadas

### 1. Customizar Cores

```json
{
  "imageUrl": "https://example.com/image.jpg",
  "title": "Melhores suplementos para hipertrofia",
  "category": "SUPLEMENTOS",
  "config": {
    "colors": {
      "SUPLEMENTOS": "#FF0000"
    }
  }
}
```

### 2. Customizar Texto do Logo

```json
{
  "imageUrl": "https://example.com/image.jpg",
  "title": "Dieta para emagrecer",
  "category": "NUTRIÇÃO",
  "config": {
    "logoText": {
      "part1": "Fit",
      "part2": "AI"
    }
  }
}
```

### 3. Customizar Tamanhos de Fonte

```json
{
  "imageUrl": "https://example.com/image.jpg",
  "title": "Fofoca da academia",
  "category": "FOFOCA MAROMBA",
  "config": {
    "fontSizes": {
      "logo": 60,
      "category": 30,
      "title": 42
    }
  }
}
```

### 4. Customizar Zoom

```json
{
  "imageUrl": "https://example.com/image.jpg",
  "title": "Treino de pernas intenso",
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

**Opções de foco:**
- `center`: Foco no centro da imagem (padrão)
- `top`: Foco na parte superior
- `bottom`: Foco na parte inferior

### 5. Desabilitar Zoom

```json
{
  "imageUrl": "https://example.com/image.jpg",
  "title": "Alimentação saudável",
  "category": "NUTRIÇÃO",
  "config": {
    "zoom": {
      "enabled": false
    }
  }
}
```

### 6. Configuração Completa

```json
{
  "imageUrl": "https://example.com/image.jpg",
  "title": "Treino completo para ganhar massa",
  "category": "TREINO",
  "config": {
    "colors": {
      "TREINO": "#FF0000",
      "SUPLEMENTOS": "#00FF00"
    },
    "logoText": {
      "part1": "Nutr",
      "part2": "IA"
    },
    "logoColorNutr": [255, 255, 255],
    "logoColorIA": [255, 107, 0],
    "fontSizes": {
      "logo": 52,
      "category": 26,
      "title": 38
    },
    "zoom": {
      "enabled": true,
      "factor": 1.2,
      "focus": "center"
    }
  }
}
```

## Categorias Disponíveis

- `SUPLEMENTOS`
- `TREINO`
- `NUTRIÇÃO`
- `FOFOCA MAROMBA` (sem underscore!)
- `FITNESS`

**Nota:** O underscore é automaticamente removido, então `FOFOCA_MAROMBA` será exibido como `FOFOCA MAROMBA`.

## Formatos de Imagem Aceitos

1. **URL**: `https://example.com/image.jpg`
2. **Base64 com prefixo**: `data:image/png;base64,iVBORw0KG...`
3. **Base64 puro**: `iVBORw0KG...` (PNG) ou `/9j/...` (JPEG)

## Zoom Inteligente

O zoom inteligente aplica um zoom na imagem antes de fazer o crop para 1080x1080, mantendo o foco na área especificada. Isso é útil para:

- Dar mais destaque ao conteúdo principal
- Criar composições mais dinâmicas
- Evitar bordas vazias em imagens menores

**Fator de zoom recomendado:** 1.1 a 1.3 (10% a 30% de zoom)
