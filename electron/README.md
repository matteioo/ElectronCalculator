# scss
## Description
In this directory you will find the final electron files, which will land in the app.
## Folder structure:
  - **css** - final css files which are the output from the scss preprocessor
  - **vendor** - here are required resources from outside like Fonts or Icons

## Changelog
### v0.1
  - added [new Font](vendor/README.md#v01)

### v0.2
  - added `test-outputs.html` which is just for testing purposes - contains just some static dummy texts.
  - added [new Icons](vendor/README.md#v02) from FontAwesome v5.1.0

### v0.3
  - restyled margin of <p>
  - set variableTable to `450px`
  - defined sroll behavior to scroll vertically (only Output and variableTable)
  - changed colors of the variableTable `<table>`
  - set height of first grid row to fill up remaining space: `height: calc(1100vh - 60px);`
  - changed margins of the input form
  - changed fonts and styling of the `<input>` in the input container -> no borders, placeholder font, transparency, margin (to display the icon correct on the left), width of the `<input>`
  - styling lines in the output container (e.x. `error` or `special` outputs)
### v0.4
  - added eclectron files
