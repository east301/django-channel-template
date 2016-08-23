#!/bin/bash

my_dir=\$(cd \$(dirname \$0) && pwd)

function goto() {
    cd \$my_dir
    mkdir -p \$1
    cd \$1
}

# bootstrap
goto $name$/apps/vendor/static/bootstrap+bootswatch/css
ln -s ../../../../../../node_modules/bootswatch/yeti/bootstrap.css
ln -s ../../../../../../node_modules/bootswatch/yeti/bootstrap.min.css

goto $name$/apps/vendor/static/bootstrap+bootswatch/fonts
ln -s ../../../../../../node_modules/bootstrap/dist/fonts/glyphicons-halflings-regular.eot
ln -s ../../../../../../node_modules/bootstrap/dist/fonts/glyphicons-halflings-regular.svg
ln -s ../../../../../../node_modules/bootstrap/dist/fonts/glyphicons-halflings-regular.ttf
ln -s ../../../../../../node_modules/bootstrap/dist/fonts/glyphicons-halflings-regular.woff
ln -s ../../../../../../node_modules/bootstrap/dist/fonts/glyphicons-halflings-regular.woff2

goto $name$/apps/vendor/static/bootstrap+bootswatch/js
ln -s ../../../../../../node_modules/bootstrap/dist/js/bootstrap.js
ln -s ../../../../../../node_modules/bootstrap/dist/js/bootstrap.min.js
ln -s ../../../../../../node_modules/bootstrap/dist/js/npm.js

# font-awesome
goto $name$/apps/vendor/static/font-awesome/css
ln -s ../../../../../../node_modules/font-awesome/css/font-awesome.css.map
ln -s ../../../../../../node_modules/font-awesome/css/font-awesome.min.css

goto $name$/apps/vendor/static/font-awesome/fonts
ln -s ../../../../../../node_modules/font-awesome/fonts/FontAwesome.otf
ln -s ../../../../../../node_modules/font-awesome/fonts/fontawesome-webfont.eot
ln -s ../../../../../../node_modules/font-awesome/fonts/fontawesome-webfont.svg
ln -s ../../../../../../node_modules/font-awesome/fonts/fontawesome-webfont.ttf
ln -s ../../../../../../node_modules/font-awesome/fonts/fontawesome-webfont.woff
ln -s ../../../../../../node_modules/font-awesome/fonts/fontawesome-webfont.woff2

# jquery
goto $name$/apps/vendor/static/jquery
ln -s ../../../../../node_modules/jquery/dist/jquery.js
ln -s ../../../../../node_modules/jquery/dist/jquery.min.js
ln -s ../../../../../node_modules/jquery/dist/jquery.min.map

# vue
ln -s ../../../../../node_modules/vue/dist/vue.common.js
ln -s ../../../../../node_modules/vue/dist/vue.js
ln -s ../../../../../node_modules/vue/dist/vue.min.js
ln -s ../../../../../node_modules/vue/dist/vue.min.js.map
