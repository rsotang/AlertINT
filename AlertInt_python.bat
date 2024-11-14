@echo off 
Z:
cd Z:\Dosis pacientes\Alertas_Intervencionismo\_PRUEBAS EN CURSO-AlertInt python
echo Ejecutando AlertInt Python
:: Ejecuta el primer script 
echo Ejecutando import_XML_biplano.py
python import_XML_biplano.py 

 :: Ejecuta el segundo script 
echo Ejecutando import_XML_hibrido.py
python import_XML_hibrido.py

 :: Ejecuta el tercer 
echo Ejecutando import_XML_SiemensHemoD.py
python import_XML_SiemensHemoD.py 

 :: Ejecuta el cuarto script
echo Ejecutando import_SR_General.py 
python import_SR_General.py
 
 :: Ejecuta el quinto script 
echo Ejecutando import_SR_Philllips.py
python import_SR_Philllips.py
 :: Fin del script 
echo Todos los scripts se han ejecutado correctamente.