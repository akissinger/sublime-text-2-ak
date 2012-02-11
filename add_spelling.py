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
            self.view.run_command('ignore_word', {'word': word})
        
