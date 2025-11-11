import requests
import base64
import os

OVERLAY_SERVICE_URL = 'http://localhost:3000'

def test_health_check():
    """Teste 1: Health Check"""
    print('\n🔍 Teste 1: Health Check')
    print('=' * 50)
    
    try:
        response = requests.get(f'{OVERLAY_SERVICE_URL}/health')
        print(f'✅ Status: {response.status_code}')
        print(f'✅ Response: {response.json()}')
        return True
    except Exception as e:
        print(f'❌ Erro: {e}')
        return False

def test_add_overlay():
    """Teste 2: Adicionar Overlay"""
    print('\n🎨 Teste 2: Adicionar Overlay')
    print('=' * 50)
    
    test_data = {
        'imageUrl': 'https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=1024&h=1024&fit=crop',
        'title': 'VOCÊ ESTÁ DESPERDIÇANDO SUA CREATINA?',
        'category': 'SUPLEMENTOS'
    }
    
    print('📤 Enviando requisição...')
    print(f'Image URL: {test_data["imageUrl"]}')
    print(f'Title: {test_data["title"]}')
    print(f'Category: {test_data["category"]}')
    
    try:
        response = requests.post(
            f'{OVERLAY_SERVICE_URL}/add-overlay',
            json=test_data,
            timeout=60
        )
        
        if response.status_code == 200:
            data = response.json()
            print(f'\n✅ Overlay adicionado com sucesso!')
            print(f'📊 Tamanho da imagem: {data["size"]} bytes')
            
            # Salvar imagem
            image_data = base64.b64decode(data['image'])
            output_path = 'test_output.png'
            with open(output_path, 'wb') as f:
                f.write(image_data)
            
            print(f'💾 Imagem salva em: {output_path}')
            print(f'\n🎉 Teste concluído! Abra o arquivo {output_path} para ver o resultado.')
            return True
        else:
            print(f'❌ Erro: {response.status_code}')
            print(f'Response: {response.text}')
            return False
            
    except Exception as e:
        print(f'❌ Erro: {e}')
        return False

def test_different_categories():
    """Teste 3: Diferentes Categorias"""
    print('\n🎨 Teste 3: Diferentes Categorias')
    print('=' * 50)
    
    categories = [
        {'name': 'SUPLEMENTOS', 'title': 'CREATINA AUMENTA FORÇA EM 15%'},
        {'name': 'TREINO', 'title': 'OS 5 MELHORES EXERCÍCIOS PARA HIPERTROFIA'},
        {'name': 'NUTRIÇÃO', 'title': 'JEJUM INTERMITENTE PODE PREJUDICAR GANHOS'},
        {'name': 'FOFOCA MAROMBA', 'title': 'BOMBA NO MUNDO MAROMBA'}
    ]
    
    image_url = 'https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=1024&h=1024&fit=crop'
    
    for cat in categories:
        print(f'\n📤 Testando categoria: {cat["name"]}')
        
        try:
            response = requests.post(
                f'{OVERLAY_SERVICE_URL}/add-overlay',
                json={
                    'imageUrl': image_url,
                    'title': cat['title'],
                    'category': cat['name']
                },
                timeout=60
            )
            
            if response.status_code == 200:
                data = response.json()
                image_data = base64.b64decode(data['image'])
                output_path = f'test_{cat["name"].lower()}.png'
                
                with open(output_path, 'wb') as f:
                    f.write(image_data)
                
                print(f'✅ {cat["name"]}: Salvo em {output_path}')
            else:
                print(f'❌ {cat["name"]}: Erro {response.status_code}')
                
        except Exception as e:
            print(f'❌ {cat["name"]}: {e}')
    
    print('\n🎉 Teste de categorias concluído!')

def test_long_title():
    """Teste 4: Título Longo (Truncamento)"""
    print('\n� ITeste 4: Título Longo (Truncamento)')
    print('=' * 50)
    
    test_cases = [
        {
            'title': 'VOCÊ ESTÁ DESPERDIÇANDO SUA CREATINA',  # 5 palavras (curto)
            'filename': 'test_titulo_curto.png',
            'words': 5
        },
        {
            'title': 'VOCÊ ESTÁ DESPERDIÇANDO SUA CREATINA SEM SABER DISSO',  # 8 palavras (ideal)
            'filename': 'test_titulo_ideal.png',
            'words': 8
        },
        {
            'title': 'ESTE ERRO NO TREINO ESTÁ MATANDO SEUS GANHOS E VOCÊ NEM SABE DISSO',  # 14 palavras (máximo)
            'filename': 'test_titulo_maximo.png',
            'words': 14
        },
        {
            'title': 'ESTE É UM TÍTULO MUITO LONGO QUE TEM MAIS DE QUINZE PALAVRAS E VAI SER TRUNCADO AUTOMATICAMENTE PELO SISTEMA',  # 19 palavras (será truncado)
            'filename': 'test_titulo_truncado.png',
            'words': 19
        }
    ]
    
    image_url = 'https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=1024&h=1024&fit=crop'
    
    for test in test_cases:
        print(f'\n📤 Testando: {test["words"]} palavras')
        print(f'Título: {test["title"][:60]}...' if len(test["title"]) > 60 else f'Título: {test["title"]}')
        
        try:
            response = requests.post(
                f'{OVERLAY_SERVICE_URL}/add-overlay',
                json={
                    'imageUrl': image_url,
                    'title': test['title'],
                    'category': 'TREINO'
                },
                timeout=60
            )
            
            if response.status_code == 200:
                data = response.json()
                image_data = base64.b64decode(data['image'])
                
                with open(test['filename'], 'wb') as f:
                    f.write(image_data)
                
                print(f'✅ Salvo em: {test["filename"]}')
            else:
                print(f'❌ Erro: {response.status_code}')
                
        except Exception as e:
            print(f'❌ Erro: {e}')
    
    print('\n🎉 Teste de títulos concluído!')
    print('📝 Verifique como ficou o truncamento nas imagens geradas.')

def run_all_tests():
    """Executar todos os testes"""
    print('\n🚀 INICIANDO TESTES DO MICROSERVIÇO DE OVERLAY (PYTHON)')
    print('=' * 70)
    
    # Teste 1: Health Check
    health_ok = test_health_check()
    if not health_ok:
        print('\n❌ Microserviço não está rodando!')
        print('Execute: python app.py')
        return
    
    # Teste 2: Overlay básico
    test_add_overlay()
    
    # Teste 3: Diferentes categorias
    test_different_categories()
    
    # Teste 4: Títulos com diferentes tamanhos
    test_long_title()
    
    print('\n' + '=' * 70)
    print('🎉 TODOS OS TESTES CONCLUÍDOS!')
    print('📁 Verifique os arquivos PNG gerados nesta pasta.')
    print('\n📊 Arquivos gerados:')
    print('  - test_output.png (teste básico)')
    print('  - test_suplementos.png (categoria verde)')
    print('  - test_treino.png (categoria laranja)')
    print('  - test_nutricao.png (categoria azul)')
    print('  - test_fofoca maromba.png (categoria magenta)')
    print('  - test_titulo_curto.png (5 palavras)')
    print('  - test_titulo_ideal.png (8 palavras)')
    print('  - test_titulo_maximo.png (14 palavras)')
    print('  - test_titulo_truncado.png (19 palavras → truncado para 15)')
    print('=' * 70)

if __name__ == '__main__':
    run_all_tests()
