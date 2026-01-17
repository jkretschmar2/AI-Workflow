Write-Host "Building AI Documentation Site..."

$sourceLists = ".\Lists"
$sourceFlowcharts = ".\Flowcharts"
$destData = ".\docs\data"

# Create destination if not exists
if (-not (Test-Path $destData)) {
    New-Item -ItemType Directory -Force -Path $destData | Out-Null
}

# Copy JSON files
Write-Host "Copying JSON data..."
Get-ChildItem -Path $sourceLists -Filter *.json | ForEach-Object {
    Copy-Item $_.FullName -Destination $destData -Force
    Write-Host "  $($_.Name)"
}

# Copy Mermaid files
Write-Host "Copying Mermaid diagrams..."
Get-ChildItem -Path $sourceFlowcharts -Filter *.mmd | ForEach-Object {
    Copy-Item $_.FullName -Destination $destData -Force
    Write-Host "  $($_.Name)"
}

Write-Host "Site build complete. Assets updated in $destData"
