from flask import Flask, redirect, request
from urllib.parse import urlparse, urljoin

FROM_DOMAIN = "from_url.com"
TO_DOMAIN = "to_url.com"

app = Flask(__name__)


@app.route("/")
@app.route("/<path:rest>")
def redirect_request(rest="/"):
    print(rest)
    print(request.url_root)
    domain_name = urlparse(request.url_root).netloc
    print(domain_name)
    if domain_name == FROM_DOMAIN:
        print(urljoin("https://" + domain_name, rest))
        return redirect(urljoin(domain_name, rest))
    return "Page not found", 404


app.app_context().push()

if __name__ == "__main__":
    # Should be run for debug purposes only
    app.run(host="0.0.0.0", port=5001)