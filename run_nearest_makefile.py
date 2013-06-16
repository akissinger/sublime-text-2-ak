import sublime, sublime_plugin
import subprocess, re
import os, os.path

class RunNearestMakefileCommand(sublime_plugin.WindowCommand):
  def run(self,target='',env=None):
    cmd = ['make']
    
    file = self.window.active_view().file_name()
    
    if file != None:
      path = os.path.dirname(file)

      found_make = False
      while path != '/' and path != '':
        if os.path.isfile(path + '/Makefile'):
          found_make = True
          break
        path = os.path.dirname(path)

      if found_make:
        if env != None: args['env'] = env
        cmd = ['(source ~/.profile; cd ' + path + '; make ' + target + ')']
        self.window.run_command('exec', {'cmd':cmd, 'shell':True})
