*GOAL*
- The goal of the project is to generate multiple koch snowflakes that form a kaleidoscope. The kaleidoscope should be animated and saved as a gif in the "Output" folder.

*MOTIVATION*
- The motivation is to create a beautiful animation :)

*STRUCTURE*
- The project is structured in 2 classes and one folder.
  - snowflake.py is able to create koch snowflakes.
  - kaleidoscope.py uses snowflakes to create an animation.
  - "Output" is a folder that contains the created gif.

*REQUIREMENTS*
- Installation of matplotlib
- Installation of numpy
- Installation of MovieWriter or Pillow (should be preinstalled when using matplotlib)

*INSTRUCTIONS*
- Run the programm by executing kaleidoscope.py
- Then follow guidance from the console

*INPUT-SETTINGS*
- The console will ask you for input. You can specify the following settings:
  - Number of snowflakes: How many koch snowflakes should spawn. If the amount doesn't fit the screen then the most possible amount of snowflakes will be spawned.
  - Colors: What colors should be possible for the snowflakes. Seperate with comma. (e.g.: red,green,blue,yellow)
  - Rotate: If the kaleidoscope should rotate or not.
  - Changing Colors: If the kaleidoscope should change colors or not.
  - Change_speed: How fast the kaleidoscope should change colors and rotate. (100 means that 1 frame lasts 100ms)

***Project for the SciPy-Course by rokock and afroemmel.***