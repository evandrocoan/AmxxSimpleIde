

import sublime
import sublime_plugin

import os

PACKAGE_NAME = "amxmodx"


def plugin_loaded() :
    install_setting_file( "Main.sublime-menu" )

def install_setting_file( target_file_name ):
    target_directory = sublime.packages_path()
    target_file      = os.path.join( target_directory, PACKAGE_NAME, target_file_name )

    attempt_to_install_file( target_directory, target_file, "\n[\n\n]\n" )

def attempt_to_install_file( target_directory, target_file, input_file_string ):

    if not os.path.exists( target_directory ):
        os.makedirs( target_directory )

    text_file = open( target_file, "w" )
    text_file.write( input_file_string )
    text_file.close()


