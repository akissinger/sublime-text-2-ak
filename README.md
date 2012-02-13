AK Sublime Text 2 Package
=========================

This is a collection of miscellaneous commands, plugins, etc. that I have found useful in Sublime Text 2. To install, simply clone into your `Packages` directory:

    git clone git://github.com/akissinger/sublime-text-2-ak.git AK



Learn Spelling Command
----------------------

For `add_spelling` to work correctly, you need to have a dictionary defined in `Preferences.sublime-settings`. For instance, to use the built-in English/US dictionary:

    "dictionary": "Packages/Language - English/en_US.dic"

The English/UK dictionary can be downloaded from [here](http://en-gb.pyxidium.co.uk/dictionary/en_GB.zip). For more info on spell checking and dictionaries, see the [Sublime doc](http://www.sublimetext.com/docs/2/spell_checking.html). I have also added the following lines to my `.sublime-keymap` file:

    [
      { "keys": ["super+shift+m"], "command": "latex_align_matrix" },
      { "keys": ["super+shift+a"], "command": "add_spelling" }
    ]


Rake Build System
-----------------

The rake build system is implemented via the `run_rake` command. The default behaviour is to run rake in the directory of the active file, however you can pass additional parameters into rake by including `!RAKE param=value` somewhere in the active file. The `task` parameter sets the task that rake builds, and all other parameters are passed in as parameters to the rake command. For example, including these comment lines:

    %!RAKE task=build
    %!RAKE verbose=1

Will invoke rake as:

    rake verbose=1 build


