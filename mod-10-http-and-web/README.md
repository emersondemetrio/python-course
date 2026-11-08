# Module 10: HTTP and the web

Until now, your programs lived alone on your computer. In this module they start talking to other programs over the network. First you learn how the web works, then you make Python ask other services for data, and finally you build your own small web service that your HTML and JavaScript can talk to.

This is where your two worlds meet: the Python you learned in this course and the HTML, CSS and JavaScript you already know.

## Files, in order

1. [How the web works](how-the-web-works.md): clients, servers, URLs, requests, responses, status codes and JSON.
2. [Calling APIs](calling-apis.md): asking other services for data with the `requests` library.
3. [Building an API](building-an-api.md): creating your own web service with Flask and calling it from a web page.

## Before you start

- You know dictionaries, lists and JSON (module 6).
- You can create a project and add libraries with uv (`uv init`, `uv add`, `uv run`, module 7).
- You know how to handle errors with `try` and `except` (module 7).

## Time estimate

Plan for 3 to 4 sessions of about one hour each. The last file is the longest: take it slowly and type every example yourself.

## You are ready for the next module when you can...

- [ ] Explain, in your own words, what a client and a server are.
- [ ] Point to the scheme, host, path and query string in a URL.
- [ ] Say what the status codes 200, 201, 400, 404 and 500 mean.
- [ ] Use `requests.get` to fetch JSON from a public API and read a value from it.
- [ ] Run a Flask app on your computer and open it in the browser.
- [ ] Write a Flask route that returns JSON and another that receives JSON with POST.
- [ ] Call your own API from a web page using `fetch()`.

**Next:** [How the web works](how-the-web-works.md)
