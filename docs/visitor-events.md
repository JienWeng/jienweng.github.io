# Useful visitor actions

Existing GoatCounter pageviews measure visits to project and CV pages. The site also sends these fixed event names through the existing GoatCounter JavaScript API:

- `contact-email`: click an email link.
- `cv-open`: open the CV page.
- `cv-download-pdf`: click the downloadable CV.
- `cv-read-text`: open the text CV.
- `project-open-<slug>`: open an individual project or the CRM case study.
- `project-resource-<slug>`: click a resource in a project page's action list.
- `project-demo-play`: start the project page's controlled workflow video (once per video per page load).

Events record a click or playback start, not a completed download, sent email, or conversion. Event names contain no email address, search query, credential, or URL query string. Automatic animation playback is not counted as a demo play.

The listener runs only on the production hostname, excluding `/pr-preview/`. Preview builds omit the GoatCounter script. Analytics blocking or an unavailable provider leaves navigation and video controls working normally.

After deployment, inspect event counts in the existing GoatCounter dashboard. Provider/account delivery is not verified by a local test.

Reference: https://www.goatcounter.com/help/events
