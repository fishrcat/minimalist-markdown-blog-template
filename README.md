# Minimalist Markdown Blog Template

Single-page, no maintenance blog site

&rarr; Add and preview posts by committing Markdown files.

&rarr; Style via config file.

&rarr; Utilizes Oat, an ultra-lightweight HTML + CSS UI component library.

![Example default blog image](content/img/default-blog.png)

## Setup Guide

### 1) Create your own site repository using this template

Select `Use This Template` in GitHub:

![Use This Template location](content/img/use-template.png)

### 2) Configure the GitHub Pages site deployment

In the repo **Settings** > **Pages** > **Build and Deployment**, set **Source** to *GitHub Actions*.

Rerun the **Build and Deploy Pages Site** GiHub Action on the initial repo commit.  This workflow indexes all available post files and deploys the site.

The *Report Pages URL* step at the end of the workflow will provide a direct link to the deployed site.  

> [!TIP]
> **PR Workflow** - the URL will specify the branch name if working in an open PR, so you can preview changes before deploying to the main site on merge.
> 
> **Custom Domain** - To configure a custom domain for your site, follow the [GitHub Docs Guide](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site).  Because the site deploys via actions, no CNAME file is required.

### 3) Update style and site info in `config.json`

Update following sections in `config.json`, commit the file to a new branch, and open a new PR. 

**Content**

* `meta` - Site title and info section displayed at the top of the page
* `postColumns` - Any number of column titles to house the posts from the associated directories.  Posts will appear in the columns in commit timestamp order.

**Style** 

* `footer` - URLs linked to the GitHub and user icons in the footer
* `colors` - Site color scheme
* `font` - Google font config, or omit url and provide standard font family

**Optional**

* Replace the `favicon.ico` file to update the site tab image.

To preview the updated site, follow the link in the *Report Pages URL* step at the end of the *Build and Deploy Pages Site* GiHub Action workflow.

When you are happy with the style, merge the PR to main to deploy the update to the main site.

## Posting

To add a new post, commit the file to the relevant `/content` column sub directory on a branch and open a new PR.

To preview the updated site, follow the link in the *Report Pages URL* step at the end of the *Build and Deploy Pages Site* GiHub Action workflow.

Merge the PR to main to deploy the update to the main site.

## Modding

All HTML, CSS, and JS are inlined in `index.html` in simplest form.

To create the required indices and run the site locally, run:

    python3 .github/workflows/build_index.py

    python3 -m http.server 8000