from flask import Flask, request, jsonify
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO
import base64
import os
import sys
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

app = Flask(__name__)

# Configurações do .env com fallback
PORT = int(os.getenv('PORT', 3000))
FONT_SIZE_LOGO = int(os.getenv('FONT_SIZE_LOGO', 52))
FONT_SIZE_CATEGORY = int(os.getenv('FONT_SIZE_CATEGORY', 26))
FONT_SIZE_TITLE = int(os.getenv('FONT_SIZE_TITLE', 38))

# Textos do logo
TEXT_LOGO_PART1 = os.getenv('TEXT_LOGO_PART1', 'Nutr')
TEXT_LOGO_PART2 = os.getenv('TEXT_LOGO_PART2', 'IA')

# Configurações de zoom
ZOOM_ENABLED = os.getenv('ZOOM_ENABLED', 'true').lower() == 'true'
ZOOM_FACTOR = float(os.getenv('ZOOM_FACTOR', 1.2))
ZOOM_FOCUS = os.getenv('ZOOM_FOCUS', 'center')

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

# Cores por categoria (do .env com fallback)
CATEGORY_COLORS = {
    'SUPLEMENTOS': os.getenv('COLOR_SUPLEMENTOS', '#00FF00'),
    'TREINO': os.getenv('COLOR_TREINO', '#FF6B00'),
    'NUTRIÇÃO': os.getenv('COLOR_NUTRICAO', '#00D4FF'),
    'FOFOCA MAROMBA': os.getenv('COLOR_FOFOCA_MAROMBA', '#FF00FF'),
    'FITNESS': os.getenv('COLOR_FITNESS', '#FFD700')
}

# Cores do logo NutrIA (do .env com fallback)
def parse_rgb(env_var, default):
    """Parse RGB do formato '255,255,255' para tupla"""
    try:
        return tuple(map(int, os.getenv(env_var, default).split(',')))
    except:
        return tuple(map(int, default.split(',')))

LOGO_COLOR_NUTR = parse_rgb('LOGO_COLOR_NUTR', '255,255,255')
LOGO_COLOR_IA = parse_rgb('LOGO_COLOR_IA', '255,107,0')

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

def apply_smart_zoom(img, target_size=(1080, 1080), zoom_factor=1.2, focus='center'):
    """
    Aplica zoom inteligente na imagem mantendo o foco
    
    Args:
        img: Imagem PIL
        target_size: Tamanho final desejado (width, height)
        zoom_factor: Fator de zoom (1.2 = 20% maior)
        focus: Ponto de foco ('center', 'top', 'bottom')
    
    Returns:
        Imagem redimensionada com zoom aplicado
    """
    target_width, target_height = target_size
    
    # Calcular novo tamanho com zoom
    zoomed_width = int(target_width * zoom_factor)
    zoomed_height = int(target_height * zoom_factor)
    
    # Redimensionar imagem para o tamanho com zoom
    img_zoomed = img.resize((zoomed_width, zoomed_height), Image.Resampling.LANCZOS)
    
    # Calcular posição de crop baseado no foco
    if focus == 'top':
        # Foco no topo
        left = (zoomed_width - target_width) // 2
        top = 0
    elif focus == 'bottom':
        # Foco na parte inferior
        left = (zoomed_width - target_width) // 2
        top = zoomed_height - target_height
    else:  # center (padrão)
        # Foco no centro
        left = (zoomed_width - target_width) // 2
        top = (zoomed_height - target_height) // 2
    
    right = left + target_width
    bottom = top + target_height
    
    # Fazer crop para o tamanho final
    img_cropped = img_zoomed.crop((left, top, right, bottom))
    
    return img_cropped

def add_overlay(image_url_or_base64, title, category, config=None):
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
    
    Args:
        config: Dicionário opcional com configurações customizadas:
            - colors: dict com cores customizadas por categoria
            - logoText: dict com 'part1' e 'part2' para customizar logo
            - fontSizes: dict com 'logo', 'category', 'title'
            - zoom: dict com 'enabled', 'factor', 'focus'
    """
    
    # Configurações padrão (do .env)
    cfg = {
        'colors': CATEGORY_COLORS.copy(),
        'logoColorNutr': LOGO_COLOR_NUTR,
        'logoColorIA': LOGO_COLOR_IA,
        'logoText': {'part1': TEXT_LOGO_PART1, 'part2': TEXT_LOGO_PART2},
        'fontSizes': {
            'logo': FONT_SIZE_LOGO,
            'category': FONT_SIZE_CATEGORY,
            'title': FONT_SIZE_TITLE
        },
        'zoom': {
            'enabled': ZOOM_ENABLED,
            'factor': ZOOM_FACTOR,
            'focus': ZOOM_FOCUS
        }
    }
    
    # Sobrescrever com configurações customizadas se fornecidas
    if config:
        if 'colors' in config:
            cfg['colors'].update(config['colors'])
        if 'logoColorNutr' in config:
            cfg['logoColorNutr'] = tuple(config['logoColorNutr'])
        if 'logoColorIA' in config:
            cfg['logoColorIA'] = tuple(config['logoColorIA'])
        if 'logoText' in config:
            cfg['logoText'].update(config['logoText'])
        if 'fontSizes' in config:
            cfg['fontSizes'].update(config['fontSizes'])
        if 'zoom' in config:
            cfg['zoom'].update(config['zoom'])
    
    # Baixar ou decodificar imagem
    img = download_image(image_url_or_base64)
    
    # Aplicar zoom inteligente se habilitado
    if cfg['zoom']['enabled']:
        img = apply_smart_zoom(
            img, 
            target_size=(1080, 1080),
            zoom_factor=cfg['zoom']['factor'],
            focus=cfg['zoom']['focus']
        )
    else:
        # Redimensionar normalmente para 1080x1080 (Instagram square)
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
    # Logo usa fonte BOLD agora para "NUTRIA" mais grosso
    font_logo = load_font(cfg['fontSizes']['logo'], bold=True)
    font_category = load_font(cfg['fontSizes']['category'], bold=True)
    font_title = load_font(cfg['fontSizes']['title'], bold=True)
    
    # Logo "NutrIA" (canto superior esquerdo)
    logo_part1 = cfg['logoText']['part1']
    logo_part2 = cfg['logoText']['part2']
    
    # Desenhar primeira parte do logo (ex: "Nutr")
    draw.text((40, 80), logo_part1, fill=cfg['logoColorNutr'] + (255,), font=font_logo)
    
    # Calcular posição da segunda parte (após primeira parte)
    bbox_part1 = draw.textbbox((40, 80), logo_part1, font=font_logo)
    x_part2 = bbox_part1[2]  # Posição X após primeira parte
    
    # Desenhar segunda parte do logo (ex: "IA")
    draw.text((x_part2, 80), logo_part2, fill=cfg['logoColorIA'] + (255,), font=font_logo)
    
    # Categoria (canto inferior esquerdo, mais para cima)
    # Normalizar categoria removendo underscores
    category_normalized = category.upper().replace('_', ' ')
    category_color = hex_to_rgb(cfg['colors'].get(category_normalized, '#00FF00'))
    draw.text((40, 880), category_normalized, fill=category_color + (255,), font=font_category)
    
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
    
    Configurações opcionais via JSON:
    {
        "imageUrl": "...",
        "title": "...",
        "category": "...",
        "config": {
            "colors": {
                "SUPLEMENTOS": "#00FF00"
            },
            "logoText": {
                "part1": "Nutr",
                "part2": "IA"
            },
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
    """
    try:
        data = request.get_json()
        
        # Validar campos obrigatórios
        if not data or 'imageUrl' not in data or 'title' not in data or 'category' not in data:
            return jsonify({
                'error': 'Missing required fields',
                'required': ['imageUrl', 'title', 'category'],
                'optional': ['config'],
                'note': 'imageUrl can be a URL or base64 string. config is optional for customization.'
            }), 400
        
        image_url = data['imageUrl']
        title = data['title']
        category = data['category']
        config = data.get('config', None)  # Configurações opcionais
        
        # Adicionar overlay com configurações customizadas
        result_image = add_overlay(image_url, title, category, config)
        
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
