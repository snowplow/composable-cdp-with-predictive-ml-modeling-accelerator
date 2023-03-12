#!/bin/bash

if [[ $# -eq 0 ]]; then
    echo "At least one argument required. Use 'serve' to run the server"
    exit 1
fi

mkdir -p build/{themes,layouts,static}

echo "Importing config..."
cp accelerator-web-ui-template/config.toml build/baseconfig.toml
cp config.toml build/

echo "Importing themes..."
git submodule update --init --recursive
cp -R accelerator-web-ui-template/{themes/hugo-theme-learn,layouts/*,static/*} build/

echo "Creating Hugo site..."
HUGO_COMMAND="hugo"
if [[ $1 = "serve" ]]; then
    echo "Will start Hugo server"
    HUGO_COMMAND+=" server"
fi

OUTPUT_DIR="../public${2:-}"
BASE_URL=${3:+"-b $3"}

$HUGO_COMMAND --config baseconfig.toml,config.toml --gc --minify -d "$OUTPUT_DIR" $BASE_URL

rm -rf build

