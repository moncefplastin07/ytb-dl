$CliUri = "https://github.com/moncefplastin07/ytb-dl/raw/main/ytb-dl.exe"
Invoke-WebRequest $CliUri -OutFile "C:\clis\ytb-dl.exe" -UseBasicParsing

Write-Output "YTB CLI was installed successfully"