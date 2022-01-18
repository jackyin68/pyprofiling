pip install Cython
Install visual studio 2019
MinGW Cygwin

python -m compileall <src> 然后删除 <src> 目录下所有 .py 文件就可以打包发布了：

$ find <src> -name '*.py' -type f -print -exec rm {} \;

https://gitforwindows.org/

https://tortoisegit.org/download/
