# Building Permits Survey
**Contributors:** Sid Kapur, Zack Subin

The goal of this project is to produce (1) a Python library for loading data from the [US Census Building Permits Survey](https://www.census.gov/construction/bps/) as a pandas DataFrame, and (2) a Plotly/Dash webapp that displays this data in an interactive way so that people can explore this data in more detail.

# Getting started

This project assumes that you have `pipenv` installed. To create the virtualenv and install the packages, just run `pipenv install` from the root directory.

When adding/updating packages, you'll want to commit both `Pipfile` and `Pipfile.lock` to the repo, to make sure that everyone is using the same versions of each package.

# Tools

[Plotly Dash](https://plotly.com/dash/) is supposedly "the most popular framework for building ML and data science apps", so that sounds like a good thing to use for the visualization.

Since this is a Python webapp, we'll have to use [Heroku](https://www.heroku.com/) to host the Python server. 
Fortunately, Dash has specific [documentation](https://dash.plotly.com/installation) for how to use Dash with Flask and Heroku, so hopefully this will be pretty easy to set up.

For CSS stuff, I like to use [tailwindcss](https://tailwindcss.com/), but I'm hoping that Dash will take care of most of it so that we don't need to mess with CSS too much.

# Deploying

Once I get the Heroku account set up, I'll post the live URL and the instructions for pushing to Heroku here!
