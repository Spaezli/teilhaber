Teilhaber
===

A prototype started at [Hack4SocialGood 2024](https://hack4socialgood.ch).

We are using the Flet framework to create an app that supports social science research into civic participation. See [install docs](https://flet.dev/docs/getting-started/) to get started.

For more background, see https://bd.hack4socialgood.ch/project/89

# Development

You need to install the libmpv library on Linux, e.g.:

`sudo apt install libmpv1`

On Arch Linux (and other distros) you might get an error that `libmpv.so.1` is not found? Try this:

`sudo ln -s /usr/lib/libmpv.so /usr/lib/libmpv.so.1`

To run the app, once you have [Poetry installed](https://python-poetry.org):

```
poetry install
poetry shell
flet run [flet run teilhaber]
```

# License

This project is open source and public domain under the [Unlicense](LICENSE).

