$CliUri = "https://github.com/moncefplastin07/ytb-dl/raw/main/ytb-dl.exe"
$BinDir = "$Home\.ytb-dl\bin"
$CliPath = "$BinDir\ytb-dl.exe"

if (!(Test-Path $BinDir)) {
    New-Item $BinDir -ItemType Directory | Out-Null
}

if (!(Test-Path $BinDir)) {
    New-Item $BinDir -ItemType Directory | Out-Null
}

Invoke-WebRequest $CliUri -OutFile $CliPath -UseBasicParsing

$User = [EnvironmentVariableTarget]::User
$Path = [Environment]::GetEnvironmentVariable('Path', $User)
if (!(";$Path;".ToLower() -like "*;$BinDir;*".ToLower())) {
  [Environment]::SetEnvironmentVariable('Path', "$Path;$BinDir", $User)
  $Env:Path += ";$BinDir"
}

Write-Output "YTB CLI was installed successfully $BinDir"
