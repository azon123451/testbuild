import os
from pathlib import Path
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer


def main() -> None:
	port = int(os.getenv("PORT", "8080"))
	project_root = Path(__file__).resolve().parent
	web_dir = project_root / "webapp"
	web_dir.mkdir(parents=True, exist_ok=True)
	os.chdir(web_dir)

	# Simple threaded HTTP server would be nicer, but basic one is fine for static content
	with TCPServer(("", port), SimpleHTTPRequestHandler) as httpd:
		print(f"Serving {web_dir} on port {port}")
		httpd.serve_forever()


if __name__ == "__main__":
	main()


