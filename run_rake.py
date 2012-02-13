import sublime, sublime_plugin
import subprocess, re

class RunRakeCommand(sublime_plugin.WindowCommand):
	def run(self,cmd="rake",env=None):
		print "building with run_rake"
		view = self.window.active_view()
		regions = view.find_all('!RAKE .*$',0)
		cmd = ['rake']
		task = None
		args = {}
		for region in regions:
			m = re.match('!RAKE \ *(.*?)\ *=\ *(.*?)\ *$', view.substr(region))
			if m.group(1) == 'task':
				task = m.group(2)
			else:
				cmd.append(m.group(1) + "=" + m.group(2))
		
		if task != None: cmd.append(task)	
		args['cmd'] = cmd
		if env != None: args['env'] = env

		self.window.run_command('exec', args)
