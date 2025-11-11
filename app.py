from flask import Flask, request, jsonify
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO
import base64
import os
import sys

app = Flask(__name__)

# Configurações
PORT = 3000
FONT_SIZE_LOGO = 52
FONT_SIZE_CATEGORY = 26
FONT_SIZE_TITLE = 38

# Caminhos de fontes por sistema operacional
FONT_PATHS = {
    'windows': [
        'C:/Windows/Fonts/arial.ttf',
        'C:/Windows/Fonts/arialbd.ttf',
    ],
    'linux': [
        '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
        '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',
    ],
    'darwin': [  # macOS
        '/System/Library/Fonts/Helvetica.ttc',
        '/System/Library/Fonts/Helvetica.ttc',
    ]
}

# Cores por categoria
CATEGORY_COLORS = {
    'SUPLEMENTOS': '#00FF00',      # Verde
    'TREINO': '#FF6B00',            # Laranja
    'NUTRIÇÃO': '#00D4FF',          # Azul
    'FOFOCA MAROMBA': '#FF00FF',    # Magenta (sem underscore)
    'FITNESS': '#FFD700'            # Dourado
}

# Cores do logo NutrIA
LOGO_COLOR_NUTR = (255, 255, 255)  # Branco para "Nutr"
LOGO_COLOR_IA = (255, 107, 0)      # Laranja para "IA"

def hex_to_rgb(hex_color):
    """Converte cor hexadecimal para RGB"""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def load_font(size, bold=False):
    """
    Carrega fonte TrueType com fallback inteligente
    Tenta múltiplos caminhos dependendo do sistema operacional
    """
    # Detectar sistema operacional
    platform = sys.platform
    
    # Lista de fontes para tentar
    font_attempts = []
    
    if platform.startswith('win'):
        # Windows
        if bold:
            font_attempts = [
                'C:/Windows/Fonts/arialbd.ttf',
                'C:/Windows/Fonts/arial.ttf',
                'arial.ttf',
            ]
        else:
            font_attempts = [
                'C:/Windows/Fonts/arial.ttf',
                'arial.ttf',
            ]
    elif platform.startswith('linux'):
        # Linux (incluindo Docker)
        if bold:
            font_attempts = [
                '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',
                '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf',
                '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
            ]
        else:
            font_attempts = [
                '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
                '/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf',
            ]
    elif platform.startswith('darwin'):
        # macOS
        font_attempts = [
            '/System/Library/Fonts/Helvetica.ttc',
            '/Library/Fonts/Arial.ttf',
        ]
    
    # Tentar carregar cada fonte
    for font_path in font_attempts:
        try:
            return ImageFont.truetype(font_path, size)
        except:
            continue
    
    # Se nenhuma fonte funcionar, criar fonte sintética grande
    # (melhor que a fonte padrão de 11px)
    print(f"⚠️ Aviso: Nenhuma fonte TrueType encontrada, usando fallback")
    try:
        # Tentar criar uma fonte maior mesmo sem TrueType
        return ImageFont.truetype("DejaVuSans.ttf", size)
    except:
        # Último recurso: fonte padrão (vai ficar pequena)
        return ImageFont.load_default()

def download_image(url_or_base64):
    """Baixa imagem de uma URL ou decodifica base64"""
    # Verificar se é base64
    if url_or_base64.startswith('data:image'):
        # Formato: data:image/png;base64,iVBORw0KG...
        base64_data = url_or_base64.split(',')[1]
        image_data = base64.b64decode(base64_data)
        return Image.open(BytesIO(image_data))
    elif url_or_base64.startswith('iVBORw0KG') or url_or_base64.startswith('/9j/'):
        # Base64 puro (PNG ou JPEG)
        image_data = base64.b64decode(url_or_base64)
        return Image.open(BytesIO(image_data))
    else:
        # URL normal
        response = requests.get(url_or_base64, timeout=30)
        response.raise_for_status()
        return Image.open(BytesIO(response.content))

def add_overlay(image_url_or_base64, title, category):
    """
    Adiciona overlay de texto na imagem
    
    TAMANHO FINAL: 1080x1080 pixels (Instagram square format)
    - Largura: 1080px
    - Altura: 1080px
    - Formato: PNG
    - Qualidade: Alta (sem compressão)
    
    Aceita:
    - URL: https://example.com/image.jpg
    - Base64 com prefixo: data:image/png;base64,iVBORw0KG...
    - Base64 puro: iVBORw0KG... (PNG) ou /9j/... (JPEG)
    """
    
    # Baixar ou decodificar imagem
    img = download_image(image_url_or_base64)
    
    # Redimensionar para 1080x1080 (Instagram square)
    # IMPORTANTE: Este é o tamanho exato que deve ser usado no DALL-E 3
    img = img.resize((1080, 1080), Image.Resampling.LANCZOS)
    
    # Converter para RGBA se necessário
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    
    # Criar camada de overlay
    overlay = Image.new('RGBA', img.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    # Adicionar gradiente escuro no bottom (maior, começa mais cedo)
    # Gradiente de 700px até 1080px (380px de altura)
    for y in range(700, 1080):
        alpha = int(((y - 700) / 380) * 240)  # 0 a 240 (mais escuro)
        draw.rectangle([(0, y), (1080, y+1)], fill=(0, 0, 0, alpha))
    
    # Carregar fontes com fallback inteligente
    font_logo = load_font(FONT_SIZE_LOGO, bold=False)
    font_category = load_font(FONT_SIZE_CATEGORY, bold=True)
    font_title = load_font(FONT_SIZE_TITLE, bold=True)
    
    # Logo "NutrIA" (canto superior esquerdo)
    # Desenhar "Nutr" em branco
    draw.text((40, 80), "Nutr", fill=LOGO_COLOR_NUTR + (255,), font=font_logo)
    
    # Calcular posição do "IA" (após "Nutr")
    bbox_nutr = draw.textbbox((40, 80), "Nutr", font=font_logo)
    x_ia = bbox_nutr[2]  # Posição X após "Nutr"
    
    # Desenhar "IA" em laranja
    draw.text((x_ia, 80), "IA", fill=LOGO_COLOR_IA + (255,), font=font_logo)
    
    # Categoria (canto inferior esquerdo, mais para cima)
    category_color = hex_to_rgb(CATEGORY_COLORS.get(category.upper(), '#00FF00'))
    draw.text((40, 880), category.upper(), fill=category_color + (255,), font=font_category)
    
    # Título (canto inferior esquerdo, quebrado em múltiplas linhas)
    # Limitar a 7-15 palavras (padrão notjournal.ai)
    words = title.split()
    
    # Se tiver mais de 15 palavras, truncar
    if len(words) > 15:
        words = words[:15]
        title = ' '.join(words) + '...'
    else:
        title = ' '.join(words)
    
    # Quebrar em linhas (máximo 2 linhas)
    max_width = 1000
    words = title.split()
    lines = []
    current_line = ""
    
    for word in words:
        test_line = current_line + word + " "
        bbox = draw.textbbox((0, 0), test_line, font=font_title)
        width = bbox[2] - bbox[0]
        
        if width > max_width and current_line:
            lines.append(current_line.strip())
            current_line = word + " "
            
            # Máximo 2 linhas
            if len(lines) >= 2:
                break
        else:
            current_line = test_line
    
    if current_line.strip() and len(lines) < 2:
        lines.append(current_line.strip())
    
    # Desenhar linhas do título (mais para cima)
    y_position = 930  # Começar mais cedo
    for line in lines[:2]:  # Máximo 2 linhas
        draw.text((40, y_position), line, fill=(255, 255, 255, 255), font=font_title)
        y_position += 50  # Espaçamento entre linhas
    
    # Combinar imagem original com overlay
    img = Image.alpha_composite(img, overlay)
    
    # Converter para RGB (remover alpha)
    img = img.convert('RGB')
    
    return img

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'ok',
        'service': 'nutria-instagram-overlay-python'
    })

@app.route('/add-overlay', methods=['POST'])
def add_overlay_endpoint():
    """
    Endpoint para adicionar overlay
    
    Aceita imageUrl como:
    - URL: https://example.com/image.jpg
    - Base64 com prefixo: data:image/png;base64,iVBORw0KG...
    - Base64 puro: iVBORw0KG... (PNG) ou /9j/... (JPEG)
    """
    try:
        data = request.get_json()
        
        # Validar campos obrigatórios
        if not data or 'imageUrl' not in data or 'title' not in data or 'category' not in data:
            return jsonify({
                'error': 'Missing required fields',
                'required': ['imageUrl', 'title', 'category'],
                'note': 'imageUrl can be a URL or base64 string'
            }), 400
        
        image_url = data['imageUrl']
        title = data['title']
        category = data['category']
        
        # Adicionar overlay
        result_image = add_overlay(image_url, title, category)
        
        # Converter para base64
        buffer = BytesIO()
        result_image.save(buffer, format='PNG')
        image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
        
        return jsonify({
            'success': True,
            'image': image_base64,
            'contentType': 'image/png',
            'size': len(buffer.getvalue())
        })
        
    except Exception as e:
        return jsonify({
            'error': 'Failed to add overlay',
            'message': str(e)
        }), 500

if __name__ == '__main__':
    print(f'🚀 Overlay Microservice (Python) running on port {PORT}')
    print(f'📍 Health check: http://localhost:{PORT}/health')
    print(f'📍 Add overlay: POST http://localhost:{PORT}/add-overlay')
    app.run(host='0.0.0.0', port=PORT, debug=False)
