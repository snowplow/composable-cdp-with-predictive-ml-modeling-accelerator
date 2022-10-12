#!/bin/bash
mkdir build

echo "Importing config..."
cp accelerator-web-ui-template/config.toml build/baseconfig.toml
cp config.toml build/config.toml
cp -R content build/

echo "Importing themes..."
git submodule update --init --recursive
mkdir build/themes
cp -R accelerator-web-ui-template/themes/hugo-theme-learn build/themes/
cp -R accelerator-web-ui-template/layouts build/
cp -R accelerator-web-ui-template/static build/

echo "Creating Hugo site..."
cd build
if [ $# -eq 2 ]
then
hugo --config baseconfig.toml,config.toml --gc --minify -d ../public$1 -b $2
elif [ $# -eq 1 ]
then
hugo --config baseconfig.toml,config.toml --gc --minify -d ../public$1
else
hugo --config baseconfig.toml,config.toml --gc --minify -d ../public
fi
cd ..
rm -r build
