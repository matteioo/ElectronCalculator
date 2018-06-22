# vendor
## Description
In this folder you will find required resources (like Fonts, Icons) which will get imported from here. This is a safer way in terms of *GDPR safety*. Even more, you will be able to use the final ElectronCalculator in offline mode :+1:.
## Folder structure:
  - **fonts** - here you find font specific files
  - **FontAwesome-5.1.0** - In this folder are the downloaded resources used to display FontAwesome Icons. **Important:** Currently the *js* version of FontAwesome is used. Here you will find an instruction on how to change it to css.
## Special Instructions
### FontAwesome
In this repository the **JavaScript version** of FontAwesome is currently been used. To change this, you need to uncomment ```<link rel="stylesheet" href="vendor/FontAwesome-5.1.0/css/all.css">``` (loads the FontAwesome css files) in the ```head``` **of each file**. Furthermore you have to delete or comment out following line: ```<script defer src="vendor/FontAwesome-5.1.0/js/all.js"></script>``` (loads the FontAwesome js files).
Remember that loading the css files of FontAwesome has to be before loading the ```styles.css``` or ```styles.min.css``` from the css folder.
## Changelog
### v0.1
  - added [Roboto Mono](https://fonts.google.com/specimen/Roboto+Mono) into the fonts folder
### v0.2
  - added [FontAwesome(5.1.0)](https://fontawesome.com/) css and js version into the folder `FontAwesome-5.0.13` (added all icons in FontAwesome Free) - *Attention:* css version of FontAwesome is currently unused but can be [activated](vendor/README.md#fontawesome)
