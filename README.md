# Metamapper

[![CircleCI](https://circleci.com/gh/getmetamapper/metamapper.svg?style=shield)](https://circleci.com/gh/getmetamapper/metamapper) [![Vulnerabilities](https://snyk.io/test/github/getmetamapper/metamapper/badge.svg)](https://snyk.io/test/github/getmetamapper/metamapper) [![latest version](https://img.shields.io/docker/v/getmetamapper/metamapper?sort=semver)](https://hub.docker.com/r/getmetamapper/metamapper) [![python](https://img.shields.io/github/pipenv/locked/python-version/getmetamapper/metamapper)](https://github.com/getmetamapper/metamapper/blob/master/Pipfile) [![discord](https://img.shields.io/discord/713821768237973535)](http://discuss.metamapper.io)

Metamapper is an open-source metadata management platform that aims to make it easier to share data and its context across your organization. It's a self-updating data catalog complete with full-text search, an integrated commenting system, and much more.

<p align="center">
  <img src="https://github.com/metamapper-io/metamapper/raw/master/.github/screenshots/preview-1.png" width="270">
  <img src="https://github.com/metamapper-io/metamapper/raw/master/.github/screenshots/preview-2.png" width="270">
  <img src="https://github.com/metamapper-io/metamapper/raw/master/.github/screenshots/preview-3.png" width="270">
</p>

*Note: Metamapper is a new project. Each release should be stable, but the project is still in it's fledgling stage. So proceed with that in mind.*

## What we're trying to accomplish

Growing organizations rely on data and analytics to drive decisions. With the emergence of tools like [Airflow](https://github.com/apache/airflow) and companies like [Segment](https://segment.com/) and [Fivetran](https://get.fivetran.com/demo), it's never been easier to get data into your warehouse.

But with all of this data comes a lot of noise. It can become difficult to keep track of things like business purpose and/or timeliness of your data, amongst other things. Plus, writing and maintaing that sort of documentation is just plain boring.

Metamapper aims to automate those boring documentation tasks and reduce the time that data engineers spend answering redundant questions. Just connect your data warehouse and Metamapper will periodically scan the datastore and maintain a commentable data catalog that can be viewed by your team via the UI.

Think of it as Google for your data warehouse – perform a search and it'll find the data that best fits your needs.

Here are a few features of Metamapper:

- *Browser-based:* Everything in your browser, with a shareable URL you can give to your team.
- *Schema inspection:* Metamapper crawls your database schema(s) every few hours and maintains a comprehensive data catalog.
- *Change detection*: Detects when data definitions change between schema inspection runs. Useful for alerting uncommunicated changes.
- *Annotations:* Supports comments on almost every object so your team can crowdsource knowledge about data assets.
- *Custom Properties:* Easily attach custom metadata to databases and tables, such as data steward or ETL process references.
- *Search:* Everything is indexed and [searchable](https://www.postgresql.org/docs/9.5/textsearch.html). Self-service data analytics, here we come.

Check out the [Introducing Metamapper](https://www.metamapper.io/blog/2020/07/12/introducting-metamapper) blog post.

## Getting started

Recommended deployment method is through [Docker](https://www.docker.com/). Setup instructions can be found in [this Github repo](https://github.com/getmetamapper/metamapper-setup).

Reading the [documentation](https://www.metamapper.io/) is also a good starting point.

## Supported datastores

Metamapper currently supports automatic crawling and indexing of six SQL-based relational database management systems with plans to add more in the near future.

- Amazon Redshift
- Microsoft SQL Server
- MySQL
- Oracle
- PostgreSQL
- Snowflake

## Community Feedback

Metamapper is an open source project. Feedback from the community greatly influences our roadmap and the direction of the project. If you want to provide some input, the best place to do it is through [this Typeform survey](https://metamapper.typeform.com/to/rQT0lccB).

## Resources

- [User Documentation](https://www.metamapper.io)
- [Contributing](CONTRIBUTING.md)
- [Issue Tracker](https://github.com/getmetamapper/metamapper/issues)
- [Roadmap](https://trello.com/b/QT28sJAz/metamapper-io)
- [Code](https://github.com/getmetamapper/metamapper)
