---
title: "Metadata annotation and DOI"
author: ""
date: ""
---

::: {.callout-note}
This page is work in progress.
:::

## What is _metadata_?

<!-- TODO -->

Mirriam-Webster dictionary defines [data][webster-data] as: "factual
information (such as measurements or statistics) used as a basis for
reasoning, discussion, or calculation", or: "information in digital
form that can be transmitted or processed."

[webster-data]: https://www.merriam-webster.com/dictionary/data

For our purposes, let us use the latter definition: data is
information in digital form that can be stored, transmitted, or
processed.  Our experiments may consume data, produce data, transmit
data between instruments and computers, and we might want to analyze
data to make sense of it.  We store data somewhere, for eventual use
and/or sharing.

[![](data_trap.png)][xkcd-data-trap]

[xkcd-data-trap]: https://xkcd.com/2582/

What is _metadata_ then?

Metadata is data that describes data, and what that description says
depends on context.

For example, [EXIF] (which is an abbreviation of "Exchangeable image
file format") is a form of image metadata.  When you take a picture
with cellphone, you get an image file.  In addition to "pure"
compressed on uncompressed image data, this image file also contains
some extra data describes the image: details about the camera, lens,
aperture, shutter speed, date and time at the time when the picture
was taken, location if available, such things.

In addition to EXIF, there is the metadata that the operating system
itself maintains about an image file: its ownership, date and time
when the file was created and modified (as far as the operating system
is concerned), and so on.

So when we talk about metadata, it is important to be clear about the
context in which we talk about metadata.

[EXIF]: https://en.wikipedia.org/wiki/Exif

For CHESS experimenters, metadata would be information about
observational or experimental data that provides a "fuller picture"
about the observation or experiment.

<!-- TODO -->

## What is annotation?

<!-- TODO -->

## What is DOI?

A DOI (Digital Object Identifier) is a unique and stable string
assigned articles, books, and other works. DOIs make it easier to find
and retrieve works. DOIs are designed to be used by humans as well as
machines. DOIs are commonly used to identify publications and data
sets.

A DOI is meant to help us to resolve its target.  The location of an
online document or data set may change over time, because domain names
and links change.  However, since a DOI remains stable over time, with
a DOI people should be able to find the current location of the
target.  The publisher of the document or data set is responsible for
keeping the record up-to-date.

A DOI takes the form of a character string divided into two parts, a
prefix and a suffix, separated by a slash, in `prefix/suffix` form.  A
DOI is also resolvable as a URL using a proxy server.   

Here is an example of a DOI:

- `10.1177/0306312719863494`
- `https://doi.org/10.1177/0306312719863494`
- (etc?)


### How can I resolve a DOI?

<!-- TODO -->

### How do I get myself a DOI?

<!-- TODO -->

## references

- [Carpentries Incubator: Data and
  Metadata](https://carpentries-incubator.github.io/scientific-metadata/instructor/data-metadata.html)

  - [Carpentries Incubator Training Course Material: Fundamentals of
    Scientific Metadata](https://zenodo.org/records/10091708)

- [Metadata accounts: Achieving data and evidence in scientific
  research](https://pmc.ncbi.nlm.nih.gov/articles/PMC7323761/). Matthew
  S Mayernik, National Center for Atmospheric Research.

- [Observational Health Data Sciences and Informatics forums: How do
  we define “Metadata” and
  “Annotation?”](https://forums.ohdsi.org/t/how-do-we-define-metadata-and-annotation/4424)

- [Wikipedia page on Digital object
  identifier](https://en.wikipedia.org/wiki/Digital_object_identifier)

- [DOI Foundation: What is a
  DOI?](https://www.doi.org/the-identifier/what-is-a-doi/)

- [Scribbr: What is a DOI? Finding and Using Digital Object
  Identifiers](https://www.scribbr.com/citing-sources/what-is-a-doi/)

- [Long Term Ecological Research Network: Enriching Ecological Data
  Using Annotated Metadata](https://lternet.edu/stories/enriching-ecological-data-using-annotated-metadata/)
