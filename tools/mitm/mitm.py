from mitmproxy import http


class Interceptor:
    def __init__(self, target_domains):
        self.target_domains = target_domains

    def request(self, flow: http.HTTPFlow) -> None:
        if any(domain in flow.request.pretty_url for domain in self.target_domains):
            print(f"Intercepting request to: {flow.request.pretty_url}")
            # Process the request here if needed
        else:
            flow.filter = True

    def response(self, flow: http.HTTPFlow) -> None:
        if any(domain in flow.request.pretty_url for domain in self.target_domains):
            print(f"Intercepting response from: {flow.request.pretty_url}")
            # Process the response here if needed
        else:
            flow.filter = True


# Define the target domains you want to intercept
target_domains = [""]

addons = [Interceptor(target_domains)]
