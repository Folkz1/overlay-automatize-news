# Changelog - Microserviço Overlay Python

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
