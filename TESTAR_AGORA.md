# 🚀 Testar Microserviço AGORA

## Passo 1: Instalar Dependências

```bash
cd workflows/agentes/instagram/microservico_overlay_python
pip install -r requirements.txt
```

## Passo 2: Iniciar Serviço (Terminal 1)

```bash
python app.py
```

Deve aparecer:
```
🚀 Overlay Microservice (Python) running on port 3000
📍 Health check: http://localhost:3000/health
📍 Add overlay: POST http://localhost:3000/add-overlay
```

## Passo 3: Executar Testes (Terminal 2)

```bash
python test.py
```

## 📊 O Que Vai Ser Gerado

### 9 Imagens PNG:

1. **test_output.png** - Teste básico
2. **test_suplementos.png** - Categoria SUPLEMENTOS (verde)
3. **test_treino.png** - Categoria TREINO (laranja)
4. **test_nutricao.png** - Categoria NUTRIÇÃO (azul)
5. **test_fofoca maromba.png** - Categoria FOFOCA MAROMBA (magenta)
6. **test_titulo_curto.png** - 5 palavras
7. **test_titulo_ideal.png** - 8 palavras (ideal)
8. **test_titulo_maximo.png** - 14 palavras
9. **test_titulo_truncado.png** - 19 palavras → truncado para 15

## ✅ O Que Validar

Abra as imagens e verifique:

### Logo NutrIA
- [ ] "Nutr" está em branco?
- [ ] "IA" está em laranja?
- [ ] Posição: canto superior esquerdo?

### Gradiente
- [ ] Começa em ~700px (mais alto)?
- [ ] Escurece gradualmente até o bottom?
- [ ] Texto está legível?

### Categoria
- [ ] Cor correta por categoria?
- [ ] Posição: Y: 880px (mais alta)?
- [ ] Sem underscore em "FOFOCA MAROMBA"?

### Título
- [ ] Posição: Y: 930px (mais alto)?
- [ ] Máximo 2 linhas?
- [ ] Truncamento funciona (15 palavras)?
- [ ] Legível sobre o gradiente?

### Tamanho
- [ ] Imagem é 1080x1080px?

## 🎯 Resultado Esperado

Deve ficar similar ao estilo **notjournal.ai**:
- Logo no topo
- Gradiente grande no bottom
- Categoria e título bem posicionados
- Texto legível

## 🔧 Se Algo Der Errado

### Erro: "No module named 'PIL'"
```bash
pip install Pillow
```

### Erro: "Address already in use"
Outro processo está na porta 3000. Mate o processo ou mude a porta em `app.py`.

### Erro: "Failed to download image"
Verifique sua conexão com internet.

---

**Tempo total:** ~2 minutos  
**Resultado:** 9 imagens PNG para validar! 🎨
