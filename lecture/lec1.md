---
title: Slides Template
separator: <!--s-->
verticalSeparator: <!--v-->
theme: solarized
revealOptions:
    transition: 'fade'
---
# Local

This will serve the presentation

and open a browser to view it

* clone the repo
* edit the `slides.md` file
* then:
```
npm install
npm run presentation
```

Note: This is a speaker note, you need node 6.x installed

<!--s-->

# GitHub Pages

* fork the repo
* setup a build in travis for the fork - don't forget the env var with your personal access token
* edit the `slides.md` file
* push to github
* view presentation on GitHub - in the project pages for your repo

<!--v-->

# References

* [reveal-md](https://github.com/webpro/reveal-md)
* [reveal.js](http://lab.hakim.se/reveal-js)
* [GitHub Pages](https://pages.github.com)
* [Travis CI](https://travis-ci.org)
* [This template](https://github.com/martinmurphy/slidestemplate)