@echo off
REM Start Claude Code with n8n MCP connection

echo Loading n8n API key...
for /f "tokens=2 delims==" %%a in ('type .env.n8n ^| findstr "N8N_API_KEY"') do set N8N_API_KEY=%%a

if "%N8N_API_KEY%"=="" (
    echo ERROR: N8N_API_KEY not found in .env.n8n
    echo Please add your API key to .env.n8n file
    pause
    exit /b 1
)

echo Starting Claude Code with n8n MCP...
claude

pause
