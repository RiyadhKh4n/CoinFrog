echo 'unset DATABASE_URL' >> ~/.bashrc
echo 'unset PGHOSTADDR' >> ~/.bashrc
echo 'alias make_url="python3 $GITPOD_REPO_ROOT/.vscode/make_url.py"' >> ~/.bashrc
echo 'ln -s /home/gitpod/.pyenv/versions/3.8.12/ /workspace/.pip-modules' >> ~/.bashrc
echo 'pip3 uninstall -y -r "$GITPOD_REPO_ROOT/.vscode/deps.txt" > /dev/null' >> ~/.bashrc

export POST_UPGRADE_RUN=1
source ~/.bashrc
