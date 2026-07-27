$ErrorActionPreference = "Stop"

$ProjectRoot = $PSScriptRoot

if ([string]::IsNullOrWhiteSpace($ProjectRoot)) {
    $ProjectRoot = (Get-Location).Path
}

Set-Location $ProjectRoot

$Timestamp = Get-Date -Format "yyyy-MM-dd_HH-mm-ss"
$SnapshotName = "SIGC_snapshot_$Timestamp.zip"
$SnapshotPath = Join-Path $ProjectRoot $SnapshotName

Write-Host ""
Write-Host "Diretorio do projeto:" -ForegroundColor Cyan
Write-Host $ProjectRoot

Write-Host ""
Write-Host "Criando snapshot..." -ForegroundColor Yellow

if (-not (Get-Command tar.exe -ErrorAction SilentlyContinue)) {
    throw "O comando tar.exe nao foi encontrado no Windows."
}

& tar.exe `
    -a `
    -c `
    -f $SnapshotPath `
    --exclude=".git" `
    --exclude=".venv" `
    --exclude="venv" `
    --exclude="env" `
    --exclude="__pycache__" `
    --exclude=".pytest_cache" `
    --exclude=".mypy_cache" `
    --exclude=".ruff_cache" `
    --exclude=".vscode" `
    --exclude=".idea" `
    --exclude="*.pyc" `
    --exclude="*.pyo" `
    --exclude="*.log" `
    --exclude="*.zip" `
    .

if ($LASTEXITCODE -ne 0) {
    throw "O tar.exe terminou com erro. Codigo: $LASTEXITCODE"
}

if (-not (Test-Path $SnapshotPath)) {
    throw "O comando terminou, mas o arquivo ZIP nao foi encontrado."
}

$SnapshotFile = Get-Item $SnapshotPath
$SizeMB = [math]::Round($SnapshotFile.Length / 1MB, 2)

Write-Host ""
Write-Host "Snapshot criado com sucesso!" -ForegroundColor Green
Write-Host "Arquivo: $($SnapshotFile.FullName)"
Write-Host "Tamanho: $SizeMB MB"
Write-Host ""