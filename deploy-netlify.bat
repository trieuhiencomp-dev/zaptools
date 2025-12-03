@echo off
echo Deploying to Netlify...
cd /d "%~dp0"

rem Deploy using git push method (Netlify will auto-deploy from connected repo)
rem Or use manual deployment with specific files

netlify deploy --prod --dir=. --filter="*.html" --filter="*.md" --filter="netlify.toml" --filter="_redirects"

echo Deployment initiated!
pause
