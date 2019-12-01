## Set Up Virtualenv
`sudo apt-get install -y virtualenv`
`pip install virtualenvwrapper`

In `~/.bashrc` add:
```
# Virtualenvs
export WORKON_HOME=~/.envs
mkdir -p $WORKON_HOME
source ~/.local/bin/virtualenvwrapper.sh
```
^ This lets us do `workon myenv`.

Now create a place to put your Virtualenvs:
`mkdir ~/.envs`

And create your Virtualenv:
`virtualenv ~/.envs/neuroblog`

Add our scripts to the Pythonpath in `~/.envs/neuroblog/bin/activate`:
```
# Update PYTHONPATH
export PYTHONPATH=/home/ryan/ryan_stuff/projects/github_pages/rschuster3.github.io/neuroblog/src
```

Work on it:
```
source ~/.envs/neuroblog activate
workon neuroblog
```

Now you can do relative imports from anything under `neuroblog/src/`. For instance in `neuroblog/src/c1s2/plot_spikes.py` you can import `from utils.generate_spikes import random_spikes` and then run `python plot_spikes.py`. This is all assuming `src/` and `utils/` have `__init__.py` files.
