Teilhaber:in
===

A prototype started at Hack4SocialGood 2024

We are using the Flet framework connected to a Baserow database to create an app that supports social science research into civic participation. For more background, please [visit our project page](https://bd.hack4socialgood.ch/project/89).

# Development

See [install docs](https://flet.dev/docs/getting-started/) to get started. You will need to install the libmpv library on Linux, e.g.:

`sudo apt install libmpv1`

On Arch Linux (and other distros) you may [get an error](https://github.com/flet-dev/flet/issues/2823) that `libmpv.so.1` is not found - try this:

`sudo ln -s /usr/lib/libmpv.so /usr/lib/libmpv.so.1`

To run the app, once you have [Poetry installed](https://python-poetry.org):

```
poetry install
poetry shell
flet run teilhaber
```

# License

This project is open source and public domain under the [Unlicense](LICENSE).

