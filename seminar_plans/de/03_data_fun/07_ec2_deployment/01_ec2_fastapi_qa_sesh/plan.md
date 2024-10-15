# Q+A session plan

Server: https://github.com/northcoders/de-sample-server

Env file:

```env
DB_HOST=nc-data-eng-production-toy.chpsczt8h1nu.eu-west-2.rds.amazonaws.com
DB_PORT=5432
DB_DB=toy
DB_USER=read_only
DB_PASSWORD=wUg2EXcQcUIa
```

Students are given the option of what they want to focus on from the following choices:

- Recap of what Cloud Computing is all about
- How to create an EC2 instance on the console and connect to it
- Updating to `python 3.11`
- Setting up the EC2 machine so it can run the server

## What is cloud computing

To quote AWS:

```txt
Cloud computing is the on-demand delivery of IT resources over the Internet with pay-as-you-go pricing. Instead of buying, owning, and maintaining physical data centers and servers, you can access technology services, such as computing power, storage, and databases, on an as-needed basis from a cloud provider like Amazon Web Services (AWS).
```

Essentially:

- Used to be that companies needed servers on site for all there hosting needs which was often very expensive.
- Now they can use AWS remote servers which can be cheaper than on premises but it's worth mentioning that this is not always the case. Care needs to be taken when provisioning services, costs can ramp up very quickly if you're not careful!

## Creating and connecting to an EC2 instance

Give a quick run through of setting up the EC2 instance - doesn't seem like many people are interested so don't need to spend loads of time.

Key things:

- `eu-west-2`
- key pairs .pem file
- allowing `ssh` and `http` access

## Updating `python`

**The sprint suggests updating the Python version - this isn't necessary the run the server but is an optional step that could be good to go through**

You may want to do this a different for example using a provided package manager (`yum` or `dnf`) or [building from source](https://realpython.com/installing-python/#linux-how-to-build-python-from-source-code). However I think it would probably be easiest to install and yse [`pyenv`](https://github.com/pyenv/pyenv/tree/master). Using `pyenv` you can do the following steps:

1. [Install Python dependencies](https://github.com/pyenv/pyenv/wiki#suggested-build-environment) - please bare in mind that the guidance for AWS Linux 2 is out of date - however I had success just running the command for CentOD/Fedora which is as follows:

```sh
sudo yum install gcc make patch zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel openssl-devel tk-devel libffi-devel xz-devel
```

2. Next you want to [install pyenv](https://github.com/pyenv/pyenv/tree/master?tab=readme-ov-file#unixmacos) - I'd recommend using the automatic installer (the other options are to install and use `brew` or clone `pyenv` directly). The command for using the automatic installer is:

```sh
curl https://pyenv.run | bash
```

3. Following that you want to add `pyenv` to the PATH. the output from running the previous command will tell you what to do and an easy way is to do the following:

```sh
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
```

and after that source the `.bashrc` file to be able to use the `pyenv` command

```sh
source ~/.bashrc
```

4. Finally you can use `pyenv` to install the required version like so:

**THIS WILL TAKE A WHILE - MAYBE UP TO 5 MINUTES**

```sh
pyenv install 3.11
```

and set the global version

```sh
pyenv global 3.11
```

**Now when you use the `python3` command it will be controlled by `pyenv`:**

## Setting up an EC2 instance to run the server

Run setup with `make`:

```sh
make requirements
```

**You should create the `.env` file here but if no one mentions it just gloss over and come back when it fails** - `/api/products`

```sh
sudo dnf install iptables
sudo iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 8000
make start-server # test endpoint from Insomnia or browser
```

## Extra:

Without updating python:

```sh
sudo yum install git -y
git clone https://github.com/northcoders/de-sample-server.git
sudo dnf install make
sudo yum update && sudo yum install python3-pip
make requirements
```

Joe solution:

```sh
sudo dnf update
sudo dnf install gcc libffi-devel python3-devel openssl-devel zlib zlib-devel bzip2 bzip2-devel xz xz-devel sqlite sqlite-devel
wget https://www.python.org/ftp/python/3.12.3/Python-3.12.3.tgz
tar xzf Python-3.12.3.tgz
cd Python-3.12.3/
sudo ./configure --enable-optimizations --enable-loadable-sqlite-extensions
sudo make install
cd
python3 --version // should show 3.12.3
sudo dnf install git
ssh-keygen -t ed25519 -C "[INSERT YOUR EMAIL ADDRESS HERE]"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
cat .ssh/id_ed25519.pub // add the output of this command as an SSH key in Github
git clone git@github.com:northcoders/de-sample-server.git
cd de-sample-server/
nano .env // add creds
make requirements
make dev-setup
make run-checks
//redirect port 80 HTTP traffic to port 8000 (API)
sudo dnf install iptables
sudo iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 8000
make start-server // test endpoint from Insomnia or browser
```
