rm -rf build/ dist/ *.spec

pyinstaller --name "AFK Bot" --clean --windowed --onefile --icon icon.png app.py --add-data "icon.png:."
