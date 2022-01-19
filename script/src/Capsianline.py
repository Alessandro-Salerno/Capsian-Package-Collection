import Capsian
from   Capsianline.commands.command import Command


class Script(Command):
	def __str__(self) -> str:
		return "script"


	def new(self, name: str, project: str):
		import os

		if not os.path.exists(f"./projects/{project}"):
			Capsian.Log.error(f"Project \"{project}\" does not exist")
			return

		if os.path.exists(f"./projects/{project}/{name}.py"):
			Capsian.Log.error(f"Script \"{name}.py\" already exists")
			return
		
		with open(f"./projects/{project}/{name}.py", "w") as script:
			script.write(f"""
# PROJECT: {project}
# SCRIPT: {name}

from Capsian import *
from addons  import *


@IndependentComponent
class {name.capitalize()}Keyboard(KeyboardInputHandler):
	def on_key_press(self, symbol, modifiers):
		if symbol == Key.ENTER:
			print("Enter pressed")

	def on_key_released(self, symbol, modifiers) -> None:
		if symbol == Key.ENTER:
			print("Enter released")

	def on_key_held(self, keys: dict) -> None:
		if keys[Key.A]:
			print("A is held down")


@IndependentComponent
class {name.capitalize()}Mouse(MouseInputHandler):
	def on_button_press(self, x, y, button, modifiers) ->None:
		if button == MouseButton.LEFT:
			print("Left button pressed")

	def on_button_released(self, x, y, button, modifiers) -> None:
		if button == MouseButton.LEFT:
			print("Left button released")

	def on_button_held(self, buttons: dict) -> None:
		if buttons[MouseButton.LEFT]:
			print("Left button held down")


@IndependentComponent
class {name.capitalize()}(Script):
	def on_start(self, time) -> None:
		print("Hello world")

	def on_update(self, dt, time) -> None:
		print("Updated")

	def on_close(self, time) -> None:
		print("Closed")
""".replace("	", "\t"))

		Capsian.Log.successful("Script created!")


	def delete(self, name: str, project: str):
		import os

		if not os.path.exists(f"./projects/{project}"):
			Capsian.Log.error(f"Project \"{project}\" does not exist")
			return

		if not os.path.exists(f"./projects/{project}/{name}.py"):
			Capsian.Log.error(f"Script \"{name}.py\" does not exist")
			return

		os.remove(f"./projects/{project}/{name}.py")
		Capsian.Log.successful("Script deleted!")


	def edit(self, name: str, project: str, editor: str):
		import os
		os.system(f"{editor} \"./projects/{project}/{name}.py\"")


__linecommand__ = Script()
