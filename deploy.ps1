# Script de Deploy para GitHub
# Execute este script para fazer commit e push dos arquivos

Write-Host "🚀 Preparando deploy do microserviço..." -ForegroundColor Green

# Verificar se está na pasta correta
if (-not (Test-Path "app.py")) {
    Write-Host "❌ Erro: Execute este script na pasta microservico_overlay_python" -ForegroundColor Red
    exit 1
}

# Verificar se Git está instalado
try {
    git --version | Out-Null
} catch {
    Write-Host "❌ Erro: Git não está instalado" -ForegroundColor Red
    Write-Host "Instale Git: https://git-scm.com/download/win" -ForegroundColor Yellow
    exit 1
}

# Verificar se já tem remote configurado
$hasRemote = git remote -v 2>&1 | Select-String "origin"

if (-not $hasRemote) {
    Write-Host "📦 Configurando remote do GitHub..." -ForegroundColor Cyan
    git remote add origin https://github.com/Folkz1/overlay-automatize-news.git
}

# Adicionar arquivos
Write-Host "📝 Adicionando arquivos..." -ForegroundColor Cyan
git add .

# Fazer commit
Write-Host "💾 Fazendo commit..." -ForegroundColor Cyan
$commitMessage = "Add overlay microservice with Docker config for Easypanel"
git commit -m $commitMessage

# Push para GitHub
Write-Host "🌐 Enviando para GitHub..." -ForegroundColor Cyan
try {
    git push -u origin main
    Write-Host "✅ Deploy preparado com sucesso!" -ForegroundColor Green
    Write-Host ""
    Write-Host "🎯 Próximos passos:" -ForegroundColor Yellow
    Write-Host "1. Acesse seu Easypanel" -ForegroundColor White
    Write-Host "2. Crie um novo App" -ForegroundColor White
    Write-Host "3. Configure o repositório: https://github.com/Folkz1/overlay-automatize-news.git" -ForegroundColor White
    Write-Host "4. Siga o guia: GUIA_DEPLOY_PASSO_A_PASSO.md" -ForegroundColor White
} catch {
    Write-Host "⚠️ Tentando branch master..." -ForegroundColor Yellow
    try {
        git push -u origin master
        Write-Host "✅ Deploy preparado com sucesso!" -ForegroundColor Green
    } catch {
        Write-Host "❌ Erro ao fazer push" -ForegroundColor Red
        Write-Host "Verifique suas credenciais do GitHub" -ForegroundColor Yellow
        exit 1
    }
}
