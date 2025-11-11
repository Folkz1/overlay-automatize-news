#!/usr/bin/env python3
"""
Teste do microserviço com imagem base64
"""

import requests
import base64
from PIL import Image
from io import BytesIO

# URL do serviço
SERVICE_URL = "http://localhost:3000"

def image_to_base64(image_path):
    """Converte imagem para base64"""
    with open(image_path, 'rb') as f:
        return base64.b64encode(f.read()).decode('utf-8')

def test_with_base64():
    """Testa com imagem base64"""
    print("🧪 Testando com imagem base64...")
    
    # Baixar uma imagem de teste
    print("📥 Baixando imagem de teste...")
    img_url = "https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=1024"
    response = requests.get(img_url)
    
    # Converter para base64
    img_base64 = base64.b64encode(response.content).decode('utf-8')
    print(f"✅ Imagem convertida para base64 ({len(img_base64)} caracteres)")
    
    # Testar com base64 puro
    print("\n1️⃣ Testando com base64 puro...")
    payload = {
        "imageUrl": img_base64,
        "title": "TESTE COM BASE64 PURO",
        "category": "SUPLEMENTOS"
    }
    
    response = requests.post(f"{SERVICE_URL}/add-overlay", json=payload)
    
    if response.status_code == 200:
        result = response.json()
        print(f"✅ Sucesso! Tamanho da resposta: {result['size']} bytes")
        
        # Salvar imagem
        img_data = base64.b64decode(result['image'])
        img = Image.open(BytesIO(img_data))
        img.save('test_base64_puro.png')
        print("💾 Imagem salva: test_base64_puro.png")
    else:
        print(f"❌ Erro: {response.status_code}")
        print(response.text)
    
    # Testar com base64 com prefixo data:image
    print("\n2️⃣ Testando com base64 com prefixo data:image...")
    payload = {
        "imageUrl": f"data:image/jpeg;base64,{img_base64}",
        "title": "TESTE COM DATA URI",
        "category": "TREINO"
    }
    
    response = requests.post(f"{SERVICE_URL}/add-overlay", json=payload)
    
    if response.status_code == 200:
        result = response.json()
        print(f"✅ Sucesso! Tamanho da resposta: {result['size']} bytes")
        
        # Salvar imagem
        img_data = base64.b64decode(result['image'])
        img = Image.open(BytesIO(img_data))
        img.save('test_base64_datauri.png')
        print("💾 Imagem salva: test_base64_datauri.png")
    else:
        print(f"❌ Erro: {response.status_code}")
        print(response.text)

def test_with_url():
    """Testa com URL (para garantir que ainda funciona)"""
    print("\n3️⃣ Testando com URL (garantir compatibilidade)...")
    
    payload = {
        "imageUrl": "https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=1024",
        "title": "TESTE COM URL NORMAL",
        "category": "NUTRIÇÃO"
    }
    
    response = requests.post(f"{SERVICE_URL}/add-overlay", json=payload)
    
    if response.status_code == 200:
        result = response.json()
        print(f"✅ Sucesso! Tamanho da resposta: {result['size']} bytes")
        
        # Salvar imagem
        img_data = base64.b64decode(result['image'])
        img = Image.open(BytesIO(img_data))
        img.save('test_url_normal.png')
        print("💾 Imagem salva: test_url_normal.png")
    else:
        print(f"❌ Erro: {response.status_code}")
        print(response.text)

if __name__ == '__main__':
    print("🚀 Teste de Base64 - Microserviço Overlay")
    print("=" * 50)
    
    # Verificar se serviço está rodando
    try:
        response = requests.get(f"{SERVICE_URL}/health")
        if response.status_code == 200:
            print("✅ Serviço está rodando!\n")
        else:
            print("❌ Serviço não está respondendo corretamente")
            exit(1)
    except:
        print("❌ Serviço não está rodando!")
        print("Execute: python app.py")
        exit(1)
    
    # Executar testes
    test_with_base64()
    test_with_url()
    
    print("\n" + "=" * 50)
    print("✅ Todos os testes concluídos!")
    print("\nImagens geradas:")
    print("- test_base64_puro.png")
    print("- test_base64_datauri.png")
    print("- test_url_normal.png")
