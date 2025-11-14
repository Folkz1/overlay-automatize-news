"""
Teste das novas funcionalidades v1.3
- Zoom inteligente
- Logo em negrito
- Configurações via JSON
- Correção FOFOCA MAROMBA
"""

import requests
import json
import base64
from pathlib import Path

BASE_URL = "http://localhost:3000"

def test_zoom_inteligente():
    """Testa zoom inteligente com diferentes configurações"""
    print("\n🔍 Testando Zoom Inteligente...")
    
    # Teste 1: Zoom habilitado (padrão)
    response = requests.post(f"{BASE_URL}/add-overlay", json={
        "imageUrl": "https://picsum.photos/800/800",
        "title": "Teste com zoom padrão habilitado",
        "category": "TREINO"
    })
    
    if response.status_code == 200:
        data = response.json()
        with open("test_zoom_default.png", "wb") as f:
            f.write(base64.b64decode(data['image']))
        print("✅ Zoom padrão: test_zoom_default.png")
    
    # Teste 2: Zoom com fator maior
    response = requests.post(f"{BASE_URL}/add-overlay", json={
        "imageUrl": "https://picsum.photos/800/800",
        "title": "Teste com zoom aumentado",
        "category": "SUPLEMENTOS",
        "config": {
            "zoom": {
                "enabled": True,
                "factor": 1.5,
                "focus": "center"
            }
        }
    })
    
    if response.status_code == 200:
        data = response.json()
        with open("test_zoom_1.5x.png", "wb") as f:
            f.write(base64.b64decode(data['image']))
        print("✅ Zoom 1.5x: test_zoom_1.5x.png")
    
    # Teste 3: Zoom desabilitado
    response = requests.post(f"{BASE_URL}/add-overlay", json={
        "imageUrl": "https://picsum.photos/800/800",
        "title": "Teste sem zoom",
        "category": "NUTRIÇÃO",
        "config": {
            "zoom": {
                "enabled": False
            }
        }
    })
    
    if response.status_code == 200:
        data = response.json()
        with open("test_sem_zoom.png", "wb") as f:
            f.write(base64.b64decode(data['image']))
        print("✅ Sem zoom: test_sem_zoom.png")

def test_fofoca_maromba():
    """Testa correção do underscore em FOFOCA MAROMBA"""
    print("\n💬 Testando FOFOCA MAROMBA...")
    
    # Teste com underscore (deve ser removido)
    response = requests.post(f"{BASE_URL}/add-overlay", json={
        "imageUrl": "https://picsum.photos/800/800",
        "title": "Fulano foi flagrado usando bomba na academia",
        "category": "FOFOCA_MAROMBA"
    })
    
    if response.status_code == 200:
        data = response.json()
        with open("test_fofoca_maromba.png", "wb") as f:
            f.write(base64.b64decode(data['image']))
        print("✅ FOFOCA MAROMBA (sem underscore): test_fofoca_maromba.png")

def test_config_customizada():
    """Testa configurações customizadas via JSON"""
    print("\n⚙️ Testando Configurações Customizadas...")
    
    response = requests.post(f"{BASE_URL}/add-overlay", json={
        "imageUrl": "https://picsum.photos/800/800",
        "title": "Teste com configurações customizadas",
        "category": "FITNESS",
        "config": {
            "colors": {
                "FITNESS": "#FF0000"  # Vermelho ao invés de dourado
            },
            "logoText": {
                "part1": "Fit",
                "part2": "AI"
            },
            "fontSizes": {
                "logo": 60,
                "category": 30,
                "title": 42
            },
            "zoom": {
                "enabled": True,
                "factor": 1.3,
                "focus": "top"
            }
        }
    })
    
    if response.status_code == 200:
        data = response.json()
        with open("test_config_custom.png", "wb") as f:
            f.write(base64.b64decode(data['image']))
        print("✅ Config customizada: test_config_custom.png")
        print("   - Logo: FitAI")
        print("   - Cor FITNESS: Vermelho")
        print("   - Fontes maiores")
        print("   - Zoom 1.3x com foco no topo")

def test_logo_negrito():
    """Testa logo em negrito"""
    print("\n🔤 Testando Logo em Negrito...")
    
    response = requests.post(f"{BASE_URL}/add-overlay", json={
        "imageUrl": "https://picsum.photos/800/800",
        "title": "Logo NutrIA agora está em negrito",
        "category": "SUPLEMENTOS"
    })
    
    if response.status_code == 200:
        data = response.json()
        with open("test_logo_negrito.png", "wb") as f:
            f.write(base64.b64decode(data['image']))
        print("✅ Logo em negrito: test_logo_negrito.png")

def run_all_tests():
    """Executa todos os testes"""
    print("=" * 60)
    print("🧪 TESTES v1.3 - Novas Funcionalidades")
    print("=" * 60)
    
    try:
        # Verificar se serviço está rodando
        response = requests.get(f"{BASE_URL}/health", timeout=5)
        if response.status_code != 200:
            print("❌ Serviço não está respondendo!")
            return
        
        print("✅ Serviço está rodando!")
        
        # Executar testes
        test_zoom_inteligente()
        test_fofoca_maromba()
        test_logo_negrito()
        test_config_customizada()
        
        print("\n" + "=" * 60)
        print("✅ TODOS OS TESTES CONCLUÍDOS!")
        print("=" * 60)
        print("\n📁 Arquivos gerados:")
        print("   - test_zoom_default.png")
        print("   - test_zoom_1.5x.png")
        print("   - test_sem_zoom.png")
        print("   - test_fofoca_maromba.png")
        print("   - test_logo_negrito.png")
        print("   - test_config_custom.png")
        
    except requests.exceptions.ConnectionError:
        print("❌ Erro: Não foi possível conectar ao serviço!")
        print("   Certifique-se de que o serviço está rodando:")
        print("   python app.py")
    except Exception as e:
        print(f"❌ Erro: {e}")

if __name__ == "__main__":
    run_all_tests()
