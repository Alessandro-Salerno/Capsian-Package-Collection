import Capsian
from   Capsianline.commands.command import Command


def get_scripts(name):
	import os
	_dirs = os.listdir(f"./projects/{name}")
	dirs = []

	for _dir in _dirs:
		if not os.path.isdir(f"./projects/{name}/{_dir}") and ".py" in _dir:
			dirs.append(_dir)

	return dirs


class Script(Command):
	def __str__(self) -> str:
		return "script"


	def new(self, name: str):
		import os

		if os.path.exists(f"./projects/{name}"):
			Capsian.Log.error(f"Project \"{name}\" already exists")
			return

		os.mkdir(f"./projects/{name}")
		Capsian.Log.successful("Project created!")


	def delete(self, name: str):
		import os
		import shutil

		if not os.path.exists(f"./projects/{name}"):
			Capsian.Log.error(f"Project \"{name}\" does not exist")
			return

		shutil.rmtree(f"./projects/{name}")
		Capsian.Log.successful("Project deleted!")


	def run(self, name: str):
		import os

		scripts = get_scripts(name)
		with open("./projects/__init__.py", "w") as __init__:
			nscripts = []
			
			for script in scripts:
				nscripts.append(f"import projects.{name}.{str(script).strip('.py')}")

			__init__.writelines(nscripts)

		os.system("python main.py" if os.name == "nt" else "python3 main.py")


__linecommand__ = Script()
