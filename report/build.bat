@echo off
REM =====================================================================
REM  build.bat -- Windows 下一键编译综述报告
REM
REM  优先使用 latexmk；未安装时回退到 pdflatex + bibtex 四遍流程。
REM  需在本文件所在目录（report\）下运行。
REM =====================================================================
setlocal enabledelayedexpansion

echo ============================================
echo   RSI Harness Review - LaTeX build
echo ============================================
echo.

REM ---- 检查 refs/refs.bib 是否存在（bibliography 指向 ../refs/refs）----
if not exist "..\refs\refs.bib" (
    echo [ERROR] 找不到 ..\refs\refs.bib
    echo         LaTeX 无法解析参考文献。请先创建该文件。
    echo         按 AGENTS.md §7.4，应由 Zotero 导出。
    echo.
    exit /b 1
)

REM ---- 路径检测：优先 latexmk ----
set "USELATEXMK=0"
where latexmk >nul 2>nul
if %ERRORLEVEL%==0 set "USELATEXMK=1"

if "%USELATEXMK%"=="1" goto :latexmk

REM ---- 回退：检查 pdflatex ----
where pdflatex >nul 2>nul
if not %ERRORLEVEL%==0 goto :nolatex

echo [INFO] 未找到 latexmk，使用 pdflatex + bibtex
echo.
pdflatex -interaction=nonstopmode -file-line-error main.tex
if %ERRORLEVEL% neq 0 goto :failed

echo [INFO] running bibtex ...
bibtex main
if %ERRORLEVEL% neq 0 (
    echo [WARN] bibtex 返回错误。若报告无引用可忽略，否则检查 refs.bib。
)

echo [INFO] pass 2/3 ...
pdflatex -interaction=nonstopmode -file-line-error main.tex
if %ERRORLEVEL% neq 0 goto :failed

echo [INFO] pass 3/3 ...
pdflatex -interaction=nonstopmode -file-line-error main.tex
if %ERRORLEVEL% neq 0 goto :failed

goto :done

:latexmk
echo [INFO] 使用 latexmk
echo.
latexmk -pdf -interaction=nonstopmode -file-line-error main.tex
if %ERRORLEVEL% neq 0 goto :failed
goto :done

:nolatex
echo [ERROR] 未找到 latexmk 或 pdflatex。
echo         请安装 TeX Live 或 MiKTeX：https://www.tug.org/texlive/
echo.
exit /b 1

:failed
echo.
echo ============================================
echo   [FAIL] 编译失败。请查看 main.log
echo   常见原因:
echo     - 缺包: 用 tlmgr install <pkgname> 安装
echo     - 中文路径: 若仓库路径含非 ASCII 字符且报错，
echo       请把本目录复制到纯 ASCII 路径再编译（如 C:\temp\rsr\）
echo ============================================
exit /b 1

:done
echo.
echo ============================================
echo   [OK] main.pdf 已生成
echo ============================================
endlocal
