pip install Cython
Install visual studio 2019
MinGW Cygwin

python -m compileall <src>   
  
删除 <src> 目录下所有 .py 文件就可以打包发布。

find . -name '*.py' -type f -print -exec rm {} \;

https://gitforwindows.org/

https://tortoisegit.org/download/

python -O -m compileall .
find . -name '*.pyc' -exec rename 's/.cpython-35.opt-1//' {} \;
find . -name '*.pyc' -execdir mv {} .. \;
find . -name '*.py' -type f -print -exec rm {} \;
find . -name '__pycache__' -exec rmdir {} \;
zip -r ../$1.zip ./*
