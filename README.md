# Fonthill Pubs · weekly management dashboard

Password-protected copy of the weekly management meeting dashboard, published with GitHub Pages:
https://hq-fonthillpubs.github.io/fonthill-dashboard/

`index.html` is encrypted with [StatiCrypt](https://github.com/robinmoisson/staticrypt) (AES-256, decrypted in the browser with the team password). The figures and page are never stored here unencrypted. It is rebuilt and republished every Monday afternoon by Claude's weekly refresh task.

- `build/build.py DATA_DIR PAGE_FILE OUT_FILE [UPDATED_ISO]` combines `build/shell.html`, `build/d3.min.js` (d3 v7.9.0), the dashboard's data JSON files and page HTML into one plain HTML file (never committed).
- Encrypt with `npx staticrypt@3.5.4 ... -c .staticrypt.json --short --remember 90`. `.staticrypt.json` holds the salt, which is not secret; keeping it fixed means "Remember me" survives weekly rebuilds.

Ask Claude in the "Dashboard" project to change the password or the page.
