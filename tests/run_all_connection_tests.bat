@echo off
echo ==========================================
echo  TEST DE CONEXIONES - BPAE
echo ==========================================
echo.

cd /d "%~dp0\.."

echo [1/3] Probando conexion a Supabase...
echo ------------------------------------------
python tests\test_connection_supabase.py
echo.

echo [2/3] Probando conexion a Tavily...
echo ------------------------------------------
python tests\test_connection_tavily.py
echo.

echo [3/3] Probando conexion a OpenCode...
echo ------------------------------------------
python tests\test_connection_opencode.py
echo.

echo ==========================================
echo  TESTS COMPLETADOS
echo ==========================================
pause
