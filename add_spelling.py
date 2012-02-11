import sublime, sublime_plugin

class AddSpellingCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        word = self.view.substr(self.view.sel()[0])
        settings = sublime.load_settings('Preferences.sublime-settings')
        dic = settings.get('dictionary')
        if word != '' and dic != '':
            dic = sublime.packages_path()[0:-8] + dic
            dicfile = open(dic, 'a')
            dicfile.write(word + '\n')
            dicfile.close()
            
            # Sublime doesn't reload dictionaries until it is closed and re-opened, so
            # ignore the word in the mean time.
            self.view.run_command('ignore_word', {'word': word})
        
