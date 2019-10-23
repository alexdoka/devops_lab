#!/bin/bash
#sudo yum install -y git libffi-devel zlib-devel bzip2-devel readline-devel sqlite-devel wget curl llvm ncurses-devel openssl-devel lzma-sdk-devel redhat-rpm-config
#curl -L  https://raw.github.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash

#echo "export PATH=\"/root/.pyenv/bin:\$PATH\"" >> ~/.bashrc
#echo "eval \"\$(pyenv init -)\"" >> ~/.bashrc
#echo "eval \"\$(pyenv virtualenv-init -)\"" >> ~/.bashrc

pyenv install 3.7.5
pyenv install 2.7.17
pyenv virtualenv 3.7.5 python-3.7.5
pyenv virtualenv 2.7.17 python-2.7.17

