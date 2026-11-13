# Quarto

Details on setting up Quarto Setup

Author

Benedict Thekkel

## Download

> Downlaod quarto : quarto-1.3.433-win

------------------------------------------------------------------------

> > Remember to restart the computer

### for linux

``` sh
wget https://quarto.org/download/latest/quarto-linux-amd64.deb
```

Next use:

``` sh
sudo apt install ./<name>.deb
```

Example:

``` sh
sudo apt install quarto-linux-amd64.deb
```

## Installs

``` sh
pip install jupyter jupyterlab
```

``` sh
pip install matplotlib plotly
```

# Useful commands

- For help\

``` sh
quarto -h
```

- For viewing\

``` sh
quarto preview FILENAME.ipynb
```

- For rendering to html

``` sh
quarto render FILENAME.ipynb --to html
```

- For rendering to docx a

``` sh
quarto render FILENAME.ipynb --to docx
```

Back to top
