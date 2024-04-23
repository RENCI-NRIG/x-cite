# X-CITE

[![publish-badge]][publish-workflow]

This repository is for CyberInfrastructure Training and Education for
Synchrotron X-Ray Science (X-CITE) course materials.

X-CITE is geared toward the community of scientists and researchers
using the [CHESS] synchrotron X-ray facility and similar light
sources.

See [index] for an outline of the course material.

## Authoring content

The content in this repository is written in the form of markdown
files or Jupyter notebooks, and processed using [Quarto] in order to
generate the website seen at https://xcitecourse.org/.

To add/update content, do this:

- Download and install Quarto from [quarto.org][Quarto].
- Clone/fork this repository.
- Add/edit content in the form of `.md`, `.qmd`, or `.ipynb` files.
- Run `quarto preview` in a terminal, which will start a local web
  server with a live preview that opens in your web browser.
- Once you are satisfied with your changes, commit them, and push them
  to this repository, or submit a pull request.

Once content is in the `main` branch of this GitHub repository, the
[publish] workflow should take care of the building and publishing the
site.

<!-- References -->

[publish-workflow]: https://github.com/RENCI-NRIG/X-CITE/actions/workflows/publish.yml
[publish-badge]: https://github.com/RENCI-NRIG/X-CITE/actions/workflows/publish.yml/badge.svg (Publish)

[CHESS]: https://www.chess.cornell.edu/
[index]: ./index.md
[publish]: .github/workflows/publish.yml

[Quarto]: https://quarto.org
[x-cite]: https://xcitecourse.org/
