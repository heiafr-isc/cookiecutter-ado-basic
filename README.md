# Cookiecutter-ado-basic

Basic template for PlatformIO project used in the assignments
of the lecture "Architecture des Ordinateurs"

## Usage

For the first time that you use the template, type the following command:

```bash
cookiecutter gh:heiafr-isc/cookiecutter-ado-basic
```

And answers the questions. For example :

```text
gitlab_url []: https://gitlab.forge.hefr.ch/ado/20xy-20xz/sup/tp01/tp01-x.git
project_name [tp01]:
author [Jacques Supcik]:
email [jacques.supcik@hefr.ch]:
project_brief [Lorem ipsum dolor sit amet, consectetur adipiscing elit.]:
```

The project name is extracted from the Gitlab URL (if given). This
cookie cutter also initializes the git repository and adds the
`gitlab_url` as remote.

The following times, you can just type:

```bash
cookiecutter cookiecutter-ado-basic
```

Read the [documentation of Cookiecutter](https://cookiecutter.readthedocs.io/en/stable/) for more detail.