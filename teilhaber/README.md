# Flet app

You need to install the libmpv library on Linux, e.g.:

`sudo apt install libmpv1`

On Arch Linux (and other distros) you might get an error that `libmpv.so.1` is not found? Try this:

`sudo ln -s /usr/lib/libmpv.so /usr/lib/libmpv.so.1`

To run the app, once you have [Poetry installed](https://python-poetry.org):

```
poetry install
poetry shell
flet run [app_directory]
```