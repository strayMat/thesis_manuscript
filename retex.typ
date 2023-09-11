#let project(
  title: "",
  abstract: [],
  authors: (),
  date: none,
  body,
) = {
  // Set the document's basic properties.
  set document(author: authors.map(a => a.name), title: title)
  set page(numbering: "1", number-align: center)
  set text(font: "Linux Libertine", lang: "en")
  set heading(numbering: "1.1")

  // Title row.
  align(center)[
    #block(text(weight: 700, 1.75em, title))
    #v(1em, weak: true)
    #date
  ]

  // Author information.
  pad(
    top: 0.5em,
    bottom: 0.5em,
    x: 2em,
    grid(
      columns: (1fr,) * calc.min(3, authors.len()),
      gutter: 1em,
      ..authors.map(author => align(center)[
        *#author.name* \
        #author.email \
        #author.affiliation
      ]),
    ),
  )

  // Main body.
  set par(justify: true)

  //heading(outlined: false, numbering: none, text(0.85em, smallcaps[Abstract]))
  abstract

  body
}

#show: project.with(
  title: "Retex d'une thèse d'IA en médecine",
  authors: (
    (name: "Matthieu Doutreligne", email: "matt.dout@gmail.com", affiliation: "HAS, Inria"),
  ),
  // Insert your abstract after the colon, wrapped in brackets.
  // Example: `abstract: [This is my abstract...]`

  date: "March 22, 2023",
)
#show link: underline

#show raw: box.with(
  fill: luma(240),
  inset: (x: 3pt, y: 0pt),
  outset: (y: 3pt),
  radius: 2pt,
)

= Retex sur une thèse d'IA en médecine  

#block(
  fill: luma(230),
  inset: 8pt,
  radius: 4pt,
  "AI enables new discoveries and improved processes in the entire health care continuum; ethical, governance, and regulatory considerations are critical in the design, implementation, and integration of every component of the AI applications and systems. Because of concerns about both utility and safety, new applications will generally have to adhere to the same standards applied to other medical technologies. This will require a level of rigor in testing similar to that used in other areas of medicine, but it also can present challenges, such as the “dataset shift” that can result when there is a mismatch between the data set with which an AI system was developed and the data on which it is being deployed.3 This summer, we hope to begin evaluating research studies for NEJM AI that bring careful methodology to understanding how to use AI and machine learning approaches in medicine. (@beam)",
)

#bibliography("references.bib", style: "chicago-author-date")
