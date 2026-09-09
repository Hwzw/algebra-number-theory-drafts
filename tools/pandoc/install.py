"""Install the pinned official macOS arm64 Pandoc binary in this directory."""
from pathlib import Path
from urllib.request import urlopen
import hashlib
import io
import json
import platform
import zipfile

assert platform.system() == "Darwin" and platform.machine() == "arm64", (
    "This installer is for macOS arm64; on another platform install official "
    "Pandoc 3.9.0.2 and set the PANDOC environment variable."
)
url = "https://github.com/jgm/pandoc/releases/download/3.9.0.2/pandoc-3.9.0.2-arm64-macOS.zip"
expected = "6e9eca844076bcbb599bbeebbba78a70f93b5307782b85c2c272872812c88875"
data = urlopen(url).read()
digest = hashlib.sha256(data).hexdigest()
assert digest == expected, "Official archive checksum mismatch"
directory = Path(__file__).resolve().parent
archive = zipfile.ZipFile(io.BytesIO(data))
matches = [name for name in archive.namelist() if name.endswith("/bin/pandoc")]
assert len(matches) == 1
target = directory / "pandoc"
target.write_bytes(archive.read(matches[0]))
target.chmod(0o755)
(directory / "provenance.json").write_text(json.dumps(
    dict(version="3.9.0.2", url=url, archive_sha256=digest), indent=2
) + "\n")
print(target)
