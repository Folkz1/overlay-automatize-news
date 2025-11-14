"""
Teste com imagem local file (1).png
"""

import requests
import json
import base64
from pathlib import Path
from PIL import Image

def image_to_base64(image_path):
    """Converte imagem local para base64"""
    with open(image_path, 'rb') as f:
        return base64.b64encode(f.read()).decode('utf-8')

def test_local_image():
    """Testa com a imagem local file (1).png"""
    
    BASE_URL = "http://localhost:3000"
    
    print("=" * 60)
    print("🧪 TESTE COM IMAGEM LOCAL: file (1).png")
    print("=" * 60)
    
    # Verificar se serviço está rodando
    try:
        response = requests.get(f"{BASE_URL}/health", timeout=5)
        if response.status_code != 200:
            print("❌ Serviço não está respondendo!")
            print("   Execute: python app.py")
            return
        print("✅ Serviço está rodando!\n")
    except requests.exceptions.ConnectionError:
        print("❌ Erro: Não foi possível conectar ao serviço!")
        print("   Execute: python app.py")
        return
    
    # Verificar se imagem existe
    image_path = "file (1).png"
    if not Path(image_path).exists():
        print(f"❌ Imagem não encontrada: {image_path}")
        return
    
    print(f"✅ Imagem encontrada: {image_path}\n")
    
    # Converter imagem para base64
    print("📦 Convertendo imagem para base64...")
    image_base64 = image_to_base64(image_path)
    print(f"✅ Imagem convertida ({len(image_base64)} bytes)\n")
    
    # Teste 1: Com zoom padrão (1.2x)
    print("🔍 Teste 1: Zoom padrão (1.2x, center)")
    response = requests.post(f"{BASE_URL}/add-overlay", json={
        "imageUrl": f"data:image/png;base64,{image_base64}",
        "title": "Como ganhar massa muscular rapidamente",
        "category": "TREINO"
    })
    
    if response.status_code == 200:
        data = response.json()
        output_file = "resultado_zoom_default.png"
        with open(output_file, "wb") as f:
            f.write(base64.b64decode(data['image']))
        print(f"✅ Salvo: {output_file}\n")
    else:
        print(f"❌ Erro: {response.status_code} - {response.text}\n")
    
    # Teste 2: Com zoom maior (1.3x)
    print("🔍 Teste 2: Zoom aumentado (1.3x, center)")
    response = requests.post(f"{BASE_URL}/add-overlay", json={
        "imageUrl": f"data:image/png;base64,{image_base64}",
        "title": "Melhores suplementos para hipertrofia",
        "category": "SUPLEMENTOS",
        "config": {
            "zoom": {
                "enabled": True,
                "factor": 1.3,
                "focus": "center"
            }
        }
    })
    
    if response.status_code == 200:
        data = response.json()
        output_file = "resultado_zoom_1.3x.png"
        with open(output_file, "wb") as f:
            f.write(base64.b64decode(data['image']))
        print(f"✅ Salvo: {output_file}\n")
    else:
        print(f"❌ Erro: {response.status_code} - {response.text}\n")
    
    # Teste 3: Sem zoom
    print("🔍 Teste 3: Sem zoom")
    response = requests.post(f"{BASE_URL}/add-overlay", json={
        "imageUrl": f"data:image/png;base64,{image_base64}",
        "title": "Dieta para emagrecer com saúde",
        "category": "NUTRIÇÃO",
        "config": {
            "zoom": {
                "enabled": False
            }
        }
    })
    
    if response.status_code == 200:
        data = response.json()
        output_file = "resultado_sem_zoom.png"
        with open(output_file, "wb") as f:
            f.write(base64.b64decode(data['image']))
        print(f"✅ Salvo: {output_file}\n")
    else:
        print(f"❌ Erro: {response.status_code} - {response.text}\n")
    
    # Teste 4: FOFOCA MAROMBA (testando correção do underscore)
    print("💬 Teste 4: FOFOCA MAROMBA (sem underscore)")
    response = requests.post(f"{BASE_URL}/add-overlay", json={
        "imageUrl": f"data:image/png;base64,{image_base64}",
        "title": "Fulano foi flagrado usando bomba na academia",
        "category": "FOFOCA_MAROMBA"
    })
    
    if response.status_code == 200:
        data = response.json()
        output_file = "resultado_fofoca_maromba.png"
        with open(output_file, "wb") as f:
            f.write(base64.b64decode(data['image']))
        print(f"✅ Salvo: {output_file}\n")
    else:
        print(f"❌ Erro: {response.status_code} - {response.text}\n")
    
    # Teste 5: Zoom com foco no topo
    print("🔍 Teste 5: Zoom com foco no topo (1.2x, top)")
    response = requests.post(f"{BASE_URL}/add-overlay", json={
        "imageUrl": f"data:image/png;base64,{image_base64}",
        "title": "Exercícios para definir abdômen",
        "category": "FITNESS",
        "config": {
            "zoom": {
                "enabled": True,
                "factor": 1.2,
                "focus": "top"
            }
        }
    })
    
    if response.status_code == 200:
        data = response.json()
        output_file = "resultado_zoom_top.png"
        with open(output_file, "wb") as f:
            f.write(base64.b64decode(data['image']))
        print(f"✅ Salvo: {output_file}\n")
    else:
        print(f"❌ Erro: {response.status_code} - {response.text}\n")
    
    print("=" * 60)
    print("✅ TODOS OS TESTES CONCLUÍDOS!")
    print("=" * 60)
    print("\n📁 Arquivos gerados:")
    print("   - resultado_zoom_default.png (zoom 1.2x padrão)")
    print("   - resultado_zoom_1.3x.png (zoom 1.3x)")
    print("   - resultado_sem_zoom.png (sem zoom)")
    print("   - resultado_fofoca_maromba.png (categoria corrigida)")
    print("   - resultado_zoom_top.png (zoom com foco no topo)")
    print("\n💡 Compare os resultados para ver a diferença do zoom!")

if __name__ == "__main__":
    test_local_image()
