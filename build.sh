rm -rf build/ dist/ *.spec

pyinstaller --name "Mouse Bot" --clean --windowed --onefile --icon icon-dark-theme.png app.py --add-data "icon-light-theme.png:." --add-data "icon-dark-theme.png:." 
