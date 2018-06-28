# scss
## Description
In this folder you will find the main styling files which are need to design the UI of the **ElectronCalculator**. This files need to be preprocessed to be able to see changes in the styling.
The scss files are going to be processed in the the directory `../../electron/css/` which you can change in the first line of the file `style.scss` in this folder.
## Folder structure:
  - **0-plugins** - the plugins directory contains imported and not changed files like resets/normalizes or framework files
  - **1-base** - in this directory you will find basic styling e.x. fonts and font sizes.
  - **2-layouts** - here are layout stylings for the grid and other positioning. Sometimes layouts can hold more than one modules.
  - **3-modules** - code in this diretory can be reused and style simple components which may be part of bigger ones, e.x. lists, buttons, ...

## Changelog
### v0.1
  - added [normalize](https://github.com/JohnAlbin/normalize-scss/tree/master/sass) into `0-plugins` and imported into the styling

### v0.2
  - added \_colors, \_forms, \_tables partials into `3-modules/`
  - changed \_layout, \_base
  - style changes [here](/electron/README.md#v03)

### v1.0
Version 1.0 released - the style does now look and work like in the UI Design ([*Adobe XD file*](/vendor/AdobeXD)).
  - changed the width to not use `calc();` in the css but setting the total width of the grid to `100vh`
