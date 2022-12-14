<!doctype html><html lang="en"><head><meta charset="utf-8"><title>JupyterLab</title><meta name="viewport" content="width=device-width,initial-scale=1">   <script id="jupyter-config-data" type="application/json">{"allow_hidden_files": false, "appName": "JupyterLab", "appNamespace": "lab", "appSettingsDir": "/Users/gazi/opt/anaconda3/share/jupyter/lab/settings", "appUrl": "/lab", "appVersion": "3.3.2", "baseUrl": "/", "buildAvailable": true, "buildCheck": true, "cacheFiles": false, "collaborative": false, "devMode": false, "disabledExtensions": [], "exposeAppInBrowser": false, "extraLabextensionsPath": [], "federated_extensions": [{"extension": "./extension", "load": "static/remoteEntry.f372bf1de02fb50ae6e0.js", "mimeExtension": "./mimeExtension", "name": "jupyterlab-plotly"}, {"extension": "./extension", "load": "static/remoteEntry.c267118552c4161d6406.js", "name": "@pyviz/jupyterlab_pyviz", "style": "./style"}, {"extension": "./extension", "load": "static/remoteEntry.ca1efc27dc965162ca86.js", "name": "@jupyter-widgets/jupyterlab-manager"}], "fullAppUrl": "/lab", "fullLabextensionsUrl": "/lab/extensions", "fullLicensesUrl": "/lab/api/licenses", "fullListingsUrl": "/lab/api/listings", "fullMathjaxUrl": "/static/notebook/components/MathJax/MathJax.js", "fullSettingsUrl": "/lab/api/settings", "fullStaticUrl": "/static/lab", "fullThemesUrl": "/lab/api/themes", "fullTranslationsApiUrl": "/lab/api/translations", "fullTreeUrl": "/lab/tree", "fullWorkspacesApiUrl": "/lab/api/workspaces", "ignorePlugins": [], "labextensionsPath": ["/Users/gazi/Library/Jupyter/labextensions", "/Users/gazi/.local/share/jupyter/labextensions", "/Users/gazi/opt/anaconda3/share/jupyter/labextensions", "/usr/local/share/jupyter/labextensions", "/usr/share/jupyter/labextensions"], "labextensionsUrl": "/lab/extensions", "licensesUrl": "/lab/api/licenses", "listingsUrl": "/lab/api/listings", "mathjaxConfig": "TeX-AMS-MML_HTMLorMML-full,Safe", "mode": "multiple-document", "notebookVersion": "[1, 13, 5, \"\", \"\"]", "preferredPath": "/", "quitButton": true, "schemasDir": "/Users/gazi/opt/anaconda3/share/jupyter/lab/schemas", "serverRoot": "/Users/gazi", "settingsUrl": "/lab/api/settings", "staticDir": "/Users/gazi/opt/anaconda3/share/jupyter/lab/static", "store_id": 0, "templatesDir": "/Users/gazi/opt/anaconda3/share/jupyter/lab/static", "terminalsAvailable": true, "themesDir": "/Users/gazi/opt/anaconda3/share/jupyter/lab/themes", "themesUrl": "/lab/api/themes", "token": "b3eb81f90fd582512a8f134d710d7da7c375275742e76aab", "translationsApiUrl": "/lab/api/translations", "treePath": "", "treeUrl": "/lab/tree", "userSettingsDir": "/Users/gazi/.jupyter/lab/user-settings", "workspace": "default", "workspacesApiUrl": "/lab/api/workspaces", "workspacesDir": "/Users/gazi/.jupyter/lab/workspaces", "wsUrl": ""}</script><link rel="icon" type="image/x-icon" href="/static/favicons/favicon.ico" class="idle favicon"><link rel="" type="image/x-icon" href="/static/favicons/favicon-busy-1.ico" class="busy favicon"><script defer="defer" src="/static/lab/main.46d6e638824298417ce9.js?v=46d6e638824298417ce9"></script></head><body><script>/* Remove token from URL. */
  (function () {
    var location = window.location;
    var search = location.search;

    // If there is no query string, bail.
    if (search.length <= 1) {
      return;
    }

    // Rebuild the query string without the `token`.
    var query = '?' + search.slice(1).split('&')
      .filter(function (param) { return param.split('=')[0] !== 'token'; })
      .join('&');

    // Rebuild the URL with the new query string.
    var url = location.origin + location.pathname +
      (query !== '?' ? query : '') + location.hash;

    if (url === location.href) {
      return;
    }

    window.history.replaceState({ }, '', url);
  })();</script></body></html>