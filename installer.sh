

## pyinstaller how to use
# https://pyinstaller.readthedocs.io/en/stable/usage.html


## variables globales
dist_folder="dist"
config_file="config.ini"
ico_file="favicon.ico"


# creador de ejecutable
pyinstaller --distpath $dist_folder -F --clean -n opm_wc_status __main__.py


## copiar archivos de configuración
cp $config_file ./$dist_folder/
cp $ico_file ./$dist_folder/


echo ""
echo "##################################################"
echo "Finalzado, presiona cualquier tecla para cerrar"
echo "##################################################"

read myothervar