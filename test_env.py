from kaggle_environments import make
env = make("hungry_geese", debug=True)

env.reset()
env.run(['example_code.py', 'example_code.py','example_code.py','example_code.py'])
env.render(mode="ipython", width=800, height=700)
